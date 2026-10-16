---
title: "Absence problems are harder to detect than presence problems"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Yari Fontebasso's local-LLM audit-trail investigation at the KENX AI in GxP East 2026 conference ([[2026-09-16-1612-local-llms-gxp-audit-trail-lecture]]), 2026-09-16.

## Missing records hide from every model

His ten audit-trail problem types split into presence problems (something anomalous is in the data) and absence problems (something required is missing from it). The anomaly-detection baseline, an Isolation Forest, flagged six to seven of ten problem types but missed absence almost entirely, because absence produces no signal to flag. Feeding the full audit trail failed silently on context limits; ordered batching restored evidence access at the cost of false positives.

## Why the frontier gap concentrates here

Completeness problems, the purest absence cases, were caught reliably only by frontier cloud models in his comparison. That lands the local-versus-cloud decision on the hardest cases: absence detection is exactly where capability is scarcest locally, and exactly where an audit cares most. [[Local models trade capability for control]] is that trade stated from the same experiments. Any audit-trail review design should assume absence needs its own evidence strategy, not a bigger model prompt. The complementary model behavior is [[An AI system in GxP must be able to answer unable to verify]], and the complementary test design is [[A golden test set must include unhappy paths]]: known-absent items are how you find out the system hid a gap.

## Related

- [[Data Foundations and Audit Trails MOC]]
- [[Local models trade capability for control]]
- [[An AI system in GxP must be able to answer unable to verify]]
- [[A golden test set must include unhappy paths]]
