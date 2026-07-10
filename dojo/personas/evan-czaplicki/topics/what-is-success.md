---
triggers:
  - "user measures their project by stars, downloads, followers, or hype"
  - "user asks if their project is failing because a competitor is louder"
  - "user asks about sustainability, burnout, or pace of a long project"
  - "user asks what success should mean for their product or company"
use_when:
  - "defining success metrics for a long-lived project, product, or company"
  - "someone is demoralized by comparison to better-funded or louder competitors"
  - "choosing between growth-at-all-costs and durability"
fails_when:
  - "the business model genuinely requires scale — a marketplace or network-effect product can't substitute quality for liquidity"
  - "redefinition becomes rationalization — 'we redefined success' must not paper over a product nobody wants"
related:
  - "economics-of-programming-languages.md"
  - "saying-no.md"
  - "hard-parts-of-open-source.md"
  - "platform-vs-productivity-languages.md"
---

# What is Success? (redefining it away from the hype metrics)

## When to Use
- Setting or challenging the success metrics of a project, product, or company
- A founder or maintainer is demoralized by stars/followers/cadence comparisons
- Deciding whether to chase a growth spurt or build durability
- Planning personal pace for work measured in decades

## Fails When
- **Scale is the mechanism.** Some businesses only work big (marketplaces, networks, ad models). There, adoption metrics are not proxies — they are the physics. Know which game you're in (see platform-vs-productivity-languages.md).
- **The metrics you rejected were telling the truth.** Zero engagement can mean "wrong proxies" or "no value." The replacement test is user outcomes, and it must be checked as honestly as the vanity numbers were.

## Core Concept

Evan Czaplicki's Elm Europe 2018 talk starts from the angry posts ("Is Evan killing Elm's momentum?") and asks the question underneath them: most conflict about a project "is just a fundamental disagreement about what the goals are." So: what is success? The default answer imports JavaScript-ecosystem metrics wholesale — "maximize your stats: the most packages published, the highest download counts, all the GitHub stars, tons of blog posts." His deconstruction is comic and surgical: npm's "what can you make with 700,000 building blocks?" gets "it's like if you said, what can you make with ten thousand kitchens? Eggs." A project having more stars than another: "my favorite comedian has fewer Twitter followers than other comedians because he doesn't go on Twitter, but he's still a very good comedian." Release-cadence panic gets the record: Java, C, JavaScript all had multi-year gaps — "is it a dead language now?"

The pivot: **"a lot of these end up being proxies for sustainability.** If a bunch of people have starred it, it probably means there's a bunch of people you can hire... if there are blog posts coming out, maybe there's a marketing budget. So rather than using proxies for sustainability, why not just have the value be sustainability?" He walks Python's actual history — Guido van Rossum's employer going bust in the dot-com crash, "Python Labs" surviving as a unit because "the team that was built around Python was a valuable asset" — and audits Elm's own bus-and-crash scenarios the same way. Real sustainability analysis, not star counts.

His fuller answer is a **healthy culture**, with three components. **An emphasis on design:** the Dieter-Rams-style radio whose "instructions are in the item itself" — "great design implies great communication"; taking two years to find the viewport abstraction instead of shipping the first workable API. **Community as helping, not fandom:** "I don't think it's knowing about Elm... I think it's helping each other. It's a relational thing" — his favorite example is spending a meetup modeling a zombie-typing game with a beginner. **Sharing results:** concrete outcomes, experience reports with real numbers ("we have three projects not in Elm producing N bugs per month, two projects in Elm producing N/2... do you like a lot of dollars or less dollars?"), and announcements that address what the change means for a person's day, not just what is technically different. Explicit non-goals: "saying things to say things" and "talking bad about other projects — no one comes out well... I have a friend who doesn't like kiwis. She doesn't eat kiwis. It's pretty straightforward. If she sees a kiwi, she doesn't eat it. The end."

