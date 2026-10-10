---
triggers:
  - "user hard-codes fs, fetch, requests, or db inside a function they want to unit test"
  - "user says dependency injection is only for OOP or only for containers"
  - "user claims DI has nothing to do with testing"
  - "user needs stubs for side effects without mocks or frameworks"
  - "user asks how to test pure pipelines that touch disk or network"
use_when:
  - "making FP or JS/Python functions unit-testable by injecting side-effect functions as parameters"
  - "explaining DI history and why containers are optional ceremony, not the idea"
  - "contrasting Elm (no side effects in the language) with ReScript/JS/Python (side effects exist)"
  - "replacing config-on-disk-only knobs with injectable readFile/fetch/logger deps"
fails_when:
  - "the language has no side effects in user code (Elm) and DI is a solution to a problem that does not exist"
  - "the team uses DI containers as magic wire-up that hides intent instead of explicit parameters"
  - "someone injects everything and still tests implementation with spies rather than return values"
related:
  - "effects-without-mocks.md"
  - "tdd-in-fp-and-oop.md"
  - "property-and-mutation-testing.md"
  - "continuous-delivery-shift-left.md"
---

# Dependency Injection in FP: It's Just Parameters

## When to Use
- Your unit under test hard-codes `fs`, `fetch`, `requests`, a DB client, or a logger and you need deterministic tests without mucking with files or the network.
- Someone on the team says "DI has nothing to do with testing" or treats DI as Java Spring baggage you should avoid in Node/Python.
- You want the same Config (or pipeline) in unit tests with stubs and in integration tests with real `readFile` / real HTTP.
- You are teaching FP people that the technique they already use (pass the effect in) is the same industrial DI practice OOP people reinvented with constructors and containers.
- You are in ReScript, TypeScript, JavaScript, or Python, where side effects exist, and you need a pure-enough core.

## Fails When
- **Elm (and similar).** All functions are pure; side effects live outside your code in the runtime. There is nothing useful to inject for unit tests of your domain logic. Do not invent DI theater.
- **Container cosplay.** You did not need Spring in Node. NestJS-style containers can reintroduce the ceremony Java refugees fled. Prefer passing parameters (or a small deps bag) you can read in the signature.
- **Mocks of implementation.** DI is not a license for spies that assert "console.log was called once." Prefer stubs that return values; test outputs, not call graphs (see effects-without-mocks.md).
- **Ambient authority still wins.** If the function still reaches for globals after you inject one dep, you only half-fixed it.

## Core Concept

In Object Oriented Programming, Dependency Injection means a class does not instantiate its own collaborators. You pass a logger, a JSON reader, a database into the constructor. The class stays the same; tests pass stubs; production passes real implementations. Inversion of Control is the same idea from the other direction: something higher up creates the deps.

In Functional Programming, that technique is a fancy way of saying: **call a function with parameters**. The parameters are not only data. They are the same kind of dependencies OOP injects: modules or functions that do side effects, so your function stays easier to test and configure.

Mark Seemann has a whole talk on Partial Application as DI in FP. You do not need partial application to start. Pass the function. Later, curry and partial-apply the static left args if you want advanced packaging.

### The untestable problem (OOP and FP look the same)

Classic untestable Config class: it `new`s a `JSONReader` inside a private method, reads `config.json` from disk, plucks `env`, returns a QA or production URL. The only pure bit is the env-to-URL branch. Unit testing whitebox is hard; your only knob is a file on disk relative to the class. Lamesauce.

Same shape in FP with a pipeline:

```js
import fs from 'fs'

const getServerURL = fileName =>
  fileName
  |> fs.readFileSync
  |> JSON.parse
  |> (json => json.env)
  |> (environment =>
    environment === 'production'
      ? 'http://server.com'
      : 'http://localhost:8000'
  )
```

`fs` is imported as a concrete implementation and closed over. The only way to test is to muck with config files. Same design smell, different syntax.

### Make it injectable

OOP: constructor takes `JSONReader`; private methods use the field.

```js
class Config {
  #JSONReader
  constructor(JSONReader) {
    this.#JSONReader = JSONReader
  }
  // ...
}
```

Unit stub:

