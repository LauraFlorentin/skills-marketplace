# Dealflow Platform

An AI-agent-native real estate deal-flow platform: a daily, personalized feed of underwritten property deals (whole rentals, STR/Airbnb, fractional equity, hotel shares, tokenized, debt) across the US, Dubai, Mexico, and Bali — "we do the math, you decide." The platform aggregates and points to third-party offerings; it never transacts, takes custody, or gives individualized advice.

## Contents

- [STRATEGY-BLUEPRINT.md](./STRATEGY-BLUEPRINT.md) — the full global strategy and product blueprint, covering:
  - **Part 1** — the fractional/hotel investment landscape (Dubai, Bali, Mexico, Europe, global comparables)
  - **Part 2** — legal/regulatory guardrails (US publisher's exclusion, MiFID II, UAE, foreign-ownership rules)
  - **Part 3** — data availability by geography, which drives market phasing (Dubai → Mexico → Bali → Europe)
  - **Part 4** — daily deal-flow engine product design (Going / Morning Brew / Motley Fool templates)
  - **Part 5** — synthesized product blueprint, MVP scope, and phased recommendations

## Core decisions (from the blueprint)

1. **Build the aggregator, not the broker** — outbound links to third-party platforms only, subscription-first revenue.
2. **Launch phasing follows data quality, not deal supply:** Phase 1 Dubai (free DLD open data), Phase 2 Mexico, Phase 3 Bali, Europe deferred.
3. **Compliance posture:** stay inside the publisher's exclusion (Lowe v. SEC; Seeking Alpha 2024) — impersonal, filter-based content, no custody/discretion/transactions, prominent disclaimers, legal opinion letter before launch.
4. **MVP:** US + Dubai daily-email product (ingest → normalize → underwrite → score against user preference vector → "why this / why you / why now" → outbound link), ~6–10 weeks solo.

> Not investment advice. This repository contains product strategy and research material only.
