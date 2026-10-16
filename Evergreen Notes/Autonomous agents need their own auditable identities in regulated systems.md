---
title: "Autonomous agents need their own auditable identities in regulated systems"
created: 2026-09-15
tags:
  - "evergreen"
---

Induced from Shelly LaPointe's lecture at the AI in GxP conference ([[2026-09-15-1201-shelly-lapointe-data-foundation-for-ai-in-gxp]]), 2026-09-15.

## Treat every agent like a person in the system

The moment autonomous agents touch regulated data, shared service accounts and blanket admin rights stop being acceptable. Each agent needs its own identity in access control: scoped to what it may read and write, time-boxed, and fully logged. Shelly LaPointe's proposal is a new tier-4 access tier written into access-control SOPs specifically for agents, and she openly puzzles over how far the analogy goes, down to whether an agent needs its own Workday HR entry.

## Why identity is the enforcement point for everything else

Named agent identity is what makes the rest of the GxP AI stack auditable: ALCOA+ trail entries need an attributable actor, human oversight gates need to know which agent acted, and requalification triggers need to know which system touched which data. Without agent identity, "human-in-the-loop" and "audit trail" both degrade to prompts about prompts. [[In the GxP control loop, AI acts, humans decide, and the system remembers]] cannot remember an actor the directory never named, and [[A security failure that changes a validated outcome is a quality failure]] starts as excess permissions on a shared account. The general principle echoes Access control on wikis belongs in the directory, not the model: enforcement belongs in the directory and the access tier, not in the model's good behavior. Those identities then sit inside [[One governed dataset should serve many consumers]], and they matter because [[GxP systems are optimized to be inspection-ready, not insight-ready]] until every consumer, including an agent, is attributable.

## Related

- [[Home]]
- [[GxP systems are optimized to be inspection-ready, not insight-ready]]
- Institutional data rules gate LLM tool adoption
- [[In the GxP control loop, AI acts, humans decide, and the system remembers]]
- [[A security failure that changes a validated outcome is a quality failure]]
- [[One governed dataset should serve many consumers]]
