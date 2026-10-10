---
triggers:
  - "user wonders if complex TypeScript types actually do what they claim"
  - "user needs compile-time tests for money currency, typestate, or permission rules"
  - "user asks about @ts-expect-error as a TDD/TyDD technique"
  - "user hand-writes combinatorial unions that should be generated"
  - "user wants type-level Assert patterns or Vitest expectTypeOf style checks"
use_when:
  - "writing functions in the type system that assert a claim is true"
  - "practicing TyDD with failing type proofs, @ts-expect-error, and compiler red/green"
  - "generating helper types (permutations, Partial-like utilities) instead of hand unions"
  - "proving exhaustiveness and invariant encoding without runtime cost"
fails_when:
  - "proofs become unreadable type soup the team cannot maintain (ROI fails)"
  - "@ts-expect-error is placed on the wrong line and silences the wrong error"
  - "type proofs are used to avoid all runtime tests for algorithms that can still be wrong"
related:
  - "tdd-in-fp-and-oop.md"
  - "property-and-mutation-testing.md"
  - "continuous-delivery-shift-left.md"
  - "effects-without-mocks.md"
---

# Type Proofs: Assert, Exhaustiveness, @ts-expect-error Red/Green

## When to Use
- You built clever conditional types (same-currency money, CanCancel permissions, typestate order) and need **evidence they work**.
- You want unit-test-like assertions that run at compile time with **zero runtime cost / no bundle impact**.
- Unhappy paths should fail to typecheck (Secondary must not cancel Primary's transaction).
- Combinatorial unions (AWS region orderings, etc.) should be generated, not hand-maintained.
- You practice Type Driven Development: red type → simplest green → refactor, interleaved with classic TDD.

## Fails When
- **Brain-hurt without payoff.** If proofs are less readable than a few runtime tests for a stable API, prefer tests. Spectrum and team understanding matter (Types vs Tests talk energy).
- **Misplaced `@ts-expect-error`.** Comment must sit above the actual error; multi-line types often need the directive moved. Wrong placement either fails to compile for the wrong reason or hides real bugs.
- **Proofs as algorithm correctness.** Type proofs check type-level claims. Wrong business math can still typecheck. Keep runtime unit/property tests.
- **Forgeable brands without opaque makers.** Proofs on `Email` mean little if anyone can `as Email`. Couple with opaque construction.

## Core Concept

**Type Proofs** let you write functions in the type system that **assert something is true**. Where TypeScript cannot express things as easily as Scala or Haskell, you still build facts with conditional types, mapped types, recursive types, and assertion helpers. They are like `expect(thing).toBe(true)`, and like Vitest's type-level `expectTypeOf` / `assertType`, except you can build your own from low-level tools.

They do not emit runtime code. File size unaffected. CI fails on `tsc` the same way tests fail on assert.

### Basic Assert pattern

Illustrative starting point from TyDD Part 12:

```ts
type Assert<T> = T
type Cow = false
// does not compile when constrained to true:
type _CowIsTrue = Assert<Cow> // with Assert<_ extends true>
```

Practical form:

```ts
type Assert<_ extends true> = void

type GreaterThan<
  A extends number,
  B extends number,
  Acc extends unknown[] = []
> =
  Acc['length'] extends A ? false :
  Acc['length'] extends B ? true :
  GreaterThan<A, B, [...Acc, 0]>

type LessThan<A extends number, B extends number> =
  GreaterThan<B, A>

type _nope = Assert<GreaterThan<8, 9>> // fail
type _yup = Assert<GreaterThan<9, 8>>  // ok
```

Name proof aliases with a leading underscore so humans see "type test," not production API. Baller when green; instructive when red.

### What proofs are for

1. **Validate type behavior:** only `Money<'USD'> + Money<'USD'>`; fails for EUR mix (ties to indexed types / generics).
2. **Typestate order:** evidence that transition types only accept legal predecessors.
3. **Phantom / evidence types:** proof tokens that a check occurred.
4. **Helper type generation:** `Partial`, `Readonly` are everyday native helpers; custom `Permutations<AWSRegions>` beats hand-writing six tuples when a third region appears.
5. **Custom compiler errors** via carefully constrained types (advanced).

### `@ts-expect-error` as TyDD red/green

Type Proofs in Jesse's usage also means using **`@ts-expect-error`** to practice Type Driven Development. Confusingly, you can combine directive suites with Assert helpers.

Part 25 workflow (Primary Jesse vs Secondary Sydney cancel rules):

1. Create fixtures and an **illegal** call with a comment above:

```ts
declare const jesseTransaction: Transaction<'transaction-123', 'jesse'>
declare const sydney: SecondaryAccount<'sydney'>

// @ts-expect-error Sydney must not cancel Jesse's transaction
cancelPayment(jesseTransaction, sydney)
```

2. Implement the simplest function so the **illegal** call is a real type error (directive not red for wrong reasons).
3. When `@ts-expect-error` is no longer underlined, either the types are right for the unhappy path or you broke the test. Refactor types, or add happy paths without the directive:

```ts
cancelPayment(jesseTransaction, jesse) // should compile
```

Caveat: directive must be directly above the compiler error site.

### Type proof loop (third TyDD mode)

1. Write a **failing proof** (`Assert<CanCancel<...>>` that should be true/false per design).
2. Improve the conditional type (`PrimaryAccount` always true; `SecondaryAccount` only when `Equal` owner ids) until proofs pass.
3. Refactor or add more proofs.

Fourth mode: intermingle compiler red/green, expect-error, and proofs **while** classic TDD. Jesse: that is what he does.

### Exhaustiveness checking (related compile-time suite)

Enums, unions, and discriminated unions enable **exhaustiveness**: all variants handled or the build fails. You do not need `default: return "shouldn't happen"`. Adding `'cancelled'` lists every update site. Wrong field access on DUs is blocked (no `error` on success).

TS DUs are awkward vs FP pattern matching (manual tags, constructors, opaque types) but **worth it** for exhaustiveness benefits. Types' high coupling becomes a refactoring force when product adds states.

Exhaustiveness is not a full type proof library, but it is the everyday "compiler as test suite" tool. Use it alongside Assert for deeper invariants. Property tests still needed for dynamic transition sequences exhaustiveness cannot see.

### Relation to property tests and runtime tests

| Tool | When it runs | Good for |
|------|--------------|----------|
| Type proofs / Assert | Compile | Type-level functions, permissions in types |
| `@ts-expect-error` | Compile | Negative API examples |
| Exhaustiveness | Compile | All variants handled |
| Unit TDD | Runtime | Algorithm behavior examples |
| Property tests | Runtime | Totality, random sequences |
| Mutation testing | Runtime tooling | Assertion strength |

Types prevent bad values from existing; when types hurt your brain, code preserves truth and property tests guard that code. Proofs are for the claims you **did** encode in types.

## How to Apply

1. **Pick one invariant worth proving.** Same currency add, cancel authority, region permutations, non-empty head present.
2. **Write the failing proof or illegal call first.** Red before green, type edition.
3. **Implement the simplest type that satisfies the proof.** Avoid dependent-type cosplay if a brand + conditional suffices.
4. **Add happy and unhappy proof pairs.** Mirror unit test naming: `_primaryCanCancel`, `_secondaryCannotCancelOther`.
5. **Keep proofs next to the types** or in a `*.types.test.ts` that is part of `tsc` / Vitest typecheck.
6. **Use `@ts-expect-error` for call-site negatives** when Assert is heavier than you need.
7. **Generate combinatorial helpers** instead of hand unions; re-prove when the input list grows.
8. **Interleave with runtime TDD** for behavior the type system cannot see (math, I/O mapping, reducer races).

## Examples

**Situation:** Money library allows `add(usd, eur)` at compile time; runtime throw is too late.
**Application:** Generic `add<C>(a: Money<C>, b: Money<C>)` plus Assert proofs that same brand compiles and mixed brands fail (and/or expect-error examples). `NoInfer` if TS widens incorrectly.
**Illustrative result:** Business rule lives in the type system; fewer unhappy-path unit tests about currency mixups.

**Situation:** AWS multi-region ordering config; three regions mean six permutations hand-written.
**Application:** `type Regions = Permutations<['us-east-2', 'us-west-1', 'eu-west-2']>` with proofs that length and membership hold.
**Illustrative result:** Fourth region does not require a combinatorial rewrite by hand.

**Situation:** Secondary accounts must not cancel others' payments.
**Application:** TyDD modes: failing expect-error on Sydney/Jesse; CanCancel proof types; runtime TDD for message and Result payloads.
**Illustrative result:** Dual stack: illegal programs do not compile; legal behavior is tested.

**Situation:** Switch on request state with a default "should never happen."
**Application:** DU + exhaustive switch without default; add state and follow compiler todos. Optional Assert helpers on mapped handlers.
**Illustrative result:** Distant undefined from misspelled strings goes away; design changes become checklists.

## Anti-Patterns

- **Hand-maintaining permutation unions** when a type function can generate them.
- **Assuming types work without type-level tests** once complexity rises.
- **`@ts-ignore` instead of `@ts-expect-error`.** Ignore never fails when the error disappears; expect-error turns green-illegal into a red signal.
- **Proofs that only test true cases.** Unhappy paths are the point of negative type tests.
- **Replacing property tests for reducers with exhaustiveness alone.** Static states ≠ legal sequences.
- **Exporting forgeable brands** while proving invariants on them.
- **Unreadability as status.** If only one person can parse the proof, CD suffers when they leave.
- **"It compiles" as "it's correct."** Still need tests for algorithms.

Type proofs are compile-time assertions and negative API tests. Assert helpers, exhaustiveness, and `@ts-expect-error` red/green are how you practice TyDD without waiting for runtime. Pair them with TDD and property tests. Zero runtime cost; non-zero clarity cost; use where invariants matter.
