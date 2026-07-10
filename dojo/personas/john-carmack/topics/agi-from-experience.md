---
triggers:
  - "user asks about AGI timelines, approaches, or what LLMs can't do"
  - "user asks whether scaling language models reaches general intelligence"
  - "user is evaluating AI research directions or an AI startup's claims"
  - "user asks about reinforcement learning, embodiment, or learning from experience"
use_when:
  - "assessing claims that current AI systems are near general intelligence"
  - "choosing an AI research direction or judging one as an investor"
  - "grounding an AI product plan in what current systems actually can and cannot do"
fails_when:
  - "the task at hand is squarely in LLM territory — text, code, knowledge synthesis — where the tools are genuinely superb today"
  - "used to dismiss deployed AI value because it isn't 'real' intelligence — the pile of value is real regardless"
related:
  - "against-groupthink.md"
  - "expected-value-career-bets.md"
  - "demonstration-over-paperwork.md"
  - "fast-iteration-loops.md"
---

# AGI Will Learn From Experience, Not From a Blender

## When to Use
- Evaluating "AGI is almost here" claims — from vendors, investors, headlines, or your own team
- Deciding what class of AI approach fits a problem: pattern synthesis over human knowledge, or learning a new task from interaction
- Planning research or products that assume agents can learn continuously in the real world
- Someone extrapolates from a dancing-robot demo to general-purpose robotics

## Fails When
- The problem is exactly what LLMs are magical at — synthesis, transformation, and recall over the corpus of human knowledge. Use them; I do, daily
- It becomes a license for AI dismissiveness — "not AGI" does not mean "not valuable," and the near-term value is enormous
- Timeline humility gets read as timeline certainty in the other direction — nobody knows; that's the point of calling it science

## Core Concept

LLMs can't be the whole answer. What they do is take all of human knowledge, put it in a giant blender, and train from there — and it's magical, it works really well, I'm amazed by it and use it constantly. But it's not the way a human brain works, and it fails at fundamental things that cats and dogs do, let alone small children: put it in a situation where it has to genuinely learn something new, from its own stream of experience, and the machinery isn't there. Humans and animals learn from a continuous stream of interactive experience — acting, observing consequences, carrying memory forward, forming a life. There are fundamental things about that loop that are just not understood yet. We don't have line of sight to the answers; we don't have systems that learn like a mouse, never mind a person. Everything I did before — games, rockets, VR — was engineering: hard, but with line of sight to the endpoint. This is science, finding knowledge nobody has, and that difference should discipline everyone's confidence about timelines, mine included.

The failure mode that hides this gap is simulation comfort. Classic RL is turn-based: the agent acts, the environment politely computes the consequence and hands back an observation and a reward — chess rules, essentially, and RL has been spectacular at that shape. Reality is not a turn-based game. The world keeps running while you think; take too long choosing an action and the environment has moved on; latency breaks the algorithms that condition on their own actions; observation is a noisy camera, not a state vector. Spectacular recent results lean on things like replay ratios of eight and models that take days of compute to generate hours of gameplay — interesting technically, and quite far from acting in the real world. So at Keen we forced honesty mechanically: a camera pointed at a real TV, a servo working a real joystick, an agent that must learn Atari in real time on modest hardware. It started learning in the morning and was mediocre by afternoon — and every inconvenience it surfaces is exactly the science the simulation lets you skip. When someone tells me robots will be doing everything in a couple of years, my test is: take your dancing robot, hand it a joystick and a game it has never seen, and watch. Those capabilities are nowhere close.

