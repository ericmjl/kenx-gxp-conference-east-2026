---
title: "Validate what you can, verify the rest"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Robert (Bob) Wherry's ten-step framework lecture at the KENX AI in GxP East 2026 conference ([[2026-09-16-1107-gxp-ai-ml-implementation-framework-lecture]]), 2026-09-16.

## The spectrum replaces the binary

Traditional validation assumes you can prove a system does what it claims. Non-deterministic AI breaks the assumption, so the framework splits the response: validate what you can (deterministic components, data pipelines, guardrails) and verify the rest against statistics-based performance metrics. Underneath sits the motto "Never Trust! Always Verify!" and the four variability sources any AI system carries: model, infrastructure, data environment, and human. The motto is the same demand as [[Human verification of AI output must be explicit because document creation no longer carries implicit verification]], and the statistics-based remainder is why [[AI validation evidence has a shelf life]].

## The framework around the spectrum

His ten steps include an authorized-use policy, honest token-cost budgeting, quality and regulatory SMEs on development teams from the start, a formal AI lifecycle with its own SOPs, pinned public models with bounded inputs, procurement controls with an AI inventory, QMS quality gates, documented human verification, and a mock audit by an SME before the formal one. The dedicated SOPs are [[AI development needs its own SOPs, separate from the software development lifecycle]]; pinning and bounding are [[Bounded inputs make AI validation tractable]]; documented human verification is [[Human-in-the-loop must be a named hard gate, not rubber-stamp oversight]]. His pushback from the floor: force-fitting AI into the software development lifecycle is a square peg in a round hole.

## Related

- [[Governance Risk and Human Factors MOC]]
- [[AI development needs its own SOPs, separate from the software development lifecycle]]
- [[AI validation evidence has a shelf life]]
- [[Human verification of AI output must be explicit because document creation no longer carries implicit verification]]
- [[Bounded inputs make AI validation tractable]]
- [[Human-in-the-loop must be a named hard gate, not rubber-stamp oversight]]
