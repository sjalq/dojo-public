---
triggers:
  - "user's unit tests are mock/spy heavy and break when implementation is refactored"
  - "user asks how Effect-TS or neverthrow relate to testing"
  - "user wants to stop mocking console, fetch, or db for simple units"
  - "user has void functions and ambient authority with no typed errors"
  - "user asks how to embed effects in types so the compiler forces the call"
use_when:
  - "removing mocks by returning effect evidence and typed Results/Effects"
  - "adopting neverthrow or Effect for typed errors and composition"
  - "introducing capabilities / typed requirements instead of ambient side effects"
  - "Angular/Jest spyOn culture is producing fragile, implementation-coupled tests"
fails_when:
  - "you still need integration confidence at real boundaries (use real stubs/servers there, not pure denial of IO)"
  - "the team uses Effect only as a fashion layer without errors-as-values or requirements"
  - "you ban all doubles but leave impure cores that secretly hit the network"
related:
  - "dependency-injection-in-fp.md"
  - "tdd-in-fp-and-oop.md"
  - "property-and-mutation-testing.md"
  - "type-proofs.md"
  - "continuous-delivery-shift-left.md"
---

# Effects Without Mocks: Typed Effects, Capabilities, neverthrow, Effect-TS

## When to Use
- Unit tests spend more lines on spy setup/teardown than on behavior, and refactors that preserve outputs still fail tests.
- Functions return `void` / `Promise<void>` while doing logging, fetch, DB, email: ambient authority with a lying signature.
- You want errors as values (Result / Effect) so try/catch is not the control flow for expected failures.
- You are ready for DI as parameters (or Effect Requirements/Layers) and pure stubs, not module mutation.
- You need production-grade TypeScript composition where success, error, and dependencies are all in the type.

## Fails When
- **Real IO still needs real tests.** Removing mocks from units does not delete integration and acceptance tests for HTTP, DB, and auth. Stub the edge in units; prove the edge elsewhere.
- **Effect cargo cult.** Importing Effect without modeling errors, requirements, or totals is costume. Start with `Effect.succeed` / fail or neverthrow `ok`/`err` if overwhelmed.
- **Impure core with pure rhetoric.** If the domain still closes over globals, typed wrappers only decorate the mess.
- **Mock nuance denial.** Some frameworks make spies less painful; fragile coupling to implementation can still remain, especially Angular + inject growing void methods. Nuance is not permission to keep ambient authority.

## Core Concept

