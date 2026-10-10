---
triggers:
  - "user treats types as optional style and CI as the only quality gate"
  - "user asks how types relate to Continuous Delivery or shift-left quality"
  - "user is drowning in LLM-generated code volume and quality risk"
  - "user navigates politics of quality practices (tests, CD, types) vs delivery pressure"
  - "user has slow acceptance suites so developers abandon quality for mocks"
use_when:
  - "framing Type Driven Development as a CD and shift-left tool, not academic typing"
  - "designing local quality: compile, types, unit, property, mutation, then CI as safety net"
  - "keeping LLMs honest with invariants, tests, and minimum-code discipline"
  - "honest conversation about quality politics and career niche of types"
fails_when:
  - "shift-left becomes infinite local process with no shipping (quality as avoidance)"
  - "CI is the first time anyone runs tests (shift-right in practice)"
  - "types are forced as a purity cult without team ROI or readability judgment"
related:
  - "tdd-in-fp-and-oop.md"
  - "property-and-mutation-testing.md"
  - "type-proofs.md"
  - "effects-without-mocks.md"
  - "dependency-injection-in-fp.md"
---

# Continuous Delivery and Shift-Left: Types, CI, LLMs, Politics

## When to Use
- You want quality feedback **before** merge and prod: compiler, types, fast units, property/mutation, then CI as a safety net, not the first sieve.
- The org claims Continuous Delivery but only has a slow pipeline and heroics.
- LLM assistants increase code volume; you need constraints that keep models and humans honest.
- You are selling types to leadership or peers as a delivery tool (faster safe change), not as taste.
- You need honest prep for the politics of quality practices that science supports but companies under-adopt.

## Fails When
- **Quality as procrastination.** Infinite typing debates with nothing shipping. Jesse: no shame deciding to be pragmatic and ship; learning is iterative over many releases.
- **CI-only quality.** If nothing runs until the pipeline, you did not shift left; you centralized delay. Local fast loops matter (mutation scoped to diff, pure units, compile on save).
- **Absolutism without ROI.** Making impossible states impossible is a spectrum with nuance. Weak type systems need more tests; steep type curves need team buy-in.
- **Ignoring integration with untyped reality.** Libraries and teammates will keep producing weak types; smart constructors and ACLs are part of CD hygiene, not optional polish.

## Core Concept

Every part of Jesse's Type Driven Development series opens with the same framing:

> Types as another tool in software development, Continuous Delivery, and keeping LLM's honest. Also design, refactoring, communication, and reducing how many tests you have to write.

That is the spine. Types are not a hobbyist purity project. They are a **shift-left quality mechanism** inside a Continuous Delivery posture.

### Shift-left quality stack

Shift-left means run as many quality checks as early and as fast as practical so bad changes never earn a long flight to a shared environment. Jesse's toolbox maps cleanly:

| Layer | What fails early | Notes |
|-------|------------------|-------|
| Types / compile | Illegal states, wrong IDs, incomplete switches, ambient partiality | Exhaustiveness, brands, proofs |
| Unit tests (TDD) | Wrong behavior on known examples | Fast, pure, stubs |
| Property tests | Totality holes, bad sequences | Random + seed |
| Mutation tests | Weak assertions / coverage theater | Improve tests or types |
| Integration | Real edge IO | Fixtures, imposters |
| Acceptance | User-visible flows | Must stay fast enough people run them |
| CI | Safety net / shared truth | Not the only bar |

Mutation testing talk: do not be afraid; it is one more tool so you know code is worthy of prod **locally**. Types can solve many mutants via DUs and records. Property tests complement from the opposite angle.

Elm experience: e2e became "boring because they'd always work" when the type system and pure domain held; unit tests focused on business logic. Sound types reduce a class of unit tests; they do not eliminate the stack.

### Continuous Delivery (translate Farley)

Dave Farley's CD teaching is OOP-flavored in dialect but applicable regardless of paradigm. CD wants:

- Small batches
- Fast feedback
- Automated proof the system is releasable
- Architecture that allows independent change

TyDD supports that: total functions and railways compose into total-ish applications; typestate and capabilities make illegal orders and ambient authority fail at compile time; parse-don't-validate stops shotgun validation from exploding mid-pipeline; immutability reduces flaky shared-state tests.

Escape hatches remain practical: `.match` at AWS Lambda edges, small-batch smart constructors around unsafe libs, spectrum of type investment.

### CI as safety net, not babysitter

If developers only discover failures in remote CI, acceptance ops get blamed and people retreat to mocks for speed (Angular PR lesson: Cypress/Playwright wrapped in slow local and remote CI shortens the feedback loop until developers tap out). Fix:

- Fast pure unit suite on every save/commit
- Scoped mutation/property where needed
- Acceptance kept lean and valuable
- CI confirms what local already suggested

Wireless-off unit tests, DI, and effects-as-values keep the local suite honest.

### Keeping LLMs honest

Series-level claim: types constrain both human and model drift under higher code volume. Part 24: LLMs understand types somewhat like tests; act as a second compiler for invariants; can help choose gradual type-safety options.

Copilot research Jesse amplified (2024):

- Correlated with mistake code pushed to repos
- Discourages reuse
- Code added faster than cleaned
- Generated code like an "itinerant contributor" violating DRY
- Suggests add/complete, not update/move/delete
- Invents future fields from similar codebases

Still cautiously positive early era: smarter models can generate more correct and hopefully less code. Juniors may love volume; seniors feel cleanup debt.

Honesty stack against LLM drift:

