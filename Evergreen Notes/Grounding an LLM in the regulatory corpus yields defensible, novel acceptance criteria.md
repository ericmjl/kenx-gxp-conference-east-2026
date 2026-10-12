---
title: "Grounding an LLM in the regulatory corpus yields defensible, novel acceptance criteria"
created: 2026-10-12
tags:
  - "evergreen"
---

Induced from Eric Ma's follow-up conversation with Abhishek Bachchan at the KENX AI in GxP East 2026 conference ([[2026-09-15-1531-abhishek-llm-acceptance-criteria-regulated-industries]]), 2026-09-15.

## The method

Ingest every regulatory document you work with, then spend a long session prompting the model to write acceptance criteria grounded only in what you have done for your own applications. When it returns a basic statement, instruct it to generalize. Then check novelty: search whether anyone else has said it. His result held up on both axes, original and still valid against the corpus.

## Why it matters for regulated writing

Facing the pile of documents a regulated environment demands, the hard part is starting, and templated statements unblock the start. Eric called it the most practical talk of the day for exactly that reason. The caveat Abhishek volunteered alongside: his six-month MIT class on LLMs was already six months out of date by the end, so the practice needs continuous refreshing even as the method holds.

## Related

- [[AI Validation and Acceptance Criteria MOC]]
- [[Validating an AI system in a regulated industry means validating a measurement system]]
- [[Eric's Field Notes MOC]]
