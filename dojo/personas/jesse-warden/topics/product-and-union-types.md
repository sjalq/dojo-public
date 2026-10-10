---
triggers:
  - "user is modeling domain data with objects, flags, optional fields, or string enums"
  - "user has boolean blindness, positional parameters, or mystery true/false args"
  - "user has a state bag like loading + data + error that allows impossible combinations"
  - "user asks about product types, records, DTOs, unions, or discriminated unions"
  - "user needs exhaustiveness checking on a switch over domain variants"
use_when:
  - "discovering what domain concepts belong together (product / AND types)"
  - "restricting what values or states are allowed (union / OR types)"
  - "replacing open strings and optional-field state bags with closed alternatives"
  - "wanting the compiler to force every branch when variants grow"
fails_when:
  - "you over-model every flag into a mega-union before the domain is clear"
  - "you use unions without a discriminant and lose safe field access"
  - "you paper over missing cases with a default that swallows new variants"
related:
  - "smart-constructors.md"
  - "non-empty-and-indexed-types.md"
  - "schema-at-the-boundary.md"
  - "typestate-and-capabilities.md"
  - "pipelines-and-composition.md"
---

# Product Types and Unions

## When to Use

- After you separate domain concepts (often with branded types), you ask the next question: **what belongs together?**
- Call sites have positional chaos or mystery booleans: `createUser("Jesse", "Warden", email, true, false)`.
- You have an open `string` for a closed domain set (`"Primary" | "Secondary" | "Authorized"`).
- UI/API state is a bag of optionals that can be loading, success, and error at once.
- You want **exhaustiveness**: when Product adds a variant or Marketing renames an account type, every switch fails until you handle it.

## Fails When

