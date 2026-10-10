---
triggers:
  - "legacy or partner APIs force foreign names and shapes into the domain"
  - "team speaks two languages: external DTO words and product words"
  - "user asks about anti-corruption layer, DTO-to-VO, or shielding the domain"
  - "snake_case, stringly enums, and flat transaction lists leak everywhere"
  - "parse validates shape but domain still thinks in someone else's model"
use_when:
  - "integrating legacy systems, third-party APIs, or other bounded contexts"
  - "protecting ubiquitous language inside your team (DDD)"
  - "mapping their types to our types after or with schema parse"
  - "thin (data map) or thick (data + behavior) boundary translation"
fails_when:
  - "ACL is a rename theater that still exposes legacy invariants and mixed lists"
  - "you skip ACL and let Products/transactions vocabulary infect core forever"
  - "ACL becomes a second entire app with no clear ownership or tests"
related:
  - "schema-at-the-boundary.md"
  - "product-and-union-types.md"
  - "smart-constructors.md"
  - "pipelines-and-composition.md"
  - "pure-and-total-functions.md"
---

# Anti-Corruption Layer (Typed)

## When to Use

- External systems use different words, shapes, and invariants than your team: snake_case ISO dates vs camelCase branded times; flat `transactions[]` vs credit vs payment; string `accountTypes` vs closed unions.
- Parse/schemas make data **trusted** but still **foreign**. You need **owned language** next.
- Multiple consumers copy legacy field names into new code "for speed," and Product/BA no longer recognize the model.
- You map DTO → Value Object in OOP terms and want the same discipline in TS/FP pipelines.
- Bidirectional talk with legacy: load their model, work in yours, save back through translation.

## Fails When

- You only rename `first_name` → `firstName` but still allow impossible legacy combinations inside the core. ACL should produce **your** products/unions, not a cosmetic twin of theirs.
- The "ACL" is an untested 5k-line dump of maps with business rules smuggled in both directions and no owner.
- Internal modules still import legacy types "just this once." Corruption resumes.
- Greenfield system with a single model and no external context: full ACL ceremony may be overkill; simple schema parse may suffice until a real second language appears.

## Core Concept

An **anti-corruption layer** is a deliberate translation at the edge of *your* system: their API shapes, names, and weird optional fields become *your* domain types. You do not let foreign mess leak into your core. Parse into your model once; map their errors into yours; keep your language.

*(DDD name: Eric Evans. Pattern matters more than the label.)*

Core idea in Jesse's framing:

- Parse / unknown / schemas: **untrusted data → trusted types**.
- ACL: **their types → our types** (sometimes the same Zod layer, sometimes a true domain boundary shielding legacy).

> An Anti-Corruption Layer turns someone else's model into your own.

OOP translation he maps for dual-skilled teams: converting **DTOs to Value Objects**.

Domain angle: **"We talk differently."** Shared language inside the team; translate at the edge. If legacy words infect the domain, you get communication bugs with Product and design bugs in code. Ubiquitous language is not sloganeering; it is which types appear in your core modules.

### Example mismatch

Legacy/partner:

- Python snake_case
- ISO date strings
- `products`, flat `transactions`, stringly `accountTypes`

Your domain:

- camelCase branded names
- POSIX time + timezone types
- `IndividualCustomer | WarehouseCustomer`
- `CreditTransaction | PaymentTransaction`
- `firstAccount` + `otherAccounts` (non-empty / primary thinking)

The ACL maps structure **and** meaning. String account types become unions. Flat lists become classified DUs. Optional noise drops. Invalid combos fail at the boundary, not in checkout.

### Thin vs thick ACL

**Thin ACL:** schema + map in a railway:

```ts
neverThrowPromise()
  .andThen(safeParseJSON)
  .andThen(legacySchema)
  .andThen(mapToCustomer)
```

Validate/parse foreign shape, then pure function to domain products/unions/opaques.

**Thick ACL:** modules that map **data and behavior** both ways:

```text
customerToLegacy |> legacyToJSON |> legacySave
legacyLoad |> legacyFromJSON |> legacyToCustomer
```

When the other system is not just a JSON shape but a set of operations you must not reimplement in corrupted form, the ACL owns the conversation.

### Relationship to schema and pure domain

