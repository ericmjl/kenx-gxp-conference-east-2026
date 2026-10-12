---
title: "Centralize evaluation when every AI pairing carries its own KPIs"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Eric Ma's vendor consultation at the KENX AI in GxP East 2026 conference ([[2026-09-16-1050-gxp-validation-platform-consultation]]), 2026-09-16.

## The problem Eric brought to the booth

Every LLM paired with an application carries distinct KPIs, and in most organizations the evals run in different places: one team's golden set lives in a notebook, another's in a vendor dashboard, a third's nowhere. The vendor platform's answer is one shape of centralization: AI entities defined with model cards, scheduled evaluations against golden datasets from the backend, token usage and KPI tracking, and continuous-monitoring frequency per entity.

## What centralization buys in a regulated setting

One place where an inspector (or a quality lead) can see what every AI touching GxP is measured against, when it was last measured, and what drifted. It is the same instinct as one governed dataset serving many consumers: build the evaluation estate once, run it continuously, and let each pairing register its metrics into the shared system instead of owning a private one.

## Related

- [[Strategy Scaling and Product MOC]]
- [[AI validation evidence has a shelf life]]
- [[Observability and evaluation answer different questions about an AI system]]
