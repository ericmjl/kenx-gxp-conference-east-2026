---
date: 2026-09-16
recorded_at: 2026-09-16T10:50:00-04:00
duration_seconds: 1002
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: of_b90aca5ab23a7264b7145ed58f0ffc53
plaud_name: "09-16 Consultation: Eric Ma - AI/LLM GxP Validation Platform for Clinical Development"
speakers:
  - Eric Ma
  - Speaker 1
tags:
  - kenx-gxp-east-2026
  - transcript
---
# GxP validation platform consultation with a vendor

> Recorded 2026-09-16 at 1050 via Plaud. 16:42.

## Summary

> Eric evaluated a vendor's AI-enabled GxP validation and quality platform at a conference booth, relevant to his move from preclinical research into overseeing a clinical development data science team. The platform covers the validation lifecycle end to end: system definition, a 47-question risk assessment that AI drafts in seconds for human review (the team effort it replaces takes about a week), requirements generation, AI-proposed test scenarios converted into executable Playwright scripts with dry-run support, evidence capture with per-step screenshots and execution video, and automated defect raising with root-cause proposals on failure. Supplier qualification, incident management, and periodic review round it out, all AI-assisted.
>
> For AI systems specifically, the platform defines AI entities with model cards, supports private LLM configurations, sets continuous-monitoring frequency, tracks token usage and KPIs, and runs scheduled evaluations against golden datasets from the backend. The vendor's flagship claim: an EKM system implemented and validated in 48 hours against a typical 40-to-45-day cycle. Eric's open question for his own context is that every LLM paired with an application carries distinct KPIs and evals run in different places, and he wants them centralized.

## Plaud AI notes
<!-- markdownlint-disable MD033 MD026 -->

<App-generated notes from the Plaud cloud, verbatim.>

> Date & Time: 2026-09-16 10:50:00
> Location: [Insert Location]
> Customer: Eric Ma

### Overview

Eric Ma, a data scientist newly overseeing a clinical development data science team after five years in preclinical research, explored a vendor’s AI-enabled GxP validation and quality platform. The discussion covered end-to-end computer/system and AI validation, supplier management, incident management, periodic review, automated testing, continuous monitoring for AI/LLM systems, KPI/evaluation configuration, and significant time reductions via AI. Eric’s primary interest is how LLM evaluations, KPIs, and automated test/monitoring workflows integrate with clinical development use cases, with the outcome of connecting the vendor to his organization’s quality team for a deeper demo and potential adoption.

### Background

- Participant: Eric Ma, a data scientist based in San Bernardino; recently assumed leadership of a clinical development data science team, transitioning from a preclinical, non-GxP environment.
- Vendor offering: An AI-enabled platform covering system definition, risk assessment, requirements generation, test scenario/script generation, automated/manual test execution with evidence capture, automated defect handling, supplier qualification/audits, incident management, and periodic reviews. Includes AI/LLM validation features (model cards, KPI setup, token usage tracking, continuous monitoring, automated evaluations via backend scripts).
- Notable claim: An EKM system implementation/validation cycle that typically takes “40 to 45 days” was completed “within 48 hours” using the platform, leveraging AI acceleration and automated workflows.
- Next steps implied: Eric to introduce the vendor to his organization’s quality team for a detailed online demo.

### Pain Points

