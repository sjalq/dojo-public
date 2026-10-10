---
triggers:
  - "user allows any order state to ship, pay, or submit"
  - "workflow bugs from steps in the wrong order"
  - "function signatures hide DB, filesystem, email (ambient authority)"
  - "user asks about typestate, capabilities, DI in FP, or functional core imperative shell"
  - "authorization is a runtime if-throw that should be a type"
use_when:
  - "domain sequences must be legal (draft→submit→pay→ship)"
  - "forms must be validated before submit at the type level"
  - "making side-effect authority explicit via parameters"
  - "keeping domain pure while the shell performs I/O"
fails_when:
  - "states are fake brands with free casts between them"
  - "you pass god-capabilities (entire db + fs + email) to every function"
  - "typestate explodes into unmaintainable micro-states before the workflow is known"
related:
  - "product-and-union-types.md"
  - "pipelines-and-composition.md"
  - "pure-and-total-functions.md"
  - "smart-constructors.md"
  - "schema-at-the-boundary.md"
---

# Typestate and Capabilities

## When to Use

- Wrong **order** of operations is a business bug: shipping unpaid orders, submitting unvalidated forms, canceling without primary authority.
- You already have pipelines/ROP but assembly order is still manual; illegal sequences still typecheck.
- Side-effecting functions look pure in the signature (`() => Promise<void>`) while touching DB, disk, and email (**ambient authority**).
- Tests drown in mocks because domain code reaches for infrastructure freely.
- You want Functional Core, Imperative Shell: pure decisions inside; effects at the edges with explicit permissions.

## Fails When

- Workflow is still exploratory; freeze typestate too early and you thrash types every sprint. Start with DUs for major statuses; tighten transitions when illegal paths appear in bugs.
- "Typestate" implemented as the same mutable object with string tags and no transition functions; nothing is enforced.
- Every function receives a mega `deps` with full ambient power; capabilities become DI theater.
- Culture rejects immutability and pure cores entirely; capabilities still help, but FC/IS needs team buy-in.

## Core Concept

### Typestate: legal transitions only

Pipelines and ROP keep order readable but order remains **hand-assembled**. When wrong order is a domain failure, use **typestate**: encode states and transitions so the compiler rejects illegal assembly.

Bad model:

```ts
type Order = "draft" | "submitted" | "paid" | "ship" | "shipped"
type Ship = (order: Order) => ...
// accepts any state; ship is either a god-function or a bug factory
```

Good model: discriminated union states + **narrow transition functions**:

```text
Draft --Submit--> Submitted
Submitted --Pay--> Paid
Paid --Ship--> Shipment
```

```ts
type Draft = { tag: "draft"; items: Items }
type Submitted = { tag: "submitted"; items: Items; submittedAt: Instant }
type Paid = { tag: "paid"; items: Items; paymentId: PaymentId }

type Submit = (order: Draft) => Result<Submitted, SubmitError>
type Pay = (order: Submitted) => ResultAsync<Paid, PayError>
type Ship = (order: Paid) => ResultAsync<Shipment, ShipError>
```

Wire with ROP: `submit(order).andThen(pay).andThen(ship)`. Wrong order does not compile: `ship(draft)` is a type error.

Jesse's metaphor: **setting up the Roomba**. You clip the transition functions together; the types force the path. Works through abstraction: total top-level signatures guide composition even when internals are hidden (TypeScript errors remain occasionally obtuse; still worth it).

UI form example:

```ts
type Form = NotValidated | ValidForm
type Submit = (form: ValidForm) => ResultAsync<Receipt, SubmitError>
// unvalidated submit does not typecheck
```

Typestate is an established systems idea (academic typestate literature; Rust-ish API practice). Jesse teaches DU states + `andThen` transitions + Roomba metaphor for TyDD. Do not claim he invented typestate.

This is **impossible sequences**, cousin to impossible data shapes (Richard Feldman / Elm "make impossible states impossible" framing for the broader goal).

### Capabilities: authority in the signature

Side effects are hard to type, non-deterministic, and hide what a function can do. **Ambient authority** means the function can reach DB/FS/network because it lives in a process that can, not because the type says so.

```ts
// Signature lies
createReport(): Promise<void>
// actually: queries DB, writes filesystem, emails users
```

**Capabilities** make authority explicit: pass the side-effect functions (or authority-bearing types) the function is allowed to use.

```ts
createReport(
  query: QueryDatabase,
  email: SendEmail
): ResultAsync<ReportId, ReportError>
// can query and email; cannot touch filesystem if FS not passed
```

No capability passed → no authority. In unit tests, capabilities are **pure stubs**. In architecture, pass only what each function needs; keep effects high, away from domain.

Authority via domain types too:

