---
triggers:
  - "user asks whether an optimization or architecture choice is worth it"
  - "team is arguing about performance or design by opinion"
  - "user works through layers of abstraction they don't understand"
  - "user asks how to make engineering debates objective"
use_when:
  - "settling a technical argument that has gone subjective"
  - "reviewing an architecture with many layers between the code and the hardware"
  - "deciding where optimization effort should go"
fails_when:
  - "measurement is used to dodge a judgment call that is genuinely about values, not costs"
  - "micro-costs are optimized while the dominant cost sits unmeasured elsewhere"
related:
  - "latency-as-the-metric.md"
  - "fast-iteration-loops.md"
  - "inlined-code-style.md"
  - "static-analysis-discipline.md"
---

# Know the Cost of Everything

## When to Use
- A technical debate is running on adjectives — "cleaner," "more scalable," "too slow" — with no numbers attached
- Choosing between an abstraction and direct code, between a dependency and writing it yourself
- Reviewing a system where nobody on the team can say what actually happens between a user action and the response
- Prioritizing optimization work

## Fails When
- The disagreement is actually about values or product direction — measuring won't settle what to want, only what things cost
- You're precise about the pennies and blind to the dollars: perfectly measured inner loops inside an unexamined architecture that wastes 10x
- The measurement becomes a benchmark game — optimizing the number instead of the experience the number was standing in for

## Core Concept

There are two kinds of engineering claims, and most teams hopelessly mix them. Some things are objective: this indirection is a cache miss that's going to cost us here — you can measure it, and there's really no arguing with it. Other things are style: whether parameters should be const, how code should be organized, what "clean" means. I spent years running code review across a team and watching the difference — where I could point to a measured cost, agreement was instant; where I was arguing from experience about style, people would just say "I've never seen that problem." The single best thing you can do for an engineering culture is push as many decisions as possible from the second category into the first. Attach costs to things. Cycles, milliseconds, megabytes, dollars, weeks. The moment a claim has a number, the argument usually ends.

To attach real costs you have to actually know what's happening all the way down. Not because you'll hand-write assembly — mostly you won't — but because every layer you can't see through is a place where costs hide. When I wrote up VR latency, the useful work wasn't the advice; it was the accounting: walking motion-to-photons through sensor, transport, processing, rendering, driver buffering, scanout, and putting numbers on each stage. A frame that "should" take 16 milliseconds was taking 50 because three different layers were each quietly buffering for throughput. Nobody had decided that; it emerged from layers nobody was watching. Systems engineering *is* the accounting. My whole career — engines, rockets, headsets — has been the same move: measure each stage of a pipeline everyone else treats as a black box, and the wins fall out.

The deeper habit is refusing to accept folklore costs. "Allocations are slow." "The database is the bottleneck." "We can't afford to do that per-frame." Maybe — measure it, in your system, this year. Hardware shifts under the folklore: things that were expensive a decade ago are free now, and things that look free — a cache miss, a synchronization point, a stalled pipeline — quietly dominate. An engineer whose cost model is ten years stale makes confidently wrong decisions daily. And the same discipline applies above the code: a meeting has a cost, a process step has a cost, a dependency has a carrying cost. People who would never waste a millisecond happily waste a person-month, because nobody put a number on it.

## How to Apply

1. **Sort every claim: objective or style.** In any design debate, ask "is this measurable?" Cache behavior, latency, memory, build time — measurable; go measure. Taste, readability, future-proofing — style; decide by judgment, but stop pretending it's physics.

2. **Build the pipeline budget.** For whatever your system does end-to-end, write down every stage and its measured cost, and make the total add up to observed reality. The stages that don't add up are where the discoveries are.

3. **Refresh your cost model with micro-experiments.** When did you last actually time an allocation, a syscall, a cache miss, a network hop on your target hardware? Ten-minute experiments that recalibrate intuition are some of the highest-return time an engineer spends.

4. **Demand numbers in review, and give them.** "This is slow" isn't a review comment; "this adds a per-item indirection on a path we run a hundred thousand times a frame" is. Symmetrically, when you argue style, label it style — you'll be trusted more on the costs.

5. **Extend it upward.** Price the meeting (people × hours × opportunity), the process gate, the extra service in the architecture. Most organizational waste survives because it's never been costed the way code is.

## Examples

**Situation:** Two senior engineers deadlocked for a week over whether the new system should use an entity-component design or straightforward structs, arguing "flexibility" versus "simplicity."

**Application:** Split the argument. Objective part: measure the two memory layouts on a realistic workload — iteration cost, cache behavior, allocation pattern. Style part: decide who has to maintain it and what they can hold in their heads. The measurement takes an afternoon; the deadlock had already cost two engineer-weeks — which is itself the kind of cost nobody was counting.

**Illustrative result:** The layouts differ measurably on the hot path and not at all anywhere else — so the hot path gets the fast layout and the rest gets the simple one, and the "philosophy" question turns out to have a two-line answer.

**Situation:** A startup's app feels sluggish; the team is planning a quarter-long rewrite of the rendering layer, which folklore says is the bottleneck.

**Application:** Before committing a quarter, do the accounting: instrument the full path from input to pixels and attribute the time. Folklore bottlenecks are wrong often enough that a day of measurement before a quarter of rewriting is always justified.

**Illustrative result:** The rendering layer turns out to be a fraction of the budget, and the sluggishness lives in a couple of synchronous waits nobody knew existed — a two-week fix instead of a quarter, found by refusing to accept an unmeasured cost claim.

## Anti-Patterns (tactical)

**Don't:** Win arguments with your seniority where you could win them with a measurement.
**Why:** The seniority win is temporary and teaches the team to defer; the measurement win is permanent and teaches the team to measure. Every time you say "trust me" where you could say "here's the number," you spend credibility you'll want later for the genuinely unmeasurable calls.

**Don't:** Let any layer of your stack stay a black box because it's "not your job."
**Why:** Costs hide in the layers you don't look at — driver buffering, ORM query expansion, allocator behavior, scheduler quirks. You don't need to own every layer; you need to be able to see through it far enough to account for where the time and memory actually go. "The framework handles it" is how a 16-millisecond budget becomes 50.
