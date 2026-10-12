---
title: "Bounded inputs make AI validation tractable"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Ben O'Brien's intended-use lecture at the KENX AI in GxP East 2026 conference ([[2026-09-15-1611-ben-obrien-intended-use-statements-gxp-ai-lecture]]), 2026-09-15.

## Define the data bounding box, then gate on it

"Images from cameras X, Y, Z on line one at standardized 5000k LED illumination" beats "visual data across liquid manufacturing lines." A bounded input definition enables pre-validation gating that rejects non-conforming data before the model sees it: wrong camera, wrong line, wrong lighting, no processing. The phone-photo question answers itself.

## The economics of the box

Unbounded inputs mean proving the model works on every permutation, which stretches a three-month test execution into potentially years, and monitoring everything outside the box you never drew. Bounded inputs shrink execution to months and simplify monitoring to the fixed parameter space. Dropping the domain later has its own cost: an oncology-trained model retargeted elsewhere may find its whole training corpus useless.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[The wording of an intended use statement sets the regulatory burden]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
