---
date: 2026-09-15
recorded_at: 2026-09-15T12:01:42-04:00
duration_seconds: 1624
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: 965af6accd9c43bd998c0969e8986b07
plaud_name: "09-15 Lecture: AI in GXP Environments and Data Foundation"
speakers:
  - Shelly LaPointe, lecturer (diarized as Speaker 1; quality-systems leader formerly at Fisher, Pifera, and Arena Pharma)
  - Attendee interjections during a mid-lecture screen-share dropout (also diarized as Speaker 1)
presenter: Shelly LaPointe
affiliation: "Quality Systems Director, Stealth Startup (virtual speaker; formerly Thermo Fisher, Pfizer, Arena Pharmaceuticals)"
session: "Building a Scalable, Governable Data Estate for AI (day one, 12:00-12:40, virtual)"
tags:
  - kenx-gxp-east-2026
  - transcript
---
# Shelly LaPointe on the data foundation for AI in GxP environments

> Recorded 2026-09-15 at 1201 via Plaud. 27:04.

## Summary

Talk recorded at the GxP and AI conference Eric is attending this week. The lecturer, Shelly LaPointe, a quality-systems leader formerly at Fisher, Pifera, and Arena Pharma who designs GXP-grade data and validation frameworks, argues that as organizations move AI from pilots to production the data estate becomes the limiting factor: AI is only as good as the data foundations underneath it. The reality she starts from is siloed systems (LIS, MES, QMS, each with its own format, access model, and governance) in environments optimized to be inspection-ready rather than insight-ready, so every AI pilot rebuilds its own non-reusable pipeline, and agentic AI multiplies the problem because each additional AI touching the data multiplies the traceability obligations. Her blueprint is one governed dataset with many consumers (autonomous agents, model-training pipelines, compliance dashboards, and humans): build the estate once, validate it once, reuse it everywhere. The reference architecture runs from sources through an ingestion framework (normalization, tagging, lineage capture) into a storage layer split into raw, curated, and consumption zones plus a metadata catalog, wrapped in role-based access controls, encryption, and a GXP validation envelope covering pipelines, storage, access, and every model and agent. ALCOA+ remains the anchor: AI does not change the requirements, only the enforcement surface, so audit trails, electronic signatures, and human-understandable agent naming matter more, and "enduring" is the hardest attribute to keep as models keep changing.

The center of the talk is agent identity. Agents must become first-class access control subjects, each treated like a person in the system with its own identity, replacing shared service accounts and blanket admin rights, because anonymous automation cannot be audited; access-control SOPs need a new tier 4 for autonomous agents that is scoped, time-boxed, and fully logged, and she raises the practical question of whether an AI agent needs its own entry in Workday just to exist on the network. Governance is the operating model that determines whether an AI program survives an inspection (named owners, stewards, escalation paths, continuous classification, automated checks), and GAMP 5-style risk-based validation, applied well, has delivered about a thirty-five percent reduction in validation cycle time: classify pipelines and models by GXP impact, embed automated testing at every stage rather than testing at the end, automate change control so updates trigger change records, and reuse validation evidence and scripts. Named pitfalls are the missing agent identity model (untraceable who-did-what-where), one-size-fits-all architectures that create performance bottlenecks in large businesses (partition by domain or division), and beautiful pipelines that will not last without defined ownership and access tiers. The closing roadmap is concrete: this week, build a system inventory of data sources and their owners (have IT export what it knows, for example from ServiceNow) and assess inspection readiness for agent identity; this month, stand up a cross-functional governance group (IT, QA, QC, manufacturing) and define data-estate zones and classification standards; this quarter, implement automated data-quality checks at ingestion, templatize ingestion, build the metadata catalog and lineage tracking, and run a mock external audit of the first reusable, agent-ready pipeline. Her closing line restates the thesis: your data estate is your AI strategy, and if the foundation is not governed, validated, and reusable, everything built on top of it is fragile. The recording includes a mid-lecture screen-share dropout during which attendees brought her back online.

## Plaud AI notes

App-generated, verbatim from Plaud's Summary tab.

<!-- markdownlint-disable MD024 MD033 -->
> Date Time: 2026-09-15 12:01:42
> Location: [Insert Location]
> Instructor: Shelly LaPointe
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i1)
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i2)