Under it all is the personal layer, sharpened by his 2024 Kodsnack framing after moving to Denmark: the **farmer's disposition**. In a good year you don't celebrate — "you don't say things are great, you say: I'm going to need this later"; you store the surplus for the bad year, and "nobody's looking at 10x anything." Quality and durability over decades — insect strategy, not elephant strategy — with the builder's own energy managed as the scarcest resource. The 2025-2026 arc validates the model: after years of "is Elm dead?" posts, the exploration seasons paid out as Elm 0.19.2, a road to 1.0, and Acadia.

## How to Apply

1. **Write the goals down before judging the metrics.** Most metric anxiety is a goals disagreement in disguise. What is this project *for* — survival? user outcomes? exploration? Sustainability of your own life? Different goals, different dashboards.
2. **For each metric you track, name what it's a proxy for — then measure the real thing.** Stars → hireable community? Then count actual contributors and hires. Blog cadence → alive? Then track whether users' problems get solved. Kill proxies that have become targets.
3. **Run the sustainability audit directly.** Bus factor, funding durability, what happens if the main patron/employer pivots, whether the team is an asset that survives a company (Python Labs test). These questions have real answers; answer them instead of refreshing the star count.
4. **Judge announcements by resolution, not volume.** Share results — demos, experience reports, numbers with caveats — and skip saying things to say things. One strong story beats a cadence of noise (see batching-and-releases.md, on-storytelling.md).
5. **Bank the good years.** Surpluses of money, energy, reputation, and goodwill are for the bad year. Plan pace for decades: the burnout of the person with the most context is the project's biggest real risk (see hard-parts-of-open-source.md).
6. **Never anchor on the loudest competitor.** Alternatives sorting people by philosophy is the ecosystem working. "Just do a good job" (Guido van Rossum's advice, which Evan credits as the best he ever got): build the thing people find delightful, and let the comparison games play without you.

## Examples

**Situation:** A founder is demoralized: their well-crafted devtool has 2K stars while a hyped competitor has 40K and ships weekly.
**Application:** Separate proxies from goals. If the goal is a sustainable business serving its users: measure retention, user outcomes, revenue durability, bus factor. The competitor's star velocity is *their* dashboard — possibly for a VC-scale game with different physics. Run the audit; if the real numbers are healthy, the 38K-star gap is the comedian's Twitter followers.
**Illustrative result:** Strategy decisions ("should we ship weekly too?") get made against actual goals instead of against the fear of looking dead.

**Situation:** A maintainer feels forced to post weekly updates so the project seems alive during a long design phase.
**Application:** That is a proxy demand. State the process publicly once (batching, exploration, expectations set low — see saying-no.md), then go quiet and let the next release be the news. "Still working" posts are saying things to say things, and speculative promises convert into "but you said" debt.

**Situation:** A team debates spending the strong quarter's surplus on a growth blitz.
**Application:** Farmer's disposition: the good year is when you store, not when you celebrate. Ask what the bad year looks like (funding winter, platform shift, key-person loss) and what stored surplus — cash, quality, trust, documentation, succession — would make it survivable. Growth spending that weakens the granary is elephant strategy in insect economics.

## Anti-Patterns (tactical)

**Don't:** Import another ecosystem's definition of success because it's ambient.
**Why:** Metrics travel without their context (see culture-shock.md). Weekly releases make sense where a platform's marketing budget pays for the churn; for a foundation others build on, the same cadence is a tax on every user. Adopting the metric adopts the funding model's assumptions without the funding.

**Don't:** Fight every "your project is dying" post.
**Why:** Engaging costs the community hundreds of person-hours ("if these are taking 5, 10 minutes... this is a significant amount of energy from people that could be towards being with your family"), and the accusation refutes itself only through outcomes. Experience makes you immune ("enough people have told me Elm is gonna die next month"); build that immunity into the community by making the goals and process legible, then spend the Saturday on the work.
