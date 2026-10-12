---
date: 2026-09-16
recorded_at: 2026-09-16T11:07:24-04:00
duration_seconds: 1540
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: of_c794a6f1aed761b15df56d4d0e44b91a
plaud_name: "09-16 Lecture: GxP-Compliant AI/ML Implementation Framework with QMS, HITL, and Audit Readiness"
speakers:
  - Speaker 1
presenter: "Robert (Bob) Wherry, MSc, MS"
affiliation: "VP, AI Compliance, QACV Consulting"
session: "10 Steps to Achieving AI Regulatory Compliance (day two, 11:00-11:40)"
tags:
  - kenx-gxp-east-2026
  - transcript
---
# Ten-step framework lecture for GxP-compliant AI/ML implementation

> Recorded 2026-09-16 at 1107 via Plaud. 25:40.

## Summary

> A ten-step framework for adopting AI/ML in GxP organizations, each step framed as an issue observed across client audits and then a remedy: an authorized-use policy (prohibit public AI tools for GxP and confidential data, require disclosure when AI was used, bar AI as a substitute for work); strategic piloting with lessons-learned cycles and honest budgeting for tokenization costs; regulatory literacy (over 120 regulations, guidances, and standards exist; put quality and regulatory SMEs on development teams from the start); a formal development lifecycle with SOPs and templates; dedicated dataset-development and model-development SOPs (pin public models, bound the inputs); procurement controls with GxP and risk assessment plus an AI inventory; QMS integration with quality-gate checks; documented human verification under the motto "Never Trust! Always Verify!"; explicit handling of the four variability sources (model, infrastructure, data environment, human); a validation-verification spectrum (validate what you can, verify the rest against statistics-based performance metrics); and a documented assessment of AI tools against the FDA's guiding principles. The bonus step: have an SME run a mock audit, close gaps, then run the formal audit.
>
> Two case studies anchor it: the Purolea warning letter, which notably omitted the actual human-verification regulation it violated (21 CFR 211.68(c), in force since 2008), and the MHRA inspectorate blog by Peter Brown (June 29, 2026) holding companies responsible for AI-drafted inspection responses regardless of the drafting tool. Asked from the floor whether AI SOPs should harmonize with the software development lifecycle, he pushed back: the two are fundamentally different, and force-fitting AI into software frameworks is a square peg in a round hole.

## Plaud AI notes
<!-- markdownlint-disable MD033 MD026 -->

<App-generated notes from the Plaud cloud, verbatim.>

Date: 2026-09-16 11:07:24
Location: KENX
Instructor: [Insert Name]

### Plaud summary

<mark style="background-color: #F9EDD4">This lecture series outlines a comprehensive ten-step framework for the compliant and strategic implementation of Artificial Intelligence (AI) and Machine Learning (ML) within organizations, particularly in GXP-regulated environments (pharmaceuticals, medical devices, biologics).</mark> The speaker addresses common issues arising from uncontrolled AI usage—such as privacy breaches, compliance risks, and regulatory failures—and provides specific remedies. Key themes include establishing clear policies, adopting a phased strategic approach starting with pilot projects, understanding regulatory requirements, and implementing a structured development lifecycle with formal procedures (SOPs). A central message is that AI/ML is fundamentally different from traditional software and must not be force-fit into existing software development frameworks. Instead, it requires robust Quality Management System (QMS) integration, proactive regulatory assessment, and a strong emphasis on "Human-in-the-Loop" (HITL) verification, summarized by the motto "Never Trust! Always Verify!!". The series concludes with a bonus eleventh step: a detailed 7-part process for auditing AI systems to ensure ongoing compliance and continuous improvement.

### Knowledge Points

#### 1. AI Usage Policy

- <mark style="background-color: #F9EDD4">**Establish a Policy for Authorized AI Use**

      **Issues**: Employees using public AI tools for work can lead to privacy violations (e.</mark>g., uploading clinical trial data), intellectual property loss (uploading confidential data), and GXP compliance issues. Some use AI as a substitute for work rather than a supplement.
      **Remedy**: Prohibit the use of public AI for GXP data and confidential information. Mandate transparency about AI use, prohibit using it as a substitute for actual work, and establish a process to develop secure, internal AI tools for efficiency gains.

#### 2. AI Implementation Strategy

- **Be Strategic with AI Programs**

      **Issues**: Companies vary from total prohibition to uncontrolled adoption. Internal development is resource-intensive, and operational costs like data tokenization are often overlooked. Uncontrolled growth leads to inefficiencies, while failure to invest risks being non-competitive.
      <mark style="background-color: #F9EDD4">**Remedy**: Start with small pilot projects for quick wins and big learnings.</mark> Conduct "lessons learned" analyses, use qualified AI vendors to jump-start efforts, and begin gradual development of larger systems in parallel. Perform thorough budget analyses that include all cost factors.

#### 3. Regulatory Compliance & History

- <mark style="background-color: #F9EDD4">**Know the Regulatory Requirements for AI/ML**

      **Issues**: Developers are often unaware of the 120+ regulations and guidance documents for AI/ML, or they use the wrong guidance.</mark> Development often excludes Quality and Regulatory SMEs, repeating past mistakes and failing to create necessary compliance documentation.
      **Remedy**: Establish multi-disciplinary development teams including Quality and Regulatory SMEs. Develop in-house or consultant-based AI/ML regulatory expertise and provide training on fundamental requirements.

- **Evolution of FDA Guidance**:

      Guidance on software development dates back to 2002 or earlier. In 2011-2012, two key guidances addressed algorithm development.
      In recent years, the FDA's focus has shifted to dynamically changing AI, introducing the "Predetermined Change Control" concept.
      Guiding principles for ML in devices and, more recently, for drugs and biologics have been published. A January 2025 guidance introduced a credibility assessment framework.