## Summary

In this lecture, Shelly LaPointe, a specialist in GXP-grade data and validation frameworks, explains how to build a scalable, governable, and inspection-ready data foundation to support AI in regulated environments. The central theme is that AI effectiveness depends entirely on its underlying data foundation, which must meet stringent GXP requirements for integrity, traceability, and reusability. <mark style="background-color: #F9EDD4">LaPointe highlights the common challenge of data silos (LIMS, MES, QMS) and systems optimized for audits rather than analytics, which hinders AI adoption.</mark> A key focus is moving from isolated AI pilots with non-reusable pipelines to a centralized, governed data estate. This requires a reference architecture with a robust ingestion framework, a structured storage layer, and end-to-end governance, security, and validation. <mark style="background-color: #F9EDD4">A major emphasis is treating autonomous AI agents as first-class access control subjects with unique identities, replacing shared service accounts to ensure full traceability.</mark> The lecture also outlines a risk-based validation approach (e.g., GAMP 5) to accelerate development safely. <mark style="background-color: #F9EDD4">Finally, LaPointe provides a practical, phased plan to begin this transformation: map data sources, establish governance, and build and audit the first reusable, agent-ready data pipeline.</mark>

## Knowledge Points

### 1. The Challenge of AI in GXP Environments

- **Current State of Data Systems**
  - Organizations operate numerous silos (LIS, MES, QMS, ERP, CRM), each with distinct formats, access models, and governance, preventing a complete data view for AI.
  - Most GXP environments are optimized to be "inspection-ready" (auditable) rather than "insight-ready" (analytics/AI-optimized).
  - As a result, each AI pilot rebuilds its own pipeline, leading to inefficiency and poor reusability.
- **The Impact of Agentic AI**
  - Agentic (autonomous) AI multiplies cost and complexity as many autonomous consumers access the same ungoverned datasets.
  - Every added AI agent increases traceability obligations, not just computational costs.
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i3)
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i4)

### 2. GXP Obligations and AI

- <mark style="background-color: #F9EDD4">**ALCOA+ as the Anchor**
  - ALCOA+ (Attributable, Legible, Contemporaneous, Original, Accurate, Complete, Enduring, Available) remains the non-negotiable foundation for data integrity in GXP environments.</mark>
  - AI does not change these requirements; it changes how, how often, and by whom they are met, expanding the enforcement surface. Every AI agent action must adhere to ALCOA+.
  - "Enduring" is highlighted as a challenge as AI models evolve over time.
- <mark style="background-color: #F9EDD4">**Enforcement Controls**
  - High-priority controls include electronic signatures, immutable records, system validation, encryption, and especially audit trail logging.</mark>
  - Audit trails are even more critical with AI agents to trace every action. Clear, human-understandable naming for agents and actions improves auditability.
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i5)
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i6)

### 3. The Governed Data Estate Blueprint

- <mark style="background-color: #F9EDD4">**Core Idea: One Governed Dataset, Many Consumers**
  - Build a single, governed data estate validated once and reused broadly for scalability and traceability.</mark>
  - The central dataset should be versioned, cataloged, and fully lineage-tracked.
  - Consumers include autonomous agents, model training pipelines, human analysts/QA, and compliance dashboards. Lineage must cover all activities across all consumers.
- <mark style="background-color: #F9EDD4">**Reference Architecture Components**
  - **1.</mark> Data Sources:** ERP, CRM, MES, SCADA, LIMS, QMS, IoT/Sensors.
  - **2. Ingestion Framework:** Normalization, metadata tagging, lineage capture, and GxP checks.
  - **3. Storage Layer:** Three zones—Raw, Curated, and Consumption—plus a metadata catalog.
  - **4. Governance & Security:** RBAC/IAM, audit trails, encryption, and a complete validation package.
  - **5. AI & Agent Consumption:** Feature engineering, agent tool calls, dashboards, and compliance reporting.
- **The GXP Validation Envelope**
  - A comprehensive validation envelope must wrap pipelines, storage, access controls, and every AI model/agent. Validation evidence must be documented and maintained throughout the lifecycle.
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i7)

### 4. AI Governance Operating Model

