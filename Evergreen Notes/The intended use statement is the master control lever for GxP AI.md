---
title: "The intended use statement is the master control lever for GxP AI"
created: 2026-09-15
tags:
  - "evergreen"
---

Induced from Ben O'Brien's (Phanero) afternoon lecture at the AI in GxP conference ([[2026-09-15-1611-ben-obrien-intended-use-statements-gxp-ai-lecture]]), 2026-09-15.

## Four pillars, locked early

The intended use statement goes beyond a traditional user requirements specification and carries four pillars: the Core Task, the Data Bounding Box, the Model Limitations, and the Governance Boundaries. Locked early and worded precisely, it determines risk tiering, validation depth, and inspection scope. Change any pillar midstream and a governance domino effect invalidates the risk assessments, data lineage, metrics, monitoring, and training data downstream.

## Wording is the regulatory surface area

The same model can be described as one that "categorizes and assigns severity to incoming deviations" or as one that "drafts preliminary deviation summaries for QA review"; the first reading carries far more regulatory burden than the second. Narrow, accurate wording shrinks the auditable surface; that is [[The wording of an intended use statement sets the regulatory burden]]. Bounded inputs do the same from the other side: named cameras and standardized 5000K LED illumination enable pre-validation gating that cuts validation from potentially years to months, which is [[Bounded inputs make AI validation tractable]]. Advisory outputs shift burden to a trained human; autonomous outputs demand confidence scoring, fallback logic, and failure-mode containment. That split is [[Assurance must scale with autonomy]].

## Human oversight cannot be camouflage

The phrase "utilising human oversight during operational execution" often describes passive rubber-stamping. Inspectors will eventually ask for training records and decision evidence, so the wording should mandate explicit QA review and electronic sign-off as a hard stop. [[Human-in-the-loop must be a named hard gate, not rubber-stamp oversight]] is that hard stop as its own claim, and it is the human-decide step in [[In the GxP control loop, AI acts, humans decide, and the system remembers]].

## Validate the model separately from the system

GAMP categories do not transfer to AI models, so AI model validation must stay separate from traditional computerized system validation. That separation is why [[AI development needs its own SOPs, separate from the software development lifecycle]]. Google-style model cards endorsed as SOP appendices carry the model's purpose, data, and limits into the quality system. Worth watching: O'Brien announced an October 22 webinar with Victor Beckman, a Danish Medicines Agency inspector on the Annex 22 authoring group, on LLMs in GxP. Locked early, the four pillars give [[Validating an AI system in a regulated industry means validating a measurement system]] a population and a context of use, and they have to be written while Manufacturing, IT, and QA are still concurrent or [[AI pilots in GxP fail on sequencing, not technology]] all over again. In a GxP market, [[In GxP markets, the MVP is the customer's intended use]] is this same lever seen from the vendor side.

## Related

- [[Home]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
- [[AI pilots in GxP fail on sequencing, not technology]]
- [[The wording of an intended use statement sets the regulatory burden]]
- [[Bounded inputs make AI validation tractable]]
- [[Assurance must scale with autonomy]]
- [[Human-in-the-loop must be a named hard gate, not rubber-stamp oversight]]
- [[AI development needs its own SOPs, separate from the software development lifecycle]]
- [[In GxP markets, the MVP is the customer's intended use]]
- [[In the GxP control loop, AI acts, humans decide, and the system remembers]]