- **Computer Software Assurance (CSA) Background**: CSA was created to address companies incorrectly applying validation rigor—either over-validating production software or under-validating medical device software. It specifically replaces Section Six of the original CDRH software guidance.

#### 4. AI/ML Development Lifecycle

- **Establish a Development Lifecycle**

      **Issues**: "Development by PowerPoint" leads to inconsistent, poorly detailed requirements and minimal documentation, creating GXP non-compliance risks.
      **Remedy**: Implement a formal development lifecycle with SOPs and templates for deliverables. <mark style="background-color: #F9EDD4">A sample lifecycle includes: Project Start-up, Data & Business Analysis, Prediction Model Design, Prediction Model Development, and Prediction Model Deployment (including maintenance and retraining).</mark>

#### 5. Standardized Procedures (SOPs)

- <mark style="background-color: #F9EDD4">**Establish AI/ML Development SOPs**

      **Issues**: Without formal procedures, development is haphazard, compliance requirements are missed, and documentation is created after the fact.</mark>
      <mark style="background-color: #F9EDD4">**Remedy**: Create key SOPs for Dataset Development and Model Development.</mark> These are necessary for internal model training and can be adapted for purchased models by "pinning" a version and bounding inputs to create a controlled system.

- **Harmonization with SDLC**: The speaker cautions against force-fitting AI development into traditional Software Development Life Cycle (SDLC) frameworks, as AI/ML and software are fundamentally different.

#### 6. Procurement of AI Tools

- **Issues with AI Procurement**: AI tools are often purchased without compliance oversight, leading to gaps in risk assessments, security procedures, user training, and maintenance planning.
- **Remedies for AI Procurement**: Establish controls over AI purchasing through formal policies. <mark style="background-color: #F9EDD4">Build GxP and Risk Assessments into the procurement process using templates and maintain an inventory of all AI systems.</mark>

#### 7. Quality Management System (QMS) Integration

- **Issues with QMS Integration**: Development activities conducted outside the QMS lack necessary controls and GxP expertise. <mark style="background-color: #F9EDD4">A series of small compliance breakdowns can cascade into a major failure, as illustrated by the "For Want of a Nail" analogy.</mark>
- **Remedies for QMS Integration**: Ensure all aspects of GxP-related AI conform to QMS policies. Integrate quality gate checks and reviews into the development process. The speaker emphasizes that AI development must fit into the QMS framework.

#### 8. Verification and Human-in-the-Loop (HITL)

- **Issues with AI Output Verification**: People incorrectly trust AI outputs, which are inferential (probabilistic guesses) and not calculated results. AI can "hallucinate." Implicit verification that occurs during human document creation must be performed explicitly and separately on AI-generated content, which takes more time than anticipated.
- <mark style="background-color: #F9EDD4">**Remedies for Verification**: The motto for critical GxP activities is: **"Never Trust!</mark> Always Verify!!"** Establish a formal process for documented human verification, reallocating time saved by AI to this task. This is critical for public AI tools and high-risk data.
- **Regulatory Basis for HITL**: The FDA has required HITL for significant automated tasks, rooted in **21 CFR §211.68(c)**, which mandates a human check to ensure automated equipment performs its operation properly.

#### 9. Variability in AI

- **Sources of AI Variability**: Users and developers are often unaware of the four primary sources of variability: the **model**, the **infrastructure**, the **data environment** (which can shift over time), and the **human** user (e.g., different prompt engineering). Variable inputs cause variable outputs and potential compliance issues.
- **Remedies for Variability**: Verify that development personnel are aware of and mitigate these variabilities. <mark style="background-color: #F9EDD4">Train users on this fact and apply the "Never Trust!</mark> Always Verify!!" principle.

#### 10. AI Validation Framework

- <mark style="background-color: #F9EDD4">**Validation as a Hybrid Approach**: Validation is a combination of qualification, verification, testing, and sometimes statistics.</mark> For AI, the framework is a spectrum between 100% validation and 100% verification. <mark style="background-color: #F9EDD4">The goal is to determine what can be validated and ensure everything else is verified to meet quality thresholds.</mark> Different ML tasks (classification, regression) and LLMs have specific, often statistics-based, performance metrics that can guide the verification process.

#### 11. Regulatory Case Studies

- <mark style="background-color: #F9EDD4">**FDA Warning Letter (Purolea, April 2, 2026)**: A company used an AI to create drug specifications and procedures but failed to review the AI-generated documents for accuracy and CGMP compliance, even being unaware of the need for process validation because the AI never mentioned it.</mark> <mark style="background-color: #F9EDD4">The speaker noted the letter was missing a citation of §211.68(c).</mark>
- **MHRA Inspectorate Blog (Peter Brown, June 29, 2026)**: The MHRA has received AI-generated inspection responses containing references to non-existent guidance and misleading information. <mark style="background-color: #F9EDD4">The agency holds companies responsible for the accuracy of all submissions, regardless of the drafting tool, and expects technical review by experienced personnel.</mark> MHRA encourages, but does not require, disclosure of AI use for transparency.

#### 12. Assessment of AI Tools Against Regulations

- **Issues with AI Compliance Assessments**: Companies often don't know how their AI systems compare against regulatory requirements and lack documented assessments to prove compliance during audits.
- <mark style="background-color: #F9EDD4">**Remedies for AI Assessments**: Assemble a multidisciplinary team (including Quality and Regulatory) to conduct a walk-through assessment of the AI system against current regulations and guiding principles.</mark> Correct any deficiencies and document the comparison for audit readiness, similar to a Part 11 assessment.