[Pain Point 1: Transitioning from non-GxP research to GxP-aligned clinical development practices without established validation processes]
Eric’s team is moving from a preclinical, non-GxP context to clinical development where **GxP validation, supplier qualification, incident/periodic review, and AI/LLM controls** are required. Impact: Potential compliance gaps, slow adoption of validated processes, and risk of misaligned practices as the team scales clinical activities. Current Situation: Eric lacks direct quality ownership and intends to route the vendor to the quality team; he seeks understanding of how LLM KPIs/evals integrate with application workflows. Quantitative Metrics: None stated for his team; the vendor cites reductions from “40 to 45 days” to “48 hours” in a referenced EKM validation case. Examples: Eric’s questions about when LLM evals run, KPI configuration, and backend test scripts show uncertainty around standardizing evals within compliant workflows. Context: New to GxP; needs frameworks, tooling, and cross-functional alignment with quality. Stakeholders: Clinical development data science team, Quality department, SMEs across business units.
[Pain Point 2: Standardizing and automating LLM evaluation and continuous monitoring within clinical applications]
Eric noted that every LLM paired with its application has **distinct KPIs and separately run evals**, creating integration and observability complexity. Impact: Fragmented evaluation processes, difficulty comparing performance across runs, and potential blind spots in production monitoring. Current Situation: Evaluations are run in different places with golden datasets and API calls; Eric seeks to centralize KPIs/evals and reporting. Quantitative Metrics: The platform mentions tracking **tokens** and usage; no specific numeric KPIs from Eric’s environment were provided. Examples: Source grounding evals via API against golden datasets; need for per-run reports and test scripts capturing exact prompts. Context: Desire for configurable KPIs, scheduled/triggered runs, and evidence-backed reports aligned with quality expectations. Stakeholders: Data science team, Application owners, Quality/Validation teams.
[Pain Point 3: Lengthy, multi-team risk assessments and validation artifact generation]
Traditional processes like **system risk assessment (e.g., 47-question industry-standard questionnaire), requirements, test scenarios/scripts, and reviews** are **team-dependent and time-consuming**. Impact: Weeks-long delays to reach a validated state; resource-intensive cross-functional coordination. Current Situation: The vendor indicates AI can draft assessments in seconds, with human review taking “few hours to few days,” reducing the typical week-long effort. Quantitative Metrics: Industry questionnaire with “forty-seven questions”; typical validation cited as “40 to 45 days” vs. “48 hours” achieved in a case using the platform. Examples: Automated defect creation, evidence capture (screenshots per step, execution video), and self-healing script updates. Context: Clinical development timelines benefit from faster validation cycles without sacrificing evidence and auditability. Stakeholders: Quality department, SMEs, Data science and engineering teams, Compliance.

### Expectations

[Expectation 1: Secure a detailed online demo for the Quality team to assess fit for GxP validation needs]
Goal: **Facilitate an in-depth demo** covering end-to-end validation (risk assessment, requirements, testing, monitoring) and AI/LLM controls to determine suitability for clinical development workflows. Timeframe: As soon as scheduling permits after 2026-09-16 10:50:00. Resources Required: Vendor demo environment, sample artifacts (e.g., approved assessments, test scripts, reports), quality and SME attendees. Success Metrics: Quality team’s positive evaluation and defined pilot scope. Stakeholders: Eric (introducer), Quality team (primary), Vendor team (presenters), SMEs.
[Expectation 2: Define how LLM KPIs and evaluations integrate with application workflows and reporting]
Goal: **Define KPI configuration, evaluation cadence, scripting, and reporting** that align with clinical use cases and quality standards. Timeframe: During/after the detailed demo following 2026-09-16 10:50:00. Resources Required: Example golden datasets, API eval scripts, KPI catalogs, dashboard/report samples. Success Metrics: Agreed list of KPIs, documented eval schedules/triggers, sample reports meeting audit needs. Stakeholders: Data science team, Quality/Validation, Vendor solution architects.

### Other Information Summary

- The platform supports defining AI entities and model cards, including private LLM configurations and continuous monitoring frequency settings.
- Automated evidence capture includes per-step screenshots and overall execution video, with automated deviation creation and root cause proposals upon failure.
- Supplier management includes initial risk assessment, categorization (high/medium/low), audits or questionnaire-based assessments.
- Incident management and periodic review modules are AI-enabled to reduce cycle times from weeks/months to minutes/hours.
- Test scenarios and scripts can be AI-generated and executed manually or fully automated (e.g., Playwright), with dry-run options.

### To-Do List

- [ ] Introduce the vendor to the Quality team and schedule a detailed online demo. Stakeholders: Eric Ma, Quality team, Vendor. Deadline: propose times within 1 week of 2026-09-16 10:50:00.
- [ ] Prepare sample use cases and golden datasets for LLM evaluations to review during the demo. Stakeholders: Data science team, Quality. Deadline: before the scheduled demo.
- [ ] Request that the vendor share example validated artifacts (approved risk assessment, requirements, test scripts, execution reports, deviations). Stakeholders: Vendor, Quality. Deadline: prior to the demo.
- [ ] Align on a preliminary KPI list for LLMs (e.g., grounding accuracy, hallucination rate, latency, token usage) and desired reporting cadence. Stakeholders: Data science, Quality, Vendor. Deadline: during/after the demo.
- [ ] Determine pilot scope (system(s) in clinical development to validate) and success criteria. Stakeholders: Quality, Data science, Vendor. Deadline: after the demo.