- Schema often **implements** the inbound half of a thin ACL.
- ACL always **protects language and model**, not only runtime validity.
- After ACL success, domain stays pure and total on **your** types. No shotgun parsing, no legacy vocabulary in core switches.
- Outbound: map domain → legacy only in ACL modules. Core never builds snake_case payloads.

Making impossible states impossible (Feldman / Elm framing) applies: legacy allows states you refuse. Your unions simply cannot represent them; the map returns `Result` errors instead of smuggling junk inward.

## How to Apply

1. **Write the owned model first.** Products, unions, brands you wish you had. Do not start from their OpenAPI as destiny.

2. **Document their model separately.** DTO types can live in `legacy/` or `vendor/` packages. Do not use them outside ACL.

3. **Implement `mapIn: Their → Result<Ours, AclError>`** pure if possible. Unit test heavily; property-test round trips where bidirectional.

4. **Implement `mapOut` only if you write back.** Keep symmetry explicit; avoid hidden partial updates that corrupt either side.

5. **Compose with parse.** `unknown → TheirDto (schema) → Ours (ACL map)` or a schema that outputs Ours directly when reshape is simple. Prefer clear stages when maps are non-trivial.

6. **Ban legacy types in domain imports** via lint boundaries or package splits.

7. **Name errors in your language.** "Unknown account classification" not only "Zod issue at path accountTypes."

8. **Keep ACL boring.** Translation and anti-corruption, not a place to grow unrelated features. New business rules belong in domain after clean types exist.

9. **Teach the team the words.** PR review: "That is their word; use CustomerAccount here." Types enforce what culture starts.

## Examples

**Situation:** New service copies partner's `products` and `transactions` arrays into every module; engineers argue with Product who say "payments" and "credits."

**Application:** ACL maps to `PaymentTransaction | CreditTransaction` and `CatalogItem`. Domain services only see DUs. Partner payload types stay in `partner/acl.ts`.

**Illustrative result:** Code review and standup use the same nouns. Illegal flat mixing fails at map with a typed error.

---

**Situation:** Date/time bugs: partner ISO strings without zone treated as local in three services.

**Application:** ACL parses to branded `UtcInstant` + explicit `TimeZone` where needed. Domain math only on owned time types. Outbound formats ISO only in ACL.

**Illustrative result:** One conversion policy; no scattered `new Date(string)` in domain.

---

**Situation:** Legacy account type strings: `"PRIMARY"`, `"primary"`, `"1"`, and empty.

**Application:** Thin ACL normalizes and maps to `"Primary" | "Secondary" | "Authorized"` or fails. Domain exhaustive switches never see empty string.

**Illustrative result:** Exhaustiveness works; garbage enums die at the edge.

---

**Situation:** Must update legacy COBOL-via-HTTP API that needs their field order and codes while new app uses rich domain model.

**Application:** Thick ACL modules: domain command → legacy request builder → HTTP → legacy response → domain Result. Domain never imports legacy request types.

**Illustrative result:** Legacy quirks quarantined. When legacy dies, delete ACL package; domain remains.

## Anti-Patterns (tactical)

**Don't:** Let legacy vocabulary leak because "the API already named it."
**Why:** Evans' point is protection of the model. Shared team language in code reduces confusion and bad assumptions (Users purchasing when only CustomerAccounts should, etc.).

**Don't:** Treat ACL as optional polish after the feature ships with foreign types everywhere.
**Why:** Infection spreads faster than cleanup. Boundary map in the first integration PR.

**Don't:** Confuse "we used Zod" with "we have an ACL."
**Why:** Schema can validate their shape and still leave you speaking their language. ACL completes the job when names and concepts differ. Sometimes one schema does both; be honest which you need.

**Don't:** Put core business rules only in the map functions and skip domain types.
**Why:** Then the ACL becomes the hidden god module. Map to proper products/unions; implement rules on those.

**Don't:** Skip crediting Eric Evans / DDD when teaching "Anti-Corruption Layer" by name.
**Why:** Borrowed framework; attribution required. Jesse's contribution is typed TS practice beside Parse Don't Validate and ROP, not renaming DDD.

**Don't:** Demand everyone read the Blue Book cover-to-cover before a map function.
**Why:** "Their types in, our types out, pure map, tested" is enough to start. Deeper DDD helps multi-context orgs; it is not a gate to stop snake_case from entering your core.
