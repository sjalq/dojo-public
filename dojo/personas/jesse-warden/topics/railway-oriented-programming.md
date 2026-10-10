---
triggers:
  - "user asks about Railway Oriented Programming or two-track Result pipelines"
  - "user is composing fallible steps and drowning in nested if/Result unwrapping"
  - "user compares Promise/async-await error handling to Result composition"
  - "user asks about neverthrow, Effect, andThen, or Result short-circuit"
  - "user needs escape hatches for Lambda edges or unit tests with Result"
use_when:
  - "you have total or Result-returning functions and need to build larger fallible flows"
  - "happy-path pipelines break down because any step can fail"
  - "you want typed errors through composition without try/catch as primary control flow"
fails_when:
  - "_unsafeUnwrap is used in production code"
  - "ROP is used where a simple happy-path transform pipeline would do (no failures)"
  - "errors are thrown inside the railway instead of returned as Err values"
related:
  - "result-and-errors-as-values.md"
  - "parse-dont-validate.md"
  - "type-driven-development.md"
  - "impossible-states.md"
---

# Railway Oriented Programming

## When to Use

- You already have (or are introducing) `Result<T, E>` / Ok-Err style functions and need to **compose** them without opening every Result by hand
- A multi-step flow is mostly pure transforms plus a few fallible steps (parse, fetch, schema, domain rule)
- You want the **whole pipeline** to stay total: always returns a value (`Ok` or `Err`), no exceptions on the expected path
- Edge needs a single decision point (HTTP response, CLI exit, log + recover) rather than try/catch sprinkled through the middle
- TypeScript stack with **Neverthrow** or **Effect** (or another language with built-in Result bind)

## Fails When

- There is no failure: plain pipeline / map is enough; ROP is overhead
- You unwrap with `_unsafeUnwrap` / `_unsafeUnwrapErr` outside unit tests (and without a linter ban in app code)
- Steps still **throw** for expected domain/infra failures; the railway cannot short-circuit what it never sees as `Err`
- You need ordered *state machine* legality beyond "next step accepts this output type"; reach for typestate on top of ROP, not instead of modeling errors
- Team treats ROP as magic and never models the `E` side intentionally (see [result-and-errors-as-values.md](result-and-errors-as-values.md))

## Core Concept

**Railway Oriented Programming** means: build a pipeline of steps where each step can succeed or fail as a *value*, and the first failure skips the rest. Happy path stays on one track; errors stay on the other. In TypeScript this is usually Neverthrow or Effect (`.andThen` / bind). In plain English: stop unwrapping every Result by hand and stop using throw as your control flow for expected failures.

*(Name and classic two-track metaphor: Scott Wlaschin. Teach the idea first; credit when someone asks where it came from.)*

### Why plain pipelines are not enough

Once you have total functions, you need a way to build **larger** functions. Pipelines wire output of one function to input of the next: fewer temps, nested ifs, and return-as-control-flow. Array fluent APIs and even `Promise.resolve(x).then(...).then(...)` teach the shape.

That breaks when steps return `Result`. Manual unwrapping inside every step is painful:

```ts
// pain pattern: open Result, branch, re-wrap, every time
.then(r => {
  if (r.isOk()) return next(r.value)
  else return r
})
```

Even if nine functions are pure and infallible, connecting a tenth that can fail makes the **entire** pipeline fallible. You need first-class support for failure in the composition mechanism.

### Two tracks

ROP designs a pipeline with **two tracks**:

- **Green (Ok):** happy path; value keeps flowing into the next function  
- **Red (Err):** unhappy path; if any function returns `Err<E>`, later functions are **not** run; the error short-circuits and surfaces  

API shape in TS libs:

```ts
safeFetch(...)
  .andThen(safeParse)
  .andThen(cowSchema)
```

`andThen` (bind) only runs the next function when the previous step was `Ok`. On `Err`, the train switches to the red track and rides it out.

### What this solves (Jesse's list)

- Unlike Promise, it **doesn't throw exceptions**; the pipeline can remain a total function  
- You can define the **error type** the pipeline returns: `Result<T, E>` vs `Promise<T>` (where failure is untyped rejection)  
- All `Result<T, E>`-style functions compose easily  
- Functions that cannot fail: wrap with `ok()` and they still fit the railway  
- You get pipeline benefits **plus** type-safe error handling: the abstraction for building larger functions and, in turn, type-safe programs  

Effect docs talk about "running a program" vs just a function for a related reason: composition of total pieces into a whole application.

### vs Promise / async-await

| Concern | Promise / async-await | ROP over Result |
|--------|------------------------|-----------------|
| Failure channel | rejection + try/catch (or catch on chain) | typed `Err<E>` in the value |
| Expected failures | often exceptions or ad-hoc checks | modeled as values, composable |
| Composition | `.then` / await; easy to reintroduce try/catch | `.andThen` short-circuit, same container type |
| Totality | easy to lie with `Promise<T>` while network/parse throws | signature can be honest `Result` / `ResultAsync` |
| Typed E | weak by default | `ReadError \| FetchError` unions grow under exhaustiveness |

Promise can act like a pipe for happy transforms. Async/await often reintroduces try/catch responsibility and breaks pure Promise composition. Prefer Result railways when errors are **domain or expected infrastructure**, not only "the process dies."

