---
triggers:
  - "user asks about Result, Either, Ok/Err, or errors as values"
  - "user relies on try/catch for expected domain or infrastructure failures"
  - "user needs to classify domain vs infrastructure vs panic vs unexpected errors"
  - "user designs fetch/API wrappers and wants honest typed failure modes"
  - "user asks why functional programmers avoid exceptions"
use_when:
  - "designing pure/total functions that can still fail in expected ways"
  - "composing fallible operations and needing exhaustiveness over error variants"
  - "wrapping unsafe APIs (JSON.parse, fetch, SDK throws) into typed Results"
fails_when:
  - "Result is used for true panics that should crash the process"
  - "try/catch remains the primary control flow for expected failures"
  - "error unions are flat strings with no payload where variants need different data"
related:
  - "railway-oriented-programming.md"
  - "parse-dont-validate.md"
  - "type-driven-development.md"
  - "impossible-states.md"
---

# Result and Errors as Values

## When to Use

- Functions can fail in **expected** ways (domain rules, network, parse, auth) and callers must handle those ways
- You want **pure** and **total** public APIs: every input yields a sensible value (`Ok` or structured `Err`), not a throw for normal failure
- You are redesigning `fetch` / file / SDK boundaries that currently lie with `Promise<T>` or bare throws
- Exhaustiveness should force handling when new error variants appear
- Teaching or adopting FP in TypeScript/JS/Python without requiring Category Theory

## Fails When

- The failure is **unrecoverable** or truly exceptional and the process should die (panic / `Effect.die` / hard fail); stuffing that into Result noise confuses operators
- You model nothing: empty `catch` or generic `Error` string with no design process
- Team uses Left/Right naming when Ok/Error would communicate (accessibility of mental model for non-Haskellers)
- You return Result but still throw on the "unhappy" path sometimes, so callers cannot trust the type
- Absence is just "maybe missing" with no error meaning: prefer Maybe/Option at edges, or a named DU, not a fake Result

## Core Concept

### FP tradition (credit the lineage)

**Errors as values** is industry and FP consensus, not a Jesse invention: Result/Either (Ok/Err), Go's `data, err`, Rust's `Result`, Lua `pcall`, Elixir `{:ok, _}`. Functional programmers avoid exceptions **in practice** because exceptions behave like side effects for software delivery: unpredictable, harder to test, worse composition, even when mathematicians argue nuances about referential transparency.

Jesse's engineer stance: "I'm not here to debate semantics, I'm here to deliver working software." Prefer returning errors as values. Prefer words people understand: **Ok** and **Error**, not Left/Right ("dabbing… or gaming… or anything other than programming").

Good type systems push **pure and total functions**. Where do errors go? Into the type.

### Result / Either shape

```ts
type Result<T, E> = Ok<T> | Err<E>
// Ok holds success value; Err holds typed failure
```

Result is a **discriminated union** convention that separates happy and unhappy paths while keeping errors typed. It is the FP world's answer to: how do you differentiate two paths from a DDD perspective?

```ts
type FetchResult = Result<Array<Person>, FetchError>
```

### Four error types (taxonomy)

Jesse classifies errors into four kinds:

