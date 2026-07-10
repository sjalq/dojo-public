---
triggers:
  - "user is designing an API, library, SDK, or interface others will build on"
  - "user asks for an API or library design review"
  - "user is tempted to make an interface maximally generic or abstract"
  - "user asks how to name things or structure documentation for a library"
use_when:
  - "designing or reviewing any surface other people program against"
  - "an API is technically complete but users struggle or misuse it"
  - "deciding between a concrete design and a general/abstract one"
fails_when:
  - "the audience is you alone — internal helpers don't need publication-grade design"
  - "the domain is still unknown — usage-driven design needs usage; when pioneering, expect to redesign after reality arrives"
related:
  - "gradual-learning.md"
  - "the-life-of-a-file.md"
  - "enforced-semver.md"
  - "types-as-sets.md"
---

# Package & API Design for the Long Term (usage-driven design)

## When to Use
- Designing a public API, SDK, internal platform library, or plugin interface
- Reviewing an API before it ships and locks in
- Someone proposes generalizing an interface "so it covers future cases"
- Writing the documentation and naming for a library

## Fails When
- **No users, no usage data.** Evan designs from example code and real questions; at the frontier ("when you're discovering how things are going to be, you don't have the luxury to be a designer") you ship, learn, and redesign — see the raw browser APIs he later cleaned up.
- **The consumer is a machine or one teammate.** These guidelines optimize for many human strangers over years; they are overkill for a private helper.

## Core Concept

Evan Czaplicki's package design guidelines open with the move most API authors skip: **"Design for a concrete use case. Before you start writing a library, think about what your goal is."** What problem, for whom, what would success mean, who else has tried, what weaknesses to avoid. And then the discipline: "Actually think about these things. Write ideas on paper. Ask for advice from someone you trust... If you are doing this right, **you will have example code and a tentative API before you start implementing anything.**" The API is designed from the caller's side first; the implementation serves the calls.

His sharpest guideline is aimed at his own community's vice: **"Avoid gratuitous abstraction.** Some functional programmers like to make their API as general as possible. This will reliably make your API harder to understand. Is that worth it?... Abstraction is a tool, not a design goal. Unless abstraction is making someone's life easier, it is not a good idea. If you cannot *demonstrate* why your abstraction is helpful, there is a problem with your API." The demand for a demonstration — example code where the abstraction visibly pays — is the test that kills speculative generality.

The rest of the guidelines are compact and mechanical: **write documentation with examples** ("the standard libraries all make a point to have examples that show how one *should* be using those functions"), and order the docs deliberately — "people will read documentation linearly when learning a library, so give them some structure!" **The data structure is always the last argument** (composition and folding work better). **Keep tags and record constructors secret** — expose opaque types so you can evolve internals "even between minor releases" without breaking anyone; convenience constructors like `fromXY` preserve your freedom to add `fromPolar` later. **Naming is communication**: "abbreviations are generally a silly idea for an API... having an API that is clear is more important than saving three or four characters," and module names should not reappear in function names (`State.run`, not `State.runState`) because redundant names encourage unqualified imports that make large codebases unreadable.

His worked example, the elm-sortable-table README, adds three deeper principles. **Own as little state as possible:** the table tracks only sorting details; data is passed to view — "this is the most important decision in this whole library... Having multiple copies of 'the same' value in your Model is a sure way to create synchronization errors... if you design your API poorly, you can force your users to make duplicates and open themselves up to bugs for no reason. Do not do that to them!" **Simple by default, full power underneath:** the easy functions "are defined in terms of crazier ones," so learners ramp gradually and never migrate off a toy API (see gradual-learning.md). **Design against misuse:** "never put functions in your Model or Msg types" is a usage *rule* shipped with the library — an API's contract includes how it should be held.

## How to Apply

1. **Write the example code first.** Before implementation: the README's usage section, three realistic call sites, the error a confused user will hit. If the examples feel awkward, the API is wrong — and it's still cheap to fix.
2. **Interrogate every abstraction with a demonstration.** For each type parameter, interface, or configuration axis: show concrete example code that is *better because of it*. No demonstration, no abstraction — solve today's concrete case and let generality be extracted later from real repetition (see the-life-of-a-file.md).
3. **Hide your representations.** Export opaque types and constructor functions; keep raw structures private. Every exposed internal is a promise you'll be forced to keep at the next redesign (and the thing that turns minor releases into majors — see enforced-semver.md).
4. **Minimize owned state.** For any stateful component, split "what I must track" from "what the caller already owns" and accept the caller's data as arguments. Duplication across the boundary is the bug factory.
5. **Name for the reader, order for the learner.** Full words, no module echo, qualified use encouraged. Docs sequenced simplest-first, each concept arriving when needed.
6. **Ship usage rules with reasons.** "Always X / Never Y" plus the why, in the README. Misuse you didn't warn against becomes support load you did earn.

## Examples

**Situation:** A platform team is about to build a "flexible" internal client library configurable for any of the company's twelve services.
**Application:** Gratuitous abstraction, pre-demonstrated by zero examples. Write the example code for the two services with real demand; build the concrete client that makes those examples beautiful. The general core, if it exists, gets extracted when the third and fourth clients show actual repetition.
**Illustrative result:** Two excellent clients ship in weeks; the speculative configuration layer nobody could learn never gets built.

**Situation:** An SDK exposes its session object as a plain struct, and a planned auth change would break every consumer.
**Application:** This is the exposed-constructor trap. The redesign: opaque `Session` type, `fromCredentials`/`fromToken` constructors, accessor functions for the fields consumers legitimately need. Do it *before* the auth change, as a minor release, so the breaking change never has to happen.

**Situation:** A reusable UI component asks each consumer to store its config (including callbacks) in their application state.
**Application:** Evan's sortable-table rules apply directly: config is functions, functions don't belong in state — "a Table.Config value is really just a bunch of view functions... It goes in your view!" State owned by the component should shrink to what only it can know; everything else arrives as arguments each render.

## Anti-Patterns (tactical)

**Don't:** Design the API by exposing whatever the implementation happens to have.
**Why:** The implementation's shape reflects your convenience, not the caller's problem. Callers then couple to accidents, and every internal improvement becomes a breaking change. The API is a designed artifact with its own users; the implementation is merely how you keep its promises.

**Don't:** Justify an abstraction with future use cases.
**Why:** "If you cannot demonstrate why your abstraction is helpful, there is a problem with your API." Futures are free to imagine and expensive to maintain; the abstraction taxes every reader now for a payoff that usually never arrives — and when the real future comes, it's shaped differently than the guess (similar is not the same).
