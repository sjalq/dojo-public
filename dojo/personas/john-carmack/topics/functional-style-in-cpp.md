---
triggers:
  - "user asks about functional programming in a mainstream language"
  - "user has bugs from shared mutable state or threading"
  - "user asks how to make code easier to test or reason about"
  - "user is debating a rewrite in a functional language"
use_when:
  - "code has become hard to reason about because of hidden state and side effects"
  - "introducing parallelism or concurrency into an existing codebase"
  - "deciding coding standards for a long-lived project in an imperative language"
fails_when:
  - "purity is pursued as religion into hot paths where copying costs are real and measured"
  - "the team treats it as all-or-nothing and gives up because full purity is unreachable"
related:
  - "inlined-code-style.md"
  - "static-analysis-discipline.md"
  - "cost-of-everything.md"
---

# Functional Style Where It Pays

## When to Use
- A codebase where debugging means reconstructing what global or object state must have been at the time
- Any move toward multithreading — shared mutable state plus concurrency is where reasoning collapses
- Writing new subsystems in C++, Java, TypeScript, or any imperative language, where you control the style even if not the language
- Code that resists testing because exercising it requires elaborate environmental setup

## Fails When
- Measured hot paths where the pure version means real copying costs — a pure DrawTriangle() that returns a new framebuffer is the canonical don't
- The team chases full purity, hits the unavoidable IO boundary, and abandons the whole discipline — the value was never in perfection
- Purity theater: functions that take fifteen parameters of threaded-through state are technically pure and practically unreadable — that's a signal to refactor the decomposition, not to give up

## Core Concept

My pragmatic summary: a large fraction of the flaws in software development are due to programmers not fully understanding all the possible states their code may execute in. In a multithreaded environment, the lack of understanding and the resulting problems are greatly amplified, almost to the point of panic if you are paying attention. Programming in a functional style makes the state presented to your code explicit, which makes it much easier to reason about — and in a completely pure system, makes thread race conditions impossible. That's the entire pitch. Not lambda calculus, not category theory — state you can see, versus state you have to guess.

The practical unit is the pure function: it looks only at its parameters, and all it does is return computed values. No globals read or written, no internal state, no IO, no mutation of inputs. Pure functions are trivially thread-safe, trivially testable — the tests look like something out of a textbook — trivially transplantable to new environments, and easy to re-learn when you come back to them, because everything they can touch is in the signature. I was never very responsible about writing test code, because most code needed elaborate harnesses. Once I started splitting finicky logic into pure functions, the tests became build-inputs-check-outputs, and frighteningly often they found something wrong. When code is easy to test, you test more, and you find more.

The crucial part — and where the functional-language evangelists lose people — is that this is not all-or-nothing. There is a continuum of purity, and the value step from spaghetti-state to mostly-pure is much larger than the step from mostly-pure to completely-pure. A function that bumps a global counter but otherwise touches nothing still reaps most of the benefits. You don't need Haskell; no matter what language you work in, programming in a functional style provides benefits: do it whenever it is convenient, and think hard about the decision when it isn't. Avoiding the worst is more important than achieving perfection — the most toxic systems you've ever handled, the ones requiring tongs and a face shield, all share the same anatomy: a complex web of state and assumptions their behavior relies on that isn't confined to their parameters. Preventing more code from becoming that is worth more than polishing your math library to ceremonial purity. And it's not C++-specific: telling an object to change itself is lesson one of OOP, and it's anti-functional behavior — the discipline applies to whatever imperative language you're standing in.

## How to Apply

1. **Audit before you preach.** Take a few non-trivial functions and track down every piece of external state they can reach and every modification they can make. If the function can trigger a screen update through the render system, you can throw up your hands and declare the effect set beyond human understanding — that's the point. The audit makes the invisible cost visible and converts the team better than any argument.

2. **Structure new work as gather → compute → apply.** Collect the inputs imperatively, pass them to a pure function that does the real thinking, then apply the results. The impure shell stays thin and boring; the logic worth testing becomes pure by construction.

3. **Extract pure functions from every finicky spot you touch.** Don't schedule a rewrite. Each time you're in something delicate, split the computation out, pass its dependencies as parameters, write the ten-line test. The codebase migrates one function at a time along the same paths you were editing anyway.

4. **Return new values instead of mutating, until measured cost says otherwise.** Normalized() alongside Normalize(); const aggressively — the frustration of making things const is itself a map of where state mutates unexpectedly, which is where the bugs breed. When profiling shows the copy matters, mutate locally and knowingly.

5. **Guard the purity you've won.** C++ and its relatives won't enforce purity for you, and one person "just adding a quick global read" to a foundation function silently poisons everything above it. Comment the contract, test it where you can, and treat violations as defects, not style nits.

## Examples

**Situation:** A simulation team wants to parallelize their per-entity update loop; every entity method mutates the entity and reads a global world object.

**Application:** Restructure toward update-as-function: each entity's step takes a read-only view of the previous world state and returns its next state; commit the new states at the end of the tick. The object-oriented poke-and-prod pattern is exactly what makes parallel execution unreasonable — when all entities reference a read-only world and produce their updates independently, the parallelism falls out almost for free.

**Illustrative result:** The race conditions that made the first parallelization attempt a fire drill are structurally impossible in the new shape, and single-entity behavior becomes testable without booting the world.

**Situation:** A payments service has one 900-line function interleaving validation, fee math, database reads, and API calls; every change breaks something unrelated, and the test suite mocks half the infrastructure.

**Application:** Carve out the decisions from the effects. Validation and fee computation become pure functions over explicit input structs; the IO gets hoisted to the boundary, which fetches everything up front and applies the results after. The mock scaffolding mostly evaporates because the logic under test no longer touches infrastructure.

**Illustrative result:** The pure core gets exhaustive table-driven tests — including the edge cases nobody dared exercise against mocks — and the next regulatory change is a change to one pure function with a visible blast radius.

## Anti-Patterns (tactical)

**Don't:** Pass an allMyGlobals pointer, a god-object, or a DI container into a function and call it pure.
**Why:** Getting the entire world handed in through one parameter defeats much of the purpose — the function can still reach anything, you still can't tell what it depends on from the signature, and the test still requires building the world. Pass the three fields it needs, not the object that contains everything. If that makes the parameter list irritating, the function is telling you its decomposition is wrong.

**Don't:** Force purity onto hot paths by copying large structures per call because the paradigm says so.
**Why:** Directly mutating memory is the speed-of-light case, and some code genuinely needs it — appending to a big list by returning a fresh copy will kill you in a language with ordinary containers. Purity is a default you buy where it's cheap, which is almost everywhere — not a tax you pay where it's ruinous. Measure, decide locally, and document the deliberate exceptions.
