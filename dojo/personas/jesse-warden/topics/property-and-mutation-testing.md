---
triggers:
  - "user has high unit coverage but still ships logic bugs"
  - "user asks how total functions are after typing them"
  - "user only writes example-based unit tests for parsers and formatters"
  - "user wants confidence that tests would fail if code were wrong"
  - "user asks about Stryker / mutation testing or property-based testing"
use_when:
  - "measuring how total a function is with random inputs (fast-check, jsverify)"
  - "killing surviving mutants to improve existing unit tests (Stryker)"
  - "choosing between fixing code and narrowing types when random cases fail"
  - "proving state machine transitions that DUs alone cannot enforce"
fails_when:
  - "mutation runs are unbounded on huge suites without diff/focus strategy (too slow to use)"
  - "property tests generate invalid domain values you never intended to support and you 'fix' by accepting nonsense"
  - "you treat mutation score as a vanity metric instead of a prompt to improve tests or types"
related:
  - "type-proofs.md"
  - "tdd-in-fp-and-oop.md"
  - "effects-without-mocks.md"
  - "continuous-delivery-shift-left.md"
---

# Property Tests and Mutation Testing: Confidence Beyond Examples

## When to Use
- Types and example unit tests are in place, but you need to know **how total** functions really are under weird inputs.
- Coverage is high (even ~100%) and bugs still ship; you need a different quality signal.
- State machines / reducers use DUs for static impossible states, but illegal **transitions** can still happen at runtime.
- AI or humans generate tests and you want an automated check that those tests would fail if the code were subtly wrong.
- Smart constructors, parsers, and formatters sit at boundaries and should be blasted with random inputs.

## Fails When
- **Mutation testing as full-suite every commit without focus.** Mutating large graphs re-runs tests for every mutant; treat like performance tests: baseline, threshold, or **diff-scoped** runs (changed files / modules they touch). Pre-commit husky patterns can keep feedback seconds, not hours.
- **Property tests without domain bounds.** Random `string()` will find empty and blank; if the API is only for non-empty names, narrow the type or the generator rather than "fixing" by accepting garbage forever.
- **Ignoring surviving mutants blindly.** Some survivors are edge noise; some are red alerts. Judgment required. Score is a conversation, not a religion.
- **Replacing type proofs or exhaustiveness.** Property and mutation testing complement compile-time proofs; they do not replace them.

## Core Concept

Example unit tests show a few cases you thought of. Types remove whole classes of invalid values. That is still not enough for "never break" energy. Two complementary tools:

1. **Property-based testing:** one test, many random inputs (e.g. 100). Failures come with a seed so you can reproduce the exact sequence (fast-check, jsverify).
2. **Mutation testing:** the tool changes your production code (flip conditionals, force returns, alter operators) and re-runs your unit tests. If tests still pass, a **mutant survived**: your tests (or types) did not notice the sabotage. You do not write "mutation tests"; you improve existing unit tests (or types) until mutants die.

Together with type proofs and exhaustiveness, they give more confidence than green examples alone. TyDD series framing: types as a Continuous Delivery tool and a way to keep LLMs honest; property tests measure totality; mutation testing shifts quality left.

### Property tests: how total are we?

Type safety is a spectrum. You can write total-looking signatures and still blow up on empty strings.

```ts
type FormatName = (name: string) => string

forAll(string(), name => {
  expect(() => formatName(name)).not.toThrow()
})
// fails on "" and " "
```

When it fails you choose:

- **Fix the code** (`trim`, safe capitalize, structured error), or
- **Narrow the type** so bad values cannot be passed:

```ts
type FormatName = (name: NonEmptyNorBlankString) => string
```

Same fork appears for state machines. Discriminated unions stop illegal static bags:

```ts
// prevented by DU
{ loading: true, data: user, error: "bad" }
```

They do **not** prove that a React `useReducer` only allows legal sequences under racey action streams:

```
Loading -> Success
Loading -> Error
Loading -> Error -> Retry -> Success
Loading -> Cancel -> Error
```

Generate random action sequences; after each step assert `isAllowedTransition(previous, action, next)`. If it breaks: improve reducer code, or encode more of the transition rules in typestate types (narrower transition functions). Property tests guard the truths types cannot (or not yet) express without melting your brain.

Opaque makers (`makeEmail`, money constructors) are prime property-test targets: blast creation functions with random strings and amounts.

### Mutation testing: do tests actually protect the code?

Coverage says a line ran. It does not say the assertion would fail if the line were wrong. Stryker-style tools:

1. Find return statements / branches / operators in your code.
2. Generate mutants (return `true` always, `false` always, `>` instead of `>=`, etc.).
3. Run unit tests per mutant.
4. Report **surviving** mutants (tests green despite sabotaged code) vs killed mutants.

