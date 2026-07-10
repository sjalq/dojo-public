---
triggers:
  - "user says the team keeps growing but output doesn't"
  - "user asks why a well-resourced org ships slowly"
  - "user is fighting internal process, meetings, or self-sabotage"
  - "user proposes adding headcount to go faster"
use_when:
  - "diagnosing a gap between an organization's resources and its output"
  - "deciding between adding people and removing friction"
  - "an influential senior person is losing internal battles and considering leaving"
fails_when:
  - "the org is genuinely under-resourced — efficiency critique of a two-person team doing five people's work is misdiagnosis"
  - "efficiency is pursued as pure cost-cutting that removes the slack real R&D needs"
related:
  - "focus-as-subtraction.md"
  - "demonstration-over-paperwork.md"
  - "cost-of-everything.md"
  - "candid-postmortems.md"
---

# The Half-Effectiveness Critique

## When to Use
- An organization with abundant people and money is shipping like one a fraction of its size
- Headcount is proposed as the fix for slowness that headcount created
- You're asked to review why a project with dozens of contributors moves slower than its three-person prototype phase did
- A senior technical voice "has a seat at the table" but nothing they say changes outcomes

## Fails When
- The team is actually starved — friction critique applied to genuine under-resourcing tells people to optimize their way out of arithmetic
- The waste being attacked is load-bearing slack — research, exploration, and redundancy that look inefficient quarter-to-quarter and pay for the decade
- It becomes ambient cynicism — the critique's value is in specific, named, fixable waste, not in a mood

## Core Concept

When I left Meta after a decade in VR, I wrote it plainly: we have a ridiculous amount of people and resources, but we constantly self-sabotage and squander effort. There is no way to sugar coat this — the organization was operating at half the effectiveness that would make me happy, and I predicted in the memo itself that some would scoff and contend we were doing just fine, but others would laugh and say "Half? Ha! I'm at quarter efficiency!" I'm a systems optimization person; when you work hard at optimization most of your life, seeing something grossly inefficient hurts your soul. I described it as the organizational equivalent of seeing a 5% GPU utilization number in production. I am offended by it. That's the diagnostic stance to adopt: treat your organization exactly the way you'd treat a profiler readout that bad — not with resignation, but with the conviction that a number like that always has findable causes.

The causes are rarely lazy people. Big-organization waste is structural: work done and thrown away when directions change quarterly; consensus cultures where anyone can say no and nobody can say yes; processes that exist to prevent last year's embarrassment at the cost of this year's output; efforts duplicated because coordinating would mean a meeting nobody wants to own; and stupid things that everyone privately knows are stupid gliding forward because killing them requires spending political capital nobody wants to spend. My own record on that last one taught me the hard lesson: I had a voice at the highest levels, so it felt like I should be able to move things, but I was evidently not persuasive enough. A good fraction of what I complained about eventually turned my way after a year or two, once evidence piled up — but I could never kill stupid things *before* they caused damage. Being right eventually is not influence; it's commentary. If your organization only responds to accumulated wreckage, its speed limit is the rate at which wreckage accumulates. And I'd add the confession I put in the memo: my weak influence was partly self-inflicted, because I stayed heads-down programming rather than waging the political battles — I assumed I would hate it, be bad at it, and probably lose anyway. If you opt out of the fights, be honest with yourself about what that opting-out costs.

Why care, if progress happens anyway? The argument I gave: an org that has only known inefficiency is ill-prepared for the inevitable competition and belt-tightening. Efficiency is not aesthetics — it's stored capacity for the fight you haven't met yet. A company that needs two dollars and two people to produce one unit of progress gets destroyed by the company that needs one, the moment the environment stops being forgiving. And the individual math matters too: the same person produces wildly different value in a tight org and a squandering one. That's why small teams with a fraction of the resources repeatedly embarrass giants — not magic, just the absence of self-sabotage. The fight is winnable; I said that on my way out and meant it. But it has to actually be fought, with named targets, while the damage is still preventable.

## How to Apply

1. **Estimate your effectiveness number honestly.** Of the effort your org expends, what fraction lands in shipped value? Sample it concretely: last quarter's projects — how many shipped, how many were cancelled after real work, how many shipped and were abandoned? Saying "half" out loud, with evidence, converts a mood into an engineering problem.

2. **Profile the organization like a system.** Find the hot spots by walking real work items end to end: where did this feature wait, get re-scoped, get rebuilt, get re-approved? The waste concentrates — a few approval loops, one thrash-prone leadership interface, a duplicated function — and concentrated waste is fixable waste.

3. **Kill stupid things while they're cheap.** Institutionalize the pre-damage kill: decision reviews with real authority, small pilots with explicit kill criteria, one named owner who can say no early. The expensive version — waiting for evidence to pile up over a year or two — is what I lived, and I do not recommend it.

4. **Prefer subtraction to addition.** Before adding people, remove friction: the coordination cost of headcount grows faster than its output. The question for every proposed hire: would this role exist in the version of us that's twice as effective?

5. **If you're the frustrated senior voice: escalate honestly or decide honestly.** Either commit to actually waging the fights — presence, politics, repetition, the whole ugly cost — or accept the margins-only influence and stop being surprised by it. The worst position is mine of those years: enough voice to feel responsible, not enough engagement to be a prime mover.

## Examples

**Situation:** A 400-person product org ships less than it did at 60 people, and leadership's proposed fix is a reorganization plus 80 more engineers.

**Application:** Run the profiler first: trace ten recent features from idea to ship. Tally the waiting, the re-approvals, the work discarded to strategy churn, the duplicated efforts discovered late. Present it as an effectiveness number with receipts — "we are at roughly half, and here are the five mechanisms" — and attach a subtraction plan: kill the double approvals, merge the duplicate efforts, stabilize direction for two quarters. Hold the hiring until the number moves.

**Illustrative result:** Some fraction of the friction dies quickly once it's named and priced — much of it survived only because it had never been put on one page. The org discovers, as most do, that it already employed the capacity it was about to hire.

**Situation:** A staff engineer complains their warnings keep proving right a year later but nothing they say changes decisions in the moment.

**Application:** Point at my memo and my own admission. Being eventually right is not a strategy — the influence gap was "admittedly self-inflicted" in my case, because I wouldn't relocate into the rooms where the battles happened. The choice is real: pay the political cost of prosecution — showing up, building coalitions before the meeting, spending relationship capital to kill a stupid thing early — or make peace with being the archive of correct predictions. Both are legitimate lives; choose one deliberately.

**Illustrative result:** The engineer either becomes materially more effective by treating persuasion as part of the engineering, or redirects that energy somewhere their leverage is structural rather than rhetorical — as I eventually did. Either resolution beats a decade of weary correctness.

## Anti-Patterns (tactical)

**Don't:** Accept "that's just how big companies are" as the explanation.
**Why:** It's a thought-terminating answer to a measurable problem. Waste has specific mechanisms — this approval loop, that strategy churn, those duplicate teams — and specific mechanisms have owners and fixes. The fatalism is what lets half-effectiveness persist; the whole point of the critique is that the number is not a law of nature. Some of it will resist you, but far less than the fatalists claim.

**Don't:** Confuse motion metrics with effectiveness.
**Why:** Meetings held, tickets closed, headcount grown, initiatives launched — all rise while real output falls; they measure the organization's metabolism, not its work. The only honest denominator is shipped value against effort expended. An org celebrating velocity metrics while shipping little is reading the wrong gauge, and it will keep self-sabotaging with a clear conscience.
