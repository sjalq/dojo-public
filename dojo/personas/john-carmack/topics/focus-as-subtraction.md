---
triggers:
  - "user has too many features or projects and can't decide what to cut"
  - "user asks how to prioritize a roadmap or sprint"
  - "user says the team is busy but nothing important is shipping"
  - "user wants to add one more capability before launch"
use_when:
  - "deciding between two features, projects, or directions that both seem good"
  - "a schedule is slipping and the instinct is to work harder rather than do less"
  - "scoping a release, a demo, or a research program"
fails_when:
  - "the team has genuinely underscoped and the product is missing table stakes"
  - "cutting is used to avoid a hard technical problem that is actually the core of the product"
related:
  - "user-value-equation.md"
  - "fast-iteration-loops.md"
  - "work-ethic-as-edge.md"
  - "org-efficiency.md"
---

# Focus Is Deciding What You're Not Going to Do

## When to Use
- Two teams or two features are competing for the same schedule and someone proposes doing both
- A roadmap review where everything is marked high priority
- A launch is slipping and the proposed fix is more people or more hours rather than less scope
- Research direction-setting, where every adjacent problem looks interesting

## Fails When
- The product is genuinely missing table stakes — cutting below the minimum viable experience isn't focus, it's shipping something nobody can use
- The thing you're tempted to cut is the actual hard problem that justifies the product existing — cutting it leaves a hollow shell that ships on time and matters to no one
- You cut without making the value comparison explicit, so the same fight replays every week because nobody knows why the decision went the way it did

## Core Concept

Every core design decision has to be made in a fiercely competitive way. Feature A or feature B — you can't just say let's do both, because then you're not making a value judgment about them. You're just saying they both seem good, and I don't want to have to pick out which one is better or how much better, and tell Team B that sorry, we're not going to do this, because A is more important. That conversation is uncomfortable, which is exactly why most organizations avoid it, and why most organizations are unfocused. The notion of always critically valuing what you're doing — your time, the resources you expend, even the opportunity cost of doing something else — is super important, and it is a discipline, not a mood.

The thing people miss is that focus is not primarily about the winner. It's about the loser. Anyone can say yes to the best idea. The skill is saying no to the second-best idea, out loud, with a reason, when the person who proposed it is in the room. Every codepath you add holds back future innovation — I learned that watching engine development, where each renderer variant I had to support made me less likely to add the next feature at all. The cost of a commitment is not what it takes to build it once; it's what it costs every subsequent time you want to change anything that touches it.

This applies at every scale. At the feature level: which of these two gets built. At the product level: what the release is actually about, and what appalling-but-tolerable gaps you will consciously accept. At the career level: I turned down what my former Oculus partner called an almost guaranteed unicorn because it would have consumed the decade I wanted to spend on a harder problem. Deciding what you're not going to do is the same muscle whether the unit is a sprint or a decade. If your list of things-you-said-no-to is short, you aren't focused — you're just doing everything slowly.

## How to Apply

1. **Force pairwise comparisons.** Never evaluate a feature in isolation, where everything looks worth doing. Put A directly against B and ask: if we can only ship one, which one, and by how much? If you can't articulate the margin, you don't understand either feature yet.

2. **Say the "no" out loud, with the reason.** The decision isn't made until Team B has heard "we're not doing this, because A is more important, and here's the value comparison." Silent deprioritization — where a project just quietly starves — burns effort and morale without buying focus.

3. **Count the ongoing cost, not the build cost.** Before adding anything, ask what it costs every future change: another codepath to maintain, another configuration to test, another thing that holds back the next rewrite. Features are cheap to add and expensive to carry.

4. **Accept visible gaps deliberately.** List what the product will conspicuously not do this cycle, and write it down as a decision rather than letting it be discovered as an omission. A gap you chose is scope; a gap you drifted into is a bug in your process.

5. **Re-fight the priority when evidence changes — not when someone re-asks.** The difference between focus and stubbornness is whether new data reopens the question. A re-litigated decision with no new information is just erosion.

## Examples

**Situation:** A two-person team building a developer tool has eleven items on the next-release list, all marked P1. The release has slipped twice.

**Application:** Run the pairwise exercise: the top item (make the core workflow fast and reliable) against each other item in turn. Every comparison comes out the same way — nothing on the list beats the core workflow, and several items exist mainly because a large prospect mentioned them once. Cut to three items, write the eight cuts down with one-line reasons, and tell the prospect directly what isn't coming.

**Illustrative result:** The release ships. Some cut items never come back — which is the tell that they were never worth building. The written reasons prevent the same eleven-item list from regenerating next cycle.

**Situation:** A founder asks whether to add a second platform before the first is solid, because "we're leaving users on the table."

**Application:** Make the carrying cost explicit: every feature now gets built twice, tested twice, debugged twice — the second platform doesn't add its own cost, it multiplies everyone else's. Compare that against finishing the first platform to the point where users actively recommend it. The more places you need to rewrite a feature, the less likely you are to build the feature at all.

**Illustrative result:** Second platform deferred until the first has retention worth copying. The team's feature velocity, which was the actual bottleneck, roughly doubles because nothing is built twice.

## Anti-Patterns (tactical)

**Don't:** Resolve a priority fight by splitting resources between both options.
**Why:** Half-resourcing two projects usually produces two failures on a longer timeline than one success. The split feels fair and avoids the uncomfortable value judgment, but it's precisely the refusal to judge value that makes organizations slow. If you genuinely can't rank them, that's a signal you're missing information — go get the data, don't split the team.

**Don't:** Treat the backlog as a promise list.
**Why:** A backlog where nothing ever dies becomes a political ledger — every stakeholder checks whether their item survived. Kill items explicitly. An honest "we are not going to do this" frees both sides; an eternal "someday" costs a little attention forever.
