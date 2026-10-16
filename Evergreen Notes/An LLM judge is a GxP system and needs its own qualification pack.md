---
title: "An LLM judge is a GxP system and needs its own qualification pack"
created: 2026-09-15
tags:
  - "evergreen"
---

Induced from the observability and evaluation lecture at the AI in GxP conference ([[2026-09-15-1112-ai-observability-evaluation-gxp-lecture]]), 2026-09-15, including Eric's own Q&A contribution on judge-human alignment.

## Four eyes means a different model at a different temperature

Using an LLM to grade another LLM's outputs only counts as independent review under the four-eyes principle if the judge is a separate model from the operating agent, run at a low but non-zero temperature. The judge can catch silent failures that correctness scores miss, for example a complaint triage completed before a death was ever reported.

## Qualify the judge like any other system

The Judge Qualification Pack mirrors every other GxP qualification: intended use, grading rubrics, a golden dataset, a calibration report, and acceptance criteria. That pack is itself an instance of [[Validating an AI system in a regulated industry means validating a measurement system]]. Risk tolerance does not need new frameworks; ICH Q9 and GAMP already provide them, and sign-off remains a human decision. Calibrate the judge against human subject-matter experts (Eric's metric: flag judge-human deviation around five percent) and remember the audience's figure of roughly 76 percent agreement for model-checking-model: useful for triage, not a substitute for the qualified record. [[Human verification of AI output must be explicit because document creation no longer carries implicit verification]] still sits above the judge, because in [[In the GxP control loop, AI acts, humans decide, and the system remembers]] the judge is not the decider.

## Golden sets need unhappy paths

Happy-path training data yields happy-path answers. Evaluation sets must enumerate failure modes and include the unhappy paths, graded by simple pass/fail graders with risk-based thresholds, a human-in-the-loop layer, and a regression baseline. [[A golden test set must include unhappy paths]] is that requirement as its own claim. Avoid generic vendor graders; grade against your own SOP compliance and schema. Layer the grading: code checks first, model checks second, human SMEs calibrating first and reviewing exceptions later. That layering is the quality half of [[Observability and evaluation answer different questions about an AI system]].

## Related

- [[Home]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
- [[Human verification of AI output must be explicit because document creation no longer carries implicit verification]]
- [[A golden test set must include unhappy paths]]
- [[Observability and evaluation answer different questions about an AI system]]
- [[In the GxP control loop, AI acts, humans decide, and the system remembers]]