1. **Domain-created** — business rules (account not activated, secondary cannot cancel primary's payment)  
2. **Expected infrastructure** — network timeout, bad HTTP status, schema/parse failure, missing secrets file  
3. **Unrecoverable** — process cannot continue meaningfully; panic / die  
4. **Unexpected / exceptional** — truly unforeseen  

**Focus design energy on (1) and (2).** Model them with Discriminated Unions and Result. Obsessing over (3) and (4) is less useful; if you nail (1) and (2), (4) "goes away" as a daily concern. Map true panics deliberately (throw / `Effect.die` / process failure) rather than pretending every failure is recoverable.

**Heuristics:**

- If neither you nor the user can do anything useful → often (3) panic  
- Ask Product/Business Owner: if they have a product answer → (1) domain; if confused / "that's infrastructure" → (2)

### Errors as Values as a design process

**Errors as Values** moves errors from a random runtime consequence to an **iterative design process using types**: intentionally design what can go wrong in functions, integrations, and the app.

For a typed `get` with schema:

- One thing can go right: schema passes  
- Narrow what can go wrong  

Example infrastructure union:

```ts
type FetchError = Timeout | BadStatus | NetworkErr | BadBody

type Timeout = { tag: 'Timeout'; time: Seconds }
type BadStatus = { tag: 'BadStatus'; code: HttpStatusCode }
type BadBody = { tag: 'BadBody'; zodErrors: ZodError[] }
// plus NetworkError, etc.
```

**Why DU not a flat union of strings?** When you get `BadStatus`, you need the status code. When you get `BadBody`, you need schema error details. DUs hold data **and** ensure you only access that data for that variant.

Domain errors appear even on "happy path" flows:

```ts
type NotActivated = { tag: 'NotActivated' }
if (!account.activated) return err({ tag: 'NotActivated' })
```

The compiler ensures you handle them as the code grows.

### Composition and exhaustiveness

Composing functions **widens** `E`:

```ts
type ReadSecrets = () => Result<Secrets, ReadError>
type fetchPeople = () => Result<Array<Person>, ReadError | FetchError>
```

Those anonymous unions of errors start happening a lot. Exhaustiveness checking ensures you handle all of them. You no longer use try/catch unless **mapping known unsafe code into a Result**:

```ts
try {
  return ok(JSON.parse(data))
} catch (error) {
  return err(error) // or structured JSONError
}
```

### Pure functions prefer Result over exceptions

Exceptions multiply possibilities (X * Y exponential complexity for callers). Pure functions want: call it, get a value. Returning Result keeps the unhappy path a **value** you can map, recover, retry, or match.

Policy from pure-vs-total teaching: **privates pure; publics total.** Total public APIs handle invalid inputs with structured failure instead of nonsense success values (Infinity, NaN, garbage string concat) or throws.

Recovery stays possible: read secrets from a service if env fails; retry `BadStatus` with 429; convert domain errors to user-facing messages at the edge.

### Fetch redesign (canonical)

Lying API:

```ts
type fetch = (url: string) => Promise<Response>
// response.ok checks, json() throws, exceptions, not type-safe
```

Honest API:

```ts
type get = <T>(s: ZodSchema<T>, url: string) => Result<T, FetchError>
// or ResultAsync in neverthrow/Effect ecosystems
```

Map runtime to tags: AbortError → Timeout, `!ok` → BadStatus, schema fail → BadBody, etc. Single switch (or match) over unhappy paths; still type-safe retry/recover.

### Library boundaries

Prefer not to leak raw Zod (or schema lib) error types across **your** library boundary forever; map to your own error types when packaging for consumers (version churn, coupling). Internally, carrying `ZodError[]` on `BadBody` is fine while you own the app.

## How to Apply

1. **List failures intentionally** for the function or use case. Classify 1–4. Design DUs for 1 and 2 with useful payloads.

2. **Introduce `Result<T, E>`** (hand-rolled Ok/Err tags, neverthrow, Effect, returns in Python, etc.).

3. **Wrap unsafe natives** at the boundary with try/catch → Result (smart constructor style). Small batches; you cannot fix all unsafe code at once.

4. **Compose** with map/andThen ([railway-oriented-programming.md](railway-oriented-programming.md)); let `E` widen; exhaustively handle at edges.

5. **Test with `ok(...)` / `err(...)` stubs**, not `expect(() => ...).toThrow()` for your pure core.

6. **Match or switch once** for user/HTTP/log translation; include enough context for humans (what failed, what to do). Domain vs infra vs panic guides display.

7. **Prefer Result over Maybe** when "none" is really a failure with meaning. Push true optionality (env vars) to edges.

8. **Panic deliberately** for unrecoverable cases; do not force every disaster into `Err` if the process must stop.

## Examples

**Situation:** Node service uses try/catch around fetch + JSON + business rules; bugs surface as 500s with stack traces only.

**Application:** Define `FetchError` DU + domain errors; `get(schema, url) → Result`; business rule returns `err({ tag: 'NotActivated' })`; Lambda `.match` maps to HTTP. try/catch only inside the fetch wrapper.

**Illustrative result:** Callers handle typed variants; retries target 429; users see intentional messages.

---

**Situation:** `divide(a, b): number` returns Infinity/NaN; pure but not total.

**Application:** `Divide = (...) => Result<number, DivideError>` or constrain `b: PositiveInteger`. Public total; private pure helpers assume validated inputs.

**Illustrative result:** Signature stops lying; UI never shows Infinity as a "success."

---

**Situation:** Team argues exceptions are fine because "TypeScript has try/catch."

**Application:** Engineer framing: industry (Go, Rust, Lua, FP) accepted errors as values for delivery reasons. Exceptions poison pure composition ("you put a grenade in it"). Keep throws for panic mapping only.

**Illustrative result:** Core becomes testable with stubs of Ok/Err; no mock theater for exception paths.

---

**Situation:** Four unhappy paths need different recovery (retry, re-auth, fix body, show domain message).

**Application:** One switch/match on `tag`; each arm has the right payload fields. Exhaustiveness fails compile when a fifth variant is added.

**Illustrative result:** New error types cannot be ignored silently.

## Anti-Patterns (tactical)

**Don't:** Use try/catch as primary control flow for domain and expected infra failures.  
**Why:** Unpredictable, hard to compose, signatures lie, tests become throw-expecting instead of value-asserting.

**Don't:** Model expected failures only as thrown `Error` with message strings.  
**Why:** No exhaustiveness, no structured payload, no type-level composition of `E`.

**Don't:** Use a flat `type FetchError = 'timeout' | 'bad-status'` when you need codes and zod details.  
**Why:** Variants need different data; DUs ensure safe field access per case.

**Don't:** Return Result in the type but throw on some branches "for convenience."  
**Why:** Callers cannot trust the signature; totality is a lie.

**Don't:** Stuff panics into Result and then ignore `Err` at the top.  
**Why:** Unrecoverable failures need a clear die/crash path; silent swallow is worse than throw.

**Don't:** Prefer Left/Right naming when teaching mixed enterprise teams.  
**Why:** Ok/Error are words people understand; reduce accidental gatekeeping.

**Don't:** Skip Product/Business conversation when classifying domain vs infra.  
**Why:** Wrong classification produces wrong UX and wrong recovery (retry a business rule, or show a stack trace for "not activated").