For pure async without a full Result library, Jesse's older "promises that don't fail" / sureThing style (always resolve to `{ok, data?, error?}`) is a related industry pattern (Go `data, err`, Elixir `{:ok, _}`, Lua pcall). ROP is the clearer model once you commit to Result.

### Escape hatches (real world)

Jesse lists two you will need:

1. **`_unsafeUnwrap` / `_unsafeUnwrapErr` for unit tests only**  
   Neverthrow-style APIs expose these so tests can assert the happy or unhappy payload without ceremony. Pair with a **linter ban** so production code cannot call them.

2. **`.match` at the edge**  
   Example: top of an AWS Lambda: turn `Result` into HTTP JSON response, or throw if you are truly panicking (`Effect.die` / process-level failure). The middle of the program stays on the railway; the boundary translates to the platform.

## How to Apply

1. **Model errors as values first.** Define `Ok` / `Err` (or library Result), and design `E` as discriminated unions with payload data (`BadStatus` with code, `BadBody` with schema errors). See [result-and-errors-as-values.md](result-and-errors-as-values.md).

2. **Make each step Result-shaped.**  
   - Fallible: `string → Result<Person, ParseError>`  
   - Infallible: `person → PersonView`, then lift with `ok(view)` when placing on the railway  

3. **Compose with `andThen` (and `map` for pure transforms).** Keep one visual order of operations; let short-circuit handle the red track.

4. **Parse and smart-construct on the railway.** Boundary flow often looks like:  
   `neverThrowPromise().andThen(safeParseJSON).andThen(legacySchema).andThen(mapToCustomer)`  
   That is ROP carrying parse-don't-validate and anti-corruption mapping. See [parse-dont-validate.md](parse-dont-validate.md).

5. **Widen `E` as you compose.** `ReadError | FetchError` is normal. Exhaustiveness at the edge forces handling of every variant.

6. **Match once at the edge.** Lambda, HTTP handler, CLI: `.match({ ok: ..., err: ... })`. Do not re-open Result in every layer "just in case."

7. **Unit tests:** assert with `_unsafeUnwrap` under lint exceptions, or match in the test; never ship `_unsafe*` in app paths.

8. **Choose tooling.** TypeScript: **Neverthrow** or **Effect**. Other languages: use the built-in Result/Either bind, or the local FP library. Prefer Ok/Error naming over Left/Right when teaching mixed teams (words people understand).

## Examples

**Situation:** `safeFetch` → JSON parse → Zod cow schema → format for UI. Manual nesting is unreadable.

**Application:**

```ts
safeFetch(url)
  .andThen(safeParseJSON)
  .andThen(data => cowSchema.safeParseResult(data)) // Result-shaped
  .andThen(cow => ok(formatCow(cow)))
```

Pure `formatCow` sits on the green track via `ok`. Any `Err` from fetch, parse, or schema skips format.

**Illustrative result:** One total pipeline, typed `E`, no try/catch in the middle.

---

**Situation:** AWS Lambda must return HTTP JSON; domain returns `Result<Order, DomainError | FetchError>`.

**Application:** Run the railway in the handler body; at the end:

```ts
result.match({
  ok: order => ({ statusCode: 200, body: JSON.stringify(order) }),
  err: e => mapErrorToHttp(e), // or rethrow only for true panic
})
```

**Illustrative result:** Platform boundary is one place; domain stays pure and total.

---

**Situation:** Nine pure transforms, one DB write that can fail.

**Application:** Keep pure steps as `map` / `ok(f(x))`; only the DB step returns `Err` on failure. The railway still short-circuits if the write fails, without forcing every pure step to know about `E`.

**Illustrative result:** Failure is localized; pure core stays free of error noise until composition time.

---

**Situation:** Unit test needs the `Ok` payload without noise.

**Application:** In test file only, `_unsafeUnwrap(result)` after arranging success; ESLint rule blocks `_unsafeUnwrap` under `src/`. Prefer `match` if the team bans unsafe entirely.

**Illustrative result:** Tests stay short; production cannot cheat the type.

## Anti-Patterns (tactical)

**Don't:** Peel every Result with `if (r.isOk())` inside each `.then`.  
**Why:** That is the pain ROP exists to remove. You reintroduce nested control flow and lose short-circuit abstraction.

**Don't:** Use Promise rejection as your only error channel for expected failures, then sprinkle try/catch.  
**Why:** `Promise<T>` lies about failure; `E` is untyped; composition becomes exception control flow again.

**Don't:** Call `_unsafeUnwrap` in application or handler code "because we know it's Ok."  
**Why:** That knowledge goes stale. Lint and culture: tests only.

**Don't:** Throw inside a railway step for `NotActivated` or `BadStatus`.  
**Why:** Throws leave the two-track model; callers must catch; purity and totality die. Return `err({ tag: 'NotActivated' })`.

**Don't:** Build a railway with a vague `Error` string and no DU structure.  
**Why:** You lose payload data and exhaustiveness. ROP without intentional `E` design is just a fancier try/catch.

**Don't:** Expect ROP alone to prevent shipping an unpaid order if `Ship` accepts any `Order`.  
**Why:** Wrong *order of states* needs typestate (transition functions that only accept `Paid`). ROP composes failures; typestate composes legal sequences.

**Don't:** Skip crediting Scott Wlaschin when teaching the name.  
**Why:** ROP is his teaching gift to the industry. Jesse adapts it; he does not own the metaphor.
