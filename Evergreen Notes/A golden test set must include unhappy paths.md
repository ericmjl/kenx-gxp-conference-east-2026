---
title: "A golden test set must include unhappy paths"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from the "Trust Is Not a Framework" lecture at the KENX AI in GxP East 2026 conference ([[2026-09-15-1112-ai-observability-evaluation-gxp-lecture]]), 2026-09-15.

## Systems trained on happy paths keep answering happy paths

A complaint-handling system evaluated only on typical complaints keeps classifying atypical ones typically. The lecture's example: a death reported days after the initial ticket changes whether the case should have been flagged reportable, and a system that saw only clean cases answers the dirty one confidently. The judge catches silent failures only if the test set contains them.

## What unhappy paths look like in practice

Known-absent items that probe hallucination, distractor questions from adjacent domains, follow-up questions that depend on prior context, and boundary cases at the edge of the intended use. In the acceptance-criteria lecture the same shape appears: close to a hundred labeled cases including roughly nine drug-versus-device distractors and known-absent items, which caught eight hallucination failures before tuning.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
- [[Observability and evaluation answer different questions about an AI system]]
