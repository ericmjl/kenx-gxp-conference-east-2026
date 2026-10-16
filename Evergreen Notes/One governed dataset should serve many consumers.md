---
title: "One governed dataset should serve many consumers"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Shelly LaPointe's data-foundation lecture at the KENX AI in GxP East 2026 conference ([[2026-09-15-1201-shelly-lapointe-data-foundation-for-ai-in-gxp]]), 2026-09-15.

## Silos make every AI pilot rebuild its plumbing

LIS, MES, and QMS each carry their own format, access model, and governance, and GxP environments are tuned to be inspection-ready rather than insight-ready ([[GxP systems are optimized to be inspection-ready, not insight-ready]]). The result is that each AI pilot builds its own non-reusable pipeline, and agentic AI multiplies the problem because every additional agent touching the data multiplies the traceability obligations.

## Build the estate once, validate it once, reuse it everywhere

Her reference architecture: sources feed an ingestion framework that normalizes, tags, and captures lineage; storage splits into raw, curated, and consumption zones beside a metadata catalog; role-based access control, encryption, and a GxP validation envelope wrap pipelines, storage, access, and every model and agent. One governed dataset then serves autonomous agents, training pipelines, compliance dashboards, and humans. [[Centralize evaluation when every AI pairing carries its own KPIs]] is the evaluation-estate version of the same reuse.

## ALCOA+ still governs; the enforcement surface changes

AI does not change the data-integrity requirements, only where they bite: audit trails, e-signatures, and human-understandable agent naming matter more, and "enduring" is the hardest attribute to keep as models keep changing. That naming requirement is why [[Autonomous agents need their own auditable identities in regulated systems]]. GAMP 5-style risk-based validation applied well cut validation cycle time about 35 percent.

## Related

- [[Data Foundations and Audit Trails MOC]]
- [[GxP systems are optimized to be inspection-ready, not insight-ready]]
- [[Autonomous agents need their own auditable identities in regulated systems]]
- [[Centralize evaluation when every AI pairing carries its own KPIs]]