- **Governance as a Survival Mechanism**
  - Governance is the operating model that ensures an AI program can withstand regulatory inspection, not a checkbox exercise.
- <mark style="background-color: #F9EDD4">**Pillars of Governance**
  - **Ownership & Stewardship:** Assign named data owners per domain, designate stewards for policy enforcement, define escalation paths, and tie ownership to change control.</mark>
  - **Access Control Tiers:** Implement tiered access, including a dedicated tier for AI agents (Tier 4: Autonomous Agent), scoped, time-boxed, and fully logged.
  - **Risk & Compliance Monitoring:** Continuous data classification, automated compliance checks on ingestion, and full traceability from source to AI output to keep evidence packages inspection-ready.
- **Agent Identity as a First-Class Subject**
  - Treat each AI agent as a unique "person" with its own identity and rights.
  - Replace shared service accounts and avoid blanket admin rights to prevent untraceable actions and anonymous automation.
  - This raises practical questions, such as whether an AI agent needs an entry in corporate HR (e.g., Workday) to be recognized on the network.
[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i8)

### 5. Risk-Based Validation for AI

- **Moving Faster Safely**
  - Apply risk-based validation (e.g.<mark style="background-color: #F9EDD4">, GAMP 5) to accelerate development without compromising quality, potentially reducing validation cycles by ~35%.</mark>
- **Key Principles of Risk-Based Validation**
  - **1. Risk Assessment First:** Classify pipelines/models by GxP impact to set validation depth (high-impact requires full protocol).
  - **2. Continuous Testing:** Embed automated tests throughout the pipeline to catch failures early.
  - **3. Change Control Automation:** Automatically trigger change records for model updates or configuration changes to avoid documentation gaps.
  - **4. Reuse of Validation Evidence:** A modular estate enables reuse of test scripts and validation packages across similar pipelines and agents.
  - Treat validation as a continuous discipline across the lifecycle, not a final gate.

### 6. A Practical Roadmap for Implementation

- **This Week (Starting September 14, 2026)**
  - Map all current GxP data sources and identify their owners via a system inventory.
  - Identify the single most important AI or agent use case to enable first.
  - Assess current inspection-readiness, especially for agent identity and access controls.
- **This Month (By mid-October 2026)**
  - Establish a cross-functional governance group (IT, QA, QC, Manufacturing).
  - Define data estate zones (raw, curated, consumption) and data classification standards.
  - Select and formally document the risk-based validation approach.
- **This Quarter (By mid-December 2026)**
  - Implement automated data quality checks at ingestion.
  - Build the metadata catalog and implement lineage tracking.
  - Run a mock audit on the first reusable, agent-ready data pipeline to test readiness from an external auditor's perspective.

## Questions

- [Insert Question/Confusion]

## Assignments

- [ ] 1. Create a system inventory of all current GxP data sources and their named owners.
- [ ] 2. Identify the top-priority AI or agent use case the organization wants to enable.
- [ ] 3. Assess the current environment's inspection-readiness, focusing on the ability to support unique agent identities and access controls.
- [ ] 4. Form a cross-functional governance group with representatives from IT, QA, Manufacturing, and other data stakeholder departments.
- [ ] 5. Define and document data estate zones, classification standards, and the organization's risk-based validation strategy.
- [ ] 6. Plan the implementation of automated data quality checks, a metadata catalog, and lineage tracking for the first data pipeline.
- [ ] 7. Schedule and conduct a mock audit of the first agent-ready pipeline.

## Related Photos

