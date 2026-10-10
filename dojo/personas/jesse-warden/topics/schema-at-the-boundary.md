---
triggers:
  - "user parses JSON with any, as casts, or manual typeof narrowing"
  - "validation is scattered through the codebase (shotgun parsing)"
  - "user asks about Zod, ArkType, Effect Schema, or decoders"
  - "user confuses unknown with any"
  - "domain code re-checks email shape, age ranges, or required fields"
use_when:
  - "untrusted data enters: HTTP, files, queues, env, legacy DB rows"
  - "designing Parse, Don't Validate boundaries (Alexis King)"
  - "producing trusted domain types once so the core stays pure"
  - "reshaping external snake_case / extra fields into your model"
fails_when:
  - "you parse again deep in the domain after a successful boundary parse"
  - "you leak Zod (or lib) error types across your public package boundary"
  - "you use schema only as runtime asserts without producing a typed value"
related:
  - "anti-corruption-layer.md"
  - "smart-constructors.md"
  - "pure-and-total-functions.md"
  - "product-and-union-types.md"
  - "pipelines-and-composition.md"
---

# Schema at the Boundary

## When to Use

- Data crosses into your process untyped or weakly typed: `response.json()`, message bus payloads, CLI args, config files.
- You see **Shotgun Parsing**: every layer validates only the slice it cares about; failures are partial; nobody trusts prior checks.
- Manual narrowing is tedious and wrong (`typeof age === "number"` still allows `NaN`).
- Domain types drift from ad-hoc parsers when the backend makes a field optional.
- You want one source of truth: parse once, get a type the rest of the program can trust without re-validation.

## Fails When

- After a successful parse, domain functions still `if (!person.email)` "just in case." That reintroduces distrust and means the schema did not encode the real invariants (or the team does not believe types).
- Library error types (`ZodError`) leak out of a shared package so every consumer couples to your schema lib version.
- You only "validate" and throw without producing a narrowed domain value; you still have shotgun risk and no parse-don't-validate win.
- You couple domain types 1:1 to a 100-field backend DTO when you need 2 fields. Schema can reshape; use that.

## Core Concept

To do anything of value, unsafe outside data must enter the type system. Good compile-time types do not make `JSON.parse` honest. Gradual systems (TypeScript, Python, Luau) make this daily pain.

### unknown vs any

**`any` turns the type system off.** One `as any` can negate branded types, products, and unions across a module.

**`unknown` forces narrowing** before use. Prefer:

```ts
const person = JSON.parse(data) as unknown
// person.name is an error until you narrow or parse
```

Legitimate `any` still exists: git-r-done spikes, untyped libs, exploratory logging when REST lies. Do not default to it under TyDD.

Manual narrowing works and is a footgun:

```ts
if (
  personMaybe &&
  typeof personMaybe === "object" &&
  "name" in personMaybe &&
  typeof (personMaybe as { name: unknown }).name === "string"
) {
  // still incomplete for real domain types
}
```

### Schemas as one source of truth

Schema libraries (Zod, ArkType, Effect Schema, etc.) give you parse + type inference + transforms in one place:

```ts
const cowSchema = z.object({
  age: z.number().gte(0),
  name: z.string(),
})

type Cow = z.infer<typeof cowSchema>

const cow = cowSchema.parse(JSON.parse(raw)) // throws or use safeParse
```

Benefits Jesse lists from Parse, Don't Validate (pattern name and core idea: **Alexis King**):

- No shotgun parsing; successful parse means valid data for the whole core
- Code using `Person` does not re-check validity
- Program does not crash "somewhere" because only half the fields were ever checked
- Validation happens in one place, not ad hoc forever
- Failures can detail what did not parse (schema errors), not a mystery throw two layers down

Design the type you want, then convert:

```ts
type ParsePerson = (data: unknown) => Result<Person, Error | ZodError>
```

Prefer `safeParse` + `Result` over throw-happy `parse` inside domain pipelines so composition stays total.

### Shape what *you* need

Schema is not only validation; it is **translation**. Snake_case Python APIs, optional noise fields, ISO strings → your camelCase branded domain with POSIX time. Transforms belong at the boundary so the core never speaks foreign shapes.

That pairs with Anti-Corruption Layer (Eric Evans / DDD): sometimes the issue is not only trust but **owned language**. Schema often implements thin ACL; thick ACL may map behavior too.

### Keep the domain pure