> AI Suggestions
> The AI has identified the client's biggest pain point as Transitioning from non-GxP research to GxP-aligned clinical development practices without established validation processes. Here are some possible solutions for your consideration:
>
> 1. Establish a lightweight GxP validation framework tailored for AI/LLM-enabled applications, including templated SOPs for system definition, risk assessment (covering the 47-question set), requirements, testing, incident management, and periodic review.
> 2. Run a time-boxed pilot using the vendor’s platform on one clinical application to validate end-to-end: configure model cards, KPIs, golden datasets, automated test scripts, continuous monitoring, and evidence capture; compare cycle time vs. current approach.
>
> 3. Create a centralized LLM evaluation registry and KPI catalog so each application-LLM pair has standardized metrics, schedules, and reporting, integrated with the platform’s dashboards and automated reports.
> 4. Implement a governance workflow with human-in-the-loop reviews: AI-generated drafts (assessments, tests) produced in seconds, followed by documented SME/Quality approvals to satisfy auditability.
>
> 5. Develop supplier qualification and change control checklists for AI components (e.g., model/version changes, prompt/template updates) tied to automated re-validation triggers to maintain continuous compliance.

<!-- markdownlint-enable MD033 -->
## Transcript

[00:02] **Eric Ma:** Hey , Hey! I stopped by yesterday. Exactly, I was looking for you. I know. I am sorry about that. I had to like go to ten stores. I'm sorry about it. I couldn't get that. How you doing? Good, good. Are those the glasses? Yeah, they they have a little yeah display on there. Yeah, that's amazing. It's amazing. And is it is it useful? Wait, is this the? Which one is it? Is it the? Is it reality? How good is it? I've been looking at that. Yeah, it's good. Put it in sleep mode. Sleep mode now. Okay. No,

[00:31] **Speaker 1:** That's fine. It has translation too. They have a latest version. That is much more. Okay. Okay. Compared to what I have, you can install additional applications and all those things. Wow. Mine is an earlier version. Earlier. That's all the translation. You can take notes, and you have your own even AI. That's cool. And you can ask some questions to that, and it's going to answer you. Wow. You can get some good Hindi transcript and all those things, and yeah. That's cool.

[00:58] **Eric Ma:** That's really cool. I can see the screen there. It takes a lot. How do you do that? Do you look up or just do it?

[01:09] **Speaker 1:** That is really cool. If you get any notification, then you would be.

[01:17] **Eric Ma:** If you get any notification, any call, anything, it'll just pop up. That's amazing. That's amazing. Anyways, we didn't come here to talk about this. I'm just curious what you guys are all about. That's all. I haven't. I'm new to the GXP space, so it's like. So what are you doing? I'm actually a data scientist. I work in San Bernardino, and for the past five years, I've been actually in the research space, completely preclinical, no GXP, no nothing. This year, I took over a team, a second team, to which is the clinical development data science team. And so that's what I'm curious about. We do custom.

[02:03] **Speaker 1:** Validation for it. Validation, valid for AI native custom validation, logical validation, custom validation. So we can perform all the validation activity end to end, right from the application till the requirement. Just search from which part. The system definition, system definition, definition, system risk assessment, risk assessment, and then requirement generation, requirement generation, requirement ah risk assessment, okay, design, yeah, ah test scenario generation, oh wow, test script generation, yeah, and test exi automated test execution, and in case of failure, that will automatically raise a test defect. Oh, okay, and during the execution, it will capture all the evidence automatically. Yeah, and the. We also have supply management. We also have supply management. Supply management. What's that all about? Because any supplier, any vendor, or any third-party supplier who is going to provide a service to a GXP company, a pharma, medical device, or So they will have to be qualified. The supplier will have to be qualified. So the suppliers will be audited. Okay. The supplier first, they will have a initial risk assessment on the supplier. So they, based on the services the supplier provides, yeah, they'll categorize the supplier if they are high risk or low risk or medium risk and so on. Yeah. Based on that risk level, they'll go and perform an audit on the supplier. Okay. Or they'll perform a questionnaire assessment of the electricity. Ah, okay.

[03:30] **Eric Ma:** And then that's where the management side.

[03:33] **Speaker 1:** That that's the supply management. Okay. So it's it's part of quality department. Okay. Okay. So that's one, and we have supply management, and then incident management, and periodic incident management, and periodic review as well, and periodic review. And all these model, whichever I said, everything is enabled with AI capabilities. Oh wow! So all the activities, whatever I said, it took many weeks or months long in the past. Yeah, yeah. Now with all AI capabilities, you can do it within few minutes, few hours. Okay, that's cool.

[04:03] **Eric Ma:** That's cool. Were you involved prior to Valorant, where you doing this?

