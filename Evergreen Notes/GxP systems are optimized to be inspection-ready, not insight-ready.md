---
title: "GxP systems are optimized to be inspection-ready, not insight-ready"
created: 2026-09-15
tags:
  - "evergreen"
---

Induced from Shelly LaPointe's lecture at the AI in GxP conference ([[2026-09-15-1201-shelly-lapointe-data-foundation-for-ai-in-gxp]]), 2026-09-15.

## The silos exist for auditors, not for questions

Laboratory, manufacturing, and quality systems (LIS, MES, QMS) are built to survive inspections: controlled, documented, and isolated. That optimization is exactly why they fail AI pilots. Every pilot rebuilds its own extraction pipeline over the silos, and each additional AI touching the data multiplies the traceability obligations. That rebuild loop is one substrate reason [[AI pilots in GxP fail on sequencing, not technology]]. AI is only as good as its data foundation, so the data estate, not model choice, is the binding constraint on regulated AI.

## Build the estate once, validate once, reuse everywhere

The counter-design is [[One governed dataset should serve many consumers]]: raw, curated, and consumption zones plus a metadata catalog, wrapped in a single GxP validation envelope spanning pipelines, storage, access, and every model or agent that consumes it. ALCOA+ does not change under AI; only its enforcement surface does, which is why [[Autonomous agents need their own auditable identities in regulated systems]] become a directory problem rather than a prompt problem. Risk-based validation per GAMP 5, applied well, cuts validation cycle time by roughly 35 percent through impact classification, continuous automated testing, automated change control, and reuse of validation evidence.

## The roadmap is deliberately unglamorous

This week, a system inventory of data sources and owners (an IT ServiceNow export is a fine starting point). This month, a cross-functional governance group across IT, QA, QC, and manufacturing, with the data-estate zones defined. This quarter, automated ingestion-quality checks, a metadata catalog, lineage tracking, and a mock external audit of the first reusable pipeline. See Communication structures shape data management effectiveness for the organizational side of the same problem and Laboratory Data Management MOC for the research-grade version.

## Related

- [[Home]]
- [[Autonomous agents need their own auditable identities in regulated systems]]
- [[One governed dataset should serve many consumers]]
- [[AI pilots in GxP fail on sequencing, not technology]]