Interior code should not ask "can I trust this input?" Ask once at `unknown → YourType`. Anytime you want to validate mid-domain, ask whether the JSON/file/database boundary could finish the job so data arrives already valid.

Optional values that drive you crazy: make required after parse, or model readiness as a discriminated union so you only access data when ready. Prefer Result when "missing" is failure with meaning.

### Library hygiene

From Zod v3/v4 learnings: do not leak schema-lib errors across package boundaries; map to your error types. Prefer Standard Schema-style interop when multiple libs matter. Wrap fetch with Result + schema so HTTP is total from the caller's view.

## How to Apply

1. **Mark every entry point.** HTTP handlers, consumers, file loaders, env readers. Each has an `unknown` (or `string`) in and a domain type out.

2. **Write the domain type first** (products, unions, brands). Then write the schema that produces it. Infer types from schema when that is the single source, or keep dual with care to avoid drift.

3. **Use `unknown`, not `any`,** for pre-parse values. Enable strict TS so nullability is honest.

4. **`safeParse` → Result.** On success, only domain types flow inward. On failure, structured errors (field paths) for UI or logs.

5. **Brand and opaque at parse when needed.** `z.string().email().brand<"Email">()` or custom refine into opaque `Email` via smart constructor.

6. **Reshape in the schema/ACL.** Pick fields, rename, convert dates, default only when product truly wants defaults (defaults can hide missing data; be deliberate).

7. **Ban re-validation in the core.** Code review smell: `if (!validEmail(user.email))` inside a function that already accepts `User`. Fix the boundary or the type.

8. **Property/fuzz the boundary.** Random JSON, missing fields, NaN, huge strings. Schema is the right place for that investment.

9. **Map lib errors before export.** Your package returns `ParseError`, not `ZodError`, if outsiders consume you.

## Examples

**Situation:** Microservice trusts API gateway "validation" then still checks fields in three services; outages show incomplete error messages.

**Application:** Each service parses its own inbound `unknown` into its own domain types (even if gateway validates too). Shared nothing on trust. Failures return full schema issues for the fields that service owns.

**Illustrative result:** Shotgun parsing stops. On-call sees "age must be >= 0" instead of "cannot read property map of undefined" three hops later.

---

**Situation:** `JSON.parse` + `as Person` after a quick demo; production gets `age: null` and UI explodes.

**Application:** Replace cast with schema requiring number age ≥ 0, non-empty name, branded id. Handler returns 400 with issues array. Domain never sees invalid Person.

**Illustrative result:** Casts gone. LLM-generated `as Person` fails review checklist. Continuous delivery: contract tests hit the same schema.

---

**Situation:** Backend sends `first_name`, 80 unused fields, and string dates; frontend types mirror the mess.

**Application:** Schema picks two fields, transforms to `firstName`, parses dates to `Date` or branded `UtcInstant`. Domain `Person` is small and owned.

**Illustrative result:** Backend can add fields without infecting UI types. Rename is one transform, not 40 files.

---

**Situation:** Manual narrow allows `age: NaN` because `typeof NaN === "number"`.

**Application:** `z.number().finite().gte(0)` or equivalent. One line in schema beats a cultural "remember NaN" rule.

**Illustrative result:** Entire class of numeric footguns dies at parse.

## Anti-Patterns (tactical)

**Don't:** Default to `any` for external data "because we validate later."
**Why:** Later is multiple places or never. `any` disables the assistant you are paying the typechecker for. Use `unknown` + schema.

**Don't:** Practice shotgun parsing: each function validates its favorite fields and assumes the rest.
**Why:** Alexis King's Parse, Don't Validate exists because this fails partially, opaquely, and everywhere. You get crashes and duplicated defensive code forever.

**Don't:** Keep validating in the domain after a successful parse.
**Why:** Either the type is lying (fix the schema) or the team does not trust the boundary (fix culture and exports so only parsed types are constructible).

**Don't:** Mirror foreign DTOs as your domain model "for speed."
**Why:** You couple to someone else's words and shape. Schema/ACL exist so your team shares one language in code.

**Don't:** Throw raw schema exceptions through 10 layers of framework.
**Why:** Map to Result early; match at the HTTP edge. Totality and error design stay intentional (errors as values).

**Don't:** Require a PhD in formal methods to adopt Zod.
**Why:** This is practical boundary engineering. Credit King for the pattern name; use a schema lib; ship. Gatekeeping with type theory essays is optional reading, not a prerequisite.
