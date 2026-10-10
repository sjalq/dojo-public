---
triggers:
  - "user asks how to make invalid states unrepresentable or make impossible states impossible"
  - "user models UI/domain state with optional flags that allow illegal combinations"
  - "user wants fewer tests by encoding invariants in types"
  - "user asks about product types, unions, and brands together as a design goal"
  - "user wonders how much type safety is enough (spectrum / ROI)"
use_when:
  - "domain or UI allows combinations that must never happen (loading+error+data, unpaid ship, wrong ID kinds)"
  - "you are choosing algebraic modeling (brand + product + union) over only tests and runtime checks"
  - "LLMs or juniors keep inventing illegal states and you need the compiler as a second line of defense"
fails_when:
  - "types are treated as replacing all tests"
  - "maximal type cleverness without ROI or team readability"
  - "illegal sequences of legal states are ignored (need typestate / property tests too)"
related:
  - "branded-types.md"
  - "type-driven-development.md"
  - "result-and-errors-as-values.md"
  - "parse-dont-validate.md"
  - "railway-oriented-programming.md"
---

# Making Impossible States Impossible

## When to Use

- Domain or UI state is modeled so that **illegal combinations still typecheck** (loading + data + error; draft order that can ship; UserID passed where CustomerID required)
- You want types to **shrink** the space of happy/unhappy/edge cases you must test and keep in your head
- Refactors should be guided by the compiler when designers add a state or product changes a rule
- Pairing with TDD: types make tests more focused and changes safer
- AI-assisted coding: types act as a second compiler for invariants while volume of code rises

## Fails When

- You claim types replace tests entirely (algorithms, illegal *sequences*, product correctness still need tests)
- You push black-and-white maximal safety with unreadable types and no ROI judgment for the team
- You only fix static shapes and ignore illegal transitions between valid states (typestate + property tests)
- Mutation quietly rebuilds impossible situations after careful construction (immutability matters)
- Culture cannot absorb the learning cost yet; shame and dogma backfire (see TyDD final thoughts)

## Core Concept

### Attribution

**Make illegal situations hard or impossible to represent.** Don't model a form as "status string plus optional fields that only make sense sometimes." Model the states as different shapes so "confirmed without evidence" or "shipped without paid" simply cannot be built. That goal drives branded IDs, unions, non-empty lists, and transition functions that only accept the previous state.

*(The popular talk slogan is associated with Richard Feldman / Elm community. Teach the goal; name the talk if asked.)*

### Why it matters

Without strong modeling, behavior lives mainly in tests and free functions/methods. Types, if you lean into algebraic structure, can **greatly speed up and simplify** what you write and **reduce how much you write**, including how many tests you need. Types **narrow or shrink** how many cases you deal with.

They are also a design, refactoring, and communication tool, a Continuous Delivery shift-left check, and a way to keep LLMs honest under higher code volume. Encode how the software works for both you and AI; remove fear from change.

### The three most powerful tools (Big 3)

Jesse highlights three:

1. **Branded types** — prevent mixing up values that share a primitive representation (see [branded-types.md](branded-types.md))  
2. **Product types** — ensure data that belongs together changes together (AND: this *and* that)  
3. **Unions / Discriminated Unions** — restrict what is allowed (OR: this *or* that); classic tool for impossible situations  

#### Brand: separate things

`CustomerID` vs `UserID` both strings underneath, different types. Wrong ID cannot be passed to `purchase`. Domain words match business language.

#### Product: things that belong together

```ts
// positional / boolean blindness
createUser("Jesse", "Warden", "jesse@...", true, false)

// product
createUser({ firstName, lastName, email, isAdmin, sendWelcomeEmail })
```

Nested products (`Person` with `Address`), DI bags, fixtures via spread. Self-documenting call sites; API growth without positional churn. Foundation for invariants that span fields.

#### Union / DU: what is allowed

Open `string` allows `"moo"`, emoji, empty. Closed union:

```ts
type AccountType = "Primary" | "Secondary" | "Authorized"
```

UI anti-pattern:

```ts
type Request = { loading: boolean; data?: User; error?: string }
// allows { loading: true, data: user, error: "failed" }
```

Rewrite:

```ts
type Request =
  | { tag: "loading" }
  | { tag: "success"; data: User }
  | { tag: "error"; error: string }
```

Only error can access `error`; only success can access `data`. Exhaustiveness checking forces every variant handled when you add `cancelled`. No `default: "shouldn't happen"` as a substitute for complete handling.

Replace bare `User | null` with named Found/NotFound when communication matters.

### Beyond the Big 3 (still in service of the goal)

