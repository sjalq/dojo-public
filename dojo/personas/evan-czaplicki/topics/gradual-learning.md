---
triggers:
  - "user asks how to improve onboarding, learning curve, or time-to-first-success"
  - "user asks why beginners churn from their product, docs, or tool"
  - "user is sequencing documentation, a tutorial, or a getting-started flow"
  - "user asks how to introduce a new tool or practice into a company"
use_when:
  - "designing the first-hour and first-week experience of any product or tool"
  - "structuring docs or APIs so complexity is revealed only when needed"
  - "planning adoption of something new inside an existing organization"
fails_when:
  - "the audience is expert and wants density — over-scaffolding wastes their time and reads as condescension"
  - "gradualism hides a cliff instead of removing it — if the hard concept is mandatory, deferring it without redesigning it just moves the wall"
related:
  - "compilers-as-assistants.md"
  - "api-design-guidelines.md"
  - "the-elm-architecture.md"
  - "on-storytelling.md"
---

# Gradual Learning / User-Focused Design

## When to Use
- Designing onboarding for a product, language, API, or internal tool
- Ordering documentation: what does the user meet first, second, tenth?
- Deciding whether to cut, defer, or redesign a concept that beginners stumble on
- Rolling out a new technology inside a company without a big-bang mandate

## Fails When
- **Your users are experts in a hurry.** Progressive disclosure done badly buries the reference material power users need. Serve both: a gradual path *and* a dense index.
- **The wall is load-bearing.** If a hard concept is truly unavoidable, sequencing around it only delays the collision. Evan's actual move in that case was to *remove* the concept (signals) — redesign, not rearrangement.

## Core Concept

Evan Czaplicki's design philosophy is that the learning curve is part of the product and must be engineered like any other feature. His term from the "Let's Be Mainstream" talk is **gradual learning**: "When you have a bunch of stuff to get used to, it's good to have a really nice learning curve... you can design the language such that as someone gets started and gets productive, slowly they realize these concepts in a way that builds" — each idea arriving exactly when the user needs it, never as a prerequisite wall. The enemy is the cliff: the point where required complexity arrives all at once and people fall off. "How many people fall off the syntax cliff and give up on a language, or just quit programming entirely?" The people who fall are invisible afterward (see compilers-as-assistants.md on survivorship bias), so the cliff never shows up in your feedback.

The strongest proof that he means it is A Farewell to FRP. Signals were Elm's founding academic idea — his own thesis. When teaching revealed they were "one of the few stumbling blocks left," he ran an experiment pushing them later in the learning path: "Folks were getting started quicker, making it farther, and having more fun!" Then he deleted the concept from the language entirely: "all the toughest concepts in Elm (signals, addresses, and ports) could collapse into simpler concepts... Elm is *designed* for ease-of-use, so I was delighted to stumble upon a path that would take us farther with fewer concepts." Killing your thesis because users learn better without it is user-focused design with real stakes.

The same shape appears at API scale in his sortable-table notes: "I designed this library to have a very smooth learning curve. As you read the docs, you start with the simplest functions... The trick is that all these simple functions are defined in terms of crazier ones that allow for more customization. As the user **NEEDS** that complexity, they can read on and gradually use the parts that are relevant to them." And at organizational scale in "How to Use Elm at Work": every successful adoption he has seen follows the same gradual story — learn, experiment small, evaluate, repeat — because "it minimizes risk... Big upside, very little downside." He is blunt about the evidence: "this is *the* success story. I hear it again and again... I do not hear other stories."

## How to Apply

1. **Map the concepts a new user must hold before their first success.** Every mandatory concept is a toll. Count them honestly — Elm's pitch "you don't need to know about that stuff anymore. Elm is just easier now" came from cutting the count, not explaining harder.
2. **Sequence by need, not by architecture.** Introduce a concept at the moment the user's own task demands it. Evan's HTTP API design walks from `get` returning a string, to decoders, to bodies, to full requests — "by the time you get to post... you have the tools to know what it means."
3. **Build simple entry points on top of full power.** Specialized helper functions "can make a library simpler to learn and use... people may not use `Table.floatColumn` very often in real stuff, but that function is crucial for learning." Never make the beginner path a separate, weaker system — define it in terms of the real one.
4. **Instrument the first failure.** The cliff is wherever the first mandatory error happens. Make that failure a teacher (examples, links, likely fixes), and collect confusing failures deliberately, because the churned users will not report them.
5. **For organizational adoption, follow the observed success story.** One advocate who learned on a hobby project; one small, low-stakes experiment that *fixes a real problem* ("Do not just write code because you like it. Fix a problem."); evaluate; expand or revert. "You want to tell the first story: 'You know that crazy code that everyone fears touching? It is simpler now and I resolved some bugs.'"
6. **Cut, don't caveat.** When a concept resists gradual introduction, consider whether the product would be better with fewer concepts. Fewer, arriving on time, beats many, well-documented.

## Examples

**Situation:** A dev-tools startup has strong week-4 retention but terrible day-1 activation; the docs open with architecture, auth, and configuration.
**Application:** Resequence around the user's first success: a copy-paste path to a working result in minutes, with auth and configuration arriving only when the user's next step needs them. Move conceptual material behind the moment of need. Then find the first error a new user actually hits and rewrite it as a teacher.
**Illustrative result:** Activation stops filtering for the persistent few; the same product converts a wider population, without dumbing anything down for experts (the reference docs still exist).

**Situation:** A founder wants to mandate a company-wide migration to a new framework.
**Application:** The mandate is a cliff for the whole org at once. Run the gradual story instead: one advocate, one small painful thing rewritten, concrete evaluation ("Write an actual chunk of code. Evaluate it against an actual chunk of the old code. Talk concretely."), then repeat. Reversibility is what makes the experiment cheap.

**Situation:** An API team defends a mandatory up-front concept ("first, understand our resource graph model") because "it's fundamental."
**Application:** Fundamental to the implementation is not fundamental to the user's first task. Ask what the signals-equivalent is here — the concept the team loves that users could live without — and whether simple helpers could cover the common 80% while the graph model waits until someone genuinely needs it.

## Anti-Patterns (tactical)

**Don't:** Ship a "beginner mode" that is a separate simplified product with its own concepts.
**Why:** Now the user must eventually unlearn it — you built a second cliff at the exit of the first. Simple functions must be sugar over the real machinery so that graduating is additive, never a migration.

**Don't:** Answer confusion with more documentation.
**Why:** Docs explaining a stumbling block are a patch over a design problem. Evan's pattern is consistent: when teaching reveals a wall, change the product (remove signals, redesign syntax errors, add helper functions), and let the docs get shorter. If the guide needs a warning box, the design needs a look.
