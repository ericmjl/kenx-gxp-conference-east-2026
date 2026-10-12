---
date: 2026-09-15
recorded_at: 2026-09-15T13:40:44-04:00
duration_seconds: 1734
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: e7b73237765f08fd2972ba3b55485f3f
plaud_name: "09-15 Lecture: Scaling AI in Regulated Industries"
speakers:
  - Ganesh Muralidharan (transcribed as "Kenneth Corley Duran") of Vaisesika, the lecturer (diarized as Speaker 2)
  - Session host who read the introduction (diarized as Speaker 1)
  - Audience members (diarized as Speakers 3, 4, 5, and 6)
presenter: Ganesh Muralidharan
affiliation: "Global Delivery Head, Vaisesika Systems"
session: "Unite IT, QA, and Manufacturing to Drive Intelligent GxP Operations (day one, 1:40-2:20)"
tags:
  - kenx-gxp-east-2026
  - transcript
---
# Ganesh Muralidharan (transcribed as "Kenneth Corley Duran") on scaling AI in regulated industries

> Recorded 2026-09-15 at 1340 via Plaud. 28:54.

## Summary

A 29-minute lecture by Ganesh Muralidharan (transcribed as "Kenneth Corley Duran") of Vaisesika, a services firm working across software engineering, quality assurance, security, and data analytics, on why AI pilots stall before production in GxP-regulated industries. Duran frames the problem as the "AI Pilot Paradox": McKinsey life-sciences data shows 100 percent of leaders have experimented with GenAI while only 5 percent generate significant financial value and 75 percent lack a strategic vision, and BCG and World Economic Forum manufacturing data shows 68 percent have started implementing AI while 98 percent face scaling challenges and only 16 percent met their targets. His diagnosis is sequencing, not disagreement: Manufacturing asks whether the solution improves the operation and fits the real workflow (an audience member adds scalability), IT asks whether it can be integrated, supported, and maintained, and QA asks whether the output can be trusted, controlled, and defended. Because Manufacturing defines a need, IT builds, and QA reviews at the end, the result is rework, delays, and unclear ownership. He illustrates with a Vaisesika supply-chain procurement pilot that succeeded but hit exactly this wall when production development started.

The prescriptions: the Vaisesika 5C framework (Context, Criticality, Controls, Confidence, Continuity) as a shared language the three functions use before solution design; classifying each use case as Assist, Augment, or Automate so assurance is proportional to autonomy ("more autonomy means more rigor"); replacing the sequential Traditional Pattern (need, build, QA review, validate, deploy) with an Intelligent Pattern of concurrent assurance (design process, assess risk, build data and integration, assure with testing and evidence, monitor); and a Unified Intelligent GxP Delivery Model in which Manufacturing owns process context and acceptance criteria, QA owns quality risk, control strategy, and approval governance, and IT owns architecture, integration, cybersecurity, and lifecycle support, with shared ownership of intended use, data quality and lineage, validation evidence, and human oversight. He walks a six-stage enterprise journey (Experiment, Govern, Assure, Integrate, Scale, Optimize), five rules for intelligent GxP (start with the process, bring QA in at design, make Manufacturing the product owner, apply assurance proportional to risk, treat deployment as the start of the lifecycle), and six questions to answer at the requirements phase. In Q&A, an audience member asked why not merge the three functions into a single unit; Duran said client companies rarely accept it, with only one of ten Vaisesika projects achieving it, and the obstacles were globally distributed teams, manufacturing staff not understanding IT terminology such as acceptance criteria, and mismatched documentation depth. Another audience member described their organization's "IT business partners" model, IT staff with functional-area expertise embedded in quality, regulatory, and safety and delegating to project managers, as a working linchpin; Duran closed that regulated adoption needs shared confidence across the three functions rather than siloed work.

## Plaud AI notes

App-generated, verbatim from Plaud's Summary tab.

<!-- markdownlint-disable MD024 -->

Date Time: 2026-09-15 13:40:44
Location: [Insert Location]: [Insert Location]
Instructor: [Insert Name]: Ganesh Muralidharan (transcribed as "Kenneth Corley Duran")
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i1)
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i2)

## Summary

In this lecture, Ganesh Muralidharan (transcribed as "Kenneth Corley Duran") from Vaisesika explores the challenge of scaling AI from successful pilots to full production, especially in regulated sectors like life sciences and manufacturing. He introduces the "AI Pilot Paradox," where high experimentation contrasts with low value realization due to functional silos among Manufacturing, IT, and Quality Assurance (QA). The core issue is not disagreement but a flawed, sequential process that brings QA in too late. To address this, he proposes a shift from a "Traditional Pattern" to an "Intelligent Pattern" of concurrent assurance, where all three functions co-design the use case, controls, and evidence from the outset.
A central theme is breaking silos. The lecture explains the Vaisesika 5C framework (Context, Criticality, Controls, Confidence, Continuity) as a shared language to align teams. It also classifies AI roles into Assist, Augment, and Automate, noting that greater autonomy requires more rigorous controls and validation. The "Unified Intelligent GXP Delivery Model" is presented as a practical operating model that assigns clear ownership to each function while mandating shared responsibility for core elements like intended use and data quality. The talk concludes with a six-stage enterprise journey for AI adoption and five key rules for intelligent GxP, emphasizing that regulated AI requires shared confidence built through collaborative, cross-functional design.

## Knowledge Points

[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i3)
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i4)

### 1. The Challenge of AI Adoption and Functional Silos

