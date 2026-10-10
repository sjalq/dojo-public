---
triggers:
  - "user asks if TDD works with functional programming or only OOP"
  - "user thinks types replace tests or tests replace types"
  - "user is afraid to refactor because the suite does not protect them"
  - "user writes bulk code then tests after, especially with AI autocomplete"
  - "user wants red-green-refactor discipline on a public API"
use_when:
  - "practicing TDD in sound-typed FP and in dynamic OOP side by side"
  - "designing public APIs by consuming them in tests first"
  - "interleaving TyDD (compiler red/green, @ts-expect-error, type proofs) with classic TDD"
  - "countering AI pressure to add unneeded code by writing minimum to pass"
fails_when:
  - "legacy has zero tests and you refactor production without characterization tests first"
  - "TDD is used as ceremony while still testing implementation via mocks only"
  - "team forces TDD theater under deadline without teaching the design feedback loop"
related:
  - "type-proofs.md"
  - "property-and-mutation-testing.md"
  - "effects-without-mocks.md"
  - "dependency-injection-in-fp.md"
  - "continuous-delivery-shift-left.md"
---

# TDD in FP and OOP: Types + Tests, Red-Green-Refactor

## When to Use
- You need fearless refactor: green suite means change structure without fear and with excitement, not nerves.
- Debate flares: "types are enough" vs "tests are enough." Use both.
- Dynamic language or weak types: tests compensate somewhat for missing compile-time proofs.
- Sound typed FP: still write tests; types reduce volume and focus remaining cases.
- Designing a public API: consume it in a failing test before implementing.
- AI assistants suggest bulk fields and future code; TDD's minimum bar is the counterweight.

