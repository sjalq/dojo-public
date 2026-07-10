---
triggers:
  - "user asks how open source, devtools, or infrastructure gets funded"
  - "user compares their indie project's output to corporate-backed competitors"
  - "user is choosing a business model for a developer tool or language"
  - "user asks why a big company gives away technology for free"
use_when:
  - "evaluating a technology by asking who pays for it and what that does to its design"
  - "planning sustainability for an independent tool, library, or platform"
  - "someone assumes free-and-corporate and free-and-indie are the same kind of free"
fails_when:
  - "applied as cynicism — funding shapes incentives, it does not make every corporate project bad or every indie project good"
  - "the project is a hobby on purpose — not everything needs a sustainability model"
related:
  - "platform-vs-productivity-languages.md"
  - "hard-parts-of-open-source.md"
  - "what-is-success.md"
  - "saying-no.md"
---

# The Economics of Programming Languages

## When to Use
- Choosing infrastructure: weighing a corporate-backed option against an independent one
- An independent builder is being compared (or comparing themselves) to teams of 10-30 funded engineers
- Designing the revenue model for a devtool, language, or platform
- Explaining why "just do what Rust/Go/Swift does" doesn't transfer to an unfunded project

## Fails When
- **Used as a purity test.** Corporate funding explains design tendencies (e.g., feature accretion for the biggest possible marketplace); it does not make the tools bad. Evan's own advice: "you can always look at a language and find something inspiring and cool about it."
- **The stakes don't warrant it.** A weekend project doesn't need a funding thesis.

## Core Concept

Evan Czaplicki's Strange Loop 2023 talk answers the question he wished someone had answered when he was a student: who pays for programming languages, and what does the money do to them? The headline discovery is **traffic acquisition costs** — "when Google pays to be default search in Safari and in Firefox... this is probably the largest flow of money into programming languages happening right now." Google pays Apple on the order of $15-20B a year and Mozilla ~$400M for default-search placement; his mental model is Google as an **internet landlord** collecting rent on digital real estate, with the search bar as the transportation network. Out of that rent flow come Chrome, V8, Android — and the languages and DevRel armies attached to them. "Corporate languages" are funded as complements: Swift sells iPhones, JavaScript keeps the marketplace running, Rust improved Firefox's market position, Go was built by the person who "made the machine that counts the money." Even the DevRel roles — evangelists, advocates, community managers — are purchased marketing and support: "programmers, we're not susceptible to marketing, we can't be persuaded of anything" is his dry joke about why nobody names it.

Against that, "the open source way" tells the independent author they will get all of this for free: enthusiasts arise and do the DevRel, contributors arise and do the compiler engineering. His response: "when Google does it, they pay those people to do those things. Why is it that I'm going to get those things for free?... Because we never talk about these huge flows of money and what they're getting us, we have the same expectations of what's going to happen in both these cases." The independent author is held to a funded project's output with no funding — and carries a structural disadvantage: they bear the cost of developing the language *and* a business, while any larger company that takes the freely given code bears only the business cost. Hence the **Jeff problem**: whatever service business you build on your own technology, someone bigger can run the same play harder. "It's not just Jeff [Bezos] — I can get Jeffed by anybody."

He then maps the independent funding options with their design incentives and career risks: **patronage** (his own path — full focus on the language, but "you have a job because it serves the purpose of a powerful person... they can just as easily say, actually not you"; when Prezi's needs changed, it ended regardless of his output: "your efforts and achievements aren't directly connected to your ability to pay the bills"); **consulting** (probably the most productive — Clojure, Elixir, Scala — usage correlates with clients, but clients compete for your time); **research grants** (great if the project is a research vehicle, no DevRel budget); **editor licenses** (Kotlin/JetBrains — works, but you must build a world-class editor first); **usage licenses** (clean alignment, unsolved switching-cost story); **hosting** (maximal Jeff exposure); **donations** (ties your income to public perception rather than usage). Funding also shapes *design*: in a corporate alliance the incentive is "just add it — if people don't like it they can not use it"; for an independent author, "why mess with simplicity" is a live option because the goals are the author's own.

His hard-won advice, stated as what he'd tell his younger self: "The open source way is for businesses. You can't come into it just wanting to do a good job; you have to figure out these other things." And concretely: had he known in 2015-16, he would have developed the consulting path alongside patronage — "try to find a business partner who can do these kinds of things... you're bringing reputation and incoming leads, but maybe you don't answer emails that good — okay, but we're partners, right?"

## How to Apply

1. **For any technology you depend on, trace the money.** Who pays the people who maintain it, and why? A platform-complement, a consultancy's flagship, a research vehicle, and one person's patronage arrangement are four different risk profiles wearing the same open-source license.
2. **Read design decisions through funding incentives.** Marketplace languages accrete features ("better a complex language than a business switching marketplaces"); independent tools can say no. Neither is wrong; know which you're buying (see platform-vs-productivity-languages.md).
3. **If you build independently, pick your funding model before you're desperate.** Rank the options by how directly doing a good job converts into staying alive. Consulting and licenses correlate income with usage; patronage and donations correlate it with someone's mood.
4. **Structure patronage defensively.** Ask: is doing a good job on the work deeply related to the patron's purposes? What changes at their next funding round? Making "the value of my output undeniable" is not a defense — Evan tried; the decision was never about his output.
5. **Assume the Jeff problem.** Before betting on a service moat, name every org bigger than you that could run your play with more people, and what — beyond effort — stops them.
6. **Take on a business partner rather than becoming half a businessperson.** The 50%-language/50%-business split loses to anyone who does one thing 60% of the time.

## Examples

**Situation:** A CTO must choose between a corporate-backed framework and a better-designed independent one.
**Application:** Trace both money flows. The corporate one persists as long as the platform strategy does; the independent one persists as long as its author's funding model does. Then ask the independent project the patronage questions: who pays, what are their purposes, what's the succession story? A great design with a fragile funding model is a real risk you can price — sometimes worth paying, but knowingly.
**Illustrative result:** The decision gets made on sustainability mechanics instead of GitHub stars and vibes.

**Situation:** A solo devtools founder plans to monetize with managed hosting.
**Application:** Jeff problem, stated plainly: the code is free, the hosting play is replicable by every larger cloud, and "I'll have the simpler UX" is what Evan believed before realizing "I can get Jeffed by anybody." Look harder at models where the paid thing is not commoditizable by scale — licenses tied to the tool's value, or the JetBrains move of a paid product beside the free core.

**Situation:** An indie maintainer is demoralized that their project ships slower than a corporate competitor.
**Application:** The comparison is with a team funded by billions in platform rent. The expectations are miscalibrated, not the effort. Either change the funding reality or change the scope and success definition (see what-is-success.md) — do not try to out-produce a DevRel budget with weekends.

## Anti-Patterns (tactical)

**Don't:** Build your sustainability plan on "if the project succeeds, money will follow."
**Why:** The open source way promises free DevRel and free engineers "arising from the users" — and when Google gets those things, it pays for them. Success in usage and success in income are connected only through a deliberately chosen mechanism; without one, more users just means more unpaid support (see hard-parts-of-open-source.md).

**Don't:** Accept patronage as if it were tenure.
**Why:** "If someone can look at you and say, you don't have to worry about food or shelter, you can work on this thing — they can just as easily say, actually, not you. That's power." Enjoy the focus it buys, keep gratitude (Evan does), and build the second leg before you need it.