- **The AI Pilot Paradox**
  - Highlights the gap between high AI experimentation and low, value-generating production deployments.
  - McKinsey data in life sciences: 100% of leaders have experimented with GenAI, but only 5% generate significant financial value; 75% lack a strategic vision.
  - BCG and World Economic Forum data in manufacturing: 68% have started implementing AI, yet 98% face scaling challenges and only 16% have met their targets.
  - Proofs of concept (POCs) often move quickly and succeed, but production adoption slows or fails.
- **The Problem of Functional Silos**
  - AI project failures often stem from silos among Manufacturing, IT/Digital, and QA/Compliance, which operate sequentially and answer critical questions separately.
  - **Manufacturing** asks about operational improvement and workflow fit ("Will this improve the operation and fit the real workflow?") and scalability.
  - **IT/Digital** focuses on sustainability—can the solution be integrated, supported, and maintained?
  - **QA/Compliance** is concerned with trust and control, questioning assurance, risks, and evidence ("Can we trust, control, and defend the output?").
  - The issue is the sequence of these questions. The traditional flow (Manufacturing defines need → IT builds → QA reviews at the end) leads to late QA involvement, rework, delays, and unclear ownership.

[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i5)

### 2. Frameworks for Breaking Silos and Managing AI

- **The Vaisesika 5C Framework**
  - A shared structure for Manufacturing, QA, and IT to use before solution design begins, creating a common language.
  - **Context**: Defines the specific process, decision, or activity the AI will support (e.g., an AI for SOP search versus one recommending a quality action).
  - **Criticality**: Assesses the impact if the AI is wrong or incomplete, distinguishing low-risk from high-risk cases.
  - **Controls**: Determines required technical, procedural, and human controls (e.g., review steps, audit trails, access controls).
  - **Confidence**: Outlines how to test and demonstrate sufficient performance—validation, traceability, and evidence.
  - **Continuity**: Plans for post-go-live monitoring of performance drift, data changes, and ongoing compliance.
- **Intended Use Framework (Assist, Augment, Automate)**
  - Classifies AI’s role, which dictates the required level of assurance and rigor. Start with the decision or activity to improve, not the technology.
  - **ASSIST**: AI summarizes, searches, or drafts; the human is the final decision-maker. Assurance can be lighter.
  - **AUGMENT**: AI analyzes and recommends; a human reviews and approves. Moderate autonomy.
  - **AUTOMATE**: AI initiates or executes actions with GxP impact. Highest rigor—stronger validation and formal control thresholds.
  - Principle: More autonomy demands more rigor in risk assessment, controls, testing, and monitoring.

[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i6)
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i7)

### 3. New Operating Models for AI Implementation

- **Shifting from Traditional to Intelligent Patterns**
  - Advocates changing the operating model to scale AI effectively.
  - **Traditional Pattern**: Sequential flow (Need → Build → QA Review → Validate → Deploy) that causes late questions, validation rework, and quality issues.
  - **Intelligent Pattern**: Concurrent assurance with assurance designed into the lifecycle from the start. Flow: Design process → Assess risk → Build data → Assure (test + evidence) → Monitor.
  - Key shift: QA, IT, and Manufacturing co-design the use case, controls, and evidence together, rather than QA approving a finished solution.
- **Unified Intelligent GXP Delivery Model**
  - Formalizes collaboration by assigning ownership while emphasizing shared responsibilities.
  - **Manufacturing**: Owns process context, user requirements, and workflow feedback.
  - **QA/Compliance**: Owns quality risk, control strategy, and approval governance.
  - **IT/Digital**: Owns architecture, integration, cybersecurity, and lifecycle support.
  - **Shared Responsibilities**: All three jointly own intended use, data quality/lineage, validation evidence, and human oversight—preventing AI from becoming another silo.

