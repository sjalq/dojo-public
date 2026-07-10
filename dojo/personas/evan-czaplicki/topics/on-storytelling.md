---
triggers:
  - "user asks how to announce, pitch, or explain a technical product or change"
  - "user's audience 'doesn't get it' or debates are going in circles"
  - "user is writing a launch post, release notes, or landing-page copy"
  - "user asks how to handle a community or audience conflict about their work"
use_when:
  - "communicating technical work to people whose experience differs from yours"
  - "a true feature list is failing to persuade anyone"
  - "turning finished work into an announcement people will actually care about"
fails_when:
  - "used to stoke anxiety rather than resolve it — the same process is the advertising/propaganda playbook, and the ethics live in the intent"
  - "there is no real conflict — storytelling scaffolding on a routine update reads as hype"
related:
  - "batching-and-releases.md"
  - "what-is-success.md"
  - "gradual-learning.md"
  - "platform-vs-productivity-languages.md"
---

# On Storytelling (observe conflict → shared language → story → news)

## When to Use
- Writing a launch, release announcement, pitch, or explanation of technical work
- Two camps are talking past each other about your product ("types make me more productive" / "types make me less productive")
- Your factually correct description is landing as "so what?"
- Deciding what needs to be true technically before a story can honestly be told

## Fails When
- **The intent is to stoke, not resolve.** Evan is explicit that advertising and politics run the same process on fears "with no intention of resolving it, just an intention of stoking it." The process is morally neutral; using it to inflame is how you become the thing your users distrust.
- **Nothing is at stake.** If there is no anxiety or conflict to resolve, forcing the frame produces breathless copy about a patch release. Say the plain thing.

## Core Concept

Evan Czaplicki's Deconstruct 2017 talk lays out the communication process behind every Elm feature and release. He credits its intellectual backbone to Walter Lippmann's *Public Opinion* (1922) — keep that attribution; Evan does. The process: "we start with people who don't care... I start by observing some conflict. There's something out there that people are anxious about... From there, I try to find some shared language... And then I try to tell a story about that. And finally, I try to create news so people actually learn about this story. And hopefully, at the end, that anxiety is resolved."

The foundation is a theory of *meaning*. Watching two people argue about static types, he asks why people looking at the same facts disagree: "When someone says a word like 'types,' they're really picking out an experience they had" — one person means Java-at-university, wrapped up with every early-programming frustration; another means a pleasant bootcamp-to-Elm path. "Someone can truthfully say, types make me more productive. And another person can say, types make me less productive. And those two true things have to coexist." Quoting Lippmann: "useful discussion, instead of comparing ideals, re-examines the visions of the facts." The conflict is emotional before it is technical; resolve the meaning problem or the debate loops forever.

Shared language is found by testing candidate statements against the listener's honest reactions. "Elm has a sound type system with full type inference" — true, and the correct response is "so what?" ("the sentence is, Elm has a thing with some stuff"). "It catches errors at compile time" — invites "so my dev cycle is slower and the messages suck." "Better error messages" — "says who? It's your thing." The one that works: **"there's no runtime errors,"** because the reaction is "wait, is that possible? Are you a liar?" — which creates curiosity ("I'm going to go fact check this guy... and now you're trying it out") *and* transmits his actual emotional experience of the language. His operating rule: "One thing I try to do in my communication is be concrete. I never want an audience or a user or a reader to infer the benefits. I want to just say, here's what the benefit is."

The last two steps: a story needs visualization (show, don't describe — the friendly-error-message screenshot does the arguing) and personal relevance (Lippmann: "no visual idea is significant until it has enveloped some stress of our own personality" — behind "why is my code crashing?" sits "am I good at my job?"). And a story without news is a book in a drawer: "Before a series of events becomes news, they usually have to make themselves noticeable in some more or less overt act." In software you get this for free — **releases are news** (see batching-and-releases.md). Critically, the causality can run backwards: "those technical details are in service to a story I want to tell, not for their own sake" — he decides the story, then works out what must be technically true for it to be honest.

## How to Apply

1. **Observe the conflict.** What are people in your market actually anxious or angry about? ("This is easy for me to do, because people just yell at me about stuff.") Collect the real phrases they use.
2. **Dig for what the words point at.** When people say "single page apps" or "scalable" or "enterprise-ready," list the concrete things they are referring to — Evan unpacked "SPA" into tree shaking, code splitting, lazy loading, routing, and reframed the pile as "asset management: how do I get people their content quickly?" Find the root concern under the buzzwords.
3. **Draft candidate statements and stress-test each against a skeptic's honest reply.** Kill everything that earns "so what?", "says who?", or "you would say that." Keep the one that earns "wait — is that possible?" It must be true, concrete, checkable, and carry your actual emotional experience of the thing.
4. **Build the story as a visual, relevant demonstration.** One image or example that does the observing and imagining for the reader, tied to a stress they personally feel.
5. **Create news.** Attach the story to an overt act — a release, a launch, a published number. Then work backwards: what must be technically true before this story can honestly ship? Build that.

## Examples

**Situation:** A founder's landing page says "AI-powered workflow orchestration platform with enterprise-grade reliability."
**Application:** Every phrase fails the so-what test — it's "a thing with some stuff." Find the conflict (say: ops teams are anxious about 2 a.m. pipeline failures), then a checkable are-you-a-liar claim ("your pipelines can't fail silently — if that sounds impossible, watch this"), then a 30-second visual demonstration of the impossible-sounding thing.
**Illustrative result:** Skeptics arrive to fact-check and leave having tried the product — the same mechanism that pulled JavaScript developers into Elm.

**Situation:** A debate between two internal camps about a rewrite is on its fortieth Slack thread.
**Application:** Stop comparing ideals; re-examine the visions of the facts. Each camp's key words ("stability," "velocity") point at different lived experiences — usually different past projects. Make each side state the experience behind the word. The discussion goal shifts from mutual agreement to mutual understanding, which is often the best available outcome and is enough to make a decision.

**Situation:** A team has shipped eleven improvements and wants to tweet each one as it lands.
**Application:** Eleven tweets are eleven non-events. Hold them, find the narrative that unifies the best of them, ship one release whose story is "X is no longer something you worry about," and let the release be the overt act that makes it news.

## Anti-Patterns (tactical)

**Don't:** List features and expect the audience to infer the benefit.
**Why:** They will infer from *their* experience, not yours — and their experience may map your feature to a cost ("compile-time errors" → "slower dev loop"). If you don't state the benefit concretely, the meaning problem fills the gap with whatever the listener already believes.

**Don't:** Choose the claim that is safest and hedge it.
**Why:** Hedged claims produce no curiosity and no news. The claim that works is the one that sounds slightly impossible *and is true*. If none of your candidate statements risks "are you a liar?", either dig deeper for the real benefit or go build something worth the sentence.