## Fails When
- **Untested legacy big-bang.** Add characterization tests before refactoring production paths you do not understand (Jesse's when-not-to-force-FP list: legacy without tests gets tests first).
- **Mockist TDD that freezes implementation.** Red-green-refactor fails if every green depends on spy call order. Prefer values and stubs (effects-without-mocks.md).
- **Ceremony without design feedback.** Writing tests after a 400-line dump is not TDD. The point is API shape and minimum code.
- **Shame for pragmatism.** Under true exploration spikes, ship learning first; then lock behavior with tests. No shame being pragmatic and shipping (Final Thoughts energy applied carefully).

## Core Concept

Jesse watched a lot of Dave Farley and wanted to **translate OOP people** for FP audiences. Farley is OOP-bent, but Continuous Delivery, architecture, and TDD transcend style. Domain Driven Design sits on the same "translate later" list. Architecture is not SOLID-as-vapor. The useful industry dialect still applies in Elm, ReScript, TypeScript FP, and Python.

Four claims from his TDD article:

1. **You can use TDD in both OOP and FP.** Useful in both styles.
2. **Types are great, but so are tests. Together they rock.** Using only one is not enough.
3. **If you do not have types, you can still succeed.** Tests compensate a little.
4. **A test suite should empower fearless refactor.** You should be excited to refactor, not fearful.

He is still a self-described n00b at TDD relative to lifelong practitioners, but has felt the benefits enough times in both paradigms to be convinced. Separate video series exist: TDD in strictly typed FP, and TDD in OOP with a dynamic language, plus a combined playlist and a one-minute explainer of red-green-refactor.

### Red-Green-Refactor (both paradigms)

Classic loop:

1. **Red:** write a failing expectation against the public API you wish existed.
2. **Green:** implement the simplest code that makes it pass.
3. **Refactor:** clean design with the suite protecting behavior; or add the next test.

Example from TyDD how-to (domain: Primary can cancel any transaction; Secondary only own):

```ts
expect(
  canCancel(
    { accountType: 'primary', id: 'jesse' },
    { transactionID: '4', accountID: 'jesse' }
  )
).toBe(true)
```

Simplest implementation to pass; then next case (Sydney secondary cannot cancel Jesse's payment). Public API discipline: tests talk to `canCancel` / `cancelPayment`, not private helpers' call graphs.

### Public API discipline

TDD is a design technique. You feel the API before it exists. In OOP that is constructor and method shape; in FP that is function signature, Result error channel, and dependency parameters. If the test is painful, the API is painful. Change the API while still red if needed.

DI and TDD are cousins historically: XP/TDD culture and DI for testability grew up together (see dependency-injection-in-fp.md). Inject effects so green is deterministic.

### Types do not retire TDD

Elm Advent of Code pill: you can have **massive bugs in code that compiles and has no runtime errors**. Wrong defaults in Maybe chains, wrong math, wrong domain logic. "Never break" is not "mostly work." Unbreakable functions still need unit, fuzz/property, feature, and manual tests.

TyDD Part 24 (Making Impossible States Impossible, Richard Feldman framing for the slogan): types shrink happy/unhappy/edge cases you must test; you still need tests; types make TDD safer and more focused. Spectrum with nuance, not absolutism.

TyDD Part 25: Type Driven Development is a lot like TDD: design technique that results in proofs for easy-to-change code. In most languages use them together; **more types in a better type system, more tests in a bad one.** Four practice modes:

1. **Compiler-driven red/green** in good type systems: write code, fix red, refactor; small batches; compiler lists breakages.
2. **`@ts-expect-error` negative type tests** for illegal call sites (Sydney must not cancel Jesse's transaction).
3. **Type proofs** (`Assert<CanCancel<...>>`) as type-level unit tests.
4. **Interleave 1-3 while doing classic TDD.** "That's what I do."

So TDD is not replaced by TyDD; Jesse intermingles them.

### FP unit testing ground rules that support TDD

From Node FP unit testing series:

- Pure functions; stubs only; no mocks as default.
- Immutability (`const`); arrow functions; no `this` theater; no classes you invent if pursuing that purity bar.
- Don't throw in the pure core; Maybe/Result/Promise as values.
- No accidental integration tests (wireless off check).
- Label Unsafe/Safe/Noop; export pure entry points; gate server start on main module.
- Optional: curry multi-arg; accept that 100% coverage is still not enough.

These make red-green cycles fast. Slow, mock-heavy, wifi-on tests kill the loop Farley-style CD depends on.

### OOP series vs FP series (same discipline, different surface)

| | Typed FP TDD | Dynamic OOP TDD |
|--|--------------|-----------------|
| Feedback | Compiler + tests | Tests carry more load |
| Doubles | Function stubs / Result ok-err | Constructor injection stubs |
| Design smell | Partial functions, ambient effects | Void methods, hard-coded `new` |
| Shared goal | Public API first, minimum code, fearless refactor | Same |

Do not let FP bias dismiss TDD as "OOP stuff." Do not let OOP bias dismiss pure functions and Result as academic. Translate.

### AI pressure vs minimum code

GitHub Copilot research Jesse highlighted:

- Strong correlation with mistaken code pushed.
- Assistants discourage reuse.
- Lines added faster than cleaned; "itinerant contributor" violating DRY.
- Suggestions for add/complete, rarely update/move/delete.
- Invents future fields from similar codebases that are not needed **right now**.

That is anti-TDD. TDD insists on **minimum code to pass the current test**. Keep assistants; keep the red bar honest. Types + tests + property/mutation checks keep LLMs honest under higher volume (series framing across TyDD).

## How to Apply

1. **Write the expectation first.** Name the public function and inputs you wish you had. Watch it fail for the right reason.
2. **Green with minimum code.** No future fields, no speculative config. Pass this test only.
3. **Refactor under green.** Extract pure helpers; inject deps; improve names. Suite must stay green.
4. **Next behavior, not next implementation detail.** Prefer new examples of domain rules over spy assertions.
5. **In typed codebases, interleave TyDD.** Compiler red, `@ts-expect-error` for illegal uses, type proofs for invariants, while TDD covers runtime behavior.
6. **In dynamic codebases, lean harder on tests and DI.** Constructor or parameter injection; stubs for edges; integration tests for reals.
7. **Keep the suite fast.** Pure units in milliseconds; quarantine slow acceptance. Slow CI kills TDD adoption (Angular PR lesson).
8. **Use AI inside the loop, not instead of it.** Accept autocomplete that passes the current test; reject speculative bulk; run mutation/property where risk is high.

## Examples

**Situation:** Team says "we use TypeScript, we don't need TDD."
**Application:** Show compile-clean wrong algorithms; add failing test for a domain rule; implement minimum; refactor. Pair with branded types to delete tests that only exist to catch ID mixups.
**Illustrative result:** Fewer tests overall, stronger remaining tests, less fear on change.

**Situation:** Dynamic Python service, no types, flaky confidence.
**Application:** TDD on pure functions with Result-style returns; inject `requests`; property-test parsers; integration for real HTTP.
**Illustrative result:** Tests compensate for missing types; pure core stays deterministic.

**Situation:** Copilot fills a DTO with six optional fields "you might need."
**Application:** Only fields required by the current failing test. Delete the rest. Next test earns the next field.
**Illustrative result:** Less DRY violation and less future cleanup debt.

**Situation:** Primary/Secondary cancel rules.
**Application:** Classic TDD for `canCancel` booleans and outcomes; `@ts-expect-error` on `cancelPayment(jesseTransaction, sydney)`; type proof `CanCancel` conditional; happy path without the directive for Jesse/Jesse.
**Illustrative result:** Runtime and type-level suites agree; illegal authority cannot compile.

## Anti-Patterns

- **Test-after-only as "we do TDD."** Naming is not the practice.
- **Types-only maximalism.** Compiles ≠ correct. Jesse swallowed that pill in Elm.
- **Tests-only maximalism when types are cheap.** You will write tests brands and DUs would delete.
- **Implementation-coupled greens.** Spy-heavy tests that force a specific private structure.
- **Giant red steps.** Small batches; one behavior at a time.
- **Breaking the suite and committing anyway.** Fearless refactor requires a trustworthy bar.
- **Forcing FP TDD style onto an untrained team without teaching.** Trust and team norms matter; bad relationships yield horrible software.
- **Skipping tests on legacy before behavior change.** No feedback for days/weeks.

TDD works in OOP and FP. Types and tests together rock. Red-green-refactor designs the public API and enables fearless change. That is the discipline; the paradigm is just the dialect.
