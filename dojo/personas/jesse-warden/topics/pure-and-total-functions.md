---
triggers:
  - "user confuses pure functions with total functions"
  - "user asks why pure code still returns NaN, Infinity, or garbage for bad inputs"
  - "user designs public APIs that throw or return nonsense while claiming type safety"
  - "user asks how much of the codebase should be pure vs total"
  - "testing is hard because functions hit network, disk, or throw"
use_when:
  - "separating pure core from effectful edges"
  - "making public entry points honest about failure (Result / structured errors)"
  - "improving predictability and unit-testability without mocks"
  - "reviewing signatures that lie (Promise<T>, number from divide-by-zero)"
fails_when:
  - "you demand every private helper return Result and drown in ceremony"
  - "you treat pure as enough and ignore nonsense outputs"
  - "you force total wrappers on exploratory throwaway code with no tests and no users"
related:
  - "pipelines-and-composition.md"
  - "schema-at-the-boundary.md"
  - "smart-constructors.md"
  - "typestate-and-capabilities.md"
  - "product-and-union-types.md"
---

# Pure Functions vs Total Functions

## When to Use

- You want **predictable** units: same input, same output, no hidden world changes.
- Pure code still surprises you with `NaN`, `Infinity`, empty string defaults, or `"1Error: moo"` string concat from bad arguments.
- Public APIs (`fetch` wrappers, Lambda handlers, library exports) claim `Promise<T>` or `number` while crashing or returning nonsensical values for real inputs.
- Unit tests need mocks for everything; that is a purity smell. Prefer stubs and pure cores.
- You are composing pipelines and need pieces that do not throw grenades into the chain.

## Fails When

- Every one-line private helper is forced to return `Result` "to be total." Ceremony without benefit. Jesse's rule of thumb: **privates pure, publics total** so privates never see bad data.
- The team is exploring a throwaway prototype with no shared boundary yet; totalizing everything can wait until shapes stabilize.
- You equate "compiles" with "total and correct." Elm Advent of Code taught hard: no runtime exceptions ≠ correct algorithms. Types + tests together.

## Core Concept

### Pure

A pure function:

1. Same inputs → same output (deterministic / referential transparency in engineer English: call it, get a value, that is it).
2. No side effects (no network, disk, global mutation, logging-as-requirement, random, clock, etc.).

```ts
const add = (a: number, b: number) => a + b
```

Why prefer pure? Predictability. Easier unit tests (no mocks; stubs only if you inject deps). Easier maintenance. Composition does not multiply hidden behaviors.

Exceptions act like side effects in practice: they skip return paths, explode combinatorial reasoning, and poison pure composition. Prefer errors as values (`Result` / Ok-Error, not Left-Right theater for humans). Tony Hoare's null was a billion-dollar mistake; unhandled throws are cousins.

Purity heuristic for tests: **if you need mocks, it is not pure enough.** If unit tests fail when wireless is off, they are not unit tests.

### Total (and why pure is not enough)

Pure is not the end of the story.

```ts
add(1, 2) // 3, fine
add(1, new Error("moo") as any) // "1Error: moo" in JS, not helpful
```

A pure function can still return **nonsense** for some inputs. Divide:

```ts
type Divide = (a: number, b: number) => number
// 2/0 → Infinity; 0/0 → NaN: numbers, but not sensible for users
```

**Total functions** aim to return a *sensible* value for every input in their domain. Two main moves:

1. **Honest failure:** return `Result` / structured `{ ok: false, error }` instead of garbage success.
2. **Narrower inputs:** `PositiveInteger` denominator, `NonEmptyArray`, branded validated types so bad cases are not in the type domain.

```ts
const addNumbers = (a: unknown, b: unknown) =>
  isNumber(a) && isNumber(b)
    ? { ok: true as const, data: a + b }
    : { ok: false as const, error: new Error("Either a or b aren't Numbers.") }
```

Or with types at the boundary already validated, publics return `Result` for domain/infra failures while privates assume good data.

**Partial functions** throw/crash or return nonsensical outputs for some inputs. Their type signatures **lie**. `fetch: (url: string) => Promise<Response>` hides network failure, non-OK status, and body parse failure. A total-leaning design:

```ts
type safeFetch = <T>(
  url: string,
  schema: Schema<T>
) => ResultAsync<T, FetchError>
// implies: typed T via schema, async Result, modeled FetchError, no thrown surprises
```

App-level total aspiration:

```ts
type AWSLambda = (
  event: APIGatewayProxyEvent
) => ResultAsync<HttpResponse, never>
// or Result with panic mapped at the absolute edge
```

### Privates pure, publics total

Not every function must be total. Validate or parse at public boundaries; keep internal helpers pure and simple on trusted types. That is how you avoid Result soup while still not lying at the API surface.