[04:09] **Speaker 1:** Yeah. Me and co - founder, so we are a PSP consultant. Yeah, we have been working for about 20 plus years now. Yeah, and then out of all our experience that we had, we converted our experience as application and we do it there. So with all the latest guidelines, with all the latest technologies and changes, what's happening with that? So we came up with the. Oh, cool, cool,

[04:35] **Eric Ma:** Cool. What does it look like? Just out of curiosity.

[04:42] **Speaker 1:** Yeah . So here, here we would be able to add widgets and say it's going to be user specific. We can have how many of our which style we would like to look at, and then we can have all the systems defined. So, so starts starts with systems. Is that correct? So when we design, define a system, or it could be a computer system, any software or AI, for example, you can define all those. And the internet is pathetic here. So when when we have the system defined, so the system will have to be risk assessed first. And for that purpose, we have a questioner with which we would be. As questioner, we would be able to assess that one for the questions to be assessed. So we have industry standard questions of about forty-seven questions we have identified. But to complete that forty-seven questions, it'll take at least a week or so because it's going to be a team's effort. So every different business unit will get involved, quality department will get involved, SMU will get involved, all these. So instead of week-long effort, so discussions and all those, you can perform the assessment with AI. That's going to get completed within few seconds. Okay, okay, it's a draft, and human will have to review and confirm and approve. So the draft itself is going to take few days, few hours to few days time, based on the team and complexity of the system. Yeah. But you get it within few seconds until the review process gets. Yeah. So eventually, even if even if it's going to be a one day full day of review, ultimately you reduce five days of effort.

[06:25] **Eric Ma:** Totally. Totally.

[06:26] **Speaker 1:** So similarly, you get to requirements.

[06:28] **Eric Ma:** Can I take a look at what one of these might look like? For example, an approved one like that.

[06:46] **Speaker 1:** SAP You will be able to put the rest. I'm guessing the description was auto-generated. It's all example. Yeah. In a real one

[06:55] **Eric Ma:** Though.

[06:56] **Speaker 1:** In a real one, it'll be a bit more elaborate.

[06:59] **Eric Ma:** Of course

[07:01] **Speaker 1:** Of course. We can have the system information, supplier details, and you can say what it is. And then if we have AI, if we we can define AI entities as well. AI, this is going to be a model card, so we can define AI. What is the type of AI that we would like to have? What is the type of AI that's within the system? Yeah, and what are the capabilities? We can put them here, and then we can also say if the provider, we can also say custom. Yeah. So then we can provide all the details for the private LLM model if the organization has their own LLM. Yeah. To put that. Yeah. And we can set frequency by when by when the. Continuous monitoring will have to happen. Yup. So once we set it up all, and then for that particular system, we have so under the AI validation module, for example. So here we will be able to see the automatic testing that happens at the backend, continuous monitoring of your AI and LLM that happens through Valid Core, and it will keep performing all these activities and keep highlighting you what's happening is. Is the AI under control? Is it within your limits? And have you set it up? And everything looks fine, and all those. So it'll be here. You'll be able to see them.

[08:19] **Eric Ma:** And the reporting. This dashboard looks really neat because it's got different performance metrics or an LLM and that sort of stuff.

[08:29] **Speaker 1:** You can still add how many hours you need. You can still add how many hours.

[08:34] **Eric Ma:** I guess what I'm what I'm curious though is like each. Because each LLM, every LLM in paired with its application has its own KPIs, and the evals are run separately in in different places. Like, how do you like how do you how do you pull that in? You can set the KPIs.

[08:59] **Speaker 1:** Here through the computer. So here we also have how much tokens have been used and how much usage of AI is. Yeah, yeah, yeah. So here. So you can you can add additional categories here. Yeah, on top of whatever we have proposed as per industry standards, you can add on top of that one. Yeah, and then here you would be able to put those KPIs, and you can put those metrics.

[09:22] **Eric Ma:** And when when did when are the LLM evals run? Which one? Like so, every time we do, yeah. Say for example, let's go back to the main dashboard. Go back there. So backing, say for example, source grounding. This is this is an example. We have to go and execute API calls against the golden data set and that sort of stuff.

[09:56] **Speaker 1:** You will be setting it up all under testing activities. Ah. You will already put them there, and you will have the setup ready. So that's going to perform at the backend. Ah, that will keep running. That will trigger. That will keep running, and that will execute, and that will continuously monitor and do all these.

