---
title: "Validating an AI system in a regulated industry means validating a measurement system"
created: 2026-09-15
tags:
  - "evergreen"
---

Induced from Abhishek Bachchan's lecture at the AI in GxP conference ([[2026-09-15-1426-abhishek-ai-acceptance-criteria-gxp-lecture]]) and the follow-up conversation with Eric ([[2026-09-15-1531-abhishek-llm-acceptance-criteria-regulated-industries]]), 2026-09-15.

## Neither CSV nor CSA fits a drifting system

Computer system validation and computer software assurance both assume a deterministic system, a human error-catcher in the loop, and a validated state that persists without further action. An AI system violates all three assumptions: performance drifts as models, prompts, providers, and corpora change, so any validated state has an expiry date. Regulators point the same direction without handing over numeric thresholds: FDA's SaMD guidance distinguishes locked from adaptive models with predetermined change control plans, the EU GMP Annex 22 draft addresses AI, and roughly four of ten joint FDA/EMA AI principles touch acceptance criteria.

## The acceptance-criteria statement names population and threshold

A defensible validation package for an AI system specifies a population (a versioned, change-controlled labeled test set), a risk-justified threshold, the conditions of use, the harness at a named commit, and a deviation route, with run records as the evidence. The conditions of use come from [[The intended use statement is the master control lever for GxP AI]], and the population is tractable only when [[Bounded inputs make AI validation tractable]]. Abhishek demonstrated this on a personal RAG project over regulations and warning letters with roughly 100 labels, including drug-versus-device distractors and known-absent probes to catch hallucination. Six acceptance-test buckets cover the space: retrieval, faithfulness, reproducibility, boundary refusal, human-in-the-loop, and guardrails and authority.

## Evidence has a shelf life, so ship the dashboard

An inspection-ready package is an interactive dashboard, not a binder: per-call provenance (which model version was requested versus served, prompt hashes), a grounding exception log, human dispositions, threshold rationale, and requalification records. Any trigger, a provider change, a prompt tweak, corpus growth, a chunking change, or simply elapsed time, forces re-measurement. That expiry is [[AI validation evidence has a shelf life]]. LLM-as-judge systems agree with human reviewers roughly 76 percent of the time while picking up biases quickly, so they serve as calibrated triage rather than as the judge of record; [[An LLM judge is a GxP system and needs its own qualification pack]] is that triage as its own system.

## Why this is the regulated-industry instance of external verification

The same principle that makes scientific agents work, verification outside the model, is what regulators demand here: What makes a scientific agent good argues the loop closes outside the model; GxP turns that argument into populations, thresholds, harnesses, and records. The population has to include [[A golden test set must include unhappy paths]], and one way to draft the threshold language is [[Grounding an LLM in the regulatory corpus yields defensible, novel acceptance criteria]]. See also [[Human error, not AI failure, drives GxP warning letters]] and [[Validation is data, not an event]].

## Related

- [[Home]]
- [[AI validation evidence has a shelf life]]
- [[An LLM judge is a GxP system and needs its own qualification pack]]
- [[A golden test set must include unhappy paths]]
- [[Grounding an LLM in the regulatory corpus yields defensible, novel acceptance criteria]]
- [[Human error, not AI failure, drives GxP warning letters]]
- [[Validation is data, not an event]]
- [[The intended use statement is the master control lever for GxP AI]]
- [[Bounded inputs make AI validation tractable]]