Type safety is a **spectrum**. Gradual typing (TypeScript, Python) helps domain discovery and legacy integration. Aim the design toward totals at the edges that matter: HTTP handlers, exported lib functions, pipeline stages that compose.

You do not need Category Theory to define pure or total. If someone says you cannot write FP until you recite morphisms, ignore them and ship a pure `calculateTax` with a total `parseOrder` in front of it.

## How to Apply

1. **Label impurity.** Name `unsafeParse`, `safeParse`, Noop-returning effect functions so risk is visible. Unlabeled impurity is how ambient authority hides.

2. **Extract pure cores.** Business rules as `(input) => output` with no I/O. Push DB, HTTP, clock, random to parameters (capabilities) or the imperative shell.

3. **Inject effects as parameters.** DI in FP is "pass the function." `readFile`, `fetch`, `sendEmail` as args. Unit tests pass stubs. No DI container required: "why build a framework around passing a parameter?"

4. **Totalize publics.** For each export, ask: what inputs are possible at runtime? Return `Result` or constrain with branded/opaque/non-empty types. Map try/catch only to wrap unsafe libs into Result.

5. **Classify errors** (domain, infrastructure, panic, unforeseen). Model 1 and 2 as values. Panic at the edge if neither user nor dev can recover. Do not obsess over 4 if you model 1 and 2 well.

6. **Prefer Result over Maybe** when absence has a reason. Maybe for true optionality pushed to edges (env vars). Result when failure needs context.

7. **Compose totals into pipelines / railways.** Happy-path pipe for pure transforms; Scott Wlaschin's Railway Oriented Programming when steps return Result. One throw in the chain makes the whole program partial again.

8. **Test pure with properties and examples; do not mock.** Assert outputs. Use `_unsafeUnwrap` only in tests if your Result lib has it, banned in prod by lint.

9. **Know when not to force it.** Untrained team + deadline + no trust: teach with small pure helpers first. Breaking team trust is a great way to ensure software never works correctly.

## Examples

**Situation:** `add` is pure and unit-tested, but a form still sends strings; users see weird concatenated errors.

**Application:** Public `addNumbers` totalizes with runtime checks or, better, parse form fields to `number` once via schema; private `add` stays pure on `number`. Do not make every arithmetic helper return Result if the boundary already guarantees numbers.

**Illustrative result:** Bad input fails at parse with field errors. Core math stays trivial and fully tested with properties.

---

**Situation:** Service method `createReport(): Promise<void>` hits DB, filesystem, and email; tests are mock festivals.

**Application:** Pure report builder `(data) => Report`. Effectful shell takes capabilities `queryDb`, `writeFile`, `sendEmail` as parameters (or only the ones it needs). Public handler is total-ish: `ResultAsync<void, ReportError>`.

**Illustrative result:** Unit tests stub capabilities with pure functions. Domain logic tests never open sockets. Signature documents authority.

---

**Situation:** `divide(a, b): number` used in financial UI; divide-by-zero shows Infinity.

**Application:** Either `Result<number, DivideError>` or `b: NonZeroNumber` from smart constructor. Prefer domain language: "Quantity must be positive" as typed error payload.

**Illustrative result:** UI matches on error tag; no stringly checks for `Infinity`.

---

**Situation:** Lambda uses try/catch soup and returns 500 for both bad JSON and business rule failures.

**Application:** Parse event with schema → domain Result pipeline → `.match` at the edge to HTTP status. Domain errors 4xx with structured body; infra 503; panic logged and 500.

**Illustrative result:** Total pipeline pieces; one impure match at the shell. Continuous delivery confidence goes up because failure modes are designed, not discovered only in Datadog.

## Anti-Patterns (tactical)

**Don't:** Treat "same input same output no side effects" as the finish line.
**Why:** Pure nonsense is still nonsense. Public APIs need sensible outputs or typed failures. That is the pure vs total distinction Jesse hammers.

**Don't:** Throw from pure cores to "keep signatures clean."
**Why:** You put a grenade in the composition. Callers need try/catch; pipelines break; tests need exception assertions. Return Result or do not claim purity.

**Don't:** Make every private total with Result wrapping.
**Why:** Noise. Validate at the boundary; trust branded types inside. Privates pure on good data; publics total for the outside world.

**Don't:** Use mocks as the primary testing strategy for "unit" tests of business logic.
**Why:** Mocks couple to implementation (Eric Elliott and others call heavy mocking a smell). Pure functions need inputs and expected outputs. Inject deps; stub returns.

**Don't:** Name errors Left/Right for a TypeScript enterprise team unless they already live in Haskell.
**Why:** Ok/Error communicates. Accessibility of mental model beats tradition. Same idea: avoid category-theory gatekeeping as a prerequisite to returning a structured failure.

**Don't:** Assume no runtime exceptions means correct software.
**Why:** Wrong defaults in Maybe chains, wrong tax math, wrong domain transitions all compile. Types reduce whole classes of bugs; tests and clear totals handle the rest.
