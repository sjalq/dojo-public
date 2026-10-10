---
triggers:
  - "user has nested ifs, temporary variables, and return-as-control-flow for multi-step logic"
  - "user asks about pipe, flow, compose, or expression-oriented code"
  - "user struggles to chain Result-returning steps without manual unwrapping"
  - "user asks about partial application or building larger functions from small pure ones"
  - "happy-path pipeline breaks when any step can fail"
use_when:
  - "composing total pure transforms into a larger total function"
  - "replacing imperative multi-step procedures with readable left-to-right data flow"
  - "adopting Railway Oriented Programming (Scott Wlaschin) for Result pipelines"
  - "teaching Promise.then as an on-ramp to pipe thinking in JavaScript"
fails_when:
  - "steps are impure and order hides side effects; pipeline cosmetics over mutation soup"
  - "you force pipe syntax without Result/ROP when failures dominate"
  - "you use _unsafeUnwrap in production to 'keep the pipe pretty'"
related:
  - "pure-and-total-functions.md"
  - "smart-constructors.md"
  - "schema-at-the-boundary.md"
  - "typestate-and-capabilities.md"
  - "product-and-union-types.md"
---

# Pipelines and Composition

## When to Use

- You have total (or pure) functions but assemble them with temps, nested ifs, early returns, and scoping mess.
- Data transformation is a sequence: parse → filter → format → respond.
- Result-returning steps make `.then` / imperative code painful: open Ok, check, else return Err, repeat.
- You want **total applications**: programs built from composed functions, not one giant procedure.
- Partial application would clean call sites: fix the config/deps, leave the varying argument for later.

## Fails When

- Pipeline is only style and the functions still throw, mutate shared state, or depend on ambient I/O. Fix purity first.
- Every step can fail and you only use happy-path `pipe` without a two-track railway; you will invent manual unwrap spaghetti.
- You optimize for point-free golf so nobody can read the order of operations. Readable left-to-right beats clever.
- Domain needs **order enforced by types** (cannot ship before pay). Plain pipelines still allow wrong assembly; add typestate.

## Core Concept

Total functions alone are not enough. You need a way to build **larger functions**. Imperative composition brings temporary variables, nested conditionals, error handling noise, and `return` used as control flow.

**Pipelines** wire functions so the output of one is the input of the next. The pipeline is responsible for feeding each stage. You keep visual order of operations without scoping landmines. The compiler checks that pipes **fit**: this stage's output type is the next stage's input type.

Everyday on-ramps:

- Array fluent APIs: `map`, `filter`, `reduce` (people already pipeline without the word).
- **Promise as pipe** without Lodash/Effect:  
  `Promise.resolve(s).then(parse).then(filter).then(format)`  
  (Still watch exceptions; Promise is not Result.)
- FP languages with `|>` (and yes, PHP eventually got in on the joke).

```ts
// Imperative mess sketch
let data = raw
try {
  data = JSON.parse(data)
} catch { return "" }
const cows = data.filter(...)
return formatNames(cows)

// Pipeline of total pieces
pipe(raw, safeParse, filterCows, formatNames)
// or Promise.resolve / Effect / neverthrow style
```

Pipelines build **"Total Applications."** That is why Effect docs talk about running a **program**, not only a function.

### Partial application

Partial application fixes some arguments now, returns a function waiting for the rest. Useful for DI-style capabilities and config:

```ts
const add = (a: number, b: number) => a + b
const add5 = (b: number) => add(5, b)

// deps fixed, order varies
const processWith = (deps: Deps) => (order: Order) => process(deps, order)
```

Jesse teaches partial application as a practical tool (see his dedicated materials), not as a category theory exercise. It makes pipelines and tests easier: inject stubs once, apply domain data later.

### When pipeline alone fails: Railway Oriented Programming

Happy-path pipelines break down when any step returns `Result`. Manual unwrapping inside each stage is painful. Even if 9 functions cannot fail, connecting a 10th that can makes the whole pipeline fallible.

