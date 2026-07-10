---
triggers:
  - "user asks what to build next or how to judge product decisions"
  - "team is polishing elegance while users get little benefit"
  - "user asks about pricing, cost-effectiveness, or accessibility of a product"
  - "debate about premium versus mass-market positioning"
use_when:
  - "prioritizing product work by what actually reaches users"
  - "an engineering-driven team needs a moral frame for product decisions"
  - "choosing between the impressive version and the affordable, available version"
fails_when:
  - "used to justify shipping junk fast — value delivered includes quality experienced, not just features listed"
  - "long-horizon research phases where user value is deliberately deferred — judge those by learning rate instead"
related:
  - "focus-as-subtraction.md"
  - "latency-as-the-metric.md"
  - "org-efficiency.md"
  - "expected-value-career-bets.md"
---

# Give the User a Big Pile of Value

## When to Use
- Deciding between product directions, features, or platforms — anything where "what should we build?" is live
- A team measures itself by internal pride (architecture, elegance, demo applause) rather than delivered benefit
- Pricing and packaging decisions where margin fights reach
- Reviewing a roadmap that optimizes for the press release instead of the daily user

## Fails When
- "Value" gets redefined as feature count — a pile of shipped-but-broken capabilities is a pile of cost, not value
- The work is explicitly pre-product research, where forcing near-term user value takes the first billion-dollar off-ramp and abandons the mission
- You serve the loudest users' requests instead of the value integral across all users — enthusiast forums are not the market

## Core Concept

The frame I used for every VR decision: total value delivered to users, against everything it costs them — money, setup friction, comfort, time. Not how impressive the technology is; how big the pile of value is once it's multiplied across the people who actually get it. That's why I fought for years for mobile, standalone, cost-effective headsets when the prestige direction was ever-more-powerful tethered rigs. A cheaper, more convenient device that millions actually use delivers a vastly bigger pile of value than a technically superior one that stays in enthusiasts' dens. When I left Meta I could write, despite every complaint: millions of people are still getting value out of it. We have a good product. It is successful, and successful products make the world a better place. That last sentence isn't marketing — it's the moral claim that makes product engineering worth doing seriously.

The equation disciplines you in both directions. On the benefit side, value is what users experience, not what you shipped: a feature nobody finds, a mode that stutters, an app that takes ninety seconds to get into — these count at their experienced value, near zero. That's why the unglamorous work — load times, comfort, reliability, one less menu — often beats the flagship feature; friction multiplies against every session of every user, and the value equation makes visible how much of your "delivered" value users never receive. On the cost side, count everything the user pays: price, hardware they need, learning curve, physical discomfort, trust. Engineers systematically underweight these because we don't pay them ourselves — we have the dev kit, the tolerance, the motivation. The user's costs are as real as your benefits, and halving their cost doubles the pile just as surely as doubling your benefit.

The multiplication is what settles the taste-versus-numbers argument. Is value measurable? Imperfectly — but you can compare honestly: users reached times benefit per user times sessions, against cost. A niche feature for a hundred enthusiasts loses to a friction fix for everyone, nearly every time, and the equation says so out loud even when internal politics wants the flagship. The same multiplication is why I kept pushing on efficiency inside Meta: every wasted person-year is user value that never got created. And the closing line of my departure memo was the other half of the frame — fill your products with "give a damn." The equation tells you where the value is; caring is what makes you actually chase the last annoying seconds out of a loading screen when no metric forced you to.

## How to Apply

1. **Write the equation for each candidate.** Roughly: (users who'll actually get it) × (real benefit per use) × (frequency), minus every user-side cost — price, friction, learning, discomfort. Crude numbers are fine; the exercise usually reorders the roadmap by itself.

2. **Count experienced value, not shipped value.** Instrument what users actually reach and feel. A shipped feature with single-digit discovery is a rounding error wearing a press release.

3. **Attack the denominators.** Price, install friction, time-to-value, comfort. These multiply across your whole user base, which is why cost-and-friction work so often dominates feature work in the equation — and why it's chronically underprioritized by teams who find it boring.

4. **Favor the version most people can have.** When choosing between the excellent-for-few and the good-for-many, do the multiplication before your pride does it for you. The prestige version usually loses by an order of magnitude.

5. **Audit where your engineering month goes.** Rank current projects by pile-of-value per unit effort. The bottom of that list is usually defended by internal enthusiasm — someone's architecture, someone's demo — rather than by any user. Cut from the bottom.

## Examples

**Situation:** A team is choosing between a photorealistic rendering upgrade (the demo everyone wants to build) and cutting app start time from 40 seconds to 5.

**Application:** Run the multiplication. The rendering upgrade delivers benefit in showcase moments to the subset with high-end hardware. The start-time fix pays every user, every session, forever — and probably changes session frequency itself, because a 40-second toll gate changes whether people bother. This was the recurring VR argument, and the friction side kept winning on the numbers even though nobody ever applauded a loading screen at a keynote.

**Illustrative result:** The unglamorous fix moves usage in a way the flagship wouldn't have, and the flagship gets rebuilt later on top of a product more people actually open.

**Situation:** A founder is pricing their developer tool at a premium "because it's worth it," reaching a small elite happily and leaving most of the addressable base out.

**Application:** The margin-per-user frame and the pile-of-value frame disagree; make the disagreement explicit. Total value (and, usually, total long-run business) is users × net benefit. Price is a user-side cost you fully control — the cheapest denominator you'll ever attack. Model the lower price against the larger reached base before declaring premium the answer; ecosystems and standards go to whatever most people can afford to adopt.

**Illustrative result:** The equation, not ideology, makes the call — sometimes premium genuinely wins on the math. But the founder now decides with the multiplication visible, instead of letting pride in the product masquerade as strategy.

## Anti-Patterns (tactical)

**Don't:** Judge product decisions by the demo response of insiders and enthusiasts.
**Why:** The keynote audience has the hardware, the patience, and the motivation your median user lacks — their applause measures impressiveness, and impressiveness is on the wrong side of nothing in the equation. Every cycle spent on demo-value that doesn't survive contact with a tired user on old hardware is value that exists only inside the building.

**Don't:** Ship the pile of features and call it a pile of value.
**Why:** Features are cost until users experience benefit from them. A roadmap that measures itself in launches accumulates surface area — more settings, more modes, more bugs — while the experienced product gets worse. The equation counts what reaches the user's actual life; when adding starts subtracting there, stop adding and start fixing, with some give-a-damn about the details nobody metrics.
