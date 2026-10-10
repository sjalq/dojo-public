---
triggers:
  - "user asks how to practice type-driven development or TyDD"
  - "user asks how types relate to TDD or when to use types vs tests"
  - "user wants a gradual path into stronger typing without dogma"
  - "user asks how types keep LLMs honest or constrain AI-generated code"
  - "user is adopting TypeScript/Elm/ReScript and needs a design technique, not just syntax"
use_when:
  - "designing or refactoring with types as a red/green loop, not only as annotations after the fact"
  - "team needs proofs for easy-to-change code and is choosing how hard to push the type system"
  - "integrating weakly typed code and still wanting total, testable boundaries"
fails_when:
  - "types are treated as a pure theory exercise with no red/green practice loop"
  - "team shame for shipping pragmatically, or maximal type safety without ROI/readability judgment"
  - "types are used as a total replacement for tests rather than alongside them"
related:
  - "impossible-states.md"
  - "result-and-errors-as-values.md"
  - "branded-types.md"
  - "parse-dont-validate.md"
  - "railway-oriented-programming.md"
---

# Type Driven Development (TyDD)

## When to Use

- You want a **design technique** that produces proofs for easy-to-change code, the same way TDD produces proofs through tests
- Your language has a usable type system (TypeScript, Elm, ReScript, Scala, Python typing, etc.) and you want types to drive design, refactoring, communication, and Continuous Delivery shift-left checks
- LLM volume is up and you need constraints so generated code cannot casually invent wrong domain shapes
- You need a practical adoption path: four concrete practice modes, not a lecture on category theory
- You are deciding **how much** type safety is valuable here, for this team, on this problem

## Fails When

- TyDD is pure theory: no compiler red/green, no negative type tests, no proofs, no interleaving with real TDD
- You only type happy paths and never force illegal calls to fail at compile time
- You treat types and tests as mutually exclusive; Jesse's line is they work **together** (more types in a good system, more tests in a weak one)
- You ignore tradeoffs: cognitive dual-mode (types + code), politics, untyped integration, learning cost. Pretending types are free kills adoption
- You shame the team for shipping simply when the type skill is still thin; learning is iterative over many releases

## Core Concept

**Type Driven Development (TyDD) is a lot like Test Driven Development (TDD): a design technique that results in proofs for easy to change code later.** In most languages you use them together. Better type systems lean on types; weaker ones lean on tests. The point is not dogma. The point is proofs that make change safe.

Jesse packages TyDD as a curriculum for enterprise TypeScript and gradual systems, not as Category Theory gatekeeping. He is an engineer delivering software: types as tools for design, refactoring, communication, Continuous Delivery, **keeping LLMs honest**, and **reducing** (not eliminating) how many tests you write. That framing runs through the whole series.

### The series promise (what types are for)

1. Software quality tool  
2. Continuous Delivery / shift-left quality  
3. **LLM honesty** constraint (models understand types much like unit tests; types act as a second compiler while you and the model change code)  
4. Design and refactoring tool  
5. Communication tool (domain words in types)  
6. Test reduction: encode invariants so entire classes of unhappy-path tests disappear  

### The goal, not the dogma