```js
class JSONReaderStub {
  getConfigJSON() {
    return { env: 'qa' }
  }
}
const config = new Config(new JSONReaderStub())
expect(config.getServerURL()).to.equal('http://localhost:8000')
```

Integration: real reader with real `fs` and a fixture file. Same assertions; different deps.

FP: pass `readFile` as a parameter.

```js
const getServerURL = (readFile, fileName) =>
  fileName
  |> readFile
  |> JSON.parse
  // ... env to URL
```

Unit stub: `const readFileStub = () => '{ "env": "qa" }'`. Integration: `getServerURL(fs.readFileSync, './test/integration/qa-config.json')`.

That is the whole move. Configurable. Deterministic. Fast. Unhappy paths (missing file, bad JSON, missing env, unknown env) are more stubs, not more filesystem choreography.

### History: why people flinch when you say DI

DI is not a 2010 fad. Rough arc Jesse defends when experienced devs have visceral reactions:

1. **1980s design tool.** Make OOP classes configurable: inject logger instead of `new Logger()` inside the constructor. Swap in-memory vs disk; swap audio codecs. Often called Inversion of Control.
2. **Composition over inheritance.** Late 90s / early 2000s: deep inheritance hierarchies hurt; composition with injected collaborators is easier to maintain. DI helps composition.
3. **Testing becomes central.** 1990s onward: inject fakes in tests, reals in prod, source code unchanged. Kent Beck's XP (TDD) 1999; Agile Manifesto 2001; Spring DI container 2002; Fowler's "Inversion of Control Containers and the Dependency Injection pattern" 2004 popularizes the term.
4. **Containers get complicated.** Spring and cousins start simple (two static factories: test vs prod deps) and grow into frameworks. Type systems and interface soup make doubles painful. JUnit-era test-double vocabulary confuses everyone (even with Meszaros's definitions).
5. **Java egress stigma.** Many Java/.NET developers fled to Rails, Node, Django for less ceremony. They still did OOP, but carried prejudice against "Java-esque" containers. Dynamic communities rejected wholesale DI containers while oddly importing test-double confusion. NestJS is a partial comeback that fights original Node rejection of Java DI soup.
6. **FP quietly does the simple thing.** Languages with side effects pass deps as function parameters. Type systems often mean one function type, not interfaces that grow ten methods and make doubles miserable. **You never see DI containers in FP languages because why would you build a framework around passing a parameter to a function?**

Origins were design. For more than twenty years testing has been a first-class reason. Over half the industry use of DI is testing-related; design is still the origin story. If someone says DI should not be used for testing, they do not know what they are talking about.

### Elm vs ReScript / JS / Python

| Language surface | Side effects in your functions? | DI as parameters? |
|------------------|---------------------------------|-------------------|
| Elm | No; purity is language law | Not used for unit testing the domain the same way |
| ReScript | Same side-effect model as JS (compiles to JS) | Yes, when you want pure-enough units |
| JS / TS / Python | Yes | Yes; inject `fs` / `fetch` / `requests` |

Do not universalize "FP never needs DI." FP that still has disk and network does.

### Stubs, not theater

FP testing ground rules Jesse teaches for Node: if you need mocks rather than stubs, the unit is not pure enough. Stubs are pure functions that return a fixed value. Happy path stub returns OK data. Unhappy path stub returns the error shape. No setup/teardown mutation of modules. Turn wireless off: if tests fail, they were never unit tests.

Default parameters or partial application can package production defaults (`getWeather(city, state, request = realRequest)`) so call sites stay clean while tests pass a third-arg stub. Order tradeoff: curry culture prefers static left / dynamic right; JS defaults often put optionals on the right. Both are DI packaging.

Capabilities (TyDD Part 22) are the typed upgrade of the same idea: ambient authority (`createReport(): Promise<void>` that queries DB, writes FS, emails) lies in the signature. Require `QueryDatabase` and `SendEmail` as parameters; no FS capability means no filesystem authority. Unit tests pass pure stubs. Architecture moves effects up and out of the domain.

Effect-TS layers and typed Requirements are industrial DI with types on the third Effect type parameter (success, error, requirements). Same story: stub services in tests, real services at runtime, compiler checks the graph. You do not need Effect to practice parameter DI; Effect is batteries-included for people who want layers.

## How to Apply

1. **Find the impurity.** Ask: does this function need mocks? If stubs alone cannot drive it, something is hard-coded (import of `fs`, global config, `new Date()`, live HTTP).
2. **Lift the effect to a parameter.** `get(url)` becomes `get(requests, ssl, url)`. `getServerURL(fileName)` becomes `getServerURL(readFile, fileName)`. Name the parameter after the capability, not the vendor.
3. **Keep business logic pure.** Env-to-URL, parse-and-decide, format-name: pure functions of data. Inject only the edge.
4. **Write stubs as pure functions.** `() => '{ "env": "qa" }'`, `() => ok([person])`, `() => err(timeout)`. Assert return values. Prefer no spies on call counts for domain behavior.
5. **Integration tests use reals.** Same public function, real `fs.readFileSync`, real fixture path, real HTTP to a stub server (Mountebank / similar) when the edge itself must be proven.
6. **Optional packaging.** Partial application (Seemann), default parameters, or a small `Dependencies` product type (`processOrder(deps, order)`) when arity gets loud. Product types absorb growth better than twenty positional params.
7. **Do not force containers.** If a container hides lifecycle and intent, you recreated the stigma. Explicit parameters are features.
8. **Language check.** In Elm, invest in pure domain tests and trust the runtime for effects. In ReScript/JS/Python, inject.

## Examples

**Situation:** Node service reads `config.json` for QA vs production API base URL. Tests either hit disk or skip the path.
**Application:** Inject `readFile`. Unit stub returns JSON string for QA; another stub returns production; another returns garbage JSON for the error branch. Integration test uses `fs.readFileSync` and fixture files.
**Illustrative result:** Config logic is unit-tested without wireless, without temp files, without changing process CWD. Integration still proves real parse and real disk once.

**Situation:** Python `get(url)` closes over a module-level `ssl` flag and hard-codes `requests`.
**Application:** Purity gradient: impure `get(url)` with global ssl → pure-er `get(ssl, url)` → unit-testable `get(requests, ssl, url)` → total-ish wrap that try/excepts into a return value (Result/error object) instead of raising through the pure core.
**Illustrative result:** You can stub `requests` and assert Ok/Error without a network. Golang-flavored shape without leaving Python.

**Situation:** Training materials claim "DI has nothing to do with testing" and "adding DI just to test is terrible."
**Application:** Teach the 40+ year history: design origin, testing as major sustained use, containers as optional (often overbuilt) mechanism. Show constructor injection and function-parameter injection side by side as the same idea.
**Illustrative result:** Team stops cargo-culting anti-DI from Java trauma and starts injecting effects where tests need determinism.

**Situation:** `createReport` queries DB, writes a file, emails; signature is `() => Promise<void>`.
**Application:** Capability parameters: `createReport(query, email)` only. File write lives at a higher composition site if needed. Tests stub query and email as pure async functions returning fixed values.
**Illustrative result:** Ambient authority shrinks; the type (or at least the parameter list) documents what the function can do.

## Anti-Patterns

- **Hard-coded side effects in the unit you claim is unit-tested.** File mucking and wifi-on tests are not unit tests.
- **DI containers as identity.** Passing a parameter is the technique. Frameworks are optional packaging with a long history of complexity.
- **"DI is not for testing."** Historical and industrial practice says otherwise. Design and testing are both legitimate reasons.
- **Mock-first after inject.** You injected the logger then asserted `info` was called with exact strings. Prefer return values and typed effects (see effects-without-mocks.md).
- **Interface bloat (OOP).** Interfaces that grow forever make doubles hard. Prefer small function types; FP stubs stay one function.
- **Forcing DI into Elm domain code.** Wrong problem. Purity is already there.
- **Default args that close over mutable globals.** Defaults can package DI, but impure defaults reintroduce nondeterminism. Prefer injecting the real module explicitly at the composition root when purity matters.
- **Import-time server start.** Requiring a module for tests should not hang on `listen()`. Gate side effects on main/module entry; return values (Maybe of server) from start helpers.

DI is design and testing. In FP it is ordinary parameter passing aimed at side effects. No container required. Stubs over mocks. Elm is the exception that proves the side-effect rule.
