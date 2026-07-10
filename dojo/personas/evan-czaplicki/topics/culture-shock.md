---
triggers:
  - "user applies best practices from a previous stack, company, or industry to a new one"
  - "user insists on short files, components, or up-front architecture as universal rules"
  - "team migrating between ecosystems is fighting the new environment's idioms"
  - "user asks why a practice that always worked is now causing problems"
use_when:
  - "onboarding people into an environment whose constraints differ from where their habits formed"
  - "reviewing rules in a style guide, process doc, or 'engineering principles' page"
  - "someone justifies a practice with 'everyone knows' rather than a mechanism"
fails_when:
  - "the old constraint actually still holds in the new environment — then the defensive instinct is correct, not baggage"
  - "used to dismiss newcomers' concerns wholesale instead of examining each habit's premise"
related:
  - "the-life-of-a-file.md"
  - "the-elm-architecture.md"
  - "what-is-success.md"
---

# Culture Shock (defensive instincts imported from other ecosystems)

## When to Use
- A team migrates stacks, tools, or methodologies and keeps re-creating the old world inside the new one
- Someone defends a rule ("shorter files," "components everywhere," "get architecture right up front") with certainty but no mechanism
- You are writing onboarding material and need to name the habits people will arrive with
- A practice that was genuinely protective in one context is producing waste in another

## Fails When
- **The premise survived the move.** Some imported instincts are still correct — checking whether the constraint still exists is the whole method, and sometimes the answer is yes. This framework is a test, not a verdict.
- **It becomes a superiority story.** The point is empathy plus analysis: the habits "are legitimately important in that context." Dismissing people's instincts without tracing them to their source just entrenches them.

## Core Concept

Evan Czaplicki gave a name to a specific failure of expertise: habits formed under one set of constraints, carried into an environment where those constraints do not exist. In the Elm guide's "Culture Shock" section: "Folks coming from JavaScript tend to bring habits, expectations, and anxieties that are specific to JavaScript. They are legitimately important in that context, but they can cause some pretty severe troubles when transferred to Elm."

His two flagship examples are pieces of "JavaScript folk knowledge" that sound like timeless engineering wisdom but are actually local adaptations. **"Prefer shorter files."** Why does this rule exist? "In JavaScript, the longer your file is, the more likely you have some sneaky mutation that will cause a really difficult bug" — as he put it in the Life of a File talk, "as the lines of code increase, the probability of sneaky mutation approaches one." Short files are a rational defense against a real hazard. But in Elm "that is not possible! Your file can be 2000 lines long and that still cannot happen." Same rule, new environment, protection against a problem that does not exist. **"Get architecture right from the beginning."** In JavaScript, "refactoring is extremely risky. In many cases, it is cheaper just to rewrite it from scratch" — which, he notes, accounts for some of the framework churn. So planning ahead is rational there. Where refactoring is cheap and reliable, the premise is gone, and with it the conclusion.

The third import is deeper than a rule — it is an ontology. "Folks coming from React expect everything to be components. Actively trying to make components is a recipe for disaster in Elm. The root issue is that components are objects: components = local state + methods; local state + methods = objects." People do not just carry rules across ecosystems; they carry the *shape of thinking* the old ecosystem rewarded, and then ask "how do I structure my application with objects?" in a place that has none.

The key psychological observation: "Knowing this in your mind is different than knowing it in your gut." People feel "deeply uncomfortable when they see files pass the 400 or 600 or 800 line mark" even after they intellectually accept the constraint is gone. Habits are gut-level; arguments are head-level. The fix is experience: "Having this experience yourself is extremely valuable!" — push the limit once and feel that nothing breaks.

This generalizes far past programming. Every best practice is a fossil of a constraint. When the environment changes — new stack, new market, new team size, new tooling, new cost structure — audit the fossils.

## How to Apply

1. **For each inherited rule, name the hazard it defends against.** Not "it's cleaner" — the concrete failure. Short files → sneaky mutation. Up-front architecture → unaffordable refactors. Heavy code review → no type/test safety net. If nobody can name the hazard, the rule is pure ritual.
2. **Check whether the hazard exists in the new environment.** This is a factual question about mechanisms, not a matter of taste or seniority.
3. **If the hazard is gone, name the cost of keeping the rule.** Arbitrary module boundaries, ontological file-placement debates, wasted abstraction work, slower shipping.
4. **Replace argument with experience.** Gut-level habits don't yield to memos. Design a low-stakes exercise where people *do* the forbidden thing and watch it not fail — Evan's version: "push your limit on number of lines! See how far you can go... but keep it all in one file."
5. **Write the new rules with their premises attached.** A style guide entry should say *why*, so the next environment change can invalidate it cleanly instead of fossilizing it.

## Examples

**Situation:** Engineers from a large-company background join a five-person startup and immediately propose service boundaries, RFC processes, and a platform team.
**Application:** Trace each practice to its hazard: services defend against hundreds of engineers colliding; RFCs defend against uncoordinated breaking changes across teams. At five people those hazards do not exist, but the costs (coordination overhead, slower iteration) arrive immediately. Keep the practices whose premise survives (e.g., migrations reviewed carefully because data loss is real at any size).
**Illustrative result:** The team adopts two of seven imported practices and can say precisely which headcount or failure would trigger the others.

**Situation:** A React team adopting Elm builds a "component library" where every widget has its own Model/Update/View and message forwarding.
**Application:** This is the components-are-objects import verbatim. "Writing a viewSidebar function does not mean you need to create a corresponding update and Model to go with it. Resist this instinct. Just write the helper functions you need." Most "components" collapse into plain view functions with arguments.

**Situation:** A founder resists shipping without a fully designed architecture because a previous startup drowned in tech debt.
**Application:** Ask what made that debt fatal — probably an environment where refactoring was risky and tests were absent. If the new stack makes large refactors cheap and safe, the rational strategy flips to grow-then-split (see the-life-of-a-file.md). The scar is real; the constraint that caused it may not have followed them here.

## Anti-Patterns (tactical)

**Don't:** Enforce the new environment's idioms by decree ("we don't do components here") without tracing the old habit to its hazard.
**Why:** The instinct is gut-level and was *earned* — it protected them for years. Untraced, it goes underground and resurfaces as passive resistance or quiet workarounds. Traced and tested, it dissolves on its own.

**Don't:** Assume your own current best practices are the timeless ones.
**Why:** The lesson is symmetric. Elm's idioms are also adaptations to Elm's constraints — Evan is explicit that guarantees are what make long files and fearless refactoring safe. Move *his* advice into an environment without those guarantees and it becomes the dangerous import.
