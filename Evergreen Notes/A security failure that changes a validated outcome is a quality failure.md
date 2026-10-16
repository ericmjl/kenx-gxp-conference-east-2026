---
title: "A security failure that changes a validated outcome is a quality failure"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Aarti (Amy) Arora's protection-by-design lecture, parts one and two, at the KENX AI in GxP East 2026 conference ([[2026-09-16-1521-ai-protection-by-design-gxp-lecture]], [[2026-09-16-1554-trust-in-ai-enabled-gxp-lecture]]), 2026-09-16.

## One event, two vocabularies

A cyber event can be a quality event. Quality and security are asking the same questions in different languages: MFA means only the right person approves a GxP action; RBAC means only qualified users perform regulated activities. Her arc taught both dialects, from R&D IT delivery into a CIO-forced takeover of global compliance, learning SOX and cyber controls as a self-described GXP nerd.

## The AI-expanded control surface

Agent privilege misuse, vendor access, prompt changes outside change control, data tampering, undetected model changes, training drift, audit-log gaps, with excess permissions named as the biggest current problem. That is why [[Autonomous agents need their own auditable identities in regulated systems]]: without a named, scoped actor, privilege misuse has no attributable trail. Her four trust checks: the system works as intended, unauthorized users cannot act, records, prompts, and models cannot change unnoticed, and monitoring runs continuously. The closing maxim: quality builds confidence, security sustains trust; test trust, not just functionality. Her S.H.A.R.E. tabletop (scope, name failures, align shared controls with named owners, reuse evidence, exercise failure) makes the collaboration concrete. Those shared controls only hold if [[Compliance controls belong in the product from inception]], and if a changed outcome still has an attributable human decision in [[In the GxP control loop, AI acts, humans decide, and the system remembers]].

## Related

- [[Governance Risk and Human Factors MOC]]
- [[Compliance controls belong in the product from inception]]
- [[Autonomous agents need their own auditable identities in regulated systems]]
- [[In the GxP control loop, AI acts, humans decide, and the system remembers]]
