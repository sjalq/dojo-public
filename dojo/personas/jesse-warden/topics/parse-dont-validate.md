---
triggers:
  - "user validates the same data in many layers or re-checks fields before every use"
  - "user asks about Parse Don't Validate or Shotgun Parsing"
  - "user brings untrusted JSON/headers/files into domain code as any or loose objects"
  - "user asks where Zod/schemas should live relative to business logic"
  - "defensive if-guards for shape litter the codebase and still crash unpredictably"
use_when:
  - "data crosses a trust boundary (HTTP, file, DB row, env, third-party API) into your typed domain"
  - "you can name the target domain type and convert unknown into it once"
  - "team wants trusted types interior to the app without ad-hoc validation forever"
fails_when:
  - "parse is partial (only the fields this function cares about) while other fields remain untrusted"
  - "validation is re-done deep in domain code after a successful boundary parse"
  - "any is used so the compiler never forces conversion"
related:
  - "branded-types.md"
  - "result-and-errors-as-values.md"
  - "railway-oriented-programming.md"
  - "impossible-states.md"
  - "type-driven-development.md"
---

# Parse, Don't Validate

## When to Use

- Untrusted data enters the system: JSON, headers, query strings, files, message buses, "REST that lies"
- Domain code is full of `if (!person || !validEmail(...)) throw` and still cannot trust data two lines later
- You want **one place** that asks "Can I trust this input?" and then never ask again
- Schemas (Zod, ArkType, Effect Schema) can be the single source of truth for runtime + static types
- You are fixing Shotgun Parsing after an incident or endless defensive coding

## Fails When

- "Parse" only checks one field and assumes the rest were already validated (hidden order-of-operations coupling)
- You parse into a type that still allows impossible states (optional bags); fix the target type, not only the parser
- Domain code keeps re-validating "just in case," destroying the trust invariant
- You use `any` so nothing forces narrowing or conversion
- Parse is treated as optional polish rather than the trust boundary for Continuous Delivery and LLM-generated boundary code

## Core Concept

### Attribution

**Parse, don't validate** means: at the boundary, convert untrusted data (`unknown` JSON, headers, LLM output) into a domain type you can trust. After that, stop re-checking the same fields with ad-hoc ifs all over the codebase. Interior code takes a `Person`, not "maybe a person if the last guard passed."

