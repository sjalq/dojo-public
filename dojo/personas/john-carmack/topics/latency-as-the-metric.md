---
triggers:
  - "user asks about VR, AR, or real-time interactive performance"
  - "user optimizes throughput or frame rate while responsiveness feels bad"
  - "user asks what metric to obsess over for an interactive product"
  - "user's system feels laggy despite good benchmark numbers"
use_when:
  - "building anything where a human acts and the system responds — VR, games, tools, robotics, live interfaces"
  - "choosing the north-star engineering metric for an interactive system"
  - "diagnosing why a system that benchmarks well feels wrong"
fails_when:
  - "batch or offline workloads where throughput genuinely is the product"
  - "latency is already below human perception for the interaction class — further heroics buy nothing"
related:
  - "cost-of-everything.md"
  - "inlined-code-style.md"
  - "fast-iteration-loops.md"
  - "user-value-equation.md"
---

# Motion-to-Photon: Pick the Metric That Maps to Experience

## When to Use
- Building or reviewing any interactive system where the user's action and the system's response form a loop
- A team is celebrating throughput numbers (frame rate, requests/sec) while users report the product feels sluggish
- Choosing what single number the engineering organization should track and budget against
- Trading off image quality, features, or architecture against responsiveness

## Fails When
- Non-interactive pipelines — renders, batch training runs, ETL — where nobody is inside the loop and throughput is the honest metric
- The interaction class is genuinely latency-tolerant and the budget is already met — polishing 40ms to 25ms in a turn-based UI is effort the user cannot perceive
- Latency is minimized by sacrificing correctness of what's displayed — a fast wrong answer

## Core Concept

In VR I reduced the entire quality argument to one number: motion-to-photons — the time from your head moving to correctly updated light hitting your eyes. Human sensory systems can detect very small relative delays, but when absolute delays are below approximately 20 milliseconds they are generally imperceptible; interactive 3D systems of the day were running several times that. The reason this one number deserved obsession is that VR's goal is to have the experience accepted at an *unconscious* level. With a mouse you consciously operate an interface and adapt to lag; presence isn't a judgment, it's a reflex, and the reptile brain does not grade on a curve. The metric earns its tyranny when it maps directly onto the experience like that.

The engineering content is the accounting. A 60fps application "should" be 16 milliseconds, but walk the real path — sensor sampling, transport, processing, simulation, rendering, driver command buffering, scanout to the panel — and you find host latencies over 50 milliseconds even at a perfectly smooth 60fps, because every layer buffers for throughput. The drive to win frame-rate benchmark wars led driver writers to aggressively buffer drawing commands; there were even cases of drivers ignoring explicit glFinish() calls in the name of "performance." That's the general disease: each layer optimizes the number it's measured on, and the user-facing number nobody owns quietly triples. So you budget it like mass on a rocket: name every stage, measure every stage, assign every stage a millisecond allowance, and make one person own the total.

Then the good part: once the whole pipeline is on one budget, you get to make cross-layer trades that are invisible to anyone optimizing a single stage — sample the sensor as late as possible, predict head motion to cover the remaining pipeline, warp the rendered image at the last instant (time warp), race the beam. None of those moves lives inside one component; they exist only for engineers who own the end-to-end number. That's the transferable lesson beyond VR: pick the single metric that maps to what the user's nervous system actually experiences, budget it across every layer including the ones you don't own, and mistrust every component metric that can improve while the experience gets worse. Frame rate was never the point — a stable 60fps with three frames of buffering feels worse than an honest 60 with none.

## How to Apply

1. **Define your motion-to-photon equivalent.** For any interactive product: from the user's physical action to the perceptible, correct response. Keystroke-to-glyph, tap-to-feedback, command-to-result. Write it down as the metric; everything else is a component number.

2. **Measure it physically, end to end.** High-speed camera, hardware timestamp, or a photodiode on the screen — not the sum of internal timers, which always flatters you. The gap between the sum-of-parts number and the measured number is where the buffering hides.

3. **Build the stage budget.** List every stage from input to output with its measured cost; force the list to add up to the physical measurement. Assign allowances. The stages that resist measurement — drivers, OS compositors, network stacks — are the ones most likely to be eating your budget.

4. **Set the perceptual threshold as the spec.** Find the number below which your users genuinely can't perceive delay for this interaction class — for head tracking it's about 20ms; other interactions are more forgiving — and engineer to that, not past it. A spec anchored to human perception ends arguments the way any measured cost does.

5. **Exploit cross-layer tricks once you own the pipeline.** Late sampling, prediction, last-instant correction, doing work speculatively and discarding it. The point of owning the end-to-end budget is that these become visible and legal.

6. **Guard it in CI.** Latency regresses one "harmless" buffer at a time. An automated end-to-end latency test that fails the build is the only way the budget survives contact with a growing team.

## Examples

**Situation:** A collaborative-editor team benchmarks 120fps rendering, yet typing "feels mushy" in reviews and nobody can explain why.

**Application:** Stop arguing about feel; measure keystroke-to-glyph with a 240fps phone camera. Then build the stage budget: input event queue, framework batching, layout, render, compositor. Find which stages buffer.

**Illustrative result:** The physical measurement comes out several frames worse than the internal timers claim — the same layer-buffering pattern as GPU drivers in the benchmark wars. Two batching layers each holding one frame "for efficiency" get late-sampled instead, and the mushiness reviews stop, with frame rate unchanged. Throughput was never the problem.

**Situation:** A cloud-gaming startup is choosing between two architectures: one maximizes video quality at ~140ms input latency, the other holds a lower bitrate at ~70ms.

**Application:** Anchor to perception, not to component specs: action-to-photon delay is the experience for a game — it's the difference between playing and watching. Budget the full path (controller, uplink, queue, render, encode, downlink, decode, display) and spend engineering on the stages that dominate. Prediction and late-correction tricks from VR apply directly: the client can render locally-predicted response for the stages you can't compress.

**Illustrative result:** The latency-first architecture wins playtests decisively even though its video-quality score is lower — the number that mapped to the nervous system beat the number that mapped to the marketing page.

## Anti-Patterns (tactical)

**Don't:** Report average latency.
**Why:** Perception is dominated by the worst cases — a spike every few seconds reads as "glitchy" even when the mean is excellent, and for something strapped to your head the bad frames are what make people ill. Track the distribution and set the spec on the high percentiles. A system that never misses at 25ms beats one that averages 15 with excursions past 60.

**Don't:** Let each layer add "just one frame" of buffering for its own smoothness.
**Why:** Nobody ever decides to have 90 milliseconds of lag; it accretes one defensible buffer at a time — driver, compositor, framework, app — each locally reasonable and globally disastrous. Every buffer needs to justify itself against the end-to-end budget, and the burden of proof sits on the buffer, not on its removal.