#### 13. Auditing AI Systems (Bonus Step)

- <mark style="background-color: #F9EDD4">**Conducting an SME Audit**: A Subject Matter Expert (SME) should audit AI systems by applying the 10-step framework in an informal "mock" audit.</mark>
- **Audit and Improvement Cycle**: The full process is:

    a. Apply the 10 Steps.
    b. Have the SME do a "Mock" Audit.
    c. Close identified gaps.
    d. Conduct the formal Audit.
    e. Close any remaining gaps.
    f. Create a roadmap for continuous improvement.
    g. Repeat audits as necessary.

### Questions

- [Insert Question/Confusion]

### Assignments

- [ ] 1. Establish a formal policy for the authorized use of AI tools.
- [ ] 2. Plan and execute small pilot AI projects for specific improvements and conduct a thorough budget analysis for AI initiatives.
- [ ] 3. Establish an AI/ML Procurement Procedure with embedded GxP and Risk Assessments and maintain an inventory of all AI systems.
- [ ] 4. Form multi-disciplinary teams, including Quality and Regulatory SMEs, for AI development.
- [ ] 5. Develop an AI/ML development lifecycle and create corresponding SOPs (e.g., for dataset and model development).
- [ ] 6. Integrate all GxP-related AI development activities into the organization’s Quality Management System (QMS).
- [ ] 7. Develop and implement a documented Human Verification process adopting the "Never Trust! Always Verify!!" motto for all critical GxP AI activities.
- [ ] 8. Train users on AI output variability and the necessity of verification.
- [ ] 9. Assemble a multidisciplinary team to assess current AI/ML tools against applicable regulations and guiding principles; document findings and correct deficiencies.
- [ ] 10. Have an SME conduct a mock audit of your AI systems, close gaps, and create a roadmap for continuous improvement.
- [ ] 11. Locate and review Peter Brown's MHRA Inspectorate Blog post (June 29, 2026) as a reference resource.
- [ ] 12. Investigate the precedent for statistics-based validation (e.g., Poisson distribution in media fills) to support its application to AI validation.
- [ ] 13. Consider establishing a policy requiring disclosure of AI use in regulatory submissions.

### Highlights (button-flagged moments)

#### Policy on Authorized AI Use: Addressing Risks and Establishing Remedies

The speaker elaborates on the presentation slide, detailing the critical issues of unauthorized public AI use, such as uploading sensitive clinical trial data, and outlines a four-part remedy focusing on security, transparency, authenticity, and innovation.
• Visual Context: The slide proposes establishing a policy for authorized AI use, listing issues like employees loading confidential and clinical trial data into public AI tools and creating compliance risks.
• Discussion Insight: Speaker 1 emphasizes the severity of these issues, stating that loading participant data into public AI "breaks so many privacy rules I can't even begin to talk about it," and also notes that some employees use AI as a substitute for work out of laziness.
• Key Takeaway: The proposed remedy is a multi-pronged policy: prohibit public AI for GXP data (Security), mandate disclosure of AI use (Transparency), forbid using AI as a work substitute (Authenticity), and create a formal process for developing beneficial AI tools (Innovation).

#### Strategic AI Adoption: Balancing Growth and Compliance Risks

The speaker elaborates on the presentation slide, which outlines the challenges and remedies for AI implementation, emphasizing a strategic approach that avoids the extremes of complete prohibition and uncontrolled growth by starting with smaller pilot projects.
• Visual Context: The slide lists key issues in AI adoption, including cost, the risk of non-competitiveness ('no growth'), and inefficiencies from 'uncontrolled growth,' leading to potential GXP & Compliance issues.
• Discussion Insight: The speaker highlights the 'wide variation' between companies, contrasting those who prohibit AI with those who adopt it without sufficient guardrails, noting both extremes are problematic.
• Key Takeaway: The recommended strategy is to start with small, targeted pilot solutions to achieve quick wins and gather lessons learned before tackling larger, higher-risk AI projects.

#### Addressing AI/ML Regulatory Compliance Gaps in Development

While presenting a slide on regulatory requirements, the speaker elaborates on the key issues, such as developers being unaware of the over 120 AI/ML regulations, and reiterates the proposed remedies, including establishing multi-disciplinary teams to prevent compliance failures.
• Visual Context: The slide identifies six issues in AI/ML development, including a lack of awareness of over 120 regulations, the use of incorrect guidance, and the absence of quality/regulatory experts, all leading to potential GXP & Compliance issues.
• Discussion Insight: The speaker confirms that these issues are common, citing a real-world example of a company that was 'full steam ahead' using the 'wrong guidance' and emphasizing that the exclusion of quality teams is a repeating historical problem.
• Key Takeaway: To remedy these compliance risks, the speaker advocates for establishing multi-disciplinary teams with regulatory SMEs, developing in-house or consultant-based expertise, and training staff on fundamental regulatory requirements.

#### Speaker Outlines a Four-Phase AI/ML Development Life Cycle

The speaker presents a slide detailing a four-phase AI/ML development life cycle and proceeds to explain each stage, from establishing the initial dataset to final model deployment and maintenance.
• Visual Context: The slide illustrates a 'Possible AI/ML Development Life Cycle' with four key phases: Data & Business Analysis, Prediction Model Design, Prediction Model Development, and Prediction Model Deployment.
• Discussion Insight: The speaker explicitly endorses this framework, sequentially describing the process of creating a dataset, selecting a predictive model, optimizing it, and finally deploying it into a GXP environment.

#### Speaker Recommends AI Development SOPs to Counteract Haphazard Practices

