---
triggers:
  - "user maintains an open source project, community, or public product and is overwhelmed"
  - "user faces 'why don't you just' demands from users or a crowd"
  - "user asks how to handle online criticism, angry threads, or community conflict"
  - "user is designing a community, forum, or feedback channel"
use_when:
  - "advising a maintainer, founder, or public builder on crowd dynamics and demand management"
  - "someone treats free contributions or community labor as an unlimited resource"
  - "designing the structure of a discussion space"
fails_when:
  - "the criticism is a signal, not noise — a pattern of similar complaints is design input (see batching), not crowd pathology"
  - "used to dismiss all accountability — maintainers still owe honesty about expectations, even when they owe no labor"
related:
  - "economics-of-programming-languages.md"
  - "saying-no.md"
  - "what-is-success.md"
  - "batching-and-releases.md"
---

# The Hard Parts of Open Source ("why don't you just...")

## When to Use
- A maintainer or founder is being flooded with confident suggestions from people without context
- Someone proposes "just delegate it" or assumes free labor scales without limit
- Angry viral threads about your project are consuming the team's energy
- You are designing a community space and choosing its mechanics

## Fails When
- **The crowd is right.** Recurring complaints from many independent people are data about a real design problem. The framework explains why *interactions* go badly; it must not become armor against the content of feedback.
- **You use it to avoid ever explaining yourself.** Evan's own practice is to eventually write the careful two pages — batched, once, in a place he can link to — not to never answer.

## Core Concept

Evan Czaplicki's Strange Loop 2018 talk names the recurring interaction patterns that grind maintainers down, and traces where they come from. The signature pattern is **"why don't you just..."** — "why don't you just get the JS API directly, or release an incremental version, or derive the JSON decoders." His answer: "in all these cases it's more complex than it sounds. If there's something that you can think of in five minutes or an hour or a day, probably someone has thought about that and considered it, and there might be implications that you don't see from your perspective, but someone else in the community might have a problem with that." Design means making things work for many parties at once; the suggester sees one.

The asymmetry is structural. "Maybe there's 10,000 people who might be curious... and the number of people who know the full context is pretty small, maybe 10 or 20 people. So if it takes five minutes to say 'why don't you just blah blah blah,' and it takes two pages of writing — and you have to write it very carefully, because if you're an influential community member people will refer back to what you said four or five years ago" — the crowd generates demands at a cost of nothing and the maintainer answers at a cost of everything.

Second pattern: **the somebody store.** Told to "just delegate," his unfiltered inner reply: "Hello, is this the somebody store? Yes, we'd like someone to take unsolicited advice on the internet... it's unpaid, no one's gonna say thank you." The calm version identifies the hidden assumption: "free rice means you can take as much as you want... does that imply that free labor means you can use as much as you want? In fact, this isn't how labor works. If you don't pay for labor, you get less." And even willing labor isn't fungible: coordination, goal alignment, and trust limit who can effectively work on what.

Third: **on whose authority** and **all discussion is constructive** — the viral hostile essay, the 320-comment thread. He quotes Rich Hickey processing one such "diatribe": "every time I have to process [this]... I have to struggle back from 'why should I bother,' and every time it gets harder." Evan's accounting: 10 minutes per comment across 300 comments is "50 hours... just dealing with someone's anger. Could that have been helping someone new, or spending time with family members?" His reframe for the debates themselves: people arguing about a feature hold different *priorities* (flexibility vs. simplicity), so arguments persuasive under one value system simply are not persuasive under another. "I've come to see directed discussion as being about **mutual understanding rather than mutual agreement**."

His structural diagnosis: these conflicts barely happen to him in person, because physical places are *for* something — work, a conference, a meetup all carry norms about what is appropriate. Online platforms are engagement machines ("do you want hashtag-disappointing-Q3, or do you want the viral one?") that mix communities with clashing priorities, decontextualize people into handles, and compress feedback into votes. His prescription sketch — intentional communication — structures discussion by declared intent (learn, answer, clarify, thank), so that "yell angrily isn't one of the states in the discussion; it's unreachable."

## How to Apply

1. **Answer "why don't you just" by enumerating the parties.** List who is affected by the suggestion and what breaks for each. This converts a status fight into a design walk-through — and shows the asymmetry rather than resenting it.
2. **Batch your careful answers.** Write the two-page explanation once, publicly, linkably (see batching-and-releases.md). Every subsequent five-minute demand costs you a link, not an evening.
3. **Budget anger-processing explicitly.** Estimate the hours a hostile thread will consume across the team, and decide *on purpose* whether to spend them. Experienced maintainers develop immunity ("enough people have told me Elm is gonna die next month"); protect the newer community members who have not.
4. **Refuse the free-labor assumption out loud.** When someone proposes "the community will handle it," ask: who specifically, coordinated by whom, paid how, aligned with the goals how? (See economics-of-programming-languages.md for the funded version of this same work.)
5. **Aim discussions at mutual understanding.** When two camps deadlock, get each to state the priority behind their position. You often cannot get agreement; you can almost always get an accurate map of the disagreement, and decisions can be made from a map.
6. **Give your spaces a purpose.** State what each channel is *for*, and design its mechanics (prompts, structured replies, feedback categories like scary/encouraging or off-topic/helpful) to match. Purposeless spaces inherit the internet's default norms, which are engagement-optimized hostility.

## Examples

**Situation:** A founder of an open-core devtools company gets a highly upvoted thread: "why don't you just open-source the whole thing?"
**Application:** Enumerate the parties: paying customers funding development, employees whose salaries depend on the paid tier, users of the free core, future users who need the company solvent. Write the careful explanation once, pin it, and link it forever. Do not litigate it thread by thread — that is 50 hours a month of anger processing on a question that does not change.
**Illustrative result:** The demand keeps arriving (it always does); the marginal cost of each arrival drops to near zero, and the team's Saturdays stop belonging to strangers.

**Situation:** A maintainer is drowning and the community suggests "just add more maintainers."
**Application:** The somebody store. Walk the actual constraints: onboarding cost, trust for merge rights, goal alignment, coordination overhead — "even if you can work with anybody you want, there are still these limitations on who is gonna be really effective." The realistic paths are funding specific people for specific roles, or shrinking scope (see saying-no.md).

**Situation:** A community Discord has become a place where every design decision reopens as a fight.
**Application:** The place is for nothing, so it is for conflict. Declare purposes per channel, add structure to how feedback is filed (intent, background, concrete case), and route design debates into a process where concerns are recorded, batched, and answered holistically — not re-argued live each week.

## Anti-Patterns (tactical)

**Don't:** Engage every critic to correct the record.
**Why:** The economics are upside down — five-minute demands versus two-page careful answers, multiplied by a crowd. You cannot win an attrition war you fund alone. Answer patterns once; let individual instances go.

**Don't:** Treat hostility as the price of openness and absorb it silently.
**Why:** Hickey's line is the warning: each round makes "why should I bother" harder to answer, and the people around you are absorbing it too — often with less immunity than you. Burnout of the one person with full context is the single biggest existential risk to the project; managing your own exposure is not self-indulgence, it is capacity planning (see what-is-success.md).