- **Non-empty collections / AtLeast1** — "must have at least one" not plain empty array  
- **Indexed types / generics** — money same-currency add as a type rule  
- **Parse don't validate** — illegal shapes never enter ([parse-dont-validate.md](parse-dont-validate.md))  
- **Result + errors as values** — failure is a typed state, not a random throw ([result-and-errors-as-values.md](result-and-errors-as-values.md))  
- **Typestate** — illegal *order* of legal states (submit before pay before ship)  
- **Capabilities** — illegal authority (secondary canceling primary's payment) encoded in parameters  
- **Immutability** — mutation can recreate partial or illegal situations after construction  
- **Railway composition** — larger total programs without reopening every failure by hand  

### Spectrum and ROI honesty

Making impossible states impossible should be the **goal**, but it is **not black and white**; it is often a **spectrum with nuance**.

Ask:

- How much type safety is valuable *here*?  
- Are the types readable for *this* team?  
- Some type systems are weak (more tests needed); some have steep learning curves  

No shame being pragmatic and shipping while skill grows over many releases ([type-driven-development.md](type-driven-development.md) Part 26 tradeoffs). Amanda Laucher and Paul Snively's "Types vs. Tests" is the classic tension: how far you push types is limited by understanding.

### Still need tests

To be clear: **you still need tests**. Types make working with TDD easier: enforce more in the compiler, focus tests, keep tests and code safer to change. Property tests measure how total functions are and catch illegal sequences DUs alone don't prevent. Compiling ≠ correct algorithm (Elm Advent of Code lesson).

### LLMs + types

LLMs can understand types, infer what to build much like unit tests, and help ensure invariants are not violated: a **second type of compiler** while you work and change code as you learn. They can also offer gradual type-safety options. Types constrain human *and* model drift. They do not remove review: AI still invents unneeded fields and anti-DRY bulk if unconstrained.

## How to Apply

1. **List illegal situations** that currently typecheck (write them as examples that must not compile or must not parse).

2. **Apply Big 3 in order of pain:**  
   - Mixups of same-shaped values → brands  
   - Related fields / mystery booleans → products  
   - Mutually exclusive modes → unions/DUs  

3. **Parse at the boundary** so illegal external shapes never become domain values.

4. **Use exhaustiveness** (switch/match without lazy defaults) so new states force updates everywhere.

5. **For workflows,** add typestate: functions only accept the legal predecessor type (`Ship = (order: Paid) => ...`).

6. **For authority,** put capability in the type (`PrimaryUser`) instead of runtime `if (!u.isPrimary) throw` alone.

7. **Practice TyDD loops** (compiler red/green, `@ts-expect-error`, type proofs, interleave TDD) so impossible becomes a failing red you fix on purpose.

8. **Judge ROI.** If the type is unreadable and the risk is low, a focused test may win today; revisit when the invariant keeps biting.

9. **Keep tests** for transitions, property sequences, and logic types cannot express.

## Examples

**Situation:** React/Elm-style request state with booleans and optionals; UI sometimes shows spinner and error and data together.

**Application:** Discriminated union with `tag`; render with exhaustive match; no default "shouldn't happen."

**Illustrative result:** Illegal combo unrepresentable; adding `cancelled` lists every update site via the compiler.

---

**Situation:** `Order = 'draft' | 'submitted' | 'paid' | 'shipped'` and `ship(order: Order)` accepts any state; bugs or giant untested branches inside ship.

**Application:** Separate state types + transitions: `Submit = (Draft) => Result<Submitted, _>`, `Pay = (Submitted) => ...`, `Ship = (Paid) => ...`. Wire with andThen ("setting up the Roomba").

**Illustrative result:** Unpaid ship does not compile; business rules live in types, not only tests.

---

**Situation:** Secondary account cancels Primary's transaction; runtime check sometimes forgotten; LLM regenerates the bug.

**Application:** Brand/account types + function types that only allow legal cancel pairs; `@ts-expect-error` on Sydney canceling Jesse; parse brands at API edge.

**Illustrative result:** Impossible authorization state is a type error; model keeps AI honest.

---

**Situation:** Team asks "do we still need unit tests if we do this?"

**Application:** Yes. Types shrink case space and encode invariants; tests cover algorithms, sequences, and integration. Together they rock; either alone is not enough.

**Illustrative result:** Smaller, sharper tests; fearless refactor remains the goal.

## Anti-Patterns (tactical)

**Don't:** Model exclusive states as independent booleans/optionals.  
**Why:** Product of flags explodes into illegal combinations the compiler accepts.

**Don't:** Rely on `default: "shouldn't happen"` instead of exhaustiveness.  
**Why:** New variants silently hit the default far from the design change.

**Don't:** Treat "Making Impossible States Impossible" as absolute purity theater.  
**Why:** Spectrum with nuance; readability and ROI matter; pragmatic shipping is allowed.

**Don't:** Encode invariants only as runtime throws after half-typed APIs.  
**Why:** Callers will mix USD/EUR or wrong states "by accident"; business rules belong in types when the system can express them.

**Don't:** Forget sequences: all static states legal but transitions illegal.  
**Why:** DUs alone don't prove state machine traces; add typestate and/or property tests on action sequences.

**Don't:** Teach the slogan without crediting Richard Feldman / Elm framing.  
**Why:** Jesse operationalizes it; the talk framing is Feldman's community gift.

**Don't:** Drop tests because "impossible states are impossible."  
**Why:** Wrong math still compiles; wrong defaults in chains still compile; product still needs proof beyond shape.
