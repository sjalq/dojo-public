---
triggers:
  - "user is overwhelmed by feature requests or scope creep"
  - "user asks whether to add a requested feature or capability"
  - "user feels pressure to ship constantly so the project 'looks alive'"
  - "user asks how to set expectations or write a roadmap"
use_when:
  - "deciding what NOT to build, and how to communicate that decision"
  - "a product's simplicity is its value and additions threaten it"
  - "setting public expectations about pace, scope, and stability"
fails_when:
  - "no is reflexive — refusing without enumerating the parties and costs is just stubbornness wearing principle's clothes"
  - "the market genuinely moved — stability of a thing nobody needs anymore is not a feature"
related:
  - "designed-boundaries.md"
  - "batching-and-releases.md"
  - "what-is-success.md"
  - "hard-parts-of-open-source.md"
---

# Saying No (intentional exclusion; stability as a feature)

## When to Use
- A feature request is popular, reasonable-sounding, and would erode what makes the product itself
- Writing a roadmap, expectations doc, or "what we won't do" statement
- Pressure mounts to match a competitor's cadence or feature list
- Deciding whether to remove something already shipped

## Fails When
- **The no has no why.** Evan's refusals always enumerate the trade (see designed-boundaries.md). A bare no reads as neglect and invites the same request forever.
- **You're refusing the market, not the noise.** When the concrete use case your product exists for has changed, holding the line is not discipline — re-derive the design from the new reality.

## Core Concept

Evan Czaplicki may be the most committed practitioner of *not building* in modern software. The Elm compiler roadmap opens: **"If you like what you see now, that's pretty much what Elm is going to be for a while."** And he manages expectations downward on purpose: "I know many readers take 'exploring X' as a promise that 'X will definitely happen', so I want to be careful in setting expectations low since there is still so much uncertainty in the work." Even his best case is stability: "even in the wildest version of success, I wouldn't expect the language or core packages to change very much." This is not stagnation — 2026's "Road to Elm 1.0" shows the exploration paying out as "a series of small non-breaking releases" — it is a refusal to let the roadmap write checks the design hasn't cashed.

The reasoning has several layers. **Design incentives:** from the economics talk, adding a feature buys "less conflict, more pleasant interactions"; refusing buys "less complexity" — and for an independent project the question "why mess with simplicity?" is allowed to win. **Downstream cost:** every change to a foundation taxes the entire ecosystem (see batching-and-releases.md), so features must be worth everyone's cost, not just interesting. **Coherence:** each language has a character, and features that fight it are wrong *for it* even when good elsewhere — "there are features I like that I know Elm wouldn't like. Elm doesn't want that." Choices cascade: having committed against familiarity-as-onboarding (ML syntax), "when a question comes up, should we use something like JSX — we've already sort of committed to not using syntax as an onboarding technique." A design is a constellation of mutually consistent nos.

He also says no *retroactively*: Elm 0.16 **removed** syntax. Multi-way ifs fought the style conventions, permitted crashes, and were redundant — cut. Record field addition/deletion was a feature he'd shipped conservatively, watched for two years, and then removed on evidence: "Pretty much no one ever used field addition or deletion. In the few cases where people *did* use it, it got pretty crazy pretty quickly." Features are experiments; unused complexity is debt you can pay down. He even prunes his own responsibilities — handing elm-sortable-table to the community "in an effort to prune my responsibilities."

Two guardrails keep the no honest. First, **route people to alternatives**: "If someone needs more certainty, I generally recommend looking into other languages to see if they have a balance that works better for their needs... Trade offs!" A no with an exit ramp preserves goodwill and the product's focus simultaneously. Second, the foundation he got from Guido van Rossum (credit Evan keeps): **"just do a good job."** Alternatives coexisting is healthy — "alternatives make each community stronger... people can find their way to a community that matches how they feel" — so you are not obligated to be everything. When type-class enthusiasts left Elm for languages that had them, he read it as the system working: "that's not to say one community is a better choice than the other; it just means we can all experiment with a different philosophy."

The payoff he claims for the looser, no-heavy style: "working in this looser style has produced a high baseline of quality... all the error message work in Elm began as a project to implement the --report=json flag... if I had been using a rigid roadmap, I might have skipped those ideas to meet the publicly-stated arbitrary deadline. We'd have a clearer roadmap, but error messages no different than other type-inferred languages."

## How to Apply

1. **Write your product's character down.** The handful of properties that, if lost, make it pointless (simplicity, guarantees, speed, coherence). Every request is judged against this, not against its own local appeal.
2. **For each no, enumerate the why.** Which parties are affected, what complexity lands on every user, what future options close. "It's more complex than it sounds" — show the complexity (see hard-parts-of-open-source.md).
3. **Set expectations low, in public, in writing.** A stable "here's what this will be for a while" statement beats optimistic roadmaps that convert into broken promises. Under-promising is a trust strategy.
4. **Offer the exit ramp.** Name the alternative that serves the need you're refusing. It costs one sentence and converts a rejected user into a respectful ex-prospect instead of a resentful camper.
5. **Ship experiments conservatively; remove on evidence.** When unsure, add the *restricted* version ("from the start I was very conservative, knowing that we could expand or contract as we got more data") and watch actual usage. Removal is allowed. Redundant syntax, unused features, and your own side responsibilities are all candidates.
6. **Ignore cadence pressure; answer with quality.** "There can only be so many Saturdays like that." The pressure to always be shipping and posting is a proxy game (see what-is-success.md); the durable answer to "is it alive?" is that what exists is excellent and maintained.

## Examples

**Situation:** A founder's most-requested feature would add a configuration system to a product whose pitch is "zero configuration."
**Application:** The request is popular *because* users don't carry the whole-system view. Judge it against the written character: zero-config is the product. Publish the no with the enumeration — what every user loses when config exists (docs, support surface, broken uniformity) — and route the requesters to the alternative tool that serves them. Watch whether the concrete pain behind the request can be solved inside the character (a better default beats a knob).
**Illustrative result:** The product keeps its reason to exist; the request keeps arriving but now hits a linkable answer instead of a negotiation.

**Situation:** A team is afraid to delete a feature used by almost nobody because "someone might rely on it."
**Application:** Evan's record-syntax playbook: measure actual usage, examine the few real cases (his one real-world case "could be rewritten with custom types, which turned out nicer anyway"), announce the removal with the reasoning and the migration, and take the major version. Carrying dead complexity taxes every future feature to spare a hypothetical user.

**Situation:** A startup's board wants monthly feature releases because a competitor ships weekly.
**Application:** Separate the games. If your users are businesses building on you, releases are a cost you impose on them, and "releases that are worth great cost" wins the decade. Show the board the Java/C release-gap chart argument: mature platforms have years-long gaps and are not dead. Then redirect the energy into one batched release with a real story (see batching-and-releases.md, on-storytelling.md).

## Anti-Patterns (tactical)

**Don't:** Say yes to end the conversation.
**Why:** "In the case you say yes, you're probably going to have less conflict, more pleasant interactions" — that is exactly why yes is dangerous. The conflict cost of no is paid once; the complexity cost of yes is paid by every user forever. If your nos never hurt, you aren't making design decisions, you're taking dictation.

**Don't:** Let "exploring X" leak as "X is coming."
**Why:** Every speculative mention compounds into commitments: "some things may or may not happen, and that kind of thing doesn't get translated well... then it's like, yeah, but you said." Speak when the work is real (batch the news), and label exploration as exploration with expectations explicitly set low.