- You invent a 40-case union on day one of domain discovery. Start with products and small closed sets; grow as code teaches you.
- You model mutually exclusive states as independent booleans/optionals and "promise" the team not to set them wrong.
- You put a silent `default` on every switch so the compiler never nags you when a new tag ships.
- You treat product types as "just DTOs" and stop there, never using unions to shrink impossible combinations (Richard Feldman's framing: make impossible states impossible).

## Core Concept

Type Driven Development is not category theory cosplay. It is using the type system as a design tool, a communication tool, and a way to write fewer tests for classes of bugs that types can kill for free. Jesse's pedagogical "Big 3" for domain modeling:

1. **Branded types**: this is a *thing* (a `CustomerID` is not a `UserID`).
2. **Product types**: this *and* that belong together.
3. **Unions / discriminated unions**: this *or* that is allowed.

Product types are records/objects. OOP folks already know DTO and Value Object. The point is cohesion discovery: group data that changes together, pass one named bag instead of five mystery parameters, and evolve the shape without thrashing every call site.

```ts
// Positional / boolean blindness
createUser("Jesse", "Warden", "jesse@example.com", true, false)

// Product type: self-documenting, evolvable
createUser({
  firstName: "Jesse",
  lastName: "Warden",
  email: "jesse@example.com",
  isAdmin: true,
  sendWelcomeEmail: false,
})
```

When you later add `locale`, `createUser(user)` still works; only the product grows. Combine with `Partial` / `Omit` / `Pick` when you need flexibility. Nest products as you discover more structure:

```ts
type Address = { street: Street; city: City }
type Person = { name: Name; address: Address }
```

Same idea for dependency bags in functional code:

```ts
type Dependencies = {
  db: Database
  logger: Logger
  emailService: EmailService
  paymentService: PaymentService
}

processOrder(deps, order)
```

Unions answer a different question: **what is allowed?** An open string allows `"moo"`, `"🐄"`, and `""`. A closed union does not.

```ts
type AccountType = "Primary" | "Secondary" | "Authorized"
```

Discriminated unions (tagged unions, sum types, algebraic data types under other names) attach *different data per alternative*. That is how you kill the classic impossible request state:

```ts
// Bad: loading + data + error can all be set
type Request = {
  loading: boolean
  data?: User
  error?: string
}

// Good: exactly one situation at a time
type Request =
  | { tag: "loading" }
  | { tag: "success"; data: User }
  | { tag: "error"; error: string }
```

Only success has `data`. Only error has `error`. The compiler blocks wrong field access. Prefer named alternatives over bare `User | null` when Found/NotFound communicates better.

**Exhaustiveness checking** is the enforcement mechanism. Switch on the discriminant without a default (or with a `never` check). When someone adds `{ tag: "stale" }`, every incomplete handler becomes a compile error. That is fewer "forgot the new status in the UI" bugs and less need for unhappy-path unit tests that only assert "we handled every enum."

Product = AND. Union = OR. Together they are how you encode business invariants so bad combinations never compile. You still need tests for algorithms and behavior. Types shrink the space of nonsense you must defend with tests.

You do not need monads lectures to ship this. Elm and ReScript give you this everyday. TypeScript gives you it with a bit more ceremony. Python can approximate with TypedDict, enums, and careful runtime checks. The idea travels; the compiler help varies.

## How to Apply

1. **Name the separate things first.** If IDs and concepts are all `string`, brand or opaque them so the product is not a bag of interchangeable primitives.

2. **Group what changes together.** Look at call sites with long parameter lists. If three arguments always travel as a set, that is a product type. Prefer `createUser(user)` over growing positional APIs.

3. **Replace open strings with closed unions** for domain sets that Product/BA already treat as fixed vocab. Put the same words in the type that users and design use (DDD ubiquitous language, not type-theory jargon).

4. **Rewrite optional-field state bags as discriminated unions.** Loading/success/error, draft/paid/shipped, found/not-found. One tag, payload only on the tags that need it.

5. **Switch exhaustively.** No silent default. Use a `never` residual if your language needs it so new variants break the build.

6. **Compose products inside products** as cohesion discovery continues. Do not force a flat god-object; nest when nested concepts are real.

7. **Use product types for test fixtures.** Spread defaults: `{ ...defaultOrder, country: canada }`. Easier variants, less constructor ceremony.

8. **Let products feed later TyDD moves.** Same-currency money needs indexing into product fields. Typestate transitions are DUs with narrow functions. Results are DUs for happy/unhappy paths. Products and unions are the substrate.

## Examples

**Situation:** A signup function takes five positional args, two of which are booleans nobody remembers at the call site.

**Application:** Introduce a `CreateUserInput` product. Call sites become labeled. Adding `locale` or `marketingOptIn` is a product change, not a mass signature rewrite. Optionally brand `Email` inside the product so invalid emails never enter as plain strings.

**Illustrative result:** PRs stop bikeshedding argument order. Reviewers read intent. LLM-generated call sites with swapped booleans fail typecheck instead of shipping.

---

**Situation:** A React/Angular request model is `{ loading, data?, error? }` and QA finds a spinner with stale data and an error toast at once.

**Application:** Replace with a tagged `Request` DU. View code switches on `tag`. Success branch only sees `data`; error only sees `error`. Exhaustiveness forces a loading UI when a new `revalidating` tag appears.

**Illustrative result:** Impossible UI states stop compiling. You delete unit tests that only asserted "don't show error and data together."

---

**Situation:** Account types live as free strings from a legacy API; sales invented "Authorized" last quarter and half the switches still assume Primary/Secondary.

**Application:** Closed union `AccountType` at the domain boundary (after schema/ACL). Exhaustive switches in billing and permissions. Schema parse rejects unknown strings into a typed error instead of silent fallthrough.

**Illustrative result:** Deploy fails at compile time when a new type is added without handling; runtime "default Primary" footguns go away.

---

**Situation:** DI list is `processOrder(db, logger, email, payment, order)` and every test wires five mocks in different orders.

**Application:** `Dependencies` product type. Pass `deps` plus domain data. Tests build one fixture bag and override one capability at a time.

**Illustrative result:** Call sites stay stable as services grow. Capability thinking (pass only what you need) becomes natural next step.

## Anti-Patterns (tactical)

**Don't:** Keep "boolean blindness" because "the team knows what the third `true` means."
**Why:** The team rotates. LLMs and juniors do not know. Named product fields cost almost nothing and remove a class of swap bugs without a single unit test.

**Don't:** Model exclusive states as independent optionals "for flexibility."
**Why:** Flexibility here means invalid combinations compile. Discriminated unions are not less flexible; they are honest about which combinations exist. Richard Feldman and the Elm community hammered this for UI state; it applies to orders, forms, and accounts too.

**Don't:** Put a catch-all `default` that logs and continues.
**Why:** You just turned off exhaustiveness. New business variants become silent no-ops in production. Prefer compile failure over quiet wrong behavior.

**Don't:** Confuse product types with "we must use classes and getters."
**Why:** A product type is a cohesion decision, not an OOP religion. Plain TS types, Elm records, Python dataclasses, ReScript records all work. Behavior can live in pure functions next to the data.

**Don't:** Skip unions because "TypeScript unions are structural and weak."
**Why:** Tag your DUs. Use `tag` or `type` discriminants. The structural system still narrows correctly on tags. Perfect nominal purity is not required to get most of the value.

**Don't:** Teach this as category theory prerequisites.
**Why:** Product and sum types are everyday modeling. If someone needs a monoid lecture to group firstName and lastName, the teaching failed. Ship software; credit the math when useful, never as a gate.
