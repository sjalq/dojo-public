---
triggers:
  - "user asks how often to ship, release, or respond to feature requests"
  - "user is drowning in issues, requests, or feedback and answering each one-by-one"
  - "user asks about release cadence, changelogs, or announcement strategy"
  - "user feels pressure to show constant public activity"
use_when:
  - "deciding cadence and grouping for releases of a platform, API, or product others build on"
  - "a backlog of related requests could be solved piecemeal or holistically"
  - "the team optimizes response latency at the cost of design coherence"
fails_when:
  - "the issue is a fire — security holes, data loss, and outages get fixed now, not batched"
  - "you depend on rapid feedback loops to find product-market fit — early-stage discovery may need latency, not batch design"
related:
  - "on-storytelling.md"
  - "saying-no.md"
  - "what-is-success.md"
  - "api-design-guidelines.md"
---

# Batching (let issues accumulate; ship coherent stories)

## When to Use
- Setting release cadence for anything other people build on top of
- A cluster of feature requests and bug reports seem vaguely related
- The team measures itself by time-to-close on issues
- Deciding between many small announcements and one strong one

## Fails When
- **Urgency is real.** Security issues, data loss, and broken builds are not design opportunities. Batching applies to design decisions, not incidents.
- **You are still searching for the product.** Batching optimizes the quality of answers to known problems; when you do not yet know the problems, faster loops may matter more than coherence.

## Core Concept

Evan Czaplicki runs his projects on a policy he calls batching, and he is upfront that it looks wrong from the outside. The default model of a healthy project: "someone will open an issue, and the ideal is that it gets resolved — open issue, resolved, open it. And so you're optimizing for latency. How quickly can I respond to everybody on the internet who has things to say to me?" His alternative, from the Deconstruct talk: "someone opens an issue, and we say, OK. And someone else opens another issue. And over time, we let these build up. And we do a more high-level analysis of all of the concerns people have. And so when you look at them holistically, you can find one fix that addresses all those concerns in a way that's clear. And I think this, in the end, leads to better design."

The elm-conf version adds the honest optics: as issues pile up "people are freaking out, you know, people are crying in the streets... the locusts have come" — but once there is a pile, "we can actually look at all those issues and start to see some trends... these people over here are all talking about a similar thing. They sort of have slightly different goals, they have different ideas of how to achieve that, but fundamentally there might be a solution that addresses all those concerns." One designed solution to the underlying theme, instead of N local patches that each made sense alone and jointly make a mess. His larger point: "a lot of times people don't realize the process they have is influencing the API decisions, the design decisions they're making." Latency-optimized process produces patchwork design; batch-optimized process produces coherent design. Choose the process for the design you want.

There are two more forces behind batching. **Platform economics:** "when Elm core library changes... every single package in the whole ecosystem has to change, and all the applications have to change. That's a lot of work to ask a whole community to do, and it doesn't make sense to do that lightly." Every release of a thing people build on imposes cost on everyone downstream; he wants "releases that are worth great cost," not a cadence maintained "just because it's exciting." **Narrative:** batching makes each release a story. "Each release is about — we did this work on the compiler; Elm has an emphasis on developer experience. You get a broader narrative than '40 things happened.' So I always am sad when I see a language release and it's just a list of 200 pull requests which were merged in. It's like, OK, but what happened?" (See on-storytelling.md — releases are news, and batching is what makes the news strong.)

His evidence that flexibility beats roadmap-latency comes from the compiler roadmap: "all the error message work in Elm began as a project to implement the `--report=json` flag. That work happened to reveal some cool ideas on improving error messages, and if I had been using a rigid roadmap, I might have skipped those ideas to meet the publicly-stated arbitrary deadline."

## How to Apply

1. **Split the queue: incidents vs. design.** Fires get latency. Everything that shapes the design of the product goes into the batch.
2. **Acknowledge fast, resolve slow.** Batching is not silence. "We say, OK" — the reporter hears they were heard, with honest expectations. Evan even automated this with a bot that explains the process on new issues, so the policy is legible instead of looking like neglect.
3. **Periodically analyze the pile as a whole.** Cluster by underlying concern, not by requested feature. Different users propose different mechanisms for the same root problem; the designed fix often matches none of the proposals and satisfies most of the concerns.
4. **Design once, against the cluster.** Do the literature review, the alternatives, the simplest-thing search (see api-design-guidelines.md). The output is one coherent change with a reason.
5. **Ship the batch as a story.** The release announcement should say what is different about your users' lives, not enumerate merges. If you cannot write the narrative sentence, the batch may not be ready.
6. **Price releases by downstream cost.** Before shipping a breaking or attention-demanding release, estimate the total hours it imposes across every user and dependent. Bundle breaking changes together — "if there's a big change to core anyway, that's actually a great time to do a lot of these fix-up issues, because you're going to need it anyway."

## Examples

**Situation:** A B2B API team ships a small breaking change every few weeks, each individually reasonable, and customers are grumbling about churn.
**Application:** Each release taxes every integrator. Batch the breaking changes into one migration with one coherent design and one upgrade guide, on a schedule customers can plan around. The measure of a good release is that it was worth its cost to *them*.
**Illustrative result:** Integrators do one planned migration instead of six surprise ones, and the release notes read as "the auth model is simpler now" instead of a changelog of paper cuts.

**Situation:** A founder answers every feature request within a day, shipping small accommodations each time, and the product is becoming a junk drawer.
**Application:** The response speed *is* the mechanism of the mess — each 5-minute yes skipped the holistic analysis. Move to acknowledge-fast/design-slow, and review the accumulated requests monthly for the theme underneath. Ten requests for export formats might really be one request for a stable data API.

**Situation:** A team feels pressure to post weekly updates so the project "looks alive."
**Application:** Evan's warning about "saying things to say things": forced updates are uninteresting, and speculative ones create "yeah, but you said..." debt when plans change. Fewer, stronger announcements attached to real releases beat a cadence of noise (see what-is-success.md on activity proxies).

## Anti-Patterns (tactical)

**Don't:** Measure the team on issue-close latency or open-issue count.
**Why:** You will get what you measure: N fast local patches, no holistic analysis, and a design shaped by whoever filed tickets loudest and most recently. The open-issue count is inventory for design work, not a debt figure.

**Don't:** Batch silently.
**Why:** Without visible acknowledgment and a stated process, batching is indistinguishable from abandonment, and the community narrative ("is this project dead?") fills the vacuum. The policy must be public, boring, and consistently applied — then long quiet stretches read as design in progress, because that is what they are.
