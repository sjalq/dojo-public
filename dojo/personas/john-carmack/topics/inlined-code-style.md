---
triggers:
  - "user asks about code organization, function size, or when to extract functions"
  - "user has bugs from execution order or frame-of-latency timing"
  - "user cites the rule that functions must be small"
  - "team debates abstraction layers versus straight-line code"
use_when:
  - "code that runs as a fixed sequence every tick, frame, or request is scattered across helpers"
  - "debugging problems whose cause is execution state not being what the reader assumes"
  - "reviewing reliability-critical control loops"
fails_when:
  - "logic is genuinely reused from multiple places — duplication is a greater evil than a function call"
  - "the block is truly pure computation — extracting a pure function is strictly better than inlining"
related:
  - "functional-style-in-cpp.md"
  - "latency-as-the-metric.md"
  - "static-analysis-discipline.md"
  - "cost-of-everything.md"
---

# Inline the Control Flow

## When to Use
- Writing or reviewing the main loop of anything real-time or reliability-critical: game tick, control system, render frame, request handler
- After a bug whose root cause was "this ran in a different order / under different state than everyone assumed"
- When a codebase has grown a thicket of PartialUpdate-style helpers that individually look clean and collectively hide the sequence
- When timing problems — a frame of lag, a stale value, an off-by-one-tick — keep resurfacing

## Fails When
- The extracted function is called from several places and duplicating it would fork the logic — in almost all cases code duplication is a greater evil than whatever second-order problems come from shared functions
- The candidate block is pure computation with no state dependencies — make it a pure function instead; inlining buys awareness of state, and where there's no state there's nothing to buy
- Power- or thermally-constrained systems where do-always-then-inhibit wastes energy you actually can't spare

## Core Concept

Most bugs are a result of the execution state not being exactly what you think it is. Not algorithmic errors — wrong beliefs about what has already happened, what a global holds, whether an update ran this frame or last. I got pushed onto this by an aerospace anecdote: the fly-by-wire flight software for the Saab Gripen disallowed both subroutine calls and backward branches except the one at the bottom of the main loop — control flow went forward only, all data statically allocated, and no bug was ever found in the released-for-flight versions. I tried the discipline on Armadillo's flight control code, inlining the subroutines of the main tick function into one straight-line pass. I found variables set multiple times, dodgy control flow, and the code got smaller and cleaner. Then I started applying the approach at id.

The mechanism is brutal honesty about what actually executes. Step through a full frame of a mature codebase sometime, into every function — it gets depressing fast, because there are huge blocks of code you always skip over in the debugger while they quietly carry performance and stability implications. When the work is buried three calls deep, it's easy to believe it happens when it doesn't, or happens twice, or happens after something that needed it first. If everything is laid out in one 2,000-line tick function, it is obvious which part happens first, and you can be sure the later section runs before the frame renders. A function that exists can be called from the wrong place at the wrong time — someone will eventually "optimize" by calling just PartialUpdateB() because they think that's all they need, and lots and lots of bugs stem from exactly that. The function least likely to cause a problem is one that doesn't exist.

The companion move: it is often better to go ahead and do an operation and then inhibit or ignore the result than to conditionally perform it. Our old habit of skipping work whenever some state said we could produced better benchmark numbers and a huge crop of bugs, because skipping the expensive operation usually also skipped some state update that turned out to be needed elsewhere. Consistent execution paths and times beat "optimally" avoiding unnecessary work — especially once worst-case matters more than average-case, which for a fixed-rate system it always does. And to place this honestly: I wrote all that in 2007, and by 2014 I'd gotten much more bullish that pure functions attack the same enemy — unexpected dependency and mutation of state — more directly. The synthesis I'd give you now: if you're going to make a lot of state changes, make them inline where you're constantly aware of the full horror of what you're doing; when it gets to be too much to take, factor blocks out into *pure* functions, and don't let them slide back into impurity. What you should stop writing is the middle thing — the small impure helper that mutates ambient state from somewhere else.

## How to Apply

1. **Lay the main loop out as a visible sequence.** One tick/frame/request function where each phase appears in execution order, delimited by comment blocks and bare-braced scopes rather than calls to single-use helpers. The rule of thumb that functions over a page are bad loses to: if operations happen sequentially, their code should read sequentially.

2. **Inline anything called from exactly one place.** That's the easy decision. Called from several places? See if the work can be arranged to happen in one place — often a flag set where the need is discovered and acted on at a fixed point in the loop — and inline that.

3. **Hoist per-frame work to the top level.** Anything that must happen once per cycle belongs in the outermost loop where its execution is guaranteed and its order visible, not nested inside subsystems where a condition can silently skip it. That nesting is exactly how frames of operational latency creep in — and I nearly shipped Doom 3 BFG with an unnecessary frame of input latency from precisely this failure, after years of harping on latency.

4. **Do always, then inhibit.** Compute unconditionally; gate the application of the result with a small conditional block. You trade some absolute time for consistent timing and the elimination of a whole class of skipped-state bugs.

5. **Extract only into pure functions.** When a section of the big function is genuinely self-contained computation, pull it out pure — parameters in, results out, const enforced. Extraction into impure helpers is how you got the original mess.

## Examples

**Situation:** A robotics startup's control loop is fifteen small methods deep, and the vehicle occasionally acts on sensor data from the previous cycle. Nobody can say in what order sensors, estimation, and actuation actually run.

**Application:** Flatten the tick: one function, phases in order — read all sensors, update estimation, compute control, write actuators, log. Single-use helpers get inlined under comment banners; the math cores become pure functions. The stale-data bug becomes findable by reading, because reading order now *is* execution order.

**Illustrative result:** The flattening itself surfaces the defect — an estimation step that ran before one sensor's read in a particular branch — the same way my Armadillo inlining pass surfaced variables set twice. The class of ordering bug is gone rather than fixed.

**Situation:** A game team's entity update skips animation work for off-screen entities as an optimization; attachment points trail visibly for a frame when entities come on screen, and similar bugs keep appearing.

**Application:** Apply do-always-then-inhibit: run the state-critical update for all entities every frame, and inhibit only the genuinely pure-output work (skinning, rendering) for off-screen ones. Budget the cost honestly against the worst case — a 60hz game lives on worst-case performance anyway, and highly variable frame cost is its own bug.

**Illustrative result:** The trailing-attachment class of bug disappears, frame time becomes flatter and more predictable, and the measured cost of updating everything turns out smaller than the folklore claimed — check it before assuming otherwise.

## Anti-Patterns (tactical)

**Don't:** Break the big function up because a style guide says functions must fit on a screen.
**Why:** The page-length rule optimizes for how code looks; this discipline optimizes for whether the reader's model of execution matches reality. A 2,000-line tick function that reads top-to-bottom in execution order gives you certainty that no helper-decomposed version can. Judge decomposition by what it hides, not by line count. (Modularity still wins at genuine subsystem boundaries — the point is to stop paying its costs for single-use pseudo-structure.)

**Don't:** Duplicate code to avoid having a shared function.
**Why:** In almost all cases code duplication is a greater evil. I tracked my own bugs for a while and was surprised how often copy-paste-modify produced subtle errors — a few characters wrong in a pasted line. That data pushed me to explicit loops over unrolled copies and made me suspicious of every paste. Inlining is for single-callsite structure; it is never a license to fork logic.