Pointing to a slide that outlines issues like haphazard development and missed GXP compliance, the speaker explicitly recommends creating a 'Dataset Development SOP' and a 'Model Development SOP' as the remedy.
• Visual Context: The slide identifies issues in AI/ML development, including haphazard processes and missed compliance, and proposes establishing 'Dataset Development SOP' and 'Model Development SOP' as the remedy.
• Discussion Insight: The speaker states that without procedures, development becomes haphazard and documentation is created retroactively, directly echoing the problems listed on the slide.
• Key Takeaway: The primary recommendation is to formally establish at least two SOPs—one for dataset development and one for model development—to bring structure and compliance to AI/ML projects.

#### To avoid haphazard development, create a data set development SOP and a model development SOP.

• Speaker 1 identifies haphazard development as a key issue that arises from a lack of procedures, leading to incomplete or non-existent documentation.
• The recommendation is to create at least two SOPs: one for data set development and another for model development, which is particularly beneficial for internal model training.
• These SOPs can also be adapted for using public tools by documenting how a model is pinned and how prompt engineering is limited to bound the information coming in.

#### Remedying Haphazard AI Development with Standard Operating Procedures

The speaker discusses the slide on screen, explaining that to counter issues like haphazard development and missed compliance, it is crucial to establish Standard Operating Procedures (SOPs) for both dataset and model development.
• Visual Context: The slide outlines common issues in AI/ML development, such as haphazard processes and missed GXP/Compliance requirements, and proposes a phased remedy culminating in creating a 'Dataset Development SOP' and a 'Model Development SOP'.
• Discussion Insight: The speaker confirms that without procedures, development is haphazard, and recommends creating these two specific SOPs to provide structure, even when using and adapting public AI models for internal use.
• Key Takeaway: Establishing formal SOPs for AI/ML dataset and model development is presented as a fundamental solution to ensure consistency, meet compliance standards, and avoid creating documentation after the fact.

#### Establishing AI Procurement Procedures to Mitigate GxP and Compliance Risks

The speaker presents a slide outlining the critical issues and remedies for AI procurement, emphasizing that tools are being purchased without adequate GxP controls or compliance oversight, which creates significant risk.
• Visual Context: The slide lists issues with AI/ML procurement, including lack of compliance oversight, unestablished GxP controls (for risk assessment, procedures, training, maintenance), and the resulting compliance risks.
• Discussion Insight: Speaker 1 verbally reinforces the points on the slide, explaining that the lack of controls over AI tool purchasing and adaptation leads to major GxP and compliance problems.
• Key Takeaway: The proposed remedy involves establishing formal controls and policies for purchasing AI, building GxP/Risk Assessments into the procurement process, and maintaining a comprehensive inventory of all AI systems and tools.

#### Integrating AI Development into QMS to Prevent Compliance Failures

The speaker presents a slide outlining the critical need to integrate AI development into the Quality Management System (QMS), using the 'For Want of a Nail' poem to illustrate how neglecting this can lead to a 'compliance disaster'.
• Visual Context: The slide lists issues with development being independent of QMS, including a lack of compliance controls and GxP expertise, and proposes conforming all GxP-related AI to QMS policies as the remedy.
• Discussion Insight: The speaker explains that a series of minor compliance breakdowns, resulting from development's separation from QMS, can escalate into a major 'compliance disaster'.
• Key Takeaway: The central recommendation is that AI development must fit into the broader Quality Management System, ensuring quality gate checks and reviews are applied, rather than necessarily being forced into a traditional software development lifecycle (SDLC).

#### The Imperative of Human Verification for AI Outputs in GxP Environments

The presentation slide outlines the necessity of human verification for AI, a point the speaker reinforces by explaining that AI is inferential, not calculative, and that any time saved must be reinvested into a formal verification process.
• Visual Context: The slide identifies that people incorrectly trust AI and use poor prompts, proposing a remedy: 'Never Trust! Always Verify!!' through documented human verification, especially for critical GxP activities.
• Discussion Insight: Speaker 1 elaborates that AI is purely inferential and can be biased by training data, giving a hypothetical where an AI might wrongly conclude '2+2=5' if only trained on inputs that result in '5'.
• Key Takeaway: The time saved by using AI is not a net gain; it must be reallocated to explicit human verification, a step that was previously an implicit part of manual document creation.

#### Speaker Analyzes Omission in FDA Warning Letter Regarding Human-in-the-Loop AI Verification

While presenting a slide on an FDA case study about improper AI use, the speaker points out a critical oversight: the FDA's warning letter failed to cite regulation § 211.68(c), which has mandated human verification for significant automated tasks since 2008.
• Visual Context: The slide presents an FDA case study of a warning letter issued to 'Purolea' for using AI to generate compliance documents without human review, and cites the relevant regulation § 211.68.
• Discussion Insight: The speaker expresses surprise that the actual FDA warning letter for this case did not mention regulation § 211.68(c), despite it being the key rule requiring human-in-the-loop verification.
• Key Takeaway: The concept of 'human in the loop' is not new; it has been a regulatory requirement in GMP regulations since 2008, underscoring the long-standing precedent for human oversight of automated systems.

#### A cosmetic lab's FDA warning letter was missing the actual GMP regulation (21168c) that calls for a human in the loop.

• During a case study, Speaker 1 pointed out that an FDA warning letter issued to a cosmetic lab failed to cite the specific GMP regulation that mandates a human-in-the-loop for verification.
• The regulation in question, 21 CFR 211.68(c), was established on September 8, 2008, and requires that any significant, automated step in a batch process must be verified by a person.
• Speaker 1 highlighted that the concept of a 'human in the loop' has been a part of GMP regulations since at least 2008, expressing surprise that the FDA did not include this specific citation in their warning letter.

#### there is specific regulation!

