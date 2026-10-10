---
triggers:
  - "user creates Email, Money, or ID with plain strings and as-casts"
  - "user asks about opaque types, branded types that cannot be forged, or smart constructors"
  - "validation is optional at construction and required at every use"
  - "Maybe/Option vs Result for construction failure"
  - "integrating unsafe JSON.parse, third-party classes, or throwing APIs safely"
use_when:
  - "a value should only exist if it passed validation"
  - "exporting a type for use while hiding how to forge it"
  - "wrapping unsafe or partial APIs in small total makers"
  - "replacing crash-in-constructor OOP intent with typed construction"
fails_when:
  - "the brand symbol is exported or `as Email` is accepted culture-wide"
  - "every struct field gets an opaque type with no real invariant"
  - "makers throw instead of returning Result/Maybe and reintroduce partiality"
related:
  - "schema-at-the-boundary.md"
  - "product-and-union-types.md"
  - "pure-and-total-functions.md"
  - "pipelines-and-composition.md"
  - "anti-corruption-layer.md"
---

# Smart Constructors, Opaque Types, and Maybe

## When to Use

- Domain values must be valid to exist: Email, Money, AccessToken, NonEmptyString, Percentage 0-100.
- Branded types are forgeable: `const e = "🐮" as Email` still compiles.
- You integrate unsafe code (JSON.parse casts, throwing libs, mutable SDK classes) and need a safe production path.
- Null/undefined checks litter the core; you want Option/Maybe at edges or Result when failure has meaning.
- OOP code taught misuse by throwing in constructors; you want the type signature to communicate "might fail" instead.

## Fails When

- Opacity without a real invariant (opaque `UserName` that accepts any string) is ceremony.
- You export the unique symbol / brand and anyone can forge values; opacity is theater.
- Smart constructors throw or return bare null without forcing handling; you recreated partial functions with extra steps.
- You opaque everything on day one of domain discovery; start with brands/products, tighten construction where bugs appear.

## Core Concept

### Smart constructors (not class constructors)

In gradually typed and mixed codebases you integrate **lying signatures**, throws, bad casts, and third-party classes. A **smart constructor** means: **make a thing; construction might fail.** It is a known FP/domain-modeling term (Haskell community, Scott Wlaschin-style domain modeling, and others). Jesse teaches it for TypeScript integration, not as a personal invention.

```ts
// Lying
function unsafeParse(s: string): MyType {
  return JSON.parse(s) as MyType
}

// Smart constructor shape
type MakeMyType = (s: string) => Result<MyType, JSONError | ZodError>

function makeMyType(s: string): Result<MyType, JSONError | ZodError> {
  try {
    const json: unknown = JSON.parse(s)
    const parsed = schema.safeParse(json)
    if (!parsed.success) return err(parsed.error)
    return ok(parsed.data)
  } catch {
    return err({ tag: "JSONError" })
  }
}
```

Work in **small batches**. You cannot wrap the world in one PR. Wrap the next unsafe edge you touch.

Helpers: neverthrow `Result.fromThrowable`, Effect error channels, schema safeParse. Escape try/catch only to map into Result.

Contrast old OOP: Singleton throws in constructor to say "you're using it wrong." The design did not communicate intent; the crash did. Types now communicate ergonomics: makers return Result; invalid instances do not exist.

### Opaque types

Some types may only exist on the happy path of construction. **Opaque** means consumers can *use* the type but cannot *see through* or *forge* the underlying structure. Couple the exported type with a safe maker; hide the brand.

```ts
declare const EmailBrand: unique symbol // NOT exported

export type Email = string & { readonly [EmailBrand]: "Email" }

export function makeEmail(value: string): Email | undefined {
  // or Result<Email, EmailError>
  if (!isValidEmail(value)) return undefined
  return value as Email
}
```

Forgeable brand problem: if the brand is a plain string property anyone can `as`, opacity failed. Unique symbol not exported is the TS recipe. Candidates: Email, Money, ValidJSON, AccessToken, anything you would validate before creation.

Opaque is a blanket teaching term covering careful brands, phantoms, and module-hidden products/DUs. Longstanding FP practice (Haskell newtypes, module boundaries). The curriculum packaging is practical TS.

Blast makers with **property tests**: random strings mostly fail; valid samples always produce values that round-trip your rules.

### Maybe / Option

**Option/Maybe** models absence and replaces null/nil/undefined. ML-style `Some | None` as a discriminated union forces handling. Tony Hoare invented null; implementations crashed far from introduction sites. Tagged option "fixed" a large class of null pointers when the language forces the match.

In TypeScript/Python you often have `string | undefined`. Name it when it matters: `type EnvironmentVariableMaybe = string | undefined`. Strict mode makes accidental nulls rarer unless you opt out with `any` / `as`.

