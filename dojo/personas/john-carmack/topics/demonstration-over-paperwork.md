---
triggers:
  - "user must convince a regulator, investor, boss, or committee"
  - "team produces documents and decks instead of working systems"
  - "user asks how to de-risk a hard technical claim"
  - "process and review gates are growing faster than output"
use_when:
  - "an approval or investment decision is being fought with documents when a demonstration is possible"
  - "choosing between analysis-heavy and test-heavy development for hardware or systems"
  - "a claim can be settled by building and showing the thing"
fails_when:
  - "failure of the demonstration is catastrophic or irreversible — you don't demo your way through crewed flight safety"
  - "the demo can be gamed — a staged demonstration is worse than paperwork because it carries false conviction"
related:
  - "fast-iteration-loops.md"
  - "candid-postmortems.md"
  - "org-efficiency.md"
  - "against-groupthink.md"
---

# Demonstration Over Paperwork

## When to Use
- You need to convince a skeptical gatekeeper — regulator, investor, exec, standards body — and you could show instead of argue
- A team is on its third document about a system that could have been prototyped in the same time
- Two engineering factions disagree about feasibility and both have decks
- Allocating a hardware program's budget between analysis and test articles

## Fails When
- The demonstration risks lives or unrecoverable assets — some domains earn their paperwork, and safety-critical process exists because failures there are not iterable
- The demo is a special case dressed as a general solution — a rigged demo converts your audience to a false belief, which costs more than skepticism
- You demo so early and so publicly that a routine failure becomes a reputation event you can't afford

## Core Concept

At Armadillo Aerospace, our regulator required us to do an untethered free flight of the lander before flying it in front of a crowd. We would have preferred not to risk the vehicle, but I very much approve of actual demonstration over yet more paperwork for convincing regulators, so I didn't argue too much. The flight went perfectly — and it settled the question in a way no document stack could. That was the whole Armadillo doctrine: cheap hardware, fly it, fix it, fly it again. We were a handful of part-timers competing against better-funded teams, and the asymmetry that kept us in the game was that a flight produces facts while a document produces opinions about facts. Reality is the only reviewer that can't be argued with.

Paperwork exists to predict what a system will do; demonstration reveals it. The prediction is expensive, slow, and systematically flattering — every analysis quietly assumes away what its author didn't think of. Our engines at the X-Prize Cup failed three times with hard starts that none of our preparation predicted: dozens of successful test flights, every requirement demonstrated in advance, backups for everything, and the vehicle still found a failure mode that lived in the gap between our test site and that launch site — altitude, humidity, we never fully knew. If demonstrated systems still surprise you, imagine how wrong the merely-documented ones are. That cuts both ways, and honesty requires saying so: demonstration is not proof of everything, it's evidence about what you actually tested, and its limits have to be respected. But paper has all the same limits plus one more — it never touched reality at all.

The doctrine generalizes far past rockets. Demo or it didn't happen — in VR we lived by that; strapping the prototype to someone's head recruited allies that no spec ever did. At Keen we built a robot that physically plays Atari off a camera and a servo-driven joystick precisely because simulation results let researchers hide from reality's inconveniences — latency, noise, a screen that keeps running while you think. When people tell me robots will be doing everything in a couple of years, my answer is: take your next dancing-robot demonstration and ask it to pick up a joystick and learn a game it's never seen. The demand for demonstration is also a hype filter — it's how you keep *yourself* honest, not just how you convince others. An organization that rewards convincing documents breeds convincing writers. An organization that rewards working demonstrations breeds working systems.

## How to Apply

1. **Convert the claim to a demonstrable unit.** Take the assertion the paperwork is trying to establish and ask: what is the smallest real artifact, running under real conditions, that would settle it? Scope the demo to the actual point of doubt, not to a general showcase.

2. **Spend document-time on demo-infrastructure instead.** The teams that demonstrate well aren't braver; they've made demonstration cheap — test stands, harnesses, spare vehicles, one-command deploys. That's the same investment as iteration speed, pointed at persuasion.

3. **Demonstrate under the audience's conditions, not yours.** The gap between your bench and their environment is where failures live — our engines worked in Texas and shattered in New Mexico. Let the skeptic pick the inputs, the site, the timing. A demo that survives hostile conditions converts permanently.

4. **Keep the required paperwork lean and downstream of tests.** Where documents are genuinely mandatory, write them from demonstrated results rather than predicted ones. A document that says "we flew it six times, here's the telemetry" is short, true, and unanswerable.

5. **Report failed demonstrations plainly.** The privilege of demonstration culture is bought with candor — you get to skip the paperwork because your demos, including the failures, are trustworthy. Spin one result and you're back to being audited like everyone else.

## Examples

**Situation:** A platform team has spent six weeks arguing by RFC about whether the new architecture can meet the throughput target; a decision meeting with the VP is scheduled to settle it.

**Application:** Skip the third document revision. Build the skeleton — real network path, real serialization, stub business logic — and run the load test at target volume. Bring the measured curve to the meeting instead of the projected one.

**Illustrative result:** The demo settles in a week what the documents couldn't settle in six, in either direction — and if the skeleton misses the target, you've been saved from winning the argument and shipping the failure.

**Situation:** A hardware founder faces a certification body demanding extensive analysis before field trials, and the analysis backlog is consuming the runway.

**Application:** Do what the process allows in parallel: build the test article, instrument everything, and generate demonstrated evidence under controlled conditions — then feed the certification paperwork from test data instead of pure analysis. Regulators are people; ours at Armadillo traded permit emails with us on nights and weekends because they could see flights happening and wanted us to succeed. Momentum you can show recruits the gatekeeper to your side.

**Illustrative result:** The document set shrinks because each claim cites a test instead of a derivation, review cycles shorten because the reviewers trust data over promises, and the relationship with the gatekeeper improves — demonstration respects their actual concern, which was never the paperwork itself.

## Anti-Patterns (tactical)

**Don't:** Build the impressive demo instead of the honest one.
**Why:** A demo tuned to look good — cherry-picked inputs, hidden operator, the one golden unit — converts your audience to a belief you know is false. When reality arrives, you lose the deal and the credibility, and credibility is the asset that made demonstration cheap for you in the first place. The demo's job is to transmit truth with force, not to win the meeting.

**Don't:** Use "we demo, we don't document" as cover for never writing anything down.
**Why:** The point is to replace *predictive* paperwork with demonstrated fact, not to erase the record. I wrote up every Armadillo flight, success or wreck, in public detail — that log was our institutional memory and our credibility. Demonstrate first; then write down what actually happened, briefly and honestly.