• Key Insight: There are over 120 international AI regulations, but focusing on approximately 18 key documents, including specific FDA guidances, is recommended.
• Risk Identified: Development teams often lack awareness of specific AI/ML regulatory requirements, leading to non-compliant documentation and submission risks.
• Key Insight: A 2008 GMP regulation (211.68c) already mandates human verification for significant automated steps, establishing an early precedent for 'human in the loop' requirements.
• Action Item: Form multidisciplinary teams that include quality and regulatory experts from the beginning of AI development projects.
• Action Item: Assess AI tools against relevant regulations, such as the FDA's 10 guiding principles, and maintain documentation for audits.

#### Speaker Highlights MHRA's Stance on AI-Generated GXP Responses

The speaker discusses the 'MHRA Case Study' slide, summarizing the regulatory body's position that data integrity is non-negotiable and adding a personal call for mandatory disclosure of AI use in regulatory responses.
• Visual Context: The slide details an MHRA case study, outlining problems with AI-generated inspection responses (e.g., misleading content, citing non-existent guidance) and asserting that accountability for accuracy remains with the submitter.
• Discussion Insight: Speaker 1 highlights the MHRA's position on data integrity and states a personal belief that disclosure of AI use in responses should be required, not merely encouraged, for transparency and integrity purposes.
• Key Takeaway: The fundamental regulatory expectation is that all submissions must be factually accurate, verifiable, and technically reviewed, a standard that is unaffected by whether AI, templates, or other tools are used for drafting.

#### person: Peter brown blog, where is it? could be good for references

• Context: The discussion covers a presentation on a case study involving the UK's Medicines and Healthcare products Regulatory Agency (MHRA), summarizing a blog post by Peter Brown on the topic.
• Key Insight: The MHRA's position is that data integrity principles apply universally, regardless of whether the data is generated by AI or other methods.
• Key Insight: The MHRA encourages, and the speaker advocates for requiring, the disclosure of AI tool usage to regulators to ensure transparency.
• Key Insight: Communicating AI use to regulators is framed as a fundamental matter of industry integrity.

#### Addressing AI Variability and Emphasizing Verification

The speaker discusses the presentation slide on AI variability, elaborating on the listed issues—such as model, infrastructure, data, and human variability—and reinforcing the proposed remedies, including training users and adopting a 'Never Trust! Always Verify!!' mindset.
• Visual Context: The slide identifies four key sources of AI variability: model, infrastructure, data environment, and human factors.
• Discussion Insight: The speaker notes that these variables can cause inconsistent outputs, potentially leading to significant compliance issues in regulated environments.
• Key Takeaway: A critical remedy proposed both on the slide and by the speaker is to train all users on the principle of 'Never Trust! Always Verify!!' for any critical activities involving AI.

#### Speaker Elaborates on AI Validation Model: Balancing Validation with Mandatory Verification

Presenting a slide on AI validation, the speaker explains his long-held model where achieving a quality threshold requires a combination of what can be validated and a mandatory verification of everything else, a crucial concept for AI.
• Visual Context: The slide illustrates that 'Validation' is a composite process, graphically showing that anything not covered by validation must be addressed by verification to meet the 'Quality/Compliance Threshold'.
• Discussion Insight: The speaker emphasizes that this validation/verification model is a concept he has used for years, applying it now to AI by stressing the need to determine where automated verification ends and human verification (Human-in-the-Loop) must begin.
• Key Takeaway: The fundamental principle for AI compliance is a two-part approach: first, validate everything possible, and second, apply rigorous verification to all remaining aspects to ensure full quality and compliance.

#### Validation is a combination of qualification, verification, testing, and sometimes a statistics-based validation.

• Validation is a process composed of qualification, verification, testing, and occasionally, statistics-based validation.
• Speaker 1 provides an example of using statistics for validation: media fills for aseptic products are assessed using a Poisson distribution to calculate acceptable production size from a sample.
• The speaker proposes a model where 100% verification is on one end and 100% validation is on the other, suggesting that any component that cannot be validated must be verified to meet quality thresholds.

#### statistical based validation — want to find precedent, is it something well known?

• Key Insight: A precedent for statistical-based validation already exists in regulated industries, such as the use of Poisson distribution for media fills in aseptic product manufacturing.
• Key Insight: For AI systems, aspects that cannot be fully qualified or tested must be verified against quality thresholds using statistical performance metrics.
• Key Insight: Metrics for LLMs, such as completeness, relevancy, and accuracy, can be used to statistically determine the required level of human verification.
• Decision: The proposed validation approach for AI is a hybrid model combining qualification, verification, testing, and statistics-based validation.

#### Strategy for Assessing AI Tools Against Regulatory and Guiding Principles

The speaker discusses the tenth step of their framework, detailed on the slide, which is to assess AI tools against regulations and guiding principles by assembling a multi-disciplinary team to review compliance and document the findings.
• Visual Context: The slide identifies a key issue where companies lack knowledge of their AI's regulatory compliance and proposes a remedy: to form a multi-disciplinary team to assess the tool against regulations and document the process.
• Discussion Insight: Speaker 1 suggests starting the assessment with the '10 guiding principles' from a specific two-page document, using it as a checklist for a multi-disciplinary team to determine compliance.
• Key Takeaway: The recommended action is to proactively assess AI systems against established principles, correct any identified deficiencies, and maintain documentation of this comparison for future audits and agency inspections.

#### I missed slide 4 photo, but at least the audio has its content.