The umbrella goal is **Making Impossible States Impossible** (Richard Feldman's Elm talk framing; see [impossible-states.md](impossible-states.md)). Brand, product, and union types shrink the space of cases you must keep in mind and test. Still: spectrum with nuance, ROI, readability for the team. You still need tests. Types make TDD safer and more focused.

### Tradeoff honesty (Part 26)

Types have real costs:

- **More to read and comprehend.** You often think in two modes: types + code. Amanda Laucher and Paul Snively's Strange Loop talk "Types vs. Tests" is the classic framing: how far you can push types is limited by understanding.
- **Team decision, not heroics.** Invest for the benefits, or do something simpler for now. **No shame being pragmatic and shipping.** Learning is iterative; skill and breadth grow over many releases.
- **Career and politics.** Types are less popular than infrastructure, IDEs, tests, language features. Positive impact on design and quality does **not** reliably translate to job opportunities or leadership importance outside rare language communities. You navigate PM, design/UX, and sales of the techniques **while** doing the engineering job. Niche makes that harder.
- **Same politics as other quality practices.** Code review, automated tests, Continuous Delivery: evidence and knowledge existed for decades before they were normal. Companies ignore science, don't know it, or cannot balance quality with delivery.
- **Integration with the real world.** Code keeps arriving from the team, other teams, library authors: much untyped or weakly typed. You learn both "what's good for our domain" and **how to safely integrate** external code (smart constructors, parse-don't-validate, anti-corruption layers).
- **Cultural loneliness is real.** You'll be confused why everyone hasn't adopted sum types; that never fully goes away. Jesse says this not to dissuade you but to prepare you. In his experience types are worth it. "Hard to learn" is a great problem for a profession full of people who learn every day.

None of that means "never start." Gradual adoption + small batches + spectrum ROI is the path.

## How to Apply

### Four ways to practice TyDD (Part 25)

Running domain constraint used in the article: **Secondary accounts cancel only their own transactions; Primary can cancel any.** Fixtures: Jesse primary, daughter Sydney secondary. Same rule, four practice loops.

#### Way 1: Compiler-driven red/green (good type systems)

1. Write code  
2. Fix the red (compiler errors)  
3. Refactor  

Keep changes small. Each break, let the compiler list what to fix. This is TDD's red/green/refactor with the type checker as the failing test suite for structural and domain-shape proofs.

#### Way 2: `@ts-expect-error` negative type tests

For unhappy paths the compiler should reject:

1. Create a **failing type usage** with a comment above the illegal call:

```ts
// @ts-expect-error Sydney must not cancel Jesse's transaction
cancelPayment(jesseTransaction, sydney)
```

2. Implement the simplest function so the *illegal* call is a real type error (the comment must not be red for the wrong reason).  
3. When `@ts-expect-error` is no longer underlined, refactor types **or** add happy paths without the comment (e.g. `cancelPayment(jesseTransaction, jesse)`).

**Caveat:** the comment must sit above the actual compiler error; multi-line types may require moving it.

This is how you test "this must not compile" without inventing a second language.

#### Way 3: Type proofs

1. Write a **failing proof** (e.g. `Assert<CanCancel<...>>` that should be true or false as designed).  
2. Improve the type (`CanCancel` conditional types with `PrimaryAccount` / `SecondaryAccount` and equality on owner id) until the proof passes.  
3. Refactor or add more proof tests.

Type proofs are compile-time assertions (like Vitest's `expectTypeOf` / `assertType` family). They don't ship in runtime JS. Use them when the invariant is about type relationships, not only about values at runtime.

#### Way 4: Interleave with classic TDD

Mix any of ways 1–3 **while** doing classic TDD:

1. Write expectation (`canCancel` primary case `toBe(true)`)  
2. Simplest implementation to pass  
3. Refactor or next test  

**Jesse: "That's what I do."** Types and tests are not rivals. Types encode what the type system can prove; tests cover transitions, algorithms, and everything types leave open.

### Gradual adoption path

1. Start with the **Big 3**: branded types (separate things), product types (AND together), unions/DUs (OR allowed). See [branded-types.md](branded-types.md) and [impossible-states.md](impossible-states.md).  
2. Put **errors as values** and `Result` on expected failures. See [result-and-errors-as-values.md](result-and-errors-as-values.md).  
3. **Parse once at the boundary** (`unknown → YourType`). See [parse-dont-validate.md](parse-dont-validate.md).  
4. Compose with **pipelines**, then **Railway Oriented Programming** when steps return `Result`. See [railway-oriented-programming.md](railway-oriented-programming.md).  
5. Measure totality with property tests; prove hard invariants with type proofs when needed.  
6. Accept **spectrum ROI**: how much type safety is valuable *here*? Are the types readable for *this* team?

### Keep LLMs honest

Series framing: as LLM use increases code volume, double down on shift-left practices. Types:

- Constrain shapes the model can invent (wrong ID types, loading+error+data bags, open strings for closed sets)  
- Act as a second compiler while you and the model iterate  
- Give the model something to *infer from* the way unit tests do  
- Still need human review and tests; types reduce drift, they don't replace judgment  

If the model suggests bulk unneeded fields (anti-TDD minimum), types that only encode *current* domain concepts make that bloat fail earlier.

### Types vs tests (policy)

- Types + tests together rock; either alone is not enough  
- Compiling with no runtime errors ≠ correct algorithms (Elm Advent of Code lesson: massive bugs in code that compiles)  
- Weak type systems need more tests; sounder systems still need property, integration, and domain tests for transitions and logic  
- Use types to **focus** tests on what types cannot prove (sequences, races, business math, UX)

## Examples

**Situation:** Secondary account must not cancel Primary's transaction; you are in TypeScript.

**Application (Way 2 + Way 4):** Encode `PrimaryAccount` / `SecondaryAccount` and transaction ownership in types. Write `@ts-expect-error` on `cancelPayment(jesseTransaction, sydney)`. Implement until that line is a real error and `cancelPayment(jesseTransaction, jesse)` typechecks. Also write a classic TDD expectation for the runtime predicate if any remaining logic lives outside the type.

**Illustrative result:** Illegal cancellation is unrepresentable at compile time; remaining tests stay short and focused.

---

**Situation:** Team is drowning in AI-generated PRs with mixed ID strings and optional-field state bags.

**Application:** Introduce branded IDs at the HTTP parse boundary (Zod `.brand`), rewrite request UI state as a discriminated union (`loading | success | error`), run TyDD Way 1 on the next feature (write code, fix red, small steps). Point the model at the types as the source of truth.

**Illustrative result:** Wrong-ID mixups and impossible UI states stop compiling; PR review discusses domain shape instead of re-litigating null checks.

---

**Situation:** Leadership wants "more type safety" but the team is mid-deadline and half the deps are untyped.

**Application:** Part 26 pragmatism: ship. Wrap the next unsafe boundary with a smart constructor / schema parse; do not rewrite the world. Increase breadth over releases. Document integration as a first-class skill, not a failure of purity.

**Illustrative result:** Trust stays intact; type skill compounds without a big-bang rewrite that never lands.

---

**Situation:** "When it compiles it works" culture, but divide returns Infinity/NaN and fetch is typed `Promise<Response>`.

**Application:** Push toward total functions: `Result` for domain/infra failures, schema on JSON body, honest signatures. Practice Way 1 on the signature change so call sites update under compiler guidance.

**Illustrative result:** Signatures stop lying; composition becomes railway-friendly; fewer "shouldn't happen" defaults.

## Anti-Patterns (tactical)

**Don't:** Practice only happy-path typing and never write a type-level unhappy path (`@ts-expect-error` or a failing proof).  
**Why:** Illegal programs that still typecheck are the whole point of TyDD. Happy-only types give false confidence.

**Don't:** Replace the entire test suite because "the types prove it."  
**Why:** Types shrink the case space; they do not prove algorithms, illegal *sequences* of legal states, or product correctness. Jesse still requires tests; TyDD makes them focused.

**Don't:** Big-bang "everything must be total and immutable by Friday."  
**Why:** Learning is iterative. Immutability alone can be a culture non-starter. Small batches, spectrum ROI, pragmatic ship path.

**Don't:** Shame shipping without maximal types.  
**Why:** No shame deciding to be pragmatic. The hard problem is continuous integration with weakly typed reality, not purity cosplay.

**Don't:** Treat TyDD as Category Theory admission control.  
**Why:** Jesse's teaching brand is useful fundamentals for web and enterprise FP: Result, brands, parse-don't-validate, railways. You do not need CT to be great at this on the web.

**Don't:** Ignore politics and integration as "not engineering."  
**Why:** Quality practices fail when you cannot sell them or when every PR fights untyped libraries without a wrap strategy. Prepare for niche, loneliness, and dual skill (domain types + safe integration).

**Don't:** Use `any` liberally while "doing TyDD."  
**Why:** `any` turns the type system off. Prefer `unknown` and parse at the boundary so proofs mean something.
