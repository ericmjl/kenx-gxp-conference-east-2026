---
title: "Local models trade capability for control"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Yari Fontebasso's local-LLM audit-trail investigation at the KENX AI in GxP East 2026 conference ([[2026-09-16-1612-local-llms-gxp-audit-trail-lecture]]), 2026-09-16.

## The trade, stated from evidence

One hundred thirteen experiments, five open-weight models, 4,898 synthetic audit-trail events, all run locally on a MacBook Pro through a scripted harness over the Ollama API. The local side buys control: frozen, fingerprintable weights and runtime, data residency, operator-owned evidence. The cloud side buys capability: on the same task, Claude caught four of four completeness problems against 37 to 43 false positives, while local RAG runs produced 102 to 455. Choosing is choosing your supplier dependency.

## The assurance structure that makes either defensible

A three-step assurance case: what ran, how it performed, how it stays controlled. A four-layer validation model: input and preparation, retrieval and RAG, model and inference runtime down to the Ollama version, and tools plus human review. A deterministic evaluation pipeline (regex scoring rather than LLM-judged) keeps the measurer out of the measured. The open strategic choices, named honestly: how human review complements rather than duplicates, the control-versus-capability call, and what counts as good enough.

## Related

- [[Data Foundations and Audit Trails MOC]]
- [[Absence problems are harder to detect than presence problems]]
- [[Regulators are becoming AI users themselves]]