**Railway Oriented Programming** originates with **Scott Wlaschin** (F# for Fun and Profit; the railway metaphor and talks). Credit him for the name and core idea. Jesse teaches ROP in TypeScript with neverthrow/Effect, Lambda edge matching, and total-function framing.

Two tracks:

- **Green (Ok):** keep passing `T` to the next function.
- **Red (Err):** short-circuit; skip remaining stages; surface `E`.

```ts
safeFetch(url)
  .andThen(safeParseJson)
  .andThen(cowSchema)
  .andThen(toDomain)
```

Benefits:

- Unlike Promise, no exception control flow; pipeline can stay total.
- Typed errors: `Result<T, E>` vs bare `Promise<T>`.
- All Result-style functions compose.
- Pure non-failing steps: wrap with `ok(value)` / `map`.

Escape hatches for the real world:

1. `_unsafeUnwrap` / `_unsafeUnwrapErr` **for unit tests only**, lint-banned in production.
2. `.match` at the edge (AWS Lambda → HTTP JSON, or rethrow/panic mapping).

Libraries: **neverthrow**, **Effect**, language built-ins elsewhere (Rust `?`, F# Result modules, etc.). Elm already pushes you toward composition with `Result`/`Task`.

### Expression-oriented mindset

Prefer expressions that evaluate to values over statements that mutate and maybe return. Pipelines are expression-oriented architecture for multi-step work. Pair with immutability so stages do not silently stomp shared objects mid-pipe.

## How to Apply

1. **Extract total stages.** Name them: `parseInput`, `applyDiscount`, `formatResponse`. Each has clear types in/out.

2. **Wire happy path with pipe/flow** when stages cannot fail or failure is already handled inside.

3. **Switch to ROP (`andThen` / `flatMap`)** when any stage returns Result. Do not hand-unwrap in the middle of the pipe.

4. **Map pure transforms; andThen fallible ones.** Know the difference in your library (`map` vs `andThen`).

5. **Partial-apply configuration and capabilities** at the shell; pass the specialized function into the pipeline.

6. **Match once at the boundary.** HTTP status, UI message, log fields. Core returns Result; shell interprets.

7. **Keep order readable.** Prefer  
   `pipe(x, a, b, c)` or chained `andThen` over point-free stacks nobody can debug at 2am.

8. **When order is a business rule, add typestate.** Pipeline shows sequence; typestate makes illegal sequences untypable ("setting up the Roomba").

9. **Do not use Promise exception flow as your Result railway.** Map known unsafe to Result early; then ROP.

## Examples

**Situation:** Handler: parse body, load user, check entitlement, charge card, write audit; nested try/catch and early returns, 80 lines.

**Application:** Each step `ResultAsync`. Railway:  
`parseBody.andThen(loadUser).andThen(checkEntitlement).andThen(charge).andThen(audit)`.  
`.match` to HTTP at the end. Pure pricing stays `map`.

**Illustrative result:** New step (fraud check) inserts as one `andThen`. Error union grows; exhaustiveness forces handling.

---

**Situation:** Team uses Lodash `flow` for transforms but errors still throw from `JSON.parse` mid-flow.

**Application:** Replace throwing parse with smart constructor Result; switch flow to neverthrow/Effect railway or explicit Result pipe. Happy `flow` remains for pure string/array stages after success.

**Illustrative result:** Pipeline stops being partial. Tests assert Err cases without try/catch.

---

**Situation:** Same `processOrder(deps, order)` called with the same deps 20 times.

**Application:** `const process = processOrder(deps)` partial; map over orders with `process`. In tests, `processOrder(stubDeps)`.

**Illustrative result:** Call sites shrink; DI without a container.

---

**Situation:** Form validation accumulates many field errors; short-circuit railway hides all but first.

**Application:** Happy pipeline is wrong tool for full-form accumulation. Use applicative-style error accumulation or a dedicated form validation pass, then railway the submit that needs sequential IO. Jesse notes pipelines also support accumulation/stream use cases when designed for them; pick the composition that matches the problem.

**Illustrative result:** UX shows all field errors; payment railway still short-circuits on first infra failure.

## Anti-Patterns (tactical)

**Don't:** Build pipelines from partial, throwing functions and call it FP.
**Why:** One throw derails totality. Wrap with smart constructors and Result first; then compose.

**Don't:** Manually unwrap Result at every step "so it's clear."
**Why:** That is the pain ROP solves. Clarity lives in stage names and types, not in repeated `if (r.isOk())` boilerplate.

**Don't:** `_unsafeUnwrap` in production handlers for convenience.
**Why:** You deleted the error track. Lint ban it outside tests.

**Don't:** Promise-only composition for domain errors you care about.
**Why:** `Promise<T>` does not type the error channel. Users get 500s or untyped rejects. Result/Effect model `E`.

**Don't:** Credit Jesse as inventor of Railway Oriented Programming.
**Why:** **Scott Wlaschin** owns the origin. Say so when teaching. Jesse adapts it for TS/enterprise TyDD.

**Don't:** Require monoid/functor lectures before `andThen`.
**Why:** "If Ok, do next; if Err, stop" is enough to ship. Category theory can be optional deepening, never a gate.