Mocks are a code smell when they become the default way to "unit test" (Eric Elliott's line Jesse endorses). Problems:

1. **Lots of setup** for one line of behavior.
2. **Tests know the implementation**, so abstraction is defeated.
3. **Tiny refactors break tests** even when behavior still works: tests stop being fun.
4. **Mutation and shared spy state** risk isolation failures (setup/teardown, order dependence).

Stubs are pure functions: given the test wants QA config, the stub returns QA config. Deterministic. Happy and unhappy paths are different return values. No wireless. Prefer that.

You can go further: **embed effects in the type system** so the compiler forces the call and the unit test asserts return values, not spies.

### Return the effect evidence

Classic greeter: builds `"Hello, Jesse!"`, `console.log`s it, returns the string. Behavior tests for the string are easy. Logging is the mock magnet: spy on `console.log`, assert call count and args. Now everyone knows the private implementation.

Step 1 without even a strong type system: **make logging return what it logged**.

```ts
type LogMessage = unknown
type Greeting = string

const log = (value: unknown): LogMessage => {
  console.log(value)
  return value
}

const greet = (name: string): [Greeting, LogMessage] => {
  const greeting = `Hello, ${name}!`
  const logMessage = log(greeting)
  return [greeting, logMessage]
}
```

Unit test: assert greeting and log message from the return tuple. No spy. You proved logging happened because the only way to get a `LogMessage` for the second slot is to call `log`.

With TypeScript enforced, if you go "imperative OOP style" and only return the string, **it will not compile**. The type requires both values. The effect is embedded: call the effect function to obtain the proof type, return the proof type, compile, then unit-test values. That is "embedding effects to remove mocks."

### Errors as values (neverthrow and friends)

Promises and throw paths hide failure types. `Promise<Response>` lies about network, status, body, parse. Prefer Result-shaped APIs:

```ts
type Result<T, E> = Ok<T> | Err<E>
// neverthrow: ok(data) / err(error), andThen, match
```

Jesse's TyDD stack: model expected domain and infrastructure failures as discriminated unions; compose by unioning error types; exhaustiveness forces handling; try/catch only to map unsafe platform code into Result.

```ts
type FetchError =
  | { tag: 'Timeout'; time: Seconds }
  | { tag: 'BadStatus'; code: HttpStatusCode }
  | { tag: 'NetworkErr' }
  | { tag: 'BadBody'; zodErrors: ZodError[] }

type get = <T>(schema: ZodSchema<T>, url: string) => Result<T, FetchError>
// or ResultAsync / Effect equivalent
```

Stubs for unit tests: `ok([person])` / `err({ tag: 'Timeout', time: 30 })`. No mock HTTP stack for domain logic that only needs a fetch capability.

neverthrow gives `andThen` railways, `_unsafeUnwrap` for tests only (lint ban in prod), and `.match` at the edge (AWS Lambda HTTP response or panic rethrow). Railway Oriented Programming (Scott Wlaschin's name and metaphor; Jesse teaches it in TS) is the two-track pipeline: Ok continues, Err short-circuits.

### Effect-TS: success, error, requirements

Effect is a library for composable, production-grade TypeScript: typed values, typed errors, concurrency, resource safety, observability, and typed dependency injection via **Requirements** and **Layers**. Not "RxJS with different branding"; RxJS observables carry weak error typing (`Observable<T>` only) and multi-shot streams. Effect is typically single-shot program style with async/await-like generators or pipes, both type-safe.

The Effect type has three parameters people care about:

1. **Success:** what you get when it works.
2. **Error:** often a growing discriminated union as you compose.
3. **Requirements:** what dependencies this effect needs (the typed DI slot).

```ts
// conceptual shape
Effect<Success, Error, Requirements>
```

Why this kills mock theater:

- **Errors are values** in the type. No checked exceptions in TS; Effect tracks every possible error as you pipe. You do not discover failure shapes only via stack traces.
- **Requirements are typed.** Not "class implements interface maybe"; layers wire the dependency graph with compiler help. Runtime gets real Random/DB/Fetch services; unit tests provide stubs that always return 4 or fixed rows. Date-and-quarter nondeterminism is exactly what Requirements fix.
- **No ambient explode.** Effects do not throw out of the program the way raw Promises can; composition short-circuits on fail like a railway.
- **Start small.** Overwhelmed by docs? Use `Effect.succeed` / fail as Result. You do not need the whole program runner on day one. Folktale/Sanctuary/True-Myth veterans already know half the mental model.

Concurrency (limited parallelism, retry, backoff, jitter), abortable resource cleanup (useEffect-like cancel), schema validation with typed schema errors, and platform wrappers (stdout, files, multi-runtime) are why people go all-in later. The testing win starts at: **typed effects + typed requirements + pure stubs**.

### Capabilities and Functional Core / Imperative Shell

DI was invented (among other reasons) to make testing side effects possible: `Ship = (db: Database) => ...` with real pg at runtime and stub in tests. Composition of mock-heavy objects still hurts. **Functional Core, Imperative Shell** keeps most domain code pure. Haskell has IO; Elm and Roc remove side effects from the language entirely.

Capabilities make authority explicit:

```ts
// ambient authority: signature lies
function createReport(): Promise<void> {
  // query db, write filesystem, email; type says nothing
}

// capabilities: no FS passed, no FS authority
async function createReport(
  query: QueryDatabase,
  email: SendEmail
): Promise<void> { /* ... */ }
```

Authority via types too: not `cancelPayment(User, Account)` with runtime `if (!u.isPrimary) throw`, but `CancelPayment = (u: PrimaryUser, a: Account) => ...`.

Unit tests: pure stubs for each capability. Architecture: pass only what is needed; keep effects high and away from domain.

### Mock nuance (enterprise honesty)

After months of Angular PRs, Jesse's own mock critique got nuance: some languages and frameworks make mocks easier (Jest `spyOn` softens some breakage claims). Fragile tests and leaky abstractions still stand when inject makes it easy to pile dependencies, encapsulate side effects everywhere, and write tests that know every implementation detail. Void-returning methods that only work via spies remain the anti-pattern. Acceptance tests that are so slow nobody runs them push teams back to brittle mocks: fix the feedback loop, do not romanticize spies.

Purity heuristic remains: **Do I need mocks? If you can't use stubs only, it's not pure enough.**

## How to Apply

1. **Inventory void and ambient IO.** List functions that log, fetch, write, email with no useful return. Those are mock magnets.
2. **Return values for effects you care about.** Log message, written path, email payload ID: put them in the return type (tuple, product type, Result).
3. **Inject effect functions.** `log`, `fetch`, `query` as parameters or Effect Requirements. Production wires reals at the edge.
4. **Model expected failures as DUs + Result/Effect.** Domain vs infrastructure vs panic. Exhaustive handling at composition points.
5. **Unit test with stubs only.** `ok`/`err` or Effect test layers. Assert data and error tags. Ban `_unsafeUnwrap` outside tests.
6. **Keep integration for real edges.** Real files, real HTTP to imposters, real schema parse once at the boundary (Parse, Don't Validate / schemas).
7. **Adopt Effect or neverthrow deliberately.** neverthrow for Result railways; Effect when you want requirements, layers, concurrency, resource safety. Piecemeal is allowed.
8. **Push pure domain inward.** Capabilities at the shell; pure total functions in the core; no throw in the pure middle ("you put a grenade in it").

## Examples

**Situation:** `greet` logs and returns a string; tests spy on `console.log`.
**Application:** Wrap log to return the message; greet returns `[Greeting, LogMessage]`. Tests assert both. Compiler refuses silent log omission.
**Illustrative result:** Refactors of how logging is implemented inside `log` do not break callers' tests; behavior stays value-based.

**Situation:** Fetch pipeline: bad URL, timeout, 429, HTML body instead of JSON, Zod fail.
**Application:** `safeFetch` / schema parse into `Result<T, FetchError>` or Effect with error union. Stubs emit each tag. UI or Lambda `.match` maps to HTTP.
**Illustrative result:** Domain code never try/catches expected infra; unit tests do not need nock for pure decision logic.

**Situation:** Effect crash course for a team scared of the docs.
**Application:** Start with succeed/fail as Result; add one Requirement (Random or Fetch); provide test layer vs live layer; only later add retry and streams.
**Illustrative result:** Team gets typed errors and DI without boiling the ocean.

**Situation:** Angular service methods return void; tests are spy graphs; inject list grows forever.
**Application:** Prefer methods/functions that return values; inject narrow capabilities; use stubs; treat fragile spy tests as a design smell, not a coverage win. Improve acceptance feedback so people stop substituting mocks for confidence.
**Illustrative result:** Less coupling to private call order; more tests that survive refactors.

## Anti-Patterns

- **Spy-on-everything unit tests.** Implementation-coupled, flaky under mutation of test doubles, verbose.
- **Void domain APIs.** If there is no return value, tests will invent observation via mocks.
- **Promise-only error channel with async/await sprawl.** Reintroduces try/catch and loses typed composition; prefer Result/Effect chains or sureThing-style always-resolve envelopes when you need isolation.
- **`_unsafeUnwrap` in production.** Test escape hatch only; lint it.
- **Ambient authority signatures.** `() => Promise<void>` that does five IOs. Read the code to discover effects.
- **Throwing for expected domain/infra failures.** Exceptions act like side effects in practice; prefer errors as values (pragmatic industry consensus Jesse sides with for delivery).
- **Mocking pure functions.** If it is pure, pass inputs and assert outputs. Full stop.
- **Wifi-required "unit" tests.** Not unit tests.
- **100% coverage as the goal.** Coverage still lies; combine types, stubs, property tests, mutation testing, and CI (see property-and-mutation-testing.md).

Effects belong in types and return values. Dependencies belong in parameters, capabilities, or Effect Requirements. Mocks become the rare tool, not the default dialect.