*(The name of the essay is Alexis King's. Use the pattern; mention her if the user asks for the essay.)*

### Shotgun Parsing

**Shotgun Parsing** is what happens when data in your domain cannot be trusted, so every layer validates the slice it cares about before use, and code throughout the codebase does ad-hoc validation.

Costs Jesse lists:

- The program can **crash at any time** because some data may be invalid, but only for a particular piece of code  
- When it fails, you **don't know if other data is ok**, even code two lines below; the error only talks about what that snippet cared about  
- A huge percentage of **all** code (domain + infra, new and old) becomes data validation  
- Failures are partial and opaque  
- Defensive code multiplies and must be maintained forever  

Manual narrowing footguns: `typeof age === 'number'` still allows `NaN`; partial checks; type and parser drift when the backend makes `age` optional.

### The solution

**Parse** the data you are getting **into the data you need**. Design the types you want first, then convert:

```ts
type ParsePerson = (data: unknown) => Result<Person, Error | ZodError>
```

Prefer **`unknown` over `any`**. `any` turns the type system off; `unknown` forces narrowing and conversion before use.

Schemas as the main tool:

```ts
const cowSchema = z.object({
  age: z.number().gte(0),
  name: z.string().transform(...), // reshape snake_case → camelCase if needed
})
type Cow = z.infer<typeof cowSchema>
const cow = cowSchema.parse(JSON.parse(data)) // or safeParse → Result
```

One source of truth: it either parses or it doesn't. The type is **validated data** all of your code can trust, use without modifying, and not re-validate. Shape can be what **you** need, not coupling to every field the backend dumps (100 fields when you need 2).

### What disappears when you do this

From the series:

- No more Shotgun Parsing; after successful parse, code has valid data  
- No code needs to "check if the data is valid"; if they hold a `Person`, it is valid  
- Program cannot crash at any time from that class of shape bugs  
- Validation happens through parsing, in **one place**, not ad-hoc everywhere  
- Defensive code no longer needs to be written or maintained for that boundary  
- When it fails, you get details of what worked and what didn't (e.g. Zod / schema errors)  

Gone are the days of "Can I trust this input?" all over. Ask that **once** at the boundary of `unknown → YourType`. Anytime you start wanting to validate data deep inside, ask whether the JSON/file/database parsing part could do more so data arrives already valid.

### Relation to other TyDD moves

- **unknown vs any:** input type of the parse  
- **Schema (Part 8):** mechanism; parse-don't-validate is the named principle  
- **Result / Errors as Values:** parse failure is a modeled error (`BadBody` with schema errors)  
- **Branded types:** Zod `.brand` at parse so IDs enter domain already distinct  
- **Opaque / smart constructors:** parse-don't-validate for single values (`makeEmail`)  
- **Anti-Corruption Layer (Eric Evans / DDD):** related but different: not only raw→valid, but **their types → our types** / their language → our language  
- **Impossible states:** parse narrows possible states so bad ones never enter the domain  

### Optionals that drive you crazy

If optional fields force endless checks, make them required at the domain type, or model readiness as a **Discriminated Union** so you only access data when ready (`NotValidated | ValidForm`). Don't leave half-parsed bags as the domain model.

## How to Apply

1. **Find trust boundaries.** HTTP handlers, workers, file loaders, DB mappers, third-party clients.

2. **Design the domain type you want** (brands, products, unions). Do not start from the backend's full JSON as the domain model.

3. **Write one schema (or parser)** that converts `unknown` → that type (or `Result<That, ParseError>`).

4. **Call parse once** at the boundary; on success, pass `Person` / `Cow` / `Order` inward. Interior functions take the trusted type, not `unknown` or `any`.

5. **Map parse failures** into your error DU (`BadBody`, etc.) and handle at the edge with the rest of [result-and-errors-as-values.md](result-and-errors-as-values.md).

6. **Put brands and transforms in the schema** so naming and nominal distinction start at the gate.

7. **Delete defensive re-checks** in domain code that only existed because nothing trusted prior validation. If a re-check remains, either the parse is incomplete or the type still allows junk.

8. **Compose on a railway** when parse is one of several fallible steps:  
   `andThen(safeParseJSON).andThen(schema).andThen(toDomain)`.

9. **Property / fuzz the boundary** when it matters; the parse function is a perfect target for random invalid input.

10. **Library authors:** consider mapping schema-lib errors to your own types at the package boundary so consumers don't couple to Zod version churn.

## Examples

**Situation:** Every service function starts with `if (!cow || typeof cow.age !== 'number') throw`; sometimes age is NaN; sometimes only `name` was checked.

**Application:** `cowSchema` with `age: z.number().gte(0)`; parse at the controller; domain functions take `Cow`. Remove interior guards.

**Illustrative result:** Invalid cows never enter domain; failures report full schema issues once.

---

**Situation:** Python backend sends `first_name`, snake_case everywhere; TS domain is camelCase; infection spreads.

**Application:** Schema transforms at the boundary into your product type. Domain never sees snake_case fields.

**Illustrative result:** Style and model stay yours; ACL-ish mapping without legacy words in the core.

---

**Situation:** UI request type is `{ loading: boolean; data?: User; error?: string }` allowing loading+data+error together; "validation" of which fields exist is scattered in render.

**Application:** Parse/construct a DU: `{ tag: 'loading' } | { tag: 'success'; data: User } | { tag: 'error'; error: string }`. Access data only in success.

**Illustrative result:** Impossible combinations unrepresentable; no shotgun checks for which optional is set.

---

**Situation:** LLM-generated handlers cast `JSON.parse(body) as Order` and ship.

**Application:** Policy: `unknown` + schema parse required at boundary; `as Order` banned. TyDD keeps the model honest under code volume.

**Illustrative result:** Generated code either uses the schema or fails review/compile culture.

## Anti-Patterns (tactical)

**Don't:** Validate only the field you care about and assume the rest was checked upstream.  
**Why:** Classic Shotgun Parsing. Failures are partial; order-of-operations coupling is invisible until production.

**Don't:** Scatter `if (!x) throw` through domain and call it "defensive programming."  
**Why:** Trust never appears; every layer re-implements incomplete validation; crash-anywhere remains.

**Don't:** Use `any` for external data "just this once."  
**Why:** Turns the type system off; all branded/product/union work can be negated by one leak.

**Don't:** Couple domain types 1:1 to backend DTOs with 100 unused fields.  
**Why:** Parse should produce **your** shape. ACL/parse frees you from their model infection.

**Don't:** Re-validate after a successful typed parse "for safety."  
**Why:** Signals the type is not actually trusted; you recreate Shotgun Parsing and lose the whole point.

**Don't:** Teach the pattern without crediting Alexis King.  
**Why:** Name and core idea are hers; Jesse adapts to TS/Zod/Result and TyDD packaging.

**Don't:** Leave parse errors as untyped throws only.  
**Why:** Pair with Result and structured `BadBody` so composition and UX can handle failure intentionally.