Held together, the two halves give you the calibrated position. Against the "it's already here" crowd: the gap between corpus-synthesis and learning-from-experience is fundamental, a half-dozen missing insights, not a scaling milestone — and my own numbers have stayed roughly stable for years: strong chance of signs of life by 2030, near-certain by mid-century, and I publicly disclaim my own likelihood of being the one to get there. Against the "it's all hype" crowd: the last decade was different in kind — perception went superhuman, and the tools are clearly among the ingredients. And on what it means: AI is going to change the world in some pretty significant ways, although not as much or as quickly as people believe. The inertia of the world's systems is enormous; ten years from now, daily life will look more familiar than the precipice-people expect. My most prosaic sketch of success is telling: universal remote employees — spin up artificial coworkers from the cloud like compute. Change-the-world-level, yes; and still banal enough that the world it changes remains recognizable. Calibration in both directions is the skill; the loudest voices are wrong in opposite ways.

## How to Apply

1. **Sort the task: blender or experience-stream?** Synthesis over existing human knowledge — writing, coding, answering, transforming — is LLM territory; expect superb results now. Learning a genuinely new task from interaction, online, with consequences — that's the unsolved side; treat any claim there as a research claim.

2. **Interrogate the demo's environment.** Simulated, turn-based, researcher-built, resettable? Then ask what survives contact with continuous time, latency, noise, and no resets. The sim-to-real gap is where AI claims go to die, and vendors know better than to show it to you.

3. **Apply the joystick test to robotics claims.** Not "can it perform the choreographed impressive thing" but "can it learn an arbitrary new task it's never seen, in the world, at the world's pace." The gap between those two is the actual distance to general robotics.

4. **Demand real-time, real-hardware evidence.** Claims of agent learning should survive the physical-Atari constraint: learning live, on plausible compute, while the environment keeps moving. Days-of-compute-per-hour-of-behavior is a lab result, not an agent.

5. **Plan products on the enormous-inertia model.** Build for AI as a powerful component inside mostly-familiar systems over the next decade — not for an imminent discontinuity. The value is real and large; the precipice is mostly narrative.

## Examples

**Situation:** A founder pitches that their agent product will "learn each customer's workflow like a new employee would," powered by an LLM with a memory layer.

**Application:** Sort it. The system will be excellent at everything blender-shaped: drafting from patterns, answering from documentation, transforming inputs it has seen the shape of. The new-employee claim — online learning of genuinely novel tasks from experience and feedback — is on the unsolved side; retrieval over a growing log is not a learning loop. Reframe the product around the strong half and stop promising the missing half.

**Illustrative result:** The demo-to-deployment gap that kills agent startups shrinks, because the promises now match what the machinery does. The blender half alone is usually a real business.

**Situation:** An investor asks whether an AGI lab's claim — "our approach reaches human-level intelligence within three years via scale" — should be believed.

**Application:** Test it against the science framing. Do they have line of sight, or a scaling extrapolation past the experience-learning gap? Ask what their system does when it must learn a new task from a stream of interactive experience in real time; ask what external, un-gameable evaluation they report on; check whether their benchmark is their own. Confidence plus a self-built benchmark plus no real-time learning story is the signature of the field's groupthink, not of line of sight.

**Illustrative result:** The claims sort quickly — most are strong narrow-AI programs wearing an AGI costume, worth funding on the narrow merits and priced accordingly. The rare honest "couple of insights missing, here's our decorrelated angle, here's our external eval" is what a real long-shot looks like.

## Anti-Patterns (tactical)

**Don't:** Extrapolate the last decade's perception breakthroughs linearly into consciousness, agency, and continual learning.
**Why:** The decade's wins — vision, speech, language synthesis — all fell to the same move: deep learning over massive static data. The missing pieces — learning online from experience, memory that constitutes a life, goals and planning in continuous time — are not further along the same axis; they're a different problem the blender move doesn't touch. Different problem, different (unknown) timeline. That's why it's science.

**Don't:** Ship "the agent learns and improves from experience" as a product promise on today's stacks.
**Why:** Customers will run the honest experiment you didn't: month three arrives, the system makes the same mistake it made in month one, and the promise is dead — taking your credibility with it. Say what's true: it retrieves, it patterns, it can be updated. The companies that survive the trough are the ones whose claims matched their machinery.
