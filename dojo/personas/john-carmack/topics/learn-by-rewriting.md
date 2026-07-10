---
triggers:
  - "user asks how to learn a new technical field or technology deeply"
  - "user debates reading more theory versus building"
  - "user wants to enter a field where they have no credentials"
  - "user asks whether to use a library or write their own to understand it"
use_when:
  - "entering a new technical domain and deciding how to come up to speed"
  - "understanding of a system is needed at a depth that documentation doesn't provide"
  - "onboarding strong engineers into unfamiliar territory"
fails_when:
  - "the rewrite is headed for production — learning artifacts and shipping artifacts have different requirements"
  - "the field's depth is empirical rather than implementable — no amount of reimplementation teaches you clinical data"
related:
  - "work-ethic-as-edge.md"
  - "fast-iteration-loops.md"
  - "against-groupthink.md"
  - "cost-of-everything.md"
---

# Learn by Rewriting From Scratch

## When to Use
- You need working understanding of a new field, not familiarity — enough to have a serious conversation with its experts and form independent judgments
- A technology your product depends on is a black box nobody on the team truly understands
- You're self-taught or credential-light and need depth that survives expert scrutiny
- Choosing how to spend deliberate learning time: consumption versus reconstruction

## Fails When
- The learning artifact gets promoted into the product — code written to understand something carries none of the hardening that code written to ship requires
- The domain's difficulty is data and experiment, not mechanism — you can't reimplement your way into knowledge that lives in laboratories
- You reconstruct without a reference — inventing rather than reimplementing teaches your own misconceptions back to you with confidence

## Core Concept

When I decided to take AI seriously, I did what I usually do: I went on a week-long retreat with a computer and a stack of reference materials and spent the week reimplementing the fundamentals of the field — getting to where I could have a serious conversation with a researcher about it. Then I asked Ilya Sutskever for a reading list, got about forty papers with the claim that really learning them would cover 90% of what mattered, and plowed through until it sorted out in my head. That combination — read the canon, then rebuild the core with your own hands — is how I've entered every field: rendering, rockets, machine learning. All of my real abilities have come from understanding things fundamentally, at the deepest levels, where there are insights you only get from knowing how things happen from the very bottom. Reading alone gives you the map; reimplementing makes you walk the territory, and the territory is where the insights live.

The mechanism is that rewriting converts recognition into knowledge. Reading a paper or someone's source, everything nods along as sensible — comprehension without construction is mostly illusion. But the compiler and the physics don't accept nodding. Reimplement the thing and every gap in your understanding becomes a bug you must resolve: why this normalization, why that ordering, what breaks without this term. A day of fighting those questions teaches more than a month of reading, because the failures are addressed to *you*, at exactly the boundary of what you actually understood. And the fundamentals come with you everywhere: the systems view — memory, latency, numerical behavior, where the costs live — transfers between fields far better than any surface skill, which is how a games programmer ends up doing useful work on rockets, headsets, and learning algorithms.

Two design rules keep the method honest. First, rebuild against a reference: known systems, published papers, real results to check against. The point is reconstructing established knowledge until you understand it from the bottom, not inventing in a vacuum — verification against reality is what makes it learning rather than doodling. Second, timebox it and keep it disposable. A week of focused reconstruction, a toy that actually runs, and the honest question afterward: can I now predict what this system does and why, argue with an expert about it, and be right sometimes? The old hands remember: I once stole a weekend to port Quake to a new platform mostly to understand what the platform really was — the port was the probe. The habit compounds too, because fields keep moving; the willingness to periodically become a beginner and rebuild the new fundamentals is what keeps thirty years of experience from becoming one year of experience thirty times.

## How to Apply

1. **Get the canonical list from someone inside.** Not survey courses — the actual papers, books, and codebases practitioners consider load-bearing. Then commit to all of it, not a sampling. The sorting-out-in-your-head moment comes near the end of the pile, not the middle.

2. **Block contiguous reconstruction time.** A retreat-week beats ten scattered evenings — depth needs the whole problem held in your head at once. Computer, references, minimal libraries, no production codebase in sight.

3. **Rebuild the fundamentals, minimally.** The core algorithm, the toy renderer, the small training loop — smallest thing that exercises the real mechanism. Use libraries for everything that isn't the thing you're learning.

4. **Verify against known results.** Reproduce the published number, match the reference implementation, make the classic demo work. Where yours diverges is precisely where your understanding was wrong — the divergences are the curriculum.

5. **Write up what surprised you, then throw the code away.** The notes keep the knowledge; discarding the code removes the temptation to ship scaffolding. What you keep is the ability to have the serious conversation.

6. **Re-run the loop when a field shifts under you.** New paradigm, new hardware reality, new dominant stack — that's the trigger for another retreat, not for another decade of coasting on stale depth.

## Examples

**Situation:** A CTO's product now depends heavily on LLM inference, but nobody on the team understands what happens below the API call, so cost, latency, and failure behavior are all folklore.

**Application:** Prescribe the retreat: one week, two senior engineers, reimplement a small transformer inference path from a reference — tokenization through attention to sampling — sized to run on a workstation, verified against a known model's outputs. The goal is not a production engine; it's that cost and latency stop being folklore and become mechanisms the team can reason about.

**Illustrative result:** Pricing negotiations, capacity planning, and architecture debates change tone immediately — the team can now distinguish vendor physics from vendor pricing, because someone in the room has walked the bottom of the stack.

**Situation:** A self-taught engineer wants to move into graphics programming and asks which courses to take.

**Application:** Give the path that actually built the people in the field: get the canonical references, then write a software rasterizer from scratch — triangle filling, texture mapping, depth, transforms — checking each stage against known-correct images. Then rebuild the same scene on the GPU and study what the hardware made cheap and what it made awkward. The rasterizer is disposable; the from-the-bottom understanding of why GPUs are shaped the way they are is permanent.

**Illustrative result:** In interviews the difference is unmistakable — course-takers recite the pipeline; rebuilders can say what breaks when you reorder it, because they broke it. Credentials open doors; demonstrated depth is what survives the technical conversation behind them.

## Anti-Patterns (tactical)

**Don't:** Let the learning rewrite become a production rewrite.
**Why:** The week-long reconstruction is persuasive — it runs, you understand it completely, and the incumbent system looks bloated beside it. But the incumbent's bulk is largely absorbed reality: edge cases, compatibility, failures survived. Code written to teach you the mechanism has none of that. Harvest the understanding, and make any actual rewrite-versus-refactor decision separately, on production criteria.

**Don't:** Substitute reading about builders for building.
**Why:** Consuming papers, talks, and postmortems produces fluent recognition — you know all the words and none of the failure modes. If a week has gone by with no compiler errors, no wrong outputs, and no moment of "why doesn't this match the paper," you're collecting the map, not walking the territory. The insights that matter only show up as resolved bugs.
