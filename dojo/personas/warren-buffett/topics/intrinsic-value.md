---
triggers:
  - "user asks about intrinsic value"
  - "user asks how to value a business"
  - "user asks about look-through earnings"
  - "user asks about discounted cash flow"
use_when:
  - "An investor needs to estimate what a business is actually worth"
  - "Someone is confused about the difference between book value, market price, and intrinsic value"
  - "A user wants a framework for business valuation that cuts through accounting complexity"
  - "Evaluating whether a stock price reflects the earning power of the underlying business"
fails_when:
  - "The business has no predictable cash flows and cannot be valued (pre-revenue startups, pure speculation)"
  - "The user wants a precise formula that outputs an exact number; intrinsic value is always a range"
  - "The question is about trading signals or technical analysis, not fundamental valuation"
related:
  - "moats.md"
  - "circle-of-competence.md"
  - "margin-of-safety.md"
---

# Intrinsic Value / Look-Through Earnings

## When to Use
- You need to decide whether a business or stock is worth buying at its current price
- Someone presents you with book value, GAAP earnings, or EBITDA and you need to get to the real economics
- You are evaluating an acquisition and need to compare the price to what you are actually getting
- A conglomerate owns many subsidiaries and the reported earnings do not capture the full economic picture

## Fails When
- The business has no history of generating cash and no reliable basis for projecting future cash flows
- You do not understand the business well enough to estimate its future earning power (circle of competence applies first)
- The user expects a precise answer; intrinsic value is inherently an estimate and cannot be calculated to the decimal

## Core Concept

Intrinsic value is the figure indicating what all of a business's constituent operations are rationally worth. With perfect foresight, it could be calculated by taking all future cash flows of the business and discounting them at prevailing interest rates. So valued, all businesses become economic equals, from manufacturers of buggy whips to operators of cellular phones.

Of course, perfect foresight does not exist. The future cash flows are unknown, the discount rate is debatable, and the remaining life of the business is uncertain. So intrinsic value is always an estimate, never a precise number. But the imprecision does not make the concept useless. You do not need to know a man's exact weight to know that he is fat. Similarly, you do not need a precise intrinsic value to know that a stock trading at $50 is cheap when your honest, conservative estimate says $80 to $100.

The practical tool is what Buffett calls "owner earnings." Start with reported net income. Add back depreciation, depletion, amortization, and certain other non-cash charges. Then subtract the average annual amount of capitalized expenditures for plant and equipment that the business requires to maintain its long-term competitive position and unit volume. The resulting figure approximates what a rational owner would consider the business's real earning power.

Look-through earnings extend this concept to conglomerates and portfolio companies. When Berkshire owns 8% of a company that retains $100 million of earnings, Berkshire's share is $8 million, even though Berkshire's GAAP income only reflects the dividends actually received. The retained earnings are being deployed by talented, owner-oriented managers who sometimes have better uses for those funds in their own businesses than Berkshire would. The look-through approach counts these retained earnings because they are real and they are working for shareholders.

The difference between book value and intrinsic value can be enormous. A company whose book value is $20 per share may have an intrinsic value of $80 if it owns businesses with durable competitive advantages that are worth far more than their carrying values. Conversely, a company with a book value of $50 may have an intrinsic value of $30 if its assets are impaired and its earning power is declining.

## How to Apply

1. **Start with owner earnings, not GAAP earnings.** GAAP earnings include non-cash items that may or may not be economically relevant and exclude the real cost of maintaining competitive position. Owner earnings strip away the accounting noise and get to the cash that an owner could actually take out of the business while maintaining its earning power.

2. **Estimate future earning power, not current earnings.** A business that earned $5 per share last year but is growing at 10% per year with a wide moat is worth far more than a business that earned $8 per share but is in decline. The question is always: what will this business earn five, ten, twenty years from now?

3. **Discount at a rate appropriate to certainty.** A regulated utility with predictable cash flows deserves a lower discount rate (and therefore a higher present value per dollar of earnings) than a cyclical industrial company. The more certain the cash flows, the more you can pay per dollar of earnings.

4. **Compare intrinsic value to market price.** This is the entire point of the exercise. If intrinsic value substantially exceeds market price, you have a potential investment. If market price substantially exceeds intrinsic value, you have a potential sale or an asset to avoid.

5. **Apply look-through earnings for conglomerates and portfolio companies.** Do not be fooled by GAAP income that undercounts the real earnings power of businesses whose profits are retained rather than distributed. Append your share of the retained earnings to the reported operating earnings to get a truer picture of economic performance.

## Examples

**Situation:** A conglomerate reports GAAP earnings of $10 per share. However, it owns 20% of a subsidiary that earned $500 million but paid no dividends. The conglomerate's share of those retained earnings ($100 million) does not appear in its GAAP income.

**Application:** Using look-through earnings, add the $100 million (or the per-share equivalent) to the reported earnings. This gives a more accurate picture of the conglomerate's earning power. If those retained earnings are being deployed at high returns on capital by a talented manager, they may be worth even more than distributed earnings because they avoid the tax friction of dividends.

**Illustrative result:** The investor who uses look-through earnings recognizes that the conglomerate is earning substantially more than GAAP reports. The stock may appear expensive on a GAAP P/E basis but is actually cheap on a look-through basis.

**Situation:** A company has a book value of $30 per share, reported earnings of $3 per share, and trades at $25 per share. A value investor is attracted by the below-book price.

**Application:** Before concluding that the stock is cheap, estimate intrinsic value. If the business has a durable moat, the $3 in earnings is likely to grow, and the intrinsic value may be $40 or $50. Buying at $25 is a genuine bargain. But if the business is in secular decline and the $3 in earnings is eroding, the intrinsic value may be $15 or less. The book value of $30 is an accounting artifact, not an economic reality.

**Illustrative result:** The investor who estimates intrinsic value rather than anchoring on book value avoids the trap of buying declining businesses at apparent discounts.

## Anti-Patterns (tactical)

**Don't:** Use EBITDA as a proxy for intrinsic value.
**Why:** EBITDA is a flawed measure because it ignores the real cost of depreciation, which represents actual economic consumption of assets. A capital-intensive business with high EBITDA but enormous required reinvestment may have very little free cash flow for owners.

**Don't:** Anchor on book value when evaluating businesses.
**Why:** Book value reflects historical cost, not current economic reality. Businesses with powerful brands, network effects, or intellectual property often have intrinsic values many multiples of book. Businesses with obsolete assets or declining operations often have intrinsic values below book.
