---
title: "AI development needs its own SOPs, separate from the software development lifecycle"
created: 2026-09-16
tags:
  - "evergreen"
---
Three speakers across both conference days converged on this. AI development and software development are different animals: a generative system has no single expected result, its training data is part of the product, and its behavior varies with model version, infrastructure, data environment, and the human prompting it. Forcing AI into a software development lifecycle SOP produces documents that describe a process nobody follows. That is the procedural consequence of [[Validate what you can, verify the rest]]: the deterministic pieces can stay in a software lifecycle, and the non-deterministic remainder needs its own written method.

The working shape: dataset development and model development SOPs when training in-house; when using a purchased or public model, pin the version, bound the inputs, and write the procedure around that. [[Bounded inputs make AI validation tractable]] is the same move at the data boundary. On the validation side, keep AI model validation SOPs separate from traditional computerized system validation, and write dedicated procedures for AI testing and validation; [[The intended use statement is the master control lever for GxP AI]] is what those dedicated procedures lock early. One pharmacovigilance team credited its dedicated AI SOPs with reducing deviations. Dedicated procedures are also how [[Regulators audit against principles, so size quality rigor to risk]] stays writable: the AI process gets its own checklist instead of inheriting a software one that nobody follows.

## Related

- [[2026-09-16-1107-gxp-ai-ml-implementation-framework-lecture]]
- [[2026-09-15-1611-ben-obrien-intended-use-statements-gxp-ai-lecture]]
- [[2026-09-16-1150-ai-validation-pharmacovigilance-it-compliance-lecture]]
- [[Home]]
- [[Validate what you can, verify the rest]]
- [[Bounded inputs make AI validation tractable]]
- [[The intended use statement is the master control lever for GxP AI]]
- [[Regulators audit against principles, so size quality rigor to risk]]