[10:15] **Eric Ma:** Things. I see. So there's a script. There are test runs. And for each run, there's test reporting. The script is each of the exact LLM prompts that are put in order

[10:47] **Speaker 1:** Right?

[10:49] **Eric Ma:** Cool. Cool.

[10:52] **Speaker 1:** That's neat. What else is there? And you also have the test management, for example. Yeah. So here, under the test management, so test scenarios and test scripts can be generated with AI. And when, when you provide, when you feed the system information and the requirements for which you would like to perform a testing, so the AI would be able to come up with test scenarios, and it's going to propose test scenarios so you can review and confirm which test scenario you would like to proceed, and then that test scenario can be converted as full automated test script. Ah, executable test script. Okay. Or you can execute it manually. Yeah. Or we can also have it as an automated test script so it can be. Performed and tap button, so it's going to help that way. Yeah. Yeah, we'll see how. And so, test scenarios and test script preparation itself would take few weeks to month long for complicated system. You can get it done maybe multiple round of cycles and all those. Yeah. Iterations, reviews. Maybe in a couple of days or so, and then having a re-review and then any changes and all those. Even the changes could be performed with AI itself. Yeah. Self-healing issues and all those. Yeah. Yeah. That's really cool. So again, once everything is set, the execution itself is going to be much more quicker. Let me show this one.

[12:18] **Eric Ma:** Probably the last one because I do want to go to the top coming up.

[12:22] **Speaker 1:** This one is an example that has been generated by AI itself. It provides a complete human readable script.

[12:35] **Eric Ma:** Submit the form.

[12:37] **Speaker 1:** Yeah, yeah. You can perform the execution manually. Yeah, or you also have a full automated test code. Yeah. So that's going to provide a complete automatic play right and that sort of stuff. Exactly. Yeah. Okay. Cool. Cool. So that's going to provide and you can you can complete the execution. So you have the code here. Yep. So you can just. That's awesome. Perform the execution. Just trigger the execution, and click click the button. It's going to show. Once once we click the button, it's going to show. This.

[13:10] **Eric Ma:** The other one. I guess there's the dry run button you can use, try it, or is that right?

[13:19] **Speaker 1:** Or yeah, dry run is a luxury. That's up to us to use it or not. Ah. So if if we have this dry run usage, yes, then we get to know if the script is okay. If there is something that we would have to modify or something like that, and for the test execution itself, we would be able to do that when with the other one. Say for example, so I'll show this one. So, so here we have start order execution. If we click this one, it's going to prompt for some details. So something that needs to be entered. They are going to be different for each and every execution. Yeah. So once we provide that, and the execution will start. Okay. And this is how it's going to look like. So in case of. Execution, so it's going to perform the execution. If it does something, then yeah, yeah, you get those things done. Yeah, cool. And in case of execution, fully automated, automated execution, so it'll be able to perform all the execution with screenshots attached for each and every step, and video evidence attached for overall execution. Yeah, and in case of failure, it's going to Raise automated test deviation. Yeah, and it's going to propose all the root cause and all those stuff. Oh, that's cool. That's really cool. So we were able to complete almost a few. Usually, it takes 40 to 45 days, at least 45 days of effort, for EKM system to be implemented, validated, and be completed in house within 48 hours. Okay. We did. We we said that okay, the team is going to be on sync. This is the plan. You guys have forty eight hours. You will have to get it done. And they used all the full potential of Alacord. Yeah. And they started system. They created system risk assessment. Yeah. Requirement generation, test generation, test execution, and all those things. They got it review cycle, review, approval, and everything was completed. And they got it done within forty eight hours.

[15:24] **Eric Ma:** Wow, that's impressive. That's really impressive. That's cool. All right. Thanks, guys. Appreciate it. Thanks for thanks for showing. Sorry. You can do a more detailed demo if you like. Like all online, if you are more. Yeah, I'll I'll probably like refer you guys to the quality team that we have. Sure. Because I'm not personally on quality. Okay. So I'm a data scientist. Like we kind of just do crazy stuff. Um, but this looks pretty pretty cool. Yeah. Could be good for them. Cool stuff. All right. Yeah.

[16:25] **Speaker 1:** Okay, yeah. Let me know and talk to your. You can introduce us to your quality team. No commitments. They could just have a look at it and probably that could benefit them. Yeah. Okay. So, all right. Thanks, guys. Appreciate it. Happy to talk to you.

[16:41] **Eric Ma:** Yeah.

## Related

- [[Home]]
- [[Eric's Field Notes MOC]]
