---
triggers:
  - "user needs to write a postmortem or communicate a failure"
  - "user asks how to handle a failed launch, missed target, or public mistake"
  - "team postmortems are spin documents or blame hunts"
  - "user is tempted to put positive spin on bad news"
use_when:
  - "writing up any failure — outage, missed milestone, lost competition, wrong decision"
  - "setting a team's postmortem culture"
  - "deciding how candid to be with users, investors, or the public after a failure"
fails_when:
  - "active litigation or genuine legal exposure constrains what can be said — get counsel first, then be as candid as permitted"
  - "candor about a failure is used as a substitute for fixing it"
related:
  - "demonstration-over-paperwork.md"
  - "static-analysis-discipline.md"
  - "org-efficiency.md"
  - "fast-iteration-loops.md"
---

# The Candid Postmortem

## When to Use
- Anything failed and people need to be told: an outage, a slipped release, a lost bid, a wrong architectural bet
- The draft in front of you opens with context-setting and achievement-listing before it admits the result
- A team's incident writeups have become exercises in passive voice and blame diffusion
- You were publicly wrong and are deciding whether to acknowledge it

## Fails When
- Lawyers genuinely need to see it first — candor within legal constraint is still possible, but freelancing during litigation converts an engineering document into an exhibit
- The postmortem becomes self-flagellation theater — the deliverable is causes and changes, not a display of contrition
- Personal fault-finding masquerades as root-cause analysis — naming the broken process is the job; naming the scapegoat is the anti-job

## Core Concept

When we lost the Lunar Lander Challenge, my update to the world opened: "We failed." Second sentence: I could try and put the best positive spin on it, but the bottom line is that we failed to win anything at the X-Prize Cup this year. Verdict first, no cushion — and *then* the forensic walk: the two perfect flights, the three engine-destroying hard starts, the IMU that died in backup checking and the Plans A through D we cascaded through, the clogged igniter orifice we cleared with a filed-down paper clip, and the honest terminal state of the analysis: we just don't know. I even wrote down my prior — I'd estimated a 90% chance of winning level 1 — because recording how wrong your confidence was is part of the data. That structure is the whole method: verdict, then causes, then what changes. Spin is a tax every reader pays and a fog you end up breathing yourself.

The argument for candor isn't moral, it's operational. First: you cannot fix what you haven't plainly stated. Every hedge in the verdict subtracts from the precision of the cause analysis, because the story has to stay consistent with the softened version. Second: candor is compounding credibility. I spent years publishing development diaries and failure writeups — engine explosions, crashed vehicles, wrong technical bets I'd argued for publicly and then reversed, like my inlined-code positions I updated in public years later. The result is that when I *do* claim something works, it moves people, because I've demonstrated I'll say it when it doesn't. An organization whose reports are reliably honest gets to spend that trust exactly when it needs it most — during the next failure. Third: the failures are where the transferable knowledge is. My "we failed" post taught other rocket teams more than any success announcement — including our competitors, who had handed us a filter off their own display vehicle mid-competition. That's the culture candor builds.

The blame question has a precise answer: honest about outcomes, forensic about causes, generous about people. The cause chain in a good postmortem runs through decisions, conditions, and processes — we changed the throat diameter, the altitude was different, the checklist step didn't exist — not through character. The moment writeups start costing individuals, people start pre-spinning their inputs to every future writeup, and your information supply is poisoned exactly where you need it pure. And one more honest admission belongs in the genre: sometimes the analysis ends at "we don't know yet." Ours did. Writing that is better than manufacturing a tidy root cause, because the false cause closes an investigation that reality will reopen. It's fine to note you're still sulking, too. I did.

## How to Apply

1. **Verdict in the first sentence.** "We failed." "The launch slipped six weeks." "The migration corrupted data." No context paragraph first — the reader knows the stakes; make them trust the document by sentence two.

2. **Walk the causal chain with specifics.** Times, part numbers, decisions, conditions — each link stated so a reader could disagree with it. Include the near-misses and the backup plans that did work; the goal is a reader who could have been there.

3. **Record what your confidence was.** If you estimated 90% and lost, write that down. Calibration data is the cheapest lesson in the document, and it keeps the next estimate honest.

4. **Say plainly what you don't know.** Separate confirmed causes from suspicions from open questions. "Our best guess is the altitude; we just don't know" ages better than a confident wrong answer, and marks where investigation continues.

5. **End with concrete changes, sized to the lesson.** What gets redesigned, what enters the checklist, what class of failure gets automated away. A postmortem whose action list is "be more careful" learned nothing.

6. **Publish to the widest audience the lawyers allow.** Internal failures to the whole team; public commitments publicly. The audience breadth is what converts a document into a reputation.

## Examples

**Situation:** A SaaS company had a nine-hour outage from a botched migration. The draft blog post opens with "We take reliability seriously" and reaches the outage in paragraph three.

**Application:** Invert it. First line: "We were down for nine hours on Tuesday, and it was our fault." Then the chain: the untested migration path, the backup that hadn't been restored-from in months, the alert that paged the wrong rotation. Then the changes, each specific and checkable. Cut every sentence that exists to make the company feel better.

**Illustrative result:** The post reads like it was written by engineers instead of counsel, which is precisely what retains the customers worth retaining — trust after a failure is rebuilt by demonstrated understanding of the failure, not by adjectives about seriousness.

**Situation:** A CTO personally championed a framework bet that two years later is clearly wrong, and the team is routing around it awkwardly because reversing it means the CTO admitting error.

**Application:** The CTO writes the postmortem on their own decision: what was believed at the time, what evidence has since accumulated, and the reversal. I've done this in public — positions I'd advocated for years, updated with "in the years since I wrote this, I have gotten much more bullish about" the opposite. The author of the mistake writing its correction is the strongest possible signal that the organization values being right over having been right.

**Illustrative result:** The framework gets replaced without a political fight, and — the larger effect — engineers below the CTO start admitting their own wrong bets earlier, because the cost of doing so has been visibly repriced.

## Anti-Patterns (tactical)

**Don't:** Open with achievements to soften the failure ("we made two perfect flights, but...").
**Why:** The reader discounts everything after a cushioned opening, and they're right to — the cushion signals the document is managing their reaction rather than informing it. The perfect flights belong in the cause analysis, where they're evidence about what worked; leading with them makes them spin. Verdict first buys you the credibility to have the successes believed.

**Don't:** Manufacture a single tidy root cause when the evidence hasn't converged.
**Why:** "Root cause identified, action item filed, ticket closed" feels like rigor, but a false cause is worse than an open question — it ends the investigation and leaves the real failure mode armed. We could not have been so unlucky as to have three different causes for three hard starts, and yet we never fully pinned it; writing "we don't know, here's the suspect list, here's the redesign that removes the whole class" was the accurate engineering statement. Prefer eliminating the class to naming a culprit.
