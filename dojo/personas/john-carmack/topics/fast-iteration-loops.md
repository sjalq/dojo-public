---
triggers:
  - "user's build, test, or deploy cycle is slow"
  - "user asks how to speed up development or experimentation"
  - "user is designing big changes with long feedback gaps"
  - "user asks about developer productivity or velocity"
use_when:
  - "the time from change to observed result is measured in hours or days"
  - "a team argues about designs in meetings instead of testing them"
  - "planning a research program or product experiment cadence"
fails_when:
  - "the domain has genuinely irreducible cycle time and the cheap iterations skip the part that matters"
  - "iteration becomes thrashing — fast loops with no hypothesis or measurement between runs"
related:
  - "cost-of-everything.md"
  - "demonstration-over-paperwork.md"
  - "learn-by-rewriting.md"
  - "latency-as-the-metric.md"
---

# Tighten the Loop Until Experiments Are Free

## When to Use
- Any time the change-to-result cycle is slow enough that people batch up changes or avoid trying things
- A design argument has gone around twice — the answer should come from a test, not a third meeting
- Setting up a new project: the first infrastructure investment should be the iteration loop itself
- Evaluating why a team with good people ships slowly

## Fails When
- The expensive step is the experiment's actual content — a clinical trial, a rocket flight, a tape-out. Then the play is to move as much learning as possible into cheap surrogate loops, while respecting that the surrogate is not the real thing
- Iterations happen without a question attached — running the loop fast while learning nothing per cycle is motion, not progress
- The fast path diverges from the real path, so everything works in the dev loop and breaks in production

## Core Concept

The speed at which you can go from an idea to a result you can observe is the single biggest lever on how good your final product gets. Not talent, not headcount — cycle time. When an experiment costs a day, you run a handful and stop at the first thing that works. When it costs a minute, you run hundreds, and you find things you would never have reasoned your way to. Most of what looks like insight from the outside is actually iteration count. Through the Quake era I lived in my .plan file posting daily build-by-build progress; the discipline of making a change, seeing the result, and posting it kept the loop honest. Decades later at Keen, we built a robot that points a camera at a TV and physically works a joystick — and the whole design constraint is that the agent learns in real time, on modest hardware, so the loop stays live: it started learning in the morning and was playing mediocre Atari by the time I gave the demo that afternoon.

The reason slow loops are so poisonous is subtle: they change behavior. When trying something is expensive, people stop trying things. They batch changes, which makes failures ambiguous. They argue in meetings, because arguing is cheaper than testing — even though the argument produces a worse answer. They defend designs they haven't validated, because validation is a week away. A slow loop doesn't just slow the work down linearly; it degrades the quality of every decision by starving it of evidence.

So treat the loop itself as a first-class engineering target. Time it. The full loop — edit, build, run, get to the interesting state, observe. Everything in that path is worth optimizing with the same seriousness you'd optimize shipping code, because it multiplies everything else. And keep the loop honest: it has to end in the real thing running, not a proxy you've quietly stopped believing. The value of an iteration is the truth it produces; a fast loop that lies is worse than a slow one that doesn't.

## How to Apply

1. **Measure the loop end to end.** Stopwatch from "I have an idea" to "I can see whether it worked." Include the forgotten parts: getting to the right state, loading the data, finding the log line. The number is usually several times what people estimate.

2. **Attack the biggest segment first.** Build time, deploy time, time-to-interesting-state — profile it like a frame. A repro case that jumps straight to the failing state is often worth more than any tooling purchase.

3. **Make experiments cheap enough to be casual.** The threshold that matters is psychological: the loop is fast enough when people try things they only mildly believe in. That's when discovery starts, because strong beliefs are where the surprises aren't.

4. **One change per cycle when diagnosing.** Fast loops make single-variable discipline affordable — so use it. Batched changes save wall-clock time and destroy information.

5. **Convert arguments to tests.** When a design discussion loops, stop it with: what's the smallest experiment that settles this? If your iteration cost makes that question reasonable, most arguments simply disappear.

6. **Keep a written log of loop results.** A daily note of what was tried and what happened — a .plan file, effectively. It stops you from re-running last month's dead ends and forces each iteration to have actually concluded something.

## Examples

**Situation:** A game team's level designers wait 40 minutes for a full rebuild to see any gameplay change, so they test ideas twice a day.

**Application:** Treat the 40 minutes as the top-priority engineering bug. Hot-reload for scripts and assets, incremental builds for code, a save-state that drops the designer at the exact encounter under test. The goal is a designer trying an idea within a minute of having it.

**Illustrative result:** Idea attempts per designer-day go from a handful to dozens. The shipped encounters aren't better because the designers got better — they're better because each one is the survivor of far more discarded versions.

**Situation:** An ML team runs training jobs that take three days, and researchers queue up "everything we changed this week" into each run.

**Application:** Build a small-scale surrogate — reduced model, reduced data — that predicts the direction of full-run results in twenty minutes, and validate the surrogate against history before trusting it. Save the three-day runs for confirmation, not exploration. This is the same constraint I put on our own research: if the experiment loop isn't fast enough to keep the researcher engaged, the research slows to the speed of the queue.

**Illustrative result:** Exploration moves to the twenty-minute loop with one variable per run; the expensive runs stop being lottery tickets and start being confirmations.

## Anti-Patterns (tactical)

**Don't:** Accept a slow loop because "we only pay it a few times a day."
**Why:** The cost isn't the minutes; it's the experiments that never happen. Every idea below the annoyance threshold dies untested, and those small untested ideas are where most of the compounding improvement lives. Count the missing iterations, not the elapsed time.

**Don't:** Optimize the loop by cutting the observation step — skipping the profile, the test suite, or actually playing the build.
**Why:** An iteration that ends before you've honestly observed the result is half an iteration. You paid the cycle cost and skipped the part that produces knowledge. The loop is edit-run-*observe*; the third step is the product.