[](plaud://image?type=summaryCard&id=oc_su_965af6accd9c43bd998c0969e8986b07_i9)
<!-- markdownlint-enable MD024 MD033 -->

## Transcript

[00:00] **Speaker 1:** You know, leader of quality systems that has started, still starting. Formerly at Fisher, Pifera, Arena Pharma. Just you know, had a had a long career. But basically, I specialize in designing GXP-grade data and validation frameworks that support scalable AI adoption. As organizations are moving from pilots to production, the data estate is really becoming the limiting factor, and that's exactly what we're here to talk about today. So this session is about building a data foundation that can actually support AI in regulated environments, not just one model or one pilot, but a scalable, governable, inspection-ready estate. They can handle exantic systems, autonomous workloads, and the traceability obligations that come with them. So it's just really, you know, taking the pilots to full scale and how to get there. So the core idea is simple: AI is as good as the data foundations underneath it. And in GXP, that foundation has to meet integrity, traceability, and reuse requirements. Even as autonomous agents start touching our systems, so my goal today is simple: to make this practical. I want you to walk away with a clear picture of what a governable real estate data estate looks like, why it matters, and what you can start doing next week. So, click here. Next slide. Okay, so. Let's start with the reality most of us are dealing with now. Many, many data silos. We've got our LIS or MES or QMS. Everything's got its own format. Everything has its own access model and its own governance. And you know, really, AI can't learn what it can't see. So, how are we going to surmount that? You know, in most GXP environments, are optimized for being inspection ready, not insight ready. So we've built systems that are great at, you know, being auditable, but not great at supporting analytics or AI workloads. I apologize. Because of that, I need to finish this whole convo. I sorry, it was my pleasure. Still, because of that, you know, every AI pilot was rebuilding its own pipeline. Because nothing that we're doing is really reusable, and when you introduce agentic AI, you've got multiple autonomous consumers hitting the same data, so it multiplies really quickly. So one of the most important things is that you know each additional AI. Sorry, that. Touches the data multiplies the obligations. So you know we really need to focus on having thorough ones in there. Okay. Slide jumped over. Get too excited there. Okay. AI, mental stuff. You know, all all of that is still non-negotiable. But AI does change how often and by whom. Those are weird. So you know, data integrity. So every data point still has to have. We now have to log and then to start auditing the models. You know, the version rolls. So change control pipelines. We're not really good. Yeah, we amend then our reflection readiness, right? We make evidence packages that we build at the end, and then it needs to live. Obviously, the models change, so really, you know, the backer, you know, is is torn apart. It really persists throughout. I can't see. Anybody else having lemons? Literally. Recording in progress. And first, whenever. Hey Shelley. We lost you for a second there. You're gonna have to reshare your screen. I apologize. Disappeared. Shelley. Good. Recording in progress. Hey Shelley, can you hear me? Hi there. Can you hear me? Okay. Yeah, we went down for a minute there, and we lost you. It looks like okay. I see. We see everything now. Um, I don't know for exactly. The increase. All right, keep going. So ingestion framework, you know, really the normalization, the tagging, not great. Okay, I will get a little closer. I apologize. I wish I had better bandwidth. Um. Okay. So I'm just moving on to the storage layer. You can hear me, okay? So the raw, you. Great curated zone and the consumption zone, plus a metadata catalog, and I think that's also something that I know our my prior company we were maybe lacking there. So that's something that I think is important to have a governable state. You know the role-based access controls. Materials encryption, the full validation package, and you know AI and agent consumption. So this is something that's new, that I think really we need to focus on. So feature engineering, you know, getting the most white papers and release notes. If there's new stuff coming, we need to know what's in there. And the agent tool calls right. What's going on with our connections, with our integrations, in dashboards, our compliance reporting? Really, it's the GXP validation envelope that wraps the entire stack. So this is something that's going on. It should be evolving throughout, you know, the lifetime. Well, the lifetime of your products. Okay. So moving on here. So really, this is nothing new for anybody here. I'll go. Plus, you know, it's still the anchor. AI doesn't change the requirements; it just changes the enforcement surface. So every agent action must also be attributable, legible, contemporaneous—all of the good things. Something that I think is a little bit of a challenge is the enduring, right? So, if we have agents that are doing things and they're based on certain models, and then the model changes, or I don't know, enduring I think is is going to be a challenge for us in the industry. So the controls that force enforce The electronic signatures, the audit trail logging, everything becomes even more important when agents are involved, because now oh, that's literally be chasing that through the audit trail. Having good, maybe human understandable naming for it increases the frequency and complexity of our Alcoa plus operations, but it doesn't. It doesn't change them, unfortunately. Okay, so really, you know, what can we do to have, you know, traceability in reuse in our platforms? So if we've got one governed data set with many consumers, then we can have more controls. So in the agentic area, you know, we're going to have autonomous agents. We're going to have model training pipelines, compliance needs, as well as humans. You know, for permitted and QA reviewers need some inspectors. All must span every consumer's activity, from the human clicks and the agent tool calls alike. And we need to be able to show that and report that out. And critically, agent identity must be first-class access control subject. We can no longer use shared service accounts and just give every agent admin rights. So you know we're no longer in a place where we can have anonymous automation. Everything needs to be audit controlled, and every agent. Needs to be really treated like a person in the system. So this is how you build the state once, validate it once, and reuse it everywhere. Of course, we all know that's you know not reality in most businesses. But if you're starting, that would be the way to do it. Start in one place, you know, with one one governed data set that you can leverage. Then you really can scale it. Okay, so moving on here. So governance, you know, it's not a check box. It's the operating model that determines whether your AI program survives an inspection. So stewardship and ownership, you know, having named owners, stewards, escalation pathways, that can sometimes be a challenge. You know, knowing who is the system owner of your AI, who's the business owner. You know, is there a support team? You know, just that's sometimes hard to track down in and of itself. Okay, but then also the access control tiers, right? Especially for tier four now, where we've got you know autonomous agents that are now going to be scoped, you know, hopefully timeboxed and fully logged. So this is something that's that's new for us, and we'll need to be adding that to all of our access control SOPs. And then, obviously, risk and compliance monitoring. So, continuous classification, automated checks, traceability from source to output. The message here is governance is how you scale safely. So we can't do that, you know, nice clean model without having really good governance. Okay, moving on here. So, a place that. I've spent a lot of time is with risk-based validation because let's face it, we all want to go faster, and you know we got some pretty good metrics now. I think you know taking a risk-based approach, right? Gang up five, has allowed you know a thirty-five percent reduction in validation cycle time, if it's applied well. If it's not, sometimes having that you know increased risk, well. It can delay, but you know. Let's face it. Validation, you know, risk-based validation is how we move faster without cutting corners. So we need to, you know, classify our pipelines, models, and doing a GXP imp assessment on them. And I think that sometimes, also a little bit of a challenge for business is recognizing. That these things do need to be documented and classified, and then we need to build in continuous testing. So automated tests at every stage should be embedded. If we're testing at the end, then we're going to catch it when it's already too late. So if we can build things in, you know, do dev testing in dev, that's that's perfect. And let's face it, once your system is in flight, you'd rather know before it hits production. So okay, and then also change control automation. So updates should change or should trigger a changed record. Ah, too magically, I say, because I think a lot of times the humans don't really want to deal with change control, but you know, the humans are fine with that. They will run the basis for you. So automating change control and making sure that this system helps you through that. This needs to be documented, and then reusing the validation evidence. So if you know. And we can reuse scripts. You don't need to, you know, a new or an I Q for things that are built on top of it. Like a some landing. Sure. Just reuse. So value is not a discipline, but it's also. Of being us, I don't know us years in the industry. I can't think about validation. Us men, so some trap organizations can fall in. You know, it's right. Governance isn't after the doing it. It's hard if we're not. Well, Biden. I'm having part of, yeah, then, yeah, you're going to crumble equipment and spare. So the session is being recorded. Recording in progress. That that it is to me. Validation is something that's coming along through the process to make sure that everything's ready, so that as you get to the various gates and sprint cycles, that you know everything's green. Nobody's having to go back, you know, and deal with you know a failed audit or something. Doing everything in real time. So moving on here. No agent identity model and untraceable actions. I think that is something that is going to be the challenge for all of us in the industry. Is who did what, where, and the more we give it, the more connections we give it. Myself personally, you know, like you know, when it comes to business, we need to have, and be true. We need to have each agent actually become its own configuration per se. And I'll just. Give them in service. Yeah, how are we ever gonna audit that? I'm getting us okay. And then I just finally hear about you know one size fits all architecture. You know, causing some performance bottlenecks. And you know, really, there are things that can be done to make the performance you know better. There's things that we can do, you know, and I've seen teams that build beautiful pipelines, but you know, if no one is defined ownership or access tiers, it's it will not last long because it it won't be usable, it's sustainable. So make sure that whatever we do build for this, you know, our beautiful future system. That if we do need to break it down by domains, let's say you've got a really large business like my last company, perhaps you need to have that broken down by group or division because it's got its own security needs, and you know it's just another way to help deal with digital bottlenecks there. Okay, so what we can. And then, whatever, you know, practical roadmap. Right. So this week, you know, IAS and their owners, you know, create a system inventory of your data sources and their owners. Ask your IT team to export whatever they know. If there's a service now or some sort of, you know, database, yeah, pull that and then. In the things that aren't there, and I have a feeling that will be its own kind of fun exercise, which will will grow. But just having that identified and documented, then you'll be able to really see. Okay, is there one place that we could focus on? And it doesn't have to be, you know, the the you know. Solving everything, but there might be some things that are easier to agen identify than others. So yeah, take take a look. You think also your ermin would be inspection red, just given the fact that we know that our agents need to have of unique naming and on trivial access controls. You know, do you have that in place now? So I would take a look at that, and then you know, as as your, I mean, you know, cross-functional governance group. Because let's face it, if you don't have it, you need one, and it should involve all of the operations team members that are stakeholders here. So you've got IT, you know, QA, QC, manufacturing, whoever. Is you know a data stakeholder or you know a using group, make sure that they are part of that governance team, and then also define your data estate zones. And if there are classification standards that you can identify, that can make you know if you do need to wind up indexing and partitioning later, that could make that a lot easier. Covering from um and trying balance difficult. How do you land constantly moving? But I think that. Work right, and that's also where AI can help us. Is because if we're constantly chasing, maybe we can build some agents who have it. And you know, if we have a validation approach that's that we will document every version. So yeah, basically, as we move on, you know, this quarter I think then we would need to start working on implementing automated data quality checks. If there's a way that at ingestion you can templateize that data so that it's going to come in smoothly, that's going to make life so much easier, and just having that you know data quality straight and you know really the the get the get go. Your metadata catalog, your lineage tracking, you know, see how it goes. You know, see what your first reusable pipeline looks like from an external auditor perspective. You know, really start small, but but start with governance, and just make sure that you know you you plant the flag if you're using it, and we oh. Pull up bar. We know that we're we've got some risk there. So just knowing. What do they say? What was old G.I. Joe? They knowing is half the battle. So get to get maps. Get to get documented. Okay. So. Massive wide. Here is you know just some questions. Theme, you know. Don't you don't necessarily have to answer, but you know just some things to think about yours to building an EIT ready ready data data your organization. Is it something where you know there's so many different types of data? You know, does it need to be cataloged? Let's see. Yeah, and is there is there an agent, an AI agent within your company that has has its own identity and access tier, and how is that working, or not working? I'm honestly, you know, was one of the things that I've had challenges with. Is do I need to put my AI agent in workday, like in the HR system? Like basic things, because if you want to have it on your network, sometimes you gotta. It's interesting. So you balancing data reuse. You know, there's there's a lot of things where you know references, procedures, and change control. But yeah, if you can, you know, reuse across your pilot and then leverage that into something that's. You know, more structured and becomes validated in production. I think that will become, you know, your eventual data state. So, you know, before we close, I just want to bring us back to the core theme, you know, about the agentic era. You know, your data estate is your AI strategy. If the foundation isn't governed, validated, and reusable, everything built on top of it becomes fragile. Because pilots will stall, traceability breaks, and inspection readiness becomes reactive instead of continuous. So, what we walked through today—just ownership, access, tier, validation, and envelopes—based approach is they aren't abstract concepts. They're the in confidently across GXP today. So I hope this blueprint and action plan gives you something you can take back to your teams this week, this month, and this quarter. Start small. Start with governance. Build the estate once you can reuse it. Build the estate once so you can reuse it everywhere. So much for spending time with me. I appreciate the engagement. And if you've got any questions, feel please feel free to let me know. And if you'd like to continue the conversation, obviously connect with me on LinkedIn. Always happy to compare notes, share lessons learned, and always happy to hear about what you're building. So thank you so much.

## Related

- [[Data Foundations and Audit Trails MOC]]
- [[Home]]
- [[GxP systems are optimized to be inspection-ready, not insight-ready]] - the data-estate thesis
- [[Autonomous agents need their own auditable identities in regulated systems]] - the tier-4 access proposal

---

← [[2026-09-15-1112-ai-observability-evaluation-gxp-lecture|Observability and evaluation]] | [[Home]] | [[2026-09-15-1340-kenneth-corley-duran-scaling-ai-in-regulated-industries|Duran on scaling]] →