1. **TDD minimum:** only code the current red requires.
2. **Types / brands / DUs / proofs:** illegal API use fails compile, including model-authored calls.
3. **Property + mutation:** random and sabotage checks on pure cores and AI-written tests.
4. **Review culture:** who cleans the mess afterward is an explicit question.
5. **CI safety net:** shared branch does not accept "it completed in the agent."

### Quality politics honesty (Final Thoughts)

Types have real tradeoffs. More to read and comprehend; you think in **two modes: types + code**. Amanda Laucher and Paul Snively, Strange Loop, "Types vs. Tests": how far you push types is limited by understanding. Team decides investment vs "something simpler for now." **No shame being pragmatic and shipping.** Learning is iterative over many releases. Can also be a demographic line in the sand (Don Syme / dependent types in F# as an example of deliberate stance).

Popularity: types lag infrastructure, IDEs, tests, language features. Better type systems in the 90s/2000s were not widely adopted for many reasons; slow change since 2010s. Positive design/quality impact **does not reliably convert to job opportunities or leadership importance** except rare language communities.

Same politics as other quality practices: code review, automated tests, Continuous Delivery. Evidence and knowledge lagged industry adoption for decades. Companies ignore science, do not know it, or cannot balance quality with delivery. You navigate politics, PM, design/UX, sales and marketing of techniques **while** doing the engineering job. Especially hard with types because niche.

Integration tax: code continually created by team, others, library authors; much untyped or weakly typed. Learn both what is good for your domain and how to safely integrate (smart constructors, ACL, parse boundaries).

Cultural loneliness is real:

> You'll be confused why everyone hasn't adopted sum types; that never goes away, a true mystery of the universe.

Not said to dissuade: said to prepare. Not all tradeoffs are equal; types in Jesse's experience are worth it. Hard to learn is a good problem for a nerd job. Hard and lonely; worth it.

Immutability is called out as the most controversial pillar and sometimes a non-starter culturally even when performance is not the issue. Expect political friction; do not pretend types are neutral technology.

### When not to force the whole doctrine

From unbreakable Python / team guidance: exploring ideas; team untrained in FP; deadline; legacy without tests (add tests first). FP has a reputation for obtuse evangelists; tread slowly. **Breaking trust in the team is one way to ensure software never works correctly.**

Shift-left CD with types works when it increases safe shipping rate, not when it becomes a purity identity.

## How to Apply

1. **Define releasable.** What automated checks must be green to ship? Compile/types, unit, critical integration, smoke acceptance.
2. **Move checks left.** Run the fast ones on every change locally. Keep CI as confirmation and multi-env truth.
3. **Invest types where change is frequent and mistakes are expensive.** Brands for IDs, DUs for state, Result for edges, proofs for critical invariants.
4. **Keep acceptance feedback humane.** If nobody runs e2e, mocks win. Fix time and flakiness, not only coverage %.
5. **LLM policy.** Types + tests required on generated code; TDD minimum; mutation/property on risky pure modules; explicit cleanup ownership.
6. **Sell delivery, not purity.** Fearless refactor, fewer production classes of bugs, faster PR cycles, fewer shotgun validations.
7. **Plan politics.** Find allies; small batches; show a module win before a platform mandate; accept pragmatic partial adoption.
8. **Integrate the wild west.** ACL and smart constructors at boundaries so the typed island stays honest without rewriting the ocean.

## Examples

**Situation:** Team has CI with tests but devs only run them after push; PRs thrash for days.
**Application:** Local compile + pure unit on save; DI so tests do not need network; optional pre-commit scoped mutation. CI stays gate, not discovery.
**Illustrative result:** Feedback minutes → seconds; CD-style small batches become psychologically possible.

**Situation:** Leadership asks why TypeScript strictness and Result types are worth it.
**Application:** Frame as CD: illegal states never reach QA; exhaustiveness turns design changes into compiler checklists; fewer flaky mock tests; LLM PRs fail compile when they invent illegal calls.
**Illustrative result:** Conversation is about delivery risk, not taste.

**Situation:** Copilot PRs add lines and optional fields weekly; reuse drops.
**Application:** Require failing test first for behavior changes; reject speculative fields; run mutation on new pure modules; brand domain IDs so invented cross-wiring fails typecheck.
**Illustrative result:** Volume without proportional debt; "who's on the hook to clean up" has an answer: the author before merge.

**Situation:** Engineer feels lonely pushing sum types in an enterprise Angular shop.
**Application:** Read Final Thoughts as prep, not defeat. Small batch: one service with Result errors and pure core. Show PR defect rate and review speed. Do not burn trust with big-bang purity.
**Illustrative result:** Political path with evidence; personal sustainability.

## Anti-Patterns

- **CI as the only quality culture.** Shift-right with better branding.
- **Types without tests** or **tests without types** when both are available.
- **Slow acceptance as the definition of quality.** Pushes people to brittle mocks.
- **Quality absolutism that blocks shipping.** Pragmatic spectrum is part of the doctrine.
- **Expecting career market to reward type skill automatically.** Prepare for niche politics.
- **LLM autopilot merges.** Completion is not releasability.
- **Evangelism that breaks team trust.** Horrible software follows broken relationships.
- **Pretending tradeoffs do not exist.** Dual cognitive mode, learning cost, integration with weak types are real.

Continuous Delivery wants fast, honest feedback that a change is releasable. Types shift whole defect classes left. Tests, property checks, mutation, and CI complete the net. LLMs raise the stakes. Politics is part of the job. Worth it; go in with eyes open.