Jesse's **Gartner hype cycle** for Maybe:

1. Love it (null pointers vanish).
2. Hate defaults and unhappy paths everywhere.
3. Ban optionals entirely.
4. Realize env vars and real absences exist.
5. Treat Maybe like side effects: **push to the edges** (Functional Core, Imperative Shell). Prefer **Result** when "none" is actually an error with meaning.

Modern FP languages like Roc can omit Maybe and lean on unions/Result. Learn the hype cycle so you use Maybe deliberately, not as free perfume on every field.

### Only valid instances exist

The combined move: opaque type + smart constructor (+ schema at system boundary). Domain functions take `Email`, not `string`. They never validate email format. Invalid emails are not representable inside the core. That is Parse, Don't Validate for single values, and a building block for making impossible states impossible (Richard Feldman / Elm community framing).

## How to Apply

1. **List forgeable "validated" types.** Anywhere you `as Brand` or comment "must be valid email," introduce opacity + maker.

2. **Choose failure channel.** Construction failure as domain error → `Result<T, E>` with context. True optional absence → `T | undefined` / Maybe, handled at edge. Prefer Result when you would log or show why.

3. **Hide the brand.** Module boundary: export type + `makeX` / `parseX`; do not export symbol or raw constructor.

4. **Parse at system edges with schema;** use smart constructors for single-field refinement or unsafe lib wrap. They stack: schema produces strings, `makeEmail` produces `Email`, or schema refine does both.

5. **Integrate unsafe code in batches.** One throwing SDK method → one `Result` wrapper. Do not rewrite the monorepo before the next feature ships.

6. **Property-test makers.** Valid samples succeed; invalid fail; no throws from maker.

7. **Push Maybe outward.** Core prefers concrete values and Result. Optional config resolved at startup into a total `Config` product.

8. **Document for OOP teammates.** "Smart constructor" ≠ `class` constructor. It is a total-ish function that returns the value or a typed failure.

## Examples

**Situation:** Payment code takes `amount: number` and `currency: string`; negative amounts and `"usd "` slip in.

**Application:** Opaque `Money` product made only via `makeMoney({ amount, currency })` returning `Result<Money, MoneyError>`. Domain `add` accepts `Money` only. Schema at HTTP uses the same maker or shared refine.

**Illustrative result:** Negative money does not exist in domain. Tests drop "rejects negative" cases on every service method; one maker suite covers it.

---

**Situation:** `as UserId` from headers; customer and user IDs swapped in a bug.

**Application:** Opaque/branded `UserId` and `CustomerId` with separate makers from header strings. Purchase function accepts only `CustomerId`. Swap does not compile.

**Illustrative result:** Primitive obsession ends for IDs. LLM-generated code cannot pass the wrong string without maker.

---

**Situation:** `JSON.parse` + cast in five modules; one throws SyntaxError, another returns partial objects.

**Application:** Single `makeThings(s: string): Result<Thing[], ParseError>` smart constructor used by all five. Internals: try/catch + schema.

**Illustrative result:** Consistent errors; railway-friendly. Partial casts deleted.

---

**Situation:** Domain model has `email?: string` on every DTO; half the code assumes present.

**Application:** After login parse, `User` has required `Email` opaque. Pre-login form state is a DU: `Anonymous | LoggedIn<User>`. Maybe stays at form field edges, not inside LoggedIn.

**Illustrative result:** Optional spam retreats to real optionality. Core stops null-checking email.

## Anti-Patterns (tactical)

**Don't:** Forge brands with `as Email` to "save time" in app code.
**Why:** You destroyed the invariant for everyone downstream. If tests need values, export `unsafeEmailForTests` gated by lint, or better, use the real maker with fixtures.

**Don't:** Throw from constructors/makers to signal invalid input as the primary API.
**Why:** That is partial. Callers need try/catch; composition dies. Return Result/Maybe so types tell the story.

**Don't:** Prefer Maybe over Result when the failure has a reason users or devs need.
**Why:** `undefined` loses context. "Invalid email format" and "disposable domain blocked" are Result payloads, not silent None.

**Don't:** Spread optional fields through the functional core "because the JSON had them optional."
**Why:** Parse into required fields or a readiness DU. Treat optionality like effects: push to edges.

**Don't:** Claim you invented opaque types or smart constructors.
**Why:** Credit the FP tradition; teach the TS recipe. Jesse's value is curriculum and enterprise pragmatism, not renaming ancient tools.

**Don't:** Require understanding of type theory universes before `makeEmail`.
**Why:** If the string has an `@` and your product rules pass, return `Email`. Ship. Gatekeeping helps no on-call rotation.
