---
title: "An AI system in GxP must be able to answer unable to verify"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Binesh Prabhakar's pharmacovigilance lessons-learned lecture at the KENX AI in GxP East 2026 conference ([[2026-09-16-1150-ai-validation-pharmacovigilance-it-compliance-lecture]]), 2026-09-16.

## Silence about missing evidence is the dangerous failure

After twenty-four months of validating AI-assisted pharmacovigilance applications, his team hardened guardrail language so the system answers "unable to verify" when evidence is missing. The failure it guards against showed up in the local-LLM investigation too: systems answering without disclosing they only saw part of the data. A confident answer over a partial record is worse than no answer, because it looks like one.

## The surrounding discipline

Their six-step GxP process: controlled evidence, fixed questions and prompts, AI analysis, evidence plus rationale, human review, approved output with audit trail. Failure modes they catalogued: severity inflation, duplicate findings, plausible but unevidenced assumptions, citation overreach. Agent personas carry CVs (training scope, versions, validation history, data residency) and get retrained when SOPs change.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[A golden test set must include unhappy paths]]
- [[Absence problems are harder to detect than presence problems]]