• Context: The team is reviewing a 10-step process for managing AI in a regulated GXP environment. This discussion focuses on Step 4: establishing a consistent and formal development lifecycle to replace current haphazard methods.
• Risk Identified: Current project management, often done in PowerPoint, is inconsistent and can lead to lost requirements and compliance issues.
• Decision: A formal Development Lifecycle (DLC) for AI projects will be established.
• Action Item: Create Standard Operating Procedures (SOPs) for the new development lifecycle.
• Action Item: Develop templates for requirements documentation and other key DLC deliverables.

#### Speaker Outlines a 10-Step Framework for AI/ML Implementation and Governance

The presented slide, titled '10 Steps - Overview,' serves as the foundational agenda for the speaker's detailed discussion on establishing comprehensive policies and procedures for AI/ML in a regulated environment.
• Visual Context: The slide lists ten key steps for managing AI, including establishing policies, being strategic, knowing regulatory requirements, and creating development and procurement procedures.
• Discussion Insight: The speaker elaborates on the risks of improper AI use, such as employees loading private company or participant data into public AI tools, which violates privacy rules and creates GXP compliance issues.
• Key Takeaway: A core theme is 'never trust, always verify,' emphasizing that time saved by using AI must be reinvested into rigorous human verification of its outputs to ensure accuracy and compliance.

#### Bonus Recommendation: A 7-Step SME Audit Process for AI Systems

The speaker presents a 'bonus' slide outlining a comprehensive, multi-step process for having a Subject Matter Expert (SME) audit AI systems, reading directly from the displayed list of actions.
• Visual Context: The slide details a 7-step audit process (a-g) for an AI System, including applying the '10 Steps', conducting mock and formal audits, closing gaps, and creating a roadmap.
• Discussion Insight: Speaker 1 introduces this audit cycle as a 'bonus' step after his main presentation, emphasizing a continuous improvement loop through mock audits, formal audits, and repeated checks.
• Key Takeaway: The recommended audit protocol is a structured, iterative cycle managed by an SME to ensure AI systems are properly evaluated, deficiencies are corrected, and procedures are refined over time.

#### mock audit!

• Action Item: Engage a subject matter expert (SME) to conduct a mock audit of the organization's AI systems and tools.
• Key Insight: The mock audit process helps proactively identify and close compliance gaps, preparing the organization for official agency inspections.
• Action Item: Refine procedures and create a roadmap for continuous improvement based on the findings from the mock audit.
• Decision: Audits of AI systems should be repeated as necessary to ensure ongoing compliance and governance.

<!-- markdownlint-enable MD033 -->
## Transcript