```ts
// Bad: runtime check
cancelPayment(user: User, account: Account) {
  if (!user.isPrimary) throw ...
}

// Better: capability in the type
type CancelPayment = (u: PrimaryUser, a: Account) => ResultAsync<..., ...>
```

Only code that possesses a `PrimaryUser` (from parse/auth typestate) can call cancel. That pairs typestate with capabilities.

### DI in FP and Functional Core, Imperative Shell

In FP, dependency injection is **calling a function with parameters**, including effectful ones. You do not need a DI container framework to pass `fetch`. Historical stigma from Java ceremony is not a reason to reject the technique; DI is both design and testing (Jesse's DI history materials). If someone says DI has nothing to do with testing, they are wrong about decades of practice.

**Functional Core, Imperative Shell:** pure domain decisions and transforms in the core; shell loads data, calls core, performs effects with the capabilities the use-case needs. Elm and Roc push effects to the language edge; Haskell uses IO types; TS/Python do it by discipline and parameters.

Immutability supports this: mutation is a side effect that breaks reasoning mid-pipeline. Prefer returning new values; convention "we return copies" often beats drowning in `readonly` keywords if the culture holds.

## How to Apply

1. **List illegal sequences** from bugs and business rules. Those become typestate transitions.

2. **Model states as DUs** with only the data each state needs (paymentId only on Paid).

3. **Write transition functions** that accept only the legal predecessor and return the next state (or Result).

4. **Compose with ROP.** Roomba wiring at the use-case level; match errors at the shell.

5. **Inventory ambient authority.** For each `Promise<void>` / service method, write the effects it actually performs. Promote them to parameters or restrict via narrower interfaces.

6. **Pass minimal capabilities.** Prefer `QueryUserById` over entire `Database`. Tests stub one function.

7. **Encode role authority as types** when runtime checks are really type invariants (PrimaryUser, AdminToken).

8. **Keep core pure.** Core returns data and decisions (`Result`, commands); shell executes capabilities.

9. **Grow states with the domain.** Do not invent fifteen payment micro-states before Product finishes the flowchart.

## Examples

**Situation:** `ship(order)` runs for draft orders in production; warehouse chaos.

**Application:** `Ship` only accepts `Paid`. Checkout railway: submit → pay → ship. Attempt to ship earlier fails typecheck. Property tests on transitions, not on "ship rejects draft" if draft cannot be passed.

**Illustrative result:** Class of workflow bugs moves from runtime to compile time. LLM-generated "just ship it" code does not compile.

---

**Situation:** `createReport` untestable without DB, FS, SMTP.

**Application:** Split pure `buildReport(data): Report` and effectful `saveAndSend(report, write, email)`. Handler acquires capabilities and calls both. Unit tests cover `buildReport` with fixtures; integration tests cover shell sparsely.

**Illustrative result:** Fast tests, explicit authority, no mock frameworks required for core.

---

**Situation:** Form submit button calls API with raw form state; server is the only validation.

**Application:** Client typestate `ValidForm` produced by `validate: RawForm => Result<ValidForm, FormErrors>`. `submit` requires `ValidForm`. Server still parses (never trust clients) with schema; client gains type-level UX discipline.

**Illustrative result:** Cannot wire submit to unvalidated state in the typechecked app path.

---

**Situation:** `cancelPayment(user, account)` with `if (!user.isPrimary) throw` scattered.

**Application:** Auth boundary produces `PrimaryUser | SecondaryUser` DU. Cancel only on Primary. Secondary paths never see the function.

**Illustrative result:** Authorization failure modes designed at parse/login, not deep in payment noise.

## Anti-Patterns (tactical)

**Don't:** Keep one Order type and a giant switch inside every operation "for flexibility."
**Why:** Flexibility means illegal calls compile. Transition functions are the flexibility that matches the business.

**Don't:** Hide effects in empty signatures and discover them by reading the body.
**Why:** Ambient authority is how surprises ship. Capabilities make the type document blast radius for humans and LLMs.

**Don't:** Pass the world as `deps: any` or a 40-service god object to every function.
**Why:** That reintroduces ambient authority with extra steps. Narrow interfaces; partial-apply at the shell.

**Don't:** Implement typestate with forgeable casts (`as Paid`).
**Why:** Same failure mode as forgeable Email. Transitions are the only legal constructors of the next state.

**Don't:** Teach capabilities as hardcore capability-security theory before showing `sendEmail` as a parameter.
**Why:** Parameterized effects are enough for enterprise TS. Depth reading is optional; shipping pure cores is not.

**Don't:** Force the whole org onto monadic IO encodings on day one.
**Why:** FC/IS + Result + explicit parameters delivers most value in gradually typed stacks. Escalate to Effect/Elm/Haskell style when the team is ready, not as a purity purity test.
