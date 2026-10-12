---
title: "AI validation evidence has a shelf life"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Abhishek Bachchan's acceptance-criteria lecture at the KENX AI in GxP East 2026 conference ([[2026-09-15-1426-abhishek-ai-acceptance-criteria-gxp-lecture]]), 2026-09-15.

## Triggers that expire a validated state

A model or provider change, a prompt tweak, corpus growth, retrieval or chunking parameter changes, a context-of-use shift, or simply elapsed time. Any one of them forces re-measurement, which makes validation a continuous loop rather than the one-pass V model that assumes a validated state persists without action.

## Evidence is a live database, not a PDF

The inspection-ready package is a dashboard: labeled test sets with rationales, dated run records, per-call provenance (requested versus served model, prompt hashes, token counts), grounding exception logs, stored outputs, human dispositions, threshold rationale, and requalification records. Screenshots age; queries against the record do not.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[Validation is data, not an event]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