Classic club example: `age >= 18` for admission. Mutating to `>` lets 18-year-olds fail incorrectly; if tests only used ages 20 and 30, the mutant survives. Fix: assert the boundary cases (17 out, 18 in). Rerun; mutants for that line die.

Surprising reality Jesse reports at work and personal projects (and Stryker docs show): code with ~100% unit coverage can still have weak mutation scores. Happy and unhappy examples can miss operator flips. **Test coverage is not going to save you** as a sole quality metric.

You iterate: run mutation → inspect survivors → add/adjust unit tests **or** tighten types (discriminated unions and records kill many classes of nonsense) → rerun. Not all at once; not every survivor is worth a test.

Property tests are roughly the opposite angle of mutation testing: random inputs stress the implementation; mutants stress the tests. Use both.

### Types as partners

Stronger types (non-empty, branded IDs, DUs, exhaustive switches) reduce the mutant surface and the random space. Weak "stringly" types force more runtime tests. Jesse's rule of thumb across TyDD: better type systems → more load on types; weaker systems → more tests. Property and mutation sit on the test side of that spectrum while type proofs sit on the type side (see type-proofs.md).

### AI and shift-left

Mutation testing is also a response to AI-generated code and tests: another automated check that "what the assistant wrote" would actually fail if production logic were wrong. Combined with property tests on parsers and TDD's minimum-code discipline (Copilot research: assistants correlate with more mistake code, less reuse, add-only suggestions), you get a practical honesty layer for high-volume generation. Run them as shift-left quality in CI/local, like lint and compile, with performance-aware scheduling.

## How to Apply

1. **Stabilize pure units first.** Mutation and property tests shine on pure or DI-stubbed functions. Mock-heavy OOP methods fight both tools.
2. **Add one property test to a risky pure function.** Prefer formatters, parsers, smart constructors, reducers. Start with `forAll` and a clear property ("never throws", "round-trip", "valid transition").
3. **On failure, choose code fix vs type narrow.** Document the choice. Prefer making illegal inputs unrepresentable when the domain allows.
4. **Introduce Stryker (or equivalent) on a small package.** Baseline mutation score. Do not boil the monorepo on day one.
5. **Kill survivors with boundary examples.** Especially equality edges (`>=`, empty collections, nullish).
6. **Scope for CI.** Diff-based mutation on changed modules; full run as scheduled/nightly; treat like performance suites.
7. **Use types to close doors.** DUs, non-empty collections, branded IDs reduce both random failures and trivial mutants.
8. **Pair with type proofs for invariants that should be compile-time** (same currency money, typestate order). Runtime property tests for sequences and totality; proofs for type-level claims.

## Examples

**Situation:** `formatName` unit tests only use `"jesse"` and `"Sam"`.
**Application:** Property test over `string()`. Fails on empty/blank. Either trim-and-handle or `NonEmptyNorBlankString` at the boundary.
**Illustrative result:** Totality is explicit; fewer production "cannot read property 0 of undefined" surprises.

**Situation:** Reducer uses Loading | Success | Failure DU; e2e occasionally shows weird transitions under double-click.
**Application:** Property test random action sequences; assert allowed transitions. Optionally encode typestate transition functions so illegal pipelines do not typecheck.
**Illustrative result:** Racey sequences fail in CI with a seed, not only in flaky UI sessions.

**Situation:** Order service has 100% coverage, mutation score ~58%.
**Application:** Inspect survivors: missing unhappy path for payment failure, operator slip on free-shipping threshold. Add focused tests; optionally model money thresholds with branded types.
**Illustrative result:** Confidence to delete and refactor rises; green bar means more than "lines executed."

**Situation:** AI wrote unit tests for a pure module.
**Application:** Run mutation testing on that module; if mutants survive, tests are theater. Improve assertions or regenerate with failing cases first (TDD).
**Illustrative result:** Human review time focuses on survivors, not reading green noise.

## Anti-Patterns

- **Example-only testing of total claims.** "It works for these three fixtures" is not a totality argument.
- **Coverage theater.** 100% with no assertions that would fail under sabotage.
- **Property tests that reimplement the code.** Properties should be laws (round-trip, ordering, invariants), not a second copy of the implementation.
- **Unbounded mutation on giant suites every PR.** Tool gets disabled; culture loses the habit.
- **Treating every survivor as P0.** Triage: critical logic vs dead edge.
- **Only mutation, no types.** You will generate and kill mutants forever for stringly domain bugs brands would prevent.
- **Only types, no random tests.** Compiling still allows wrong algorithms (Elm Advent of Code lesson: massive bugs in code that compiles and has no runtime errors). Property tests and unit tests remain.
- **Wifi-dependent property tests.** Generators should not hit the network; inject stubs.

Property tests ask: what inputs break me? Mutation testing asks: would my tests notice if I were wrong? Types and type proofs ask: can wrongness even be represented? Use the stack. Example tests alone under-deliver confidence.
