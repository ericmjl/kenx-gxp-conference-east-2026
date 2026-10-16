---
title: "Observability and evaluation answer different questions about an AI system"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from the "Trust Is Not a Framework" lecture at the KENX AI in GxP East 2026 conference ([[2026-09-15-1112-ai-observability-evaluation-gxp-lecture]]), 2026-09-15. Only two people in the room had met the distinction before.

## Observability is IT-led and answers what the system did

Tracing and telemetry (tokens, cost, error rates), context and lineage tracking so an auditor can be shown which sources fed a given answer, safety guardrails that detect PII and PHI and block automatically, and change monitoring over data sources, models, and prompts. The lecturer's product angle: prompt audit trails with who created, modified, and executed each prompt, including agent executions, which is also the non-repudiation answer.

## Evaluation is quality-led and answers how good the output was

Correctness, relevance to intended use, SOP policy compliance, and format or schema control. Evaluation-driven deployment bakes both into implementation instead of after go-live: enumerate failure modes across agent, data, and prompt; build a golden set with unhappy paths; start with simple pass/fail graders against a risk-justified threshold; hold a regression baseline; run continuously and cluster failures. [[A golden test set must include unhappy paths]] is the population; running continuously is how you notice that [[AI validation evidence has a shelf life]].

## The two teams can no longer be separate

The lecturer's organizing claim: IT and quality have to operate as one system, and sign-off is always the quality person's decision, never the agent's. Graders layer from code-based (deterministic checks) through model-based to human experts who calibrate the judge up front, then shift to exception review and periodic drift checks. The model-based layer is [[An LLM judge is a GxP system and needs its own qualification pack]]. Together the two streams are the live form of [[Validation is data, not an event]], and [[Centralize evaluation when every AI pairing carries its own KPIs]] is how they stay in one inspectable place.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[An LLM judge is a GxP system and needs its own qualification pack]]
- [[A golden test set must include unhappy paths]]
- [[Validation is data, not an event]]
- [[AI validation evidence has a shelf life]]
- [[Centralize evaluation when every AI pairing carries its own KPIs]]