[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i8)
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i9)
[](plaud://image?type=summaryCard&id=oc_su_e7b73237765f08fd2972ba3b55485f3f_i10)

### 4. Practical Implementation and Way Forward

- **The Enterprise Journey: From Pilot to Operations**
  - Six-stage journey for scaling AI:
    1. **Experiment**: Run pilots and POCs.
    2. **Govern**: Classify use cases, establish policy guardrails, and define ownership.
    3. **Assure**: Implement risk-based validation and an evidence strategy.
    4. **Integrate**: Connect with enterprise systems (MES, QMS, ERP, LIMS).
    5. **Scale**: Develop reusable patterns, controls, and delivery pods.
    6. **Optimize**: Continuously monitor performance, drift, and improvement.
  - Progress from Stage 1 to Stage 6 requires cross-functional design and a managed AI operating model.
- **Five Rules for Intelligent GxP**
  1. Start with the process, not the AI.
  2. Bring QA into the design stage, not just for final approval.
  3. Make the Manufacturing team the product owner, not just an end user.
  4. Apply assurance proportional to risk.
  5. Treat deployment as the start of the lifecycle (monitoring), not the end.
- **Key Questions to Start With**
  - To shift AI from an innovation risk to a controlled capability, teams should answer six questions upfront:
    1. What is the intended use?
    2. What data does it rely on?
    3. What happens if it is wrong?
    4. Who reviews the output?
    5. How is performance tested?
    6. How are changes monitored?

## Questions

- [Insert Question/Confusion]

## Next Arrangements

- Coordinate a cross-functional design workshop with Manufacturing, IT, and QA to co-define the next AI use case, controls, and evidence approach.
- Assess current AI projects against the 5C framework and the Assist–Augment–Automate model to align assurance levels and control strategies.
- Establish governance guardrails and ownership for upcoming pilots, with QA embedded from the outset and defined monitoring plans post-deployment.

## Assignments

- [ ] 1. Evaluate your organization's current AI project lifecycle to identify whether it follows a "Traditional" or "Intelligent" pattern.
- [ ] 2. For an upcoming AI project, bring Manufacturing, IT, and QA together at the design stage to co-define the use case, controls, and evidence.
- [ ] 3. Apply the 5C framework (Context, Criticality, Controls, Confidence, Continuity) to an existing or planned AI use case to ensure all aspects are covered.
- [ ] 4. Classify your AI use cases using the Assist–Augment–Automate model to determine the appropriate level of risk-based assurance for each.

<!-- markdownlint-enable MD024 -->

## Highlights

<!-- markdownlint-disable MD022 MD024 MD026 -->

### AI Adoption Lag: High Experimentation Rates Fail to Translate into Scaled Production Success
The speaker presents a slide titled 'The AI Pilot Paradox,' using statistics from McKinsey and BCG to illustrate a critical business challenge: while AI experimentation is widespread, very few projects achieve their targets or scale successfully, a problem attributed to the difficulty of moving from pilots to real implementation.
• Visual Context: The slide shows that while 100% of life sciences firms have experimented with GenAI, only 32% are scaling, and in manufacturing, 68% have started AI implementation but only 16% have met their targets.
• Discussion Insight: The speaker explicitly defines the 'AI pilot paradox' by referencing the slide's data, explaining that companies can easily create successful proofs of concept, but struggle to convert them into real, scaled production implementations.
• Key Takeaway: There is a significant, industry-wide paradox where the initial phase of AI adoption (pilots and experimentation) is successful, but the crucial subsequent phase of scaling to production consistently slows down or fails.

### Speaker Analyzes AI Project Failures Caused by Departmental Silos
While displaying a slide that illustrates the distinct questions and concerns of QA, IT, and Manufacturing, the speaker explains that these functions working in silos, rather than in a proper sequence, is a primary reason AI projects fail to transition from pilot to production.
• Visual Context: The slide shows three separate organizational functions (QA/Compliance, IT/Digital, Manufacturing), their core operational questions, and the resulting problems when they are answered separately, creating silos.
• Discussion Insight: The speaker explicitly states that the core issue leading to AI project failure is not disagreement among these departments, but the 'sequence' of their involvement, which causes them to work in isolating silos.
• Key Takeaway: The failure of AI projects to scale from concept to production often stems from a flawed operational model where QA, IT, and Manufacturing do not collaborate from the start, leading to issues like rework, unclear ownership, and delays.

### Silos between Manufacturing, IT, and QA can result in a final product that doesn't serve its purpose.
• Speaker 2 explained that when Manufacturing provides a requirement, IT understands it differently, and QA tests it differently, resulting in rework, delays, and unclear ownership.
• This siloed approach contrasts with a proposed "Intelligen pattern" where Manufacturing, IT, and QA design the use case, controls, and evidence together from the start.
• To counteract these silos, Speaker 2's company Vaisishka has successfully implemented a "5C framework" (Context, Criticality, Control, Confidence, Continuity) to ensure all three teams use the same structure before a project begins.

### main point is about removing silos.
• Context: The discussion centered on why many successful AI pilots fail to scale to production. The core issue identified was the traditional, sequential handoff between siloed teams like manufacturing, IT, and Quality Assurance, which creates friction and rework.
• Key Insight: The root cause of failure isn't disagreement, but a broken sequence of work where teams with different priorities (operations vs. integration vs. trust) engage too late in the process.
• Risk Identified: Without a unified approach, AI projects will remain stuck in the 'AI pilot paradox,' where successful proofs-of-concept fail to achieve production adoption and business value.
• Decision: Adopt a unified delivery model where manufacturing, QA, and IT collaborate from the very beginning to co-design the use case, controls, and evidence requirements.
• Action Item: Consider implementing 'IT business partners'—subject matter experts embedded within functional teams like quality—to bridge communication and process gaps between departments.

### Explaining the Vaisesika 5C Framework for Unified AI Solution Design
The speaker elaborates on the visually presented 'Vaisesika 5C Framework', explaining how each component—Context, Criticality, Controls, Confidence, and Continuity—serves as a shared structure to align Manufacturing, QA, and IT teams before AI solution design begins.
• Visual Context: The slide presents the 'Vaisesika 5C Framework', which includes Context, Criticality, Controls, Confidence, and Continuity as key areas of consideration.
• Discussion Insight: The speaker details each of the 5Cs, providing examples such as using 'Context' to distinguish an SOP search chatbot from a quality action engine and using 'Criticality' to separate low-risk from high-risk cases.
• Key Takeaway: The primary goal of the 5C model is to act as a common language and workshop structure, ensuring that Manufacturing, QA, and IT teams are aligned before starting solution design, thereby preventing siloed development.

### 5C framework. I am seeing multiple mental frameworks in the broader conference. would be good to catalogue them.
• Context: The speaker introduced the 5C framework, a model for intelligent GXP (Good Practice), designed to ensure cross-functional teams start with a shared understanding of an AI project's purpose, risks, and lifecycle.
• Key Insight: The framework's primary goal is to break down silos between manufacturing, QA, and IT, which is a common cause of AI project failure in production.
• Key Insight: Context & Criticality: Teams must define a specific purpose for the AI and assess the impact of potential failures to differentiate low-risk from high-risk applications.
• Key Insight: Control & Confidence: Requires defining technical/human controls (e.g., audit trails, review steps) and establishing robust testing, validation, and traceability methods.
• Key Insight: Continuity: The model extends beyond launch to include post-go-live monitoring of performance, data drift, and user behavior to ensure sustained value.
• Action Item: Catalogue the 5C framework as a best-practice model for initiating cross-functional AI projects in GXP environments.

### AI Implementation Framework: Balancing Autonomy with Rigor
The speaker uses the slide to explain a framework for AI implementation, distinguishing between 'Assist', 'Augment', and 'Automate' functions to clarify that as AI autonomy increases, so too must the rigor of controls, testing, and monitoring.
• Visual Context: The slide presents a three-stage model for AI autonomy—Assist (human decides), Augment (human approves), and Automate (AI executes)—correlating higher autonomy with increased rigor.
• Discussion Insight: Speaker 2 elaborates that this classification is a practical way to manage risk, ensuring that low-risk 'Assist' use cases are not over-controlled, while high-risk 'Automate' use cases receive the necessary stronger validation.
• Key Takeaway: The fundamental principle discussed is to match the level of assurance and control directly to the AI's intended use and level of autonomy, a concept described as 'More autonomy → more rigor'.

### from assisting to augmenting to finally automating. these form a ladder. not everything is automated right from the beginning; not everyone wants automation either.
• Context: The discussion centered on creating a framework to classify AI use cases. This ensures that the level of control and validation applied is proportional to the AI's autonomy, preventing bottlenecks for low-risk applications and ensuring safety for high-risk ones.
• Key Insight: A three-tiered framework classifies AI roles: Assist (summarizing), Augment (recommending), and Automate (executing).
• Key Insight: The rigor of validation and controls must increase significantly as the AI's role shifts from assisting to full automation.
• Decision: Human oversight remains the default, with its level formally defined for each use case, especially in assistive and augmenting roles.

### AI automation requires stronger validation and more rigor when it initiates actions, triggers workflows, or executes tasks with GxP impact.
• Speaker 2 explains that AI's role can be categorized as assist, augment, or automate, with the required level of rigor increasing with its autonomy.
• For automation use cases where the AI initiates an action, changes a status, or executes a task with GxP impact, the control threshold becomes much higher, necessitating stronger validation.
• Properly classifying use cases ensures that low-risk scenarios are not over-controlled and high-risk ones, like automation, receive the necessary rigor, which is a practical way to speed up AI adoption.

### Shifting from Sequential to Collaborative AI Development Models
The speaker uses this slide to illustrate the shift from a flawed 'Traditional pattern' of AI development, which results in delays, to a superior 'Intelligent pattern' where QA, IT, and Manufacturing collaborate from the beginning.
• Visual Context: The slide visually contrasts a linear 'Traditional pattern' (leading to late questions and rework) with a cyclical 'Intelligent pattern' that integrates design, risk assessment, and assurance early in the lifecycle.
• Discussion Insight: Speaker 2 explains that traditional models fail because QA is involved too late, whereas the proposed intelligent model involves QA, IT, and manufacturing teams designing the use case and controls together from the start.
• Key Takeaway: The fundamental change proposed is to stop asking QA to approve a finished AI solution and instead have them collaborate with IT and Manufacturing throughout the entire design and build process to ensure built-in assurance.

### jfyi, the arrows are in reverse order wrt the points they progress.
• Context: The analyzed audio segment did not contain any discussion related to the specified topic or any other key business matters.

### co-design super important. need this to help build context over what’s going on.
• Decision: Adopt the 'Intelligent Pattern' for AI projects, shifting from a sequential process to a collaborative one involving Manufacturing, QA, and IT from the start.
• Action Item: Involve the QA team in the initial design phase to define quality risks and controls, rather than only at the final approval stage.
• Key Insight: This unified model establishes shared ownership: Manufacturing defines context, QA defines controls, and IT handles architecture, ensuring the final product meets its intended purpose.
• Risk Identified: A key challenge is overcoming communication barriers, as the teams use different terminology and have different documentation standards and availability.

### Unified GXP Delivery Model: Integrating Manufacturing, QA, and IT for AI Success
The speaker presents a 'Unified Intelligent GXP Delivery Model' slide, detailing how shared ownership and responsibilities among Manufacturing, QA/Compliance, and IT/Digital teams prevent AI projects from becoming dysfunctional silos.
• Visual Context: The slide diagrams a collaborative model where Manufacturing provides process context, QA/Compliance defines quality risk and control strategy, and IT/Digital handles architecture and integration.
• Discussion Insight: Speaker 2 argues that this unified approach is superior to the traditional pattern where teams work in sequence, which often leads to late-stage quality issues and rework.
• Key Takeaway: The fundamental principle is that shared ownership across all three functional groups—as illustrated on the slide—is essential to prevent AI from becoming an isolated, ineffective technology within the organization.

### Practical Application of an AI-Assisted Change Assurance Workflow
The speaker references the on-screen diagram of an AI-assisted change assurance workflow to illustrate how this integrated, multi-team approach was successfully applied in a recent supply chain project, enabling a smooth transition from pilot to production.
• Visual Context: The slide outlines a cyclical workflow for AI-assisted MES/QMS change assurance, detailing steps from 'Manufacturing need' through 'IT delivery', 'QA risk review', and final 'Approval + monitor'.
• Discussion Insight: Speaker 2 explains that this workflow is not just theoretical but a practical model his company uses, referencing a recent supply chain project where involving manufacturing, tech, and QA teams together from the start proved successful.
• Key Takeaway: The presented workflow, which emphasizes concurrent input from manufacturing, IT, and QA, is validated by the speaker's experience as an effective method for avoiding deviations when moving AI projects from pilot to production.

### Speaker Elaborates on Six Key Questions for AI Implementation
The speaker reviews the on-screen slide titled 'Way Forward', detailing the six critical questions that must be answered during the requirement phase to shift an AI project from an innovation risk to a controlled capability.
• Visual Context: The slide presents six foundational questions for AI projects, starting with 'What is the intended use?' and ending with 'How are changes monitored?'.
• Discussion Insight: The speaker explained that answering 'What happens if it is wrong?' helps classify risk and decide if the AI's role is assistive, augmenting, or fully automated.
• Key Takeaway: The core message is that addressing these six questions upfront transforms AI development from a risky innovation into a well-controlled, manageable process.

### this slide shows a recurring theme. intended use, data source..
• Context: A framework of six essential questions was presented as the standard process for planning and de-risking any new AI project, moving it from an innovative idea to a controlled capability.
• Key Insight: The most common mistake is starting with technology rather than first defining the intended business use, which dictates the necessary controls.
• Key Insight: The consequence of the AI being wrong determines its risk classification and whether its role is to assist, augment, or fully automate a task.
• Key Insight: Data quality, source, and lineage are fundamental, as the reliability of the AI's output is entirely dependent on its input.
• Risk Identified: Without clear answers to these six questions early on, AI projects are highly likely to face significant late-stage quality issues, rework, and delays.

### Mapping the Six-Stage Enterprise AI Journey from Pilot to Optimization
The presenter details the six-stage 'Enterprise Journey' for AI adoption shown on the slide, walking through the process from initial 'Experiment' and 'Govern' stages to full-scale 'Integrate', 'Scale', and 'Optimize' operations.
• Visual Context: The slide presents a six-stage roadmap titled 'The Enterprise Journey', illustrating the progression of AI initiatives from pilot experiments to sustained, optimized operations.
• Discussion Insight: Speaker 2 verbally explains each of the six stages in detail, starting with experimentation (POCs), moving to governance, assurance, integration with systems like MES/QMS, scaling with reusable patterns, and finally, optimization through performance monitoring.
• Key Takeaway: The core message, both on the slide and in the discussion, is that successfully transitioning from an AI pilot (Stage 1) to sustained operations (Stage 6) requires cross-functional design and a managed AI operating model.

### Speaker Elaborates on Five Core Rules for Intelligent GxP
A presentation slide visually outlines the "Five rules for Intelligent GxP," which the speaker then verbally explains in detail as a method to break down organizational silos and ensure successful AI adoption.
• Visual Context: The slide presents a five-step circular flow diagram detailing rules for intelligent GxP, including 'Start with the process, not the AI' and 'Bring QA in at design - not approval'.
• Discussion Insight: Speaker 2 dedicates a segment of the presentation (starting around 1364410 ms) to walk through each of the five rules shown on the slide, emphasizing that teams should not work in silos.
• Key Takeaway: The central theme, reinforced both visually and verbally, is that successful and compliant AI adoption requires a collaborative approach where Manufacturing, QA, and IT work together from the initial design phase.

## Transcript

[00:00] **Speaker 1:** Again, for those who are here this morning, sorry, just here for an intro. So, I'm here to introduce Ganesh Muralidharan (transcribed as "Kenneth Corley Duran"). Is a global delivery and quality engineering leader with 20 plus years of experience during driving enterprise scale delivery, keyway transformation, and Gen AI quality governance across banking, healthcare, life sciences, retail, telecom, and professional services. Specializing in making Gen AI production ready through LLM. Frameworks, automated AI validation pipelines, and governance models that ensures accuracy, relevance, consistency, and hallucination risk. In his current role, he leads global delivery QA strategy and GenAI initiatives with accountability for revenue margins, delivery excellence, and client satisfaction, while building global teams of 100 plus and establishing automation-first, CI/CD-driven validation engineering practices. His GenAI experience. Includes prompt evaluation, regression testing, output scoring, and continuous LLM validation using tools such as Deep Eval and REVAS. With experienced partners across business, engineering, and legal teams to support responsible AI adoption. He's held senior leadership roles at Vice, Sesca, System Consulting, Orion Business Innovation, Cap Gemini, NTT Data, EY. Whipro, Infosys, and Hexaware delivering global programs across the U. S., India, A. N. Z., and Europe. Okay.

[01:30] **Speaker 2:** Hi everyone. I hope I'm audible.

[01:35] **Speaker 1:** Good translation.

[02:02] **Speaker 2:** Am I audible? Yeah. Yeah. Thank you. So, just starting with the slides. So before I get into the nitty-gritties of the deck that I have to present, I just want to introduce my company. I won't take much time on it because you know that's not the aim of this discussion. Vaisishka as a company, you know, we have been involved in a lot of work in the software engineering space, quality assurance, security affairs. You know, data analytics, enterprise tools, and all that. The reason why I want to introduce the company is that we are well placed to discuss on how manufacturing, IT, quality assurance can jump together because we are working on projects in this manner. That's the idea behind this. There, that one slide about it. I'm just going to first slide. There is a. Primary point about this is the AI pilot paradox. You might have heard about this. You might have seen these matrices before. If you look at it here, I have just added some matrices from the McKinsey, where we see that you know there are hundred percent amount of experimentation going on, but how much of that is getting converted into real AI project deliveries? That's the data what we are showing, and also from a manufacturing perspective. We are just getting some data from BCG, where we are seeing that you know 68% have started implementing AI, and out of that, how much have they achieved? I mean, I mean, what percentage of projects have really reached the AI-related targets? So that means that there are challenges while we implement AI. That's what I like. So that's why we are saying this as AI pilot paradox, because you know. We are able to do pilot projects, but converting that into real implementations is what we are seeing as a challenge across the board for AI projects. Why? Because the primary reason would be that when we understand the data that is involved when we implement AI, right? How is that getting converted, or who reviews the output, who owns it? That's what we are looking for. You know, so that's what we are highlighting in this. So what we, the endpoint of this. Slide would be more into, you know, proof of concepts move fast, but production adoption slows down. More or less, I have been working on some of these AI projects for one of the scenario where we are working with supply chain procurement teams. We did a POC or a pilot for the team. The pilot was pretty successful, but when we plan to move into real production development, the challenge just started because, you know, the involvement of QA, AI. And the tech teams working together doesn't happen mostly. That is one of the reasons why we observe this. Proof of concepts are successful; they move fast, but production adoption is slow, or or sometimes it really fails. So, just coming back to three valid questions or three functions, right? This is more on why silos fall because you know the. Reason why we observe that some of these air projects fail is because there are three silos. What are the silos? Manufacturing. So manufacturing, what it does? That is the adoption question, right? Can we? Will this improve the operation and fit the real workflow? That means that a manufacturing team would ask, would there be any change in the? Suppose one question would be like, would the process improve? If I implement it, that question comes from the manufacturing side, and IT asks can we integrate, support and maintain this? So that means when we the sustainability question, right? That comes from the IT team. That okay, you build it, but can is it sustainable? Is it implementable? Can we build it for other teams? That question comes from the IT team, and the QA would ask from a trust and control part. They would ask that what is the assurance? That in a just DXP environment, we cannot simply say that AI looks impressive, right? We need to understand the use, the risks, the controls, the evidence. So the issue is not disagreement. The issue is the sequencing part here, right? You have manufacturing, you have QA compliance, and IT digital working together. They are not actually working. This is this leads to silos. So we are trying to build the sequence. That is okay. There is a sequence issue which is causing the disagreement, or you know. Lack of creation of silos. If manufacturing defines a need, IT builds a solution and QA reviews the end. That is how it typically happens. QA.

[07:02] **Speaker 3:** Yeah, just from the manufacturing perspective, you're saying, will this improve? I'm operational through and through, so I know that is a big question that we typically focus on. But the other thing that comes with manufacturing is, is it scalable, right? Yeah. So the scalability of it too. Sure that you've seen it, and the functions that you've watched it as well.

[07:21] **Speaker 2:** Just wanted to raise that. Yeah, that's true. Because that that occurs a lot. We have seen that happening. That manufacturing gives a requirement. IT understands it in a different manner. QA tests it in a different manner. When these silos happen, we find a final product which doesn't really serve the purpose, right? So that's what we are trying to highlight here. So it could lead to more of rework, delays, unclear ownership as well. So this slide has been more into that side of it, where we have just highlighting the three functions or three valid questions. Move the next one. So Viseshika as a company has built something called as a 5C framework for, I'd say, for intelligent GXP, where we we actually work in this manner for all of the things. So we have implemented this with our clients, where we start with the context part of it. The FISY framework has got five areas. Where one is context. Without context, the you know the AI discussion becomes too general, right? We have to understand for what context we are building a solution. So the context part of it would be you know suppose an example would be like a chatbot is built for search for SOP search, but it will very different from an AI engine recommending a quality action. So we should be very clear when we are documenting the context. And we are able to understand that okay, this this is the context we want to serve. Second part is the criticality, so criticality is more into what is the impact if AI is wrong or incomplete. So we want to highlight that second as okay. Criticality part would be more into suppose this helps us in suppose is in separating maybe low risk versus high risk cases. You know, third is control. That means. What kind of technical, procedural, and human controls are needed? So you know this could be like review steps, access controls, audit trails, approved data sources, and all. Fourth is confidence. So how do we test and demonstrate that the AI is adequately performing as intended? This is where the testing part comes in, right? So testing is very important part of the end-to-end delivery process. So we keep this as a very critical element because you know when the testing, validation, traceability, and evidence become important. And finally, the continuity. What happens after go live, right? So how do we monitor performance or data changes or drift as a real user behavior and changing time? So the value of the FISI model is that manufacturing Q and I T can use the same structure before they start building. So this is one of the frameworks which we have been implementing in our projects, and we have been seeing a lot of success in the five C model, where we put in a lot of effort to you know define all the five C's before we start on a project. So, just move on this slide. So, do not start with AI, right? So, what we, I mean, what what decision? One of the biggest mistakes organization make is. Starting with the tech part, and we have observed this happening with many of the projects we have handled. That they go with tech, they check, they start building it. Then they look at other aspects like QA or you know the the near workflow that comes in. So if AI is assisting, we have just highlighted that what decision activity are we trying to improve? So suppose there is assist, augment, automate. What is the role AI is playing in your project? Is it AI assisting you is AI augmenting for you, or is AI automating for you? So basically, what assist means is it it summarizes. Just a second. If AI is assisting, for example, by summarizing a SOP, searching control documents, or drafting a first version of a response, the human remains the decision maker. So the assurance model still matters, but it may be lighter because the AI is not making the final decision. So if AI is taking an assist role. The the human decides the final decision, right? Same way when AI takes the augment role, that is AI analyzes and recommends, human reviews and approves. So then it is more of an augmentation part process. Finally, when AI is actually doing the automation, that is AI initiates or executes actions, formal control thresholds, then it becomes the automation part of it. So if AI is automating, the control threshold becomes much higher. If the AI initiates an action, triggers a workflow, changes a status, or executes something with GXP impact, we get stronger validation. So more autonomy means more rigor, right? So this is also a practical way to speed adoption. When we classify use cases properly, we do not over-control low-risk use cases, and we do not under-control high-risk ones. So. We are just trying to highlight how the AI would work in a real-life scenario where you have an assist, augment, and automate part, and the kind of rigor that we want to implement. This more to you know from this more what we are trying to have the two operating models right that we have seen being followed in some of the projects. One is the traditional pattern. Where you have the AI depends on data. The sequence may look efficient at first, but AI depends on data quality. That is the first sequence. That is the traditional pattern, where you go with need, then build, then QA comes in, then they validate and they deploy. So result is late questions, late validation, quality issues, and all that. So these are traditional patterns that many of the projects we have seen happening with respect to AI as well. We have seen lot of AI projects failing due to this. The Intelligen pattern is in a different manner where you start with design a process that is designed to be more into process plus definition, and then we assess the risk, then we build data plus integration, assure, then the testing comes in and evidence gathering is done, and then the monitoring happens. So, the Intelligen pattern is what we try to implement in our projects because the traditional pattern is gradually causing a lot of you know delays. Or reworks, so that's the idea behind going with a new intelligent pattern of development that we kind of implement and use. So this is a operating model that we propose that we should gradually shift to. So the key shift here is that we do not ask QA to approve a finished QA solution, AI solution. Ask QA, IT, and manufacturer to design the use case, controls, and evidence together. So it is like a. This model, the new engine pattern, you have got the three teams working together. You have got QA, IT, and manufacturing working together and delivering the result. So that's the idea behind this pattern. So I'm just going to the model that we have been following in our company for the United Unified Intelligent EXP Delivery Model, where you have got manufacturing. Compliance or QA and IT or digital team working together, so shared ownership is what prevents AI from becoming another silo. So what it means is that manufacturer brings the process context here. They understand the real workflow. They come with the user requirements and the acceptance criteria and also the workflow feedback. So manufacturing basically works in that manner where they they actually are. Maybe I would say that they. They bring in the acceptance criteria for a deliverable, whereas quality team actually highlights the quality risks that comes to the solution. They are working to, I would say, as as one group, so that they highlight the quality risk. They have the quality control strategy in place. What would be the QA approach, and you know the approval governance as well. Who approves what? So that activities would be handled by the QA or compliance team, and Finally, the IT and digital team is more into designing the architecture and the integrations that come into the solution, anything on the cybersecurity side and the life cycle support. So, what it means here is that all these three teams are working together to come out with a unified, intelligent DXP kind of delivery model, and we have been seeing that this has been bringing us very good results in all the projects we have been doing right now. So, there are shared responsibilities between the teams. That is one is the AI intented user pretty much clear data quality and lineage comes up validation plan is very much well defined and the human oversight or human input is always defined and manufacturing part of it is also, manufacturing and change control is also handled. So what happens? So one advantage of this unified intelligent GXP data model is that shared ownership prevents AI from becoming another silo. So we have observed that this a pattern that we have observed from other projects that we have analyzed, and it has been good. Now, one of the practical scenarios which we wanted to highlight that, this more of a manufacturing need. We have just shown a scenario where we have got manufacturing coming coming out with the process context. This just an example of a MES QMS change. But I can also give from my experience of one of the recent projects that I'm in handling. We had a project where we had supply chain procurement and other manufacturing teams working with AI and the tech team. So we worked in this manner where we got all the manufacturing needs documented. Same time we had the tech team also come in and document their inputs, and the QA came in and came out with their own Ruth reviews. So that helped us in finally. Getting a very good IT delivery, and the testing was also well assisted and approved by the team. So, requirements, risk, test strategy, evidence, traceability, monitoring—this all into end was delivered at one go with good quality as well. So, when we moved from pilot to production, we did not find any. We did not encounter any major deviations from what we planned to. So that's the idea. That's a unified intellectual view. So the way forward. So when we start with the way forward, right? So first, these are some of the questions we should be asking. That's why we just highlighted these questions here. Like what is the intended use? Why we are building a solution, or what is the reason? If we cannot define how the AI will be used, we cannot define the right controls. So that is why the first question is why? What is the intended use? Second is what data does it rely on? So data quality, source, lineage, and access matter because output is only as reliable as input context. Third would be what happens if it is wrong? So, what this helps classify risk, and decide whether the use case is assistive, augmenting, or automated. So we talked about assistive, augmented, or you know, automated. So that can be decided in the if it is wrong part of it. Finally, fourth is who reviews the output. So who is owning the output of it? That is, human oversight must be clear. We typically define. When we are defining or when we are designing some solutions, the human-in-loop part is critical, right? So we want to highlight that. And how is the performance tested? We need to demonstrate that AI is good enough for the intended use, not perfect in every abstract scenario. Sixth is how are changes monitored? How are the AI behavior data, behavior sorry AI behavior data prompts integrations and usage patterns? So these keep on changing, and how are these changes? Going to be monitored. So these are the typical questions that we ask. Or when we are, you know, these questions should be answered at the requirement phase itself, from innovation to risk and control capability. So these questions are documented, and when we work with teams, we try to gather all these answers to most of these questions, so that we do not work on those in future. This is more into the enterprise journey from pilot to sustained operations, where we are just trying to highlight which of the stages we want to go with. You know, the first part is the experiment or the POC part of it, where you have an experiment. So we do pilots, and we have we run these pilots to showcase whether it is a doable solution or not, and and that is how the approach we follow in many of our projects. Then we go with the ground grounding part of it. That is at this point the automation needs use case classification and policy guardrails. We define the ownership and decision rights. Then we go into stage three, that is assure, that is risk-based validation and evidence strategy, where we try to gather all kinds of risks, CSA thinking, evidence strategy, and all that. Fourth is the integration part of it, so where we have integration with other solutions like MBS, CRM, so those integration comes into picture. Finally, there is a scaling part. That is, you need to have now the organization needs a reusable pattern, templates. So how can we scale the delivery? Finally, that comes up there. And the last is optimize. That is, when we optimize the solution and monitor the performance, drift, and continuous improvement. So this is an enterprise journey that we try to implement, and we have been implementing as well. So from POC to the optimizing stage, is what matters from a, end-to-end delivery perspective. So moving from stage one to stage six, so requires lot of course functional design and all that. Just highlighting how this entire enterprise journey would look like. So. So the five rules for intelligent Q&A start with the process, not the AI. That is the approach we follow. That you first define all the process. Do not try to build AI first. Bring QA in at the QA teams should be inaudible from the beginning and not at the approval stage or not at the validation stage because that is the only way that QA can highlight the risks that coming when the actual delivery or when the actual build happens. Mac manufacturing a product owner, not just an end user. Yes, so the manufacturing team, which gives us the acceptance criteria, they should own the entire flow. They can give us the exact requirements and documented. And finally, apply assurance proportional to the risk. So we have to have the proper assurance process in place so that we understand which which areas are high risk, low risk, and how should it should be managed. And finally, you should look for target deployment as a beginning note there. Post deployment, you have the activity of monitoring and the delivery. So those things are monitored and delivered. So this is more into breaking the silos, building the confidence and scale laterally. So these are the five rules that we try to follow, and we have been following in some of the projects, and we have seen good results as well. Where instead of be working in silos. So yeah, I have just covered most of the content I have. So the main point I want to leave with you is simple: that AI can act, can move fast, and you know. But regulated adoption needs shared confidence. That means that the teams should not be working in silos; they should be working within as a group, where we have the AI team, the I would say the manufacturing team, and the QA team working together to deliver the final result. So that's about it from my end. Any questions.

[24:43] **Speaker 4:** I can ask? I've got a question. It's a bit organizational because what I'm reading from your presentation is we gotta get three groups, each with different interests, together. Maybe this is a little bit of a provocative question, but why not just make them one unit? You know, one. Organizational group, rather than having them cross - functionally come together. Yeah, it's provo provocative on on purpose.

[25:20] **Speaker 2:** But the companies that we have been working with, we have seen that manufacturing was three teams.

[25:26] **Speaker 4:** Exactly.

[25:27] **Speaker 2:** Which doesn't connect with IT at all, understood? Or QA and IT maybe work together, but they can't be the same group. Yeah. So that's the one challenge we have observed that. You know, companies do not agree to have building this as a single team and working together. But in one of the cases for one of the client projects, we did that actually. We brought in the manufacturing team to come with their requirements first, so that the POC can be built in that manner. Where we had a supply chain solution, which was being built by the manufacturing team. The AI team came with their solution, and the QA and other IT-related teams came together. So this one group building groups is possible, but. It's rare that we have seen, out of the ten projects, we have handled one project at that situation.

[26:08] **Speaker 4:** What kind of challenges did they have to overcome to be able to work together?

[26:12] **Speaker 2:** Getting time from the manufacturing team was one time. Time was there because these people are located in different parts of the globe. First of all, secondly, they never understood the IT terminology. So we have seen scenarios where the IT guys were saying that I mean. We need your acceptance criteria and the business. Sorry, the manufacturing guys. I don't understand what is an acceptance criteria. So sometimes that happens, and and again, the level of documentation that a IT project needs is very very different from how the manufacturing team comes out with. Right, you come with requirements, you have the VRS, and then the user user stories, then the acceptance criteria. And the threshold that the AI team wants from an output from this system, right? That it's very hard for these people to understand. The manufacturing guys to understand. So that's one of the reason we never worked. But one of the projects did work out like that, and it has been a success. We did the pilot with them, and we've delivered the project as.

[27:19] **Speaker 5:** Well with them. Thank you. May I ask about, So we faced the same challenge at our organization, getting all the multiple functional areas to sit down and talk to each other. And IT was that interface. So what we decided to implement was what we call IT business partners. So they're IT team members who have some level of SME within those functional areas, like quality, regulatory, and safety. And then they sit within those different functions, listen to their meetings, listen to their projects that they have going on. And we're able to serve as that linchpin to bring everyone together when we're hearing the multiple conversations throughout the room. Then, underneath that, what we have is project managers underneath our business partners. So our business partners can then delegate to a project manager to say, "This is the task that needs to be done. Bring these three teams together. They all need to talk about how we're going to implement this new batch release module and get all the stakeholders in one room." So we we face that problem and and. It seems to be working for us. Having that business partner rule established within the IT team, having project managers there to help.

[28:30] **Speaker 2:** Cool. Thank you. That's a good experience we have. Any other inputs? Any questions?

[28:37] **Speaker 6:** Thank you so much.

## Related

- [[Strategy Scaling and Product MOC]]
- [[Home]]
- [[AI pilots in GxP fail on sequencing, not technology]] - the 5C framework and unified delivery model

---

← [[2026-09-15-1201-shelly-lapointe-data-foundation-for-ai-in-gxp.md|LaPointe on data foundation]] | [[Home]] | [[2026-09-15-1426-abhishek-ai-acceptance-criteria-gxp-lecture.md|Abhishek on acceptance criteria]] →