[00:00] **Speaker 1:** That I'll be talking about. All right, so here are the ten steps. I'm going to read them all. We'll be reading them shortly, or covering them shortly. But this is basically it. So, and and I've characterized each of these steps by what are the issues that we're seeing, especially as we do audits across a number of different clients, and then what's the remedy. So, have a policy. Why? Because employees are using the tools. You get in clinical trials. You get in participant data being loaded up into a public AI tool that breaks so many privacy rules I can't even begin to talk about it. You get company scientific data that's being loaded into public AI that's bad too, and the intention is good. They want to analyze, summarize, or do additional research, but the approach is very bad because they're using a. So, also, there are some employees who just are lazy, and they use it as a substitute for work, rather than supplementing initial research or doing it as a review check subsequent to something they've created. So, those are problems. All of the above create potential GXP and compliance issues. So, what's the remedy? Security prohibit the use of public tools. Transparency prohibit personnel. Using AI without acknowledgement that AI was used, I think that's very important. I did that on my word class. So there you go. Authenticity prohibit using AI as an actual as a substitute for actual work, and then innovation. Think about where you could use AI to improve efficiencies, and then get the team focused on that. So. Strategy. Be strategic with AI deployments. We're seeing a lot of variation, a wide, wide variation between companies. Some prohibit the use, so indicated by the red, and some have a you know all systems go, don't stop, let's do AI. So there's that wide variety, and what people don't often realize, if you're going to do internal development of AI, it's very time and resource and cost. It's Intensive, and and the operations can be too. If you don't understand that a model can't read data the way we read it, it has to tokenize it, though making the data readable by the model, and that can be very costly operationally. So you have you have these cost factors that you need to be aware of. So I think these you know you you have the two extremes: no growth. So failure to invest will lead to non-competitiveness, and uncontrolled growth leads to haphazard designs and inefficiencies. So, as with all of these, you'll see this recurring theme. These create potential GXP and compliance issues. So, what's the remedy? Be strategic. Focus initially on pilot solutions. I hear we're in pilot purgatory apparently, but. Really get those in, not just small projects for the sake of small projects, but do small projects that are targeted to improve specific areas. And then, I think what is often not done enough is doing the lessons learned after an implementation, and breaking that down so you can understand what lessons need to be applied to future pilot projects, and use procurement. And we'll talk about that a little bit more in a couple of slides about qualified AI vendors to jumpstart your efforts, and then begin that big project. And lastly, do a bunch of analysis. It's very important to be aware of the cost factors because a lot of people do not understand the true costs of some of these things. And I don't have an infinite budget. I'm sure your company doesn't either. Know the regulatory requirements. There are over 120 regulation, guidance, guiding principles, guides, and standards. When you look at the international space, and are aware of all the standards and stuff out there, I think there are about 17 or 18 of those 120 that I would recommend reading. I think I might get into that in this slide. But so developers are often unaware of the specific AI, ML regulatory requirements. I was talking with. One company, they're head down the path, full steam ahead. Wrong guidance, not good, and so had to switch that around. So unaware, using the wrong one. Sometimes it's done without any participation from quality and regulatory subject matter experts. Not that that has ever happened before, but if you're familiar. When software started really ramping up in the 80s and 90s, that was the big problem. Just quality was not involved in any of these decisions. History is repeating itself. So the development effort does not necessarily create, or does not create the necessary compliance documentation, and these actions create GXP and compliance issues. So establish multidisciplinary teams. That's actually the first recommendation on the guiding principles put out in 2025, I think. Maybe earlier this year, then develop AI, machine learning, regulatory expertise in-house or consultants. Establish training on the fundamental regulatory requirements. Establish a lifecycle. Too many development vendors do development and project management by PowerPoint. I have literally sat, sat down, and asked for requirements, and they gave me two slide decks of. Hundreds of slides and said, "Well, the requirements are in here." Okay, great. That's that's just not the way to do development. So, what does this lead to? It's it's haphazard. It lacks consistency, and over time, some of the requirements get lost in the slides. There's often minimal development documentation, if any, and these requirements and specifications that do get generated lack. Details and precisions, and sometimes miss critical features. That I don't have it here, but that would lead to GXP incompliance. And so, get a development life cycle together, create SOPs for that development life cycle, and create templates for requirements and other DLC deliverables. I am sorry, I don't know why the slides that I sent have been slightly altered, so the fonts a little bit off, but. Here's a sample of a development life cycle that I think is really useful. So you first get, you first establish that if you're doing internal development, you first establish your data set. That's the thing that you're going to use to train the model. Then you get in the process of selecting that predictive model, and then you optimize the predictive model and phase key, and then you go live and. To the GXP environment, and you include model maintenance and retraining as necessary. So, fifth, establish some procedures. So many of the same issues are here: haphazard development. If you don't have procedures, the development documentation doesn't get created, and then what happens is you have this. So. You have these problems, so create at least a couple of SOPs. I recommend a data set development SOP and a model development SOP. If you're doing the training, or if you're doing the model training internally, this is a good thing to do. You can do the same thing if you're leveraging a available public tool and you pin the model. You're you're pinning that. What it's been trained on, and then you limit the prompt engineering and bound the information that's coming in. And you can write an SOP for all that. Then you can create using public tools or using a purchased model. You can create a necessary model for use inside the company. But you should still have these type of SOPs. In order to do it properly, yes. Yeah. How do you harmonize between the existing software SDLC? That so that's that's a great question. Should they be harmonized? I think so. Well, it so if. I would recommend if you go. I don't know if were you here for my the session I did yesterday. So that slide showing the differences between the software and the machine learning. There's so many fundamental differences. I I really have a fear that people are trying to force fit software development or AI development into software development frameworks. And I I think that that is they're they're very they're fundamentally different. And I think that's that. And you can argue against my premise, but because they're so fundamentally different, you're you're you know it's the square peg in a round hole, or or and part of part of the problem is people end up trying to treat AI as exactly the same as software, and it's just not. And I think that's that adds a lot of of problems. You know you. But I'm just here making recommendations. You can do whatever you want, and I think that's that's the key. I have worked with companies who developed software and then moved into the AI space, and I there's enough differences that they they need to at least make sure that they don't confuse the two. So, so that that's not to kind of derail that, but if you if you understand the guidances that come out in two thousand two, or maybe earlier than that, they had the software development in. Issued from CDRH in 2011, 2012, they had two guidances that talked about algorithm development, and those were the predominant things until you start getting in the last six years with the predetermined change control. Their their main concern is changing, is AI changing on the fly, and so that's where they came out initially in the last six years. They've updated those two algorithm guidances in 2022. They've come out with guiding principles for machine learning development for devices about four or five years ago. They came out with the guiding principles for drug and biologics development and use of AI just in the last couple years, and then they had the January 2025 guidance, which has the credibility assessment. So there's a whole, If you understand the history, they they've given a lot, and I've heard talk. Someone was talking earlier about CSA. CSA was written. Just this is a freebie here, folks. CSA was written because what you had is you had medical device companies who had medical device software, and then they had production and quality software, and they were doing two things that were problematic. They were validating their quality and production software at the level that they validated medical devices. Or they were validating their medical devices at the level of the quality and production software was done. If you look in the footnotes on the front pages of the CSA guidance, it talks about the original guidance that CDRH issued on software and how this this replaces Section Six of that guidance. So, there's some people dismiss regulatory as as unimportant until you submit something. It's it's really important to understand the history and how they got there. So anyway, I'm going to continue on with the presentation. Because otherwise, Brittany will yell at me. Bob, you're moving too slow. So all right, procurement. All right, establish a procurement procedure. AI tools being purchased without adequate compliance oversight. GXP controls are not established, so there's no compliance or risk assessments, no impact analysis. There's no procedures for the infrastructure types of things. There's no training for operation, authorized use, even at admin functions. No maintenance. The AI tools are adopted, adapted without the necessary GXP compliance, and these lead to issues. So, what's the remedy? Establish controls over purchasing AI and policies and procedures, and build in risk assessments into the AI procurement process. Again, I always recommend using templates to make it simplified for what. People have to do and maintain that inventory registry of AI systems and AI tools. QMS. Make sure you integrate the development life cycle into the quality management system. So I like this poem. Basically, it talks about a kingdom being lost because the shoe for a the nail for a horseshoe was lost. So you can read through out read through that. I won't do that in the interest of time, but. So, what are the issues? Development activities are independent of the QMS, and therefore they lack the necessary compliance controls. GXP expertise is not involved, and you get a series of compliance breakdowns, which leads to a compliance disaster. So, have all aspects of the GXP-related AI conform to QMS policies, procedures, and processes. Maybe that's what you're getting at, but I think there need to be quality gate checks. Reviews of things; those have to fit into the QMS. I'm not again. I'm not. I don't want to debate, but I'm not sure that AI development needs to fit into the SDLC so much as it needs to fit into the QMS. Well, well, but but we'll get into this. Is is verification is the challenging part. So. So establish a process for documented human verification. People often incorrectly assume the AI outputs are trustworthy. It's only inferring. It's it's giving a guess. I have a a theory. I haven't tried it out yet. But if you put in a whole bunch of equations into the inputs, saying two plus three equals five, negative one plus four. Our negative one plus six equals five, and so on and so forth. Whole number of series that end up with the answer five. And then you put in infer what two plus two is. Would it give me five or would it give me four? It's not calculating. It is only inferring. If I load the data and bias the data so it only has the answer of five, it's not going to give me four. So. People. So another thing is, people use untargeted, non-specific prop engineering, and they get gawky new cancers like farming. So the remedy: always trust, never, never trust, always verify. Excuse me, and recognize that some of the time saved by using AI must be spent in human verification. There's been a lot of discussion about human verification taking longer than expected. Why is that? I'll tell you why. Because verification is embedded in the creation of documents, you don't realize it, but psychologically, people are verifying things as they create things. All that verification that has been spent in the creation of the document that is implicit now has to be carried over into the explicit verification that you do with the output. My dad was a human factors engineer; he would love this kind of stuff. So, all right. So, this is especially true for public AI tools, and especially true for higher risk GXP data and activities. So, human in the loop. I want to do a couple of case studies now. Other people have mentioned this already. Again, I apologize for the fonts here. Sometimes we send things over and they get jumbled in the in the transfer. But this is what happened to that cosmetic lab, and we saw the FDA warning letter. But what I was surprised was missing from the warning letter is the actual GMP regulation that calls for human in the loop. In 21168C, this came. This was promulgated and came out. It was chapered into law or regulations. In September 8, 2008, and it calls for that if you're using automated equipment on a significant and there's a significant step in that batch, and that step is automated, that has to be verified by a by a person. Normally, those traditionally those second those significant steps were Verified by two people. So if you use automation, you need a person to actually verify it. So human in the loop, conceptually, has been around at least since two thousand eight in the GMP regulations. But people, I was surprised FDA didn't pick this up. But anyway, MHRa case study. So Peter Brown has a blog, or put out a blog on this. Again, this is just a summary of what he said, but I would highlight, you know, their position is you you have to have data integrity regardless of you know your sources here, and they encourage I would say they ought to require, quite frankly, disclosure of AI use and responses for the transparency purposes. I think. I think we in the healthcare industry need to do that as a matter of integrity and data integrity. We need to be communicating that to regulators so they know what they're getting. All right. So variability: understand the sources of variability and their controls. Users and some developers are not aware of the variability that occurs with AI. So there's model variability, there's infrastructure variability, data environment. Variability—the data you can—a classic example is in the asset protection realm, where fraud can can shift, fraud techniques can shift, and so your data environment changes. And then there's human variability, and the var variables cause variable output, and may lead to compliance issues. So, determine whether development people are aware of these variables, and then ask what you know. What have you done to Like control these, and then train users on the fact that the the outputs are subject to variability, and then never trust, always verify. Now, there's been a lot of questions about validation throughout this conference. I'd like to throw out a thought of mine that I've I've used literally for years. Validation has always been a combination of qualification. Verification, testing, and at times, a statistics-based validation. When do we use statistics? We use it every time we do media fills for aseptic products. We use a Poisson distribution. You do a sample size, and you calculate what size production you can from that sample size, and whether or not met the acceptance criteria that you've established. So. What? How do you use it? So I, I have this little drawing. So 100% of validation is on the right. 100% verification is on the left. Figure out what you can validate, and then everything else has to be verified. So to to meet that quality threshold. Now with AI, some verification can't maybe automated, but must be determined where the human verification will be required, and you can use. Performance metrics. So, a lot of the machine learning tasks, like classification, regression, or clustering, have these different performance metrics that are statistics-based. LLMs. We talked about this a little bit with agentic AI, but you can look at completeness, relevancy, accuracy, and one other one I can't remember. And there are others that you can you can do, but. Think about leveraging performance metrics in order to figure out how much you need to verify and what you need to look at during that verification process. And then ten assessment. So assess the AI tools against regulations and guiding principles. I think we we do that a lot in the GXB companies. We have a lot of Part 11 assessments. You know, does this meet these. Part 11 acceptance criteria or or regulation regulatory requirements, so I I would suggest just doing that against the guiding principles as a starting place. This is a two page document. It has 10 guiding principles. You can go through and say, well, you know, get the multidisciplinary team together and figure out, all right, did we meet these guiding principles or not, or how do we how are we going to meet them during development even, so. Do this. Correct any deficiencies. Document the comparison, and have it available for audits and agency inspections. So those are the ten steps, kind of away from single word things. But that that covers all of them. I have a bonus though. So have an SME audit your AI systems and AI tools. So you know, apply the ten steps. Do a mock audit. Close the gaps, refine the procedures, conduct the formal audit, close any remaining gaps, and you can identify a roadmap for continuous opportunity improvements or continuous improvement opportunities, and then repeat audits as necessary. So here's the 11-word recap. Did anyone pick up which word was missing? Transparency. No, it was actually procedures. I'll flip back real quick here. Sorry if. So it, even though I gave it procedures in my original instructions, it did not. It omitted procedures for some reason. I didn't go. I only did two iterations. I'm not going to do five iterations to get it perfect. So, but I noticed that that. Because why did I notice it? Because I verified it. So, all right. So let me get back to where I was. Oh, I had it there, son. So yeah, procedures is missing from this. It's implied maybe with documentation and some other things, but all right. Any questions? Sorry, I moved pretty quickly, but I hope it was okay. All right. Then thank you very much for coming.

## Related

- [[Home]]
- [[Governance Risk and Human Factors MOC]]
