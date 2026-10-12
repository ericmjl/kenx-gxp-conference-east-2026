date: 2026-09-15
recorded_at: 2026-09-15T11:12:05-04:00
duration_seconds: 2445
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: 7bc4c14f84ce4608cd029436aa687dda
plaud_name: "09-15 Lecture: AI Systems in GxP, Observability, and Evaluation"
speakers:
  - Lecturer, QMS pioneer with One Two Three Compliance, later Trackwise Digital (diarized as Speaker 1)
  - Audience member from unregulated research, addressed as Eric by the lecturer (diarized as Speaker 2)
  - Larry, audience member asking about prompt audit trails (diarized as Speaker 3)
  - Yari, audience member raising silent failures (diarized as Speaker 4)
  - Audience quality member who scores new agent builds as final signer (diarized as Speaker 5)
  - Audience member citing ICH and GAMP risk frameworks (diarized as Speaker 6)
  - Jonathan, audience member who builds agents (diarized as Speaker 7)
  - Audience member citing 76 percent effectiveness for model-checking-model (diarized as Speaker 8)
presenter: "Rosalind Beasley"
affiliation: "Co-Founder & CEO, Genari AI"
session: "Trust Is Not a Framework: Building Observable, Evaluated AI Systems in GxP (day one, 11:10-11:50)"
tags:
  - kenx-gxp-east-2026
  - transcript

<!-- markdownlint-disable MD033 MD024 -->
# GxP lecture on AI observability, evaluation, and the LLM-as-judge

> Recorded 2026-09-15 at 1112 via Plaud. 40:45.

## Summary

A 41-minute conference lecture by an unnamed QMS veteran on how to observe and evaluate AI systems used for GxP purposes. He introduces himself through credentials: he co-founded One Two Three Compliance around 2010 to 2011, whose cloud quality management system became Trackwise Digital, he worked on predicting survivability of implantable medical devices at Allergan around 2008 to 2009, and he gave a 2018 talk on computer vision for returns analysis. The spine of the lecture is a distinction only two audience members had encountered: observability versus evaluation, terms people use interchangeably but should not. Observability is IT-led and answers what the system did: tracing and telemetry (tokens consumed, cost, error rates), context and lineage tracking so an auditor can be shown which data sources fed a given prompt's answer, safety-signal guardrails such as PII and patient health information detection with automatic blocking, and change monitoring for data sources, models, and prompts. Evaluation is quality-led and answers how good the output is: correctness and factualness, relevance to intended use, SOP policy compliance, and format and schema control (plain text, report, HTML, or JSON for feeding downstream systems). His organizing claim is that IT and quality can no longer operate as two separate teams, and that sign-off is always the quality person's decision, never the agent's. The LLM-as-judge must be a different model from the operating agent, run at low but non-zero temperature (never zero, or why use an LLM at all), mirroring the four eyes principle; the judge also catches silent failures, following Yari's point that systems answer without disclosing they only saw part of the data, illustrated by his complaint-handling example where a death reported days later changes whether a ticket should have been classified reportable, with confidence scores tracked and updated as information accrues.

The second half argues we have moved beyond deterministic pass/fail testing to what he calls evaluation-driven deployment: bake observability and evaluation into implementation, not after go-live. Concretely, enumerate failure modes (agent, data, prompt), build a golden set that includes unhappy paths, because complaint systems trained on happy-path data keep giving happy-path answers, start with simple pass/fail graders against an accuracy threshold set by risk tolerance (90 percent versus 99 percent), keep humans in the loop during setup, and hold a regression baseline. He warns against generic out-of-the-box vendor graders in favor of metrics defined for your intended use, then run evaluators continuously and cluster failures to find trends. Graders come in three layers: code-based (deterministic schema, citations, prohibited terms), model-based, and human subject-matter experts who calibrate the judge up front, then shift to exception review plus periodic drift checks in production. Audience contributions extend the frame: Larry pushes on prompt audit trails and non-repudiation, which the lecturer answers is literally what his product does, tracking who created, modified, and executed each prompt including agent executions; Jonathan builds stop-and-escalate constraints into agent instructions and frames the agent as an employee whose prompt is its job description; the lecturer shares his completeness trick of making the agent report record counts at start and end and keep going until they match; Eric raises measuring judge-to-human alignment with an acceptable deviation threshold (five percent); a remote audience member points to ICH Q9 and GAMP as long-standing risk frameworks that extend to AI; another cites roughly 76 percent effectiveness for one model checking another. The close is the judge qualification pack: documented intended use and boundaries, scoring rubrics and thresholds, acceptance criteria, a golden dataset, and a calibration report usable as an exception report. He points to a free hands-on AI lab handout and offers a real-time dashboard demo at the booth.

## Plaud AI notes

App-generated, verbatim from Plaud's Summary tab.

> Date Time: 2026-09-15 11:12:05
> Location: [Insert Location]
> Instructor: [Insert Name]
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i1)

## Summary

The lecture, “Trust Is Not a Framework: Building Observable, Evaluated AI Systems in GxP,” outlines a practical, defensible approach to governing AI in life sciences by integrating IT-led observability with quality-led evaluation, and by adopting Evaluation-Driven Development (EDD). Drawing on deep QMS experience—pioneering a cloud QMS circa 2010–2011 (One Two Three Compliance, later Trackwise Digital), early AI work at Allergan (2008–2009) on implantable device survivability, and a 2018 talk on computer vision—the speaker argues for continuous oversight of how AI systems operate and how well their outputs meet intended use. <mark style="background-color: #F9EDD4">The session differentiates observability (what happened, why, and how risky) from evaluation (how good the outputs are against correctness, relevance, policy, and formatting), and emphasizes cross-functional IT–quality collaboration, prompt governance with audit trails, context engineering, safety signals (PII/PHI protection), change monitoring, and automated evaluators including an independent low-temperature “LLM-as-judge.</mark>” It introduces EDD with a Minimum Viable Evaluation (MVE) built alongside the MVP, a layered defense of graders (code, model, human), a “Judge Qualification Pack” to validate evaluators, and a continuous error-analysis loop to turn failures into improvements. The lecture focuses on GxP-aligned practices such as SOP-driven policy compliance, schema-controlled outputs (JSON/HTML), confidence scoring, and guardrails in prompts, with example applications in complaint handling, regulatory mapping, SOP checks, document generation, and RAG quality. A free AI lab handout guides hands-on work with observability and evaluation tools. Content created 2026-09-15; references 2008–2009, 2010–2011, 2018.

## Knowledge Points

### 1. Speaker background and context

- Pioneered early cloud QMS (2010–2011), later known as Trackwise Digital, bringing rigorous quality disciplines to AI governance in regulated GxP.
- Early AI at Allergan (2008–2009) on implantable device survivability; 2018 talk on computer vision for returns analysis.
- Acceleration of LLM/agentic systems necessitates new governance mechanisms grounded in QMS principles.
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i2)
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i3)
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i4)

### 2. From deterministic testing to evaluation systems (EDD)

- <mark style="background-color: #F9EDD4">Traditional pass/fail testing is inadequate for non-deterministic AI; instead, build continuous, context-specific evaluation systems.</mark>
- <mark style="background-color: #F9EDD4">Evaluation-Driven Development (EDD): develop MVP and Minimum Viable Evaluation (MVE) in parallel to embed validation from day one.</mark>
- <mark style="background-color: #F9EDD4">MVE components:
  1) Failure modes list (ranked by impact/likelihood)
  2) Golden set dataset (including unhappy paths)
  3) Simple graders with thresholds
  4) Review workflow with human-in-the-loop
  5) Regression baseline for comparisons</mark>
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i5)

### 3. Distinguishing observability vs. evaluation in AI governance

- <mark style="background-color: #F9EDD4">Observability (IT-led): traces/telemetry answer what/why/how risky; supports audits, root-cause analysis, and safety signals.</mark>
- Evaluation (quality-led): measures output fitness vs. correctness/factualness, relevance/completeness, SOP/policy compliance, and schema/format adherence.
- Integration is essential in GxP to meet expectations for traceability, reliability, and validation.

### 4. AI observability: core practices and tooling (IT-led)

- Tracing/telemetry: latency, token counts, error rates, tool failures, and costs for anomaly detection and troubleshooting.
- Context/lineage tracking: inputs, retrieved chunks, tools, and policies per output for auditability.
- Safety signals/guardrails: PII/PHI detection/redaction, jailbreak/policy violation monitoring, access controls, and automatic blocking.
- Change monitoring: prompt edits, model swaps, retrieval index updates, performance drift.
- Prompt governance/audit trails: controlled, reviewed, and versioned prompts; who created, modified, and executed; agent executions tracked.
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i6)

### 5. AI evaluation: automated quality assessment at scale (quality-led)

- <mark style="background-color: #F9EDD4">Dimensions: correctness/factualness, relevance/completeness, SOP/policy compliance, and format/schema validation for predictable integration.</mark>
- LLM-as-judge with independence: separate model from the operating agent; low temperature; applies “four eyes” quality principle.
- Confidence and silent failures: evaluators detect insufficient information and score low confidence to surface gaps.
- Tooling/templates: platform evaluators plus custom graders aligned to business needs; low (non-zero) temperatures for regulated use.
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i7)
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i8)

### <mark style="background-color: #F9EDD4">6. Layered defense: code, model, and human graders</mark>

- Code-based graders: deterministic checks (schema, citations, prohibited terms).
- Model-based graders: nuanced scoring (completeness, clarity, consistency); calibrated against humans.
- Human graders (SMEs): calibrate and validate judges, adjudicate edge cases, provide final accountability; shift to exception review post-deployment.
- <mark style="background-color: #F9EDD4">Judge Qualification Pack: intended use/boundaries, rubric definitions and thresholds, golden dataset, calibration report (SME-judge agreement), acceptance criteria with escalation rules, and bias check report.</mark>

### 7. Guardrails and prompt-level instructions

- Embed constraints to stop and escalate when required inputs are missing or to persist until completeness criteria are met (e.g., record counts).
- <mark style="background-color: #F9EDD4">SOP knowledge base informs agent behavior, aligning outputs with established workflows and compliance requirements.</mark>
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i9)
[](plaud://image?type=summaryCard&id=oc_su_7bc4c14f84ce4608cd029436aa687dda_i10)

### 8. Risk frameworks, metrics, and error analysis

- Use established frameworks (e.g., ICH Q9, GAMP) to define risk tolerance and evaluation methods; human quality retains sign-off.
- <mark style="background-color: #F9EDD4">Avoid generic vendor metrics; create context-specific, defensible metrics tied to intended use, control, factual integrity, and traceability.</mark>
- <mark style="background-color: #F9EDD4">Error analysis loop: name failure modes, build evaluators, run evaluations continuously, cluster failures to guide iterative improvements.</mark>

### 9. Example GxP applications and failure handling

- Complaint handling: information evolves; judge flags decisions made with insufficient data, assigns confidence scores, and updates as data accrues.
- Regulatory mapping: evaluate correct identification of applicable regulations given sufficient product/domain context.
- Complaint triage/reportability: assess classification completeness/correctness with confidence tracking and escalation triggers.
- SOP compliance checks: ensure outputs/actions align with organizational policies.
- Document/record generation: validate schema and factual accuracy for reports and structured outputs (JSON/HTML).
- RAG quality: evaluate retrieval relevance/completeness to reduce hallucinations and off-topic sources.

### 10. Organizational practices and lab resources

- Cross-functional alignment: IT runs observability, lineage, guardrails, change monitoring; quality defines evaluation rubrics, SOP alignment, independent judging.
- Hands-on AI lab: participants define prompts, select data, observe data flows and anomalies, and apply evaluation tooling to learn methods and rationale in practice.

## Assignments

- [ ] Establish prompt governance with full audit trails (creator, modifier, executor, agent runs) and approvals before deployment.
- [ ] Implement observability: end-to-end tracing (latency, tokens, errors, tool failures, costs), lineage tracking, safety signals (PII/PHI, policy violations, jailbreaks), and change monitoring (prompts/models/indexes, drift).
- [ ] Build/integrate redaction APIs to detect and redact PII/PHI; enforce blocking policies on detection.
- [ ] Create and maintain an SOP knowledge base; integrate SOP checks into evaluation pipelines.
- [ ] Design evaluation pipelines with rubrics for correctness, relevance/completeness, policy compliance, and schema; use an independent, low-temperature LLM-as-judge with documented confidence scoring.
- [ ] Configure and validate output schemas (JSON, HTML, reports) for downstream integration.
- [ ] Add prompt-level guardrails to escalate when critical information is missing or to ensure completeness criteria are met.
- [ ] Pilot high-value use cases: regulatory mapping, complaint triage/reportability, SOP adherence checks, and RAG quality evaluations; capture metrics and iterate.
- [ ] Conduct hands-on lab exercises to practice observability/evaluation, detect anomalies, and connect failures to root causes.
- [ ] Define temperature policies: low (non-zero) for GxP agents; separate, independent low-temperature judges; document rationale, thresholds, and controls.

## Transcript

[00:02] **Speaker 1:** Client side, and also as a vendor to life science organizations. Fun fact about me is I am a bit of a pioneer in the QMS space. And around 2010-2011 timeframe, I developed a me and my partner developed a quality management system in the cloud, which was unheard of back then, and. We kind of pioneered in the space, and ultimately, the name of our company was One Two Three Compliance. We were immediately snapped up, and now, in the industry known as Trackwise Digital, but that was literally our invention. It was just renamed as Trackwise Digital in the cloud. So, that's sort of my experience in the industry. Have a vast experience in QMS. Also on the AI side, as well, worked on several projects in life sciences. Probably one of the most interesting one was one that my colleague and I, Tim, worked on at Allergan many years ago, in roughly 2008-2009 time frame. We were working with implantable medical devices and trying to understand the survivability of those medical Devices like they were inside of patients, allowed us to hear from many different sources. Really good visual, from that so distribution, and trying to predict if there could potentially be a point in time where we need to take action. So the survivors really need that insight within a patient survivor. So that was a long time ago. Things have changed quite a bit since then. I gave my first presentation AI at Salesforce conference back 2018, I believe. It was a session using computer vision in the in the return analysis. Department within an organization, so using computer vision to do the visual analysis of returned products, and that was a pretty interesting session. Again, pre where we live today, right? Interestingly, in that session, I was giving a very technical presentation, and it turns out that maybe one percent of the audience was technical. So people had interest even back then, right? But fast forward to where we are today. Very different world, right? Things are moving so fast; it's really hard for us to even keep up. And so that's what the session is going to be about today. So, how do we think about observability and evaluation within an organization that's using AI for GXP purposes? And so, how many people here are even familiar with the terms observability and evaluation? One. Awesome, two, awesome. I had a suspicion that would be the case, so we'll we'll take it as it goes. I do like to interact with the audience, so the two people who raise their hands, please acknowledge the fact that you will be asked questions. That's the that's the trick question that I ask at front to get people involved. So. Make sure these are working. Does it look like they are? So let's just talk about AI observability and AI development. So really, how are we going to observe, for example, an agent as it's operating in our in our, Ecosystem. There's two different disciplines. You'll hear people use these terms interchangeably, but they're really not the same thing. Without looking at the screen, I'll ask one of the folks who raised their hands, " What do you think the difference is between observability and evaluation.

[04:49] **Speaker 2:** I guess observability is what it did, and evaluation is how good it did at its core.

[04:57] **Speaker 1:** Yeah. So great answer. So. The answer was what observability is. What did AI do, right? Whether it's an agent or a chat bot or whatever it happens to be, and then observability is how well did it do it. And so for me, whenever I see the two terms, I like to think it and quality, right? Observability is going to be handled most of the time by it. There. Running, they're running tools behind the scenes to understand, you know, what's happening, why it happened, when it happened, et cetera. We'll dive a little bit deeper. Whereas quality is more interested in, did the result like it actually make sense, right? Was it valid? So we've all heard the terms, for example, hallucination, right? And everybody's afraid of that term. It's like, oh gosh, you know, it's not. How do we how can how can we really prove that this answer is valid or correct? I classify that as evaluation, and so that's why we need to understand going forward. There has to be a close tie between IT and quality. We can't operate as two separate teams anymore when it comes to AI. We really have to work together closely. So that's kind of how we'll we'll kick it off here. And I did leave with you a handout. It's something that we offer in the national conversation. It's free. It's an AI lab, and it really dives into the details of what I'm going to talk about today. Today, I'm just going to talk about it. But in our lab, we actually walk you through the process of observability and evaluation using actual tools, and it gives you a feel for. In the real world, what needs to happen, how, and the why behind it. So, just a FYI on that handout that I gave you. So, we'll dive a little bit deeper into observability, and the reason why I said this is more of an IT function is because it's really about things that you as quality. How many folks are quality folks? Okay, IT. Figure as much. I knew you were. So that's a good ratio, and I kind of had a feeling that's what it would be. So, from an IT perspective, you're going to have folks out there running utilities that are going to identify things like tracing and telemetry, telemetry, right? So really, that's more about what's running in the background. How many tokens are you consuming? That's really important in our world, right? You know, basically, what is it going to cost, right? They're also going to be looking at context. Context is really where is the data coming from that the agent. I'm going to use the word term agent just kind of make it simple for everyone. You know, where is the data coming from that the agent is using to define the results? And there's a whole discipline around context engineering, and that's really about how do I ensure that the agent is using the appropriate data to make the decision that it's making, right? To provide the results that it's providing, and that's an extremely important function. So, from equality perspective and from a compliance perspective, you might be asking an audit, well. Show me the results from this particular prompt. Where did it get that data from to make that particular to come up with that particular answer? Right, you can't do that unless you have some tools behind the scenes, basically querying and saying this particular this particular prompt retrieve data from these particular sources. And so those are all IT functions behind the scenes. They're they're they're running constantly, and then other things might be like, it says safety signals here, but those are really guardrails, right? So do you have the guardrails in place? These are the reason why I classify it as IT is because behind the scenes, they're configuring things like ensuring that you know the response doesn't have any you know health information, patient health information in it. It doesn't have any, you know, PII data, and these are all things that can be controlled behind the scenes, right? So, as an example, if I if the tool sees that you know there's a patient making it up, social security number, and the response, it gets blocked, right? That would never make it to the infuser, and then change monitoring. So the ability to detect significant changes—it could be a change in a data source, as I just mentioned, right? It could be a change to the actual model that's being used. So these are all things that need to be in place behind the scenes, managed by IT, to ensure that you're running in a secure and safe environment, providing accurate results. So. In our lab that we've developed, you actually go through the process of defining. In a, we we create a scenario for you. You define a prompt, right? You define what data actually will feed into that prompt, and then you actually go in and you observe the data using one of the tools that we've provided for you. And you can see, and we set up scenarios where. You know we've pre - defined where you'd see and find anomalies in in the system, but this is very important. So we'll switch then from IT folks, and if an IT person wants to share some input, please feel free to add.

[11:39] **Speaker 3:** Nope. Well, I'll ask on behalf of IT folks. Okay. So we're talking about AI. I don't. I have a friend here at Napa. It's focusing on the prompts rather than you know the output that comes out. So, is there any talk? I mean, can you please you know tell me where are any standards or work being done about actually having an audit trail for prompts, having a repudiation element of prompting? The prompting really is the user need. The so the user things they're doing right.

[12:12] **Speaker 1:** And your name is.

[12:13] **Speaker 3:** I'm Larry.

[12:14] **Speaker 1:** Larry. Larry, Larry, ask a question. I'm doing repeating for the folks who are online. Right. So, from the perspective of monitoring AI, you know, is there any way that we can monitor the prompts themselves, right? An audit trail, the prompts, et cetera.

[12:33] **Speaker 3:** To that level of it is now a record. What prompting between?

[12:36] **Speaker 1:** Yes. And I did not. Again, name again. Larry. Larry, I'm horrible with names. I did not plant. Larry in the audience, but that's literally what our product does. So one of the things that it does is we recognize because we've been in the industry forever. One of the first things we did was all prompts are defined and audited and approved before they're even allowed to even go out and roam around in the ecosystem. So there's an audit trail: who created it, who modified it, and who's executing it. And if it's executed by an agent, then that also tracks as well. So there, there are tools to do that. Ours is one of them.

[13:20] **Speaker 3:** Yeah. Yeah. So yeah, I'm not planted. We're obviously thinking the same thing. Yes. And and think of also the next step is timing and validation. What do validation?

[13:32] **Speaker 1:** And so then the next question was how do you validate that? We'll talk a little bit about that today. Great question. So then, if we move on to from a quality perspective, so we've got all those guardrails in place from a technical perspective, right? All those things are being monitored behind the scenes, alerts are being generated, but really from a quality perspective, that's not enough, right? It's great for the IT folks; they can tell us all these really cool things they're doing behind the scenes, but, Is my prompt actually returning, or is my agent actually returning accurate results? Nobody knows, right? So, is it correct? Is it factual? Is it relevant, right? Remember going back to the data, right? Is it is it relevant to the intended use? That also goes back to the prompt, by the way, Larry. So, if your prompt isn't being provided the. Proper context; it can lead to incorrect results. An example is, for example, our validation product, right? It's used in for different types of life sciences organizations. It could be med device, it could be biotech, it could be pharma, right? But if your prompts aren't providing enough context, and I ask, for example, the agent to you know. Based on this requirement, tell me which regulations are applicable. If I didn't apply it enough context, it's going to come back with all sorts of crazy answers, right? So that's very important, and that's something we see all the time. So it's important to provide that that context to get the the proper response relative to what you're trying to the problem you're trying to solve. Policy compliance. I think everyone here can relate to this. You're probably already doing some. Level of this already, but you do want to have a knowledge base of your SOPs in place, so that any agent that you might be running within your organization is adhering to the same policies that you, as a human, adhere to, and so that's important as well. And then formatting and schema. You may not have gotten there yet, but for us, it's extremely important. The response itself, right? How do you want it to come back to you? Do you want it to come back in just kind of plain text, like you see in your chat all the time? Do you want it to come back as a report? Do you want it to come back as HTML? Do you want to come back as JSON so you can feed it to another system and update another system? All those things are important and can be controlled. But the important things I think for the folks here in the room are correctness, relevance, and compliance. Any questions or comments here? Yari? Yes.

[16:46] **Speaker 4:** One point about completeness. I agree, and also another thing that I've observed is many times the polls will fail silently, meaning that they won't tell you that it can only see a particular thing portion.

[17:06] **Speaker 1:** Yeah, Yari brought up a very good point. Is in it that a an agent or an AI algorithm or an LLM, whatever you want to call it, can fail silently? It may not know that it didn't have enough information to provide the correct answer. Interestingly, using evaluation. You can track its confidence in its response, and it will tell you. So I'm getting ahead of myself, but you'll basically use another LLM to judge the LLM that's running in your in your environment, and the other LLM will say he didn't have enough information to answer that question, and I'm going to rate it as low in confidence as far as accuracy goes. So Yari, thank you. Jumped a little bit ahead, but that's okay. And Tim. Yes , It is important. So you've got the LLM as a judge, and then you have the LLM that's actually running in your environment to respond to your prompts or questions. They can never be the same. It's like the four eyes principle in quality, right? You've always got another person to check the work of another person.

[18:28] **Speaker 3:** Yes. That makes sense. You you don't know what you don't know. So how do you? What's the metric for the quality of that pairing? What's the rephrase? What's the metric for the quality of that pairing? You're you're kind of you're your mutual allies checking each other.

[18:45] **Speaker 1:** What if they both don't know anything? One's actually checking all that information that IT kind of collected behind the scenes. So that judge is actually checking like where did that data come from? For example. That was a good example that we had, where there wasn't enough information to provide the the answer. So, as an example, let's say it's a complaint system, right? Complaint comes in, and it's typically they don't come in as complaints; they come in as tickets, right? Then they have to be classified as a complaint, and then potentially reportable to an authority. But let's say you didn't have enough information to make that particular decision, to make it reportable or not, and so the judge would be able to determine whether or not there was enough information to make that decision. It could be that maybe there was a piece of information that was dropped during an integration, right, and the agent of the agent made. Its best guess based on the information that was provided, the judge and it would like Yari said silently would silently answer the question. The judge would say, "No, you didn't have a critical piece of information to make that that statement." For example, there was a death, right? That came in later. That's a common thing that happens in the complaint world, in that you're not going to get all the information up front, right? But later on, you might find that there was something. That changed the makeup of that information, and the and the judge would say, " Hold on. When this decision was made, there wasn't enough information. At that time, the accuracy level was maybe sixty percent. Now we're going to bump it up tonight. That makes sense.

[20:48] **Speaker 3:** Yeah, it does. So the judge has the human empathy filter turned way.

[20:52] **Speaker 1:** Down. Yes. Speaking of which. Getting ahead again. There's different ways to. How many people are familiar with temperature in AI? It it it. Quality quality knows temperature. Temperature is a setting that dictates how creative the algorithm can be. Set high, it's going to wildly exaggerate. Set low, it's going to try and stick to the facts.

[21:29] **Speaker 6:** Low. Want high for? I just out of curiosity, what industry is like? I wanted to make things up. Entertainment, marketing.

[21:38] **Speaker 1:** That's not good. Let's not go there. So, someone for the folks who are on the call, someone said, " When would you ever want to set the temperature high in our industry? Never in the entertainment industry, one hundred percent, right? But you can't set it to zero, right?" Then why are you using the LLM in the first place? So you have to give it some leeway to actually respond, right? Creatively. So we usually set just very low, but not zero. Yes.

[22:16] **Speaker 7:** Yes. What I've done as far as the agent, I kind of rely on the instructions, so I kind of set the requirements in the instructions, so it kind of knows the process is working once it. So if it's missing any information, then it stops and it escalates back to the user to upload or give this type of information. So it doesn't just move forward and close the line. It's pluggable.

[22:40] **Speaker 1:** Yes, and your name is Jonathan. Jonathan said he actually added on that you can also build some of those constraints into your prompts as well, so that I've had to do this as well where. You're basically telling it right. If you don't have the appropriate information, then stop, right? And one that I always do is opposite of that: don't stop, continue until you get the right. So there's some cases where you'll get a response that's not based on the full set of data, and like no, tell me how many records you. Start it with. Tell me how many you ended with, and if that number isn't the same, keep going till you get me the full answer, right? And so we have to do creative things like that to make sure that we're getting the proper response. And so this goes back to why we need tools like this because not everyone's going to be able. Not everyone's a Jonathan, right? And so their prompts may not be fully baked, and so we've got these guardrails in place to catch. Scenarios where we make it incomplete or inaccurate responses. So, just this is something that I think everyone in the room already knows. We've just moved beyond deterministic testing to evaluation systems. We can no longer rely on the original ways that we tested, right? Because we knew what we were looking for. We knew that. We knew that we were looking for a very specific outcome in our response, right? In our testing, you know, pass or fail, right? It either one plus one equals two or it doesn't, right? But in today's world, that's no longer the case. We have to look at the things we talked about in the prior slide. You know, what's our tolerance for accuracy, right? Is ninety nine percent acceptable? Is ninety percent acceptable? Depends on the use case, right? It could be a low risk use case, and you're willing to accept that risk. In other cases, not. If it's super high risk, then you probably want a human in the loop, anyways,

[25:10] **Speaker 2:** Right? I have a little question about that. It's it's a it's a question about like, how do people? I understand risk based assessment. Ultimately, someone has to say I'm acceptable. I feel this level of risk is acceptable, but what frameworks are they doing it? Are they just doing it like is it a partially emotional decision as well? That like I'm willing to sign my name on this, or what? What are people thinking when? Because I come from research, unregulated, do whatever the hell you want kind of a space, and I'm this is new for me, so I'm kind of.

[25:43] **Speaker 1:** Bunch of quality people. I want a quality person, and I'm an IT person. I want a quality person to answer that question.

[25:51] **Speaker 5:** Yeah, so. The job is to build it. I build a quality, approved FDA approved agent. My agent is an FDA three years experience. Here's what I've done for years how I do it. I run it against all his builds. When he builds it, sends it to me. I run it through that. Gets me a score and says, user score 15, 60. Yes, it's FDA approved or not. Here's what you have to fix. I send it back to the right and say, these are your gaps. So it's easier for me as the final signature to say, I'm the last one. So let's make sure everything's perfect. We train the assistant agents FDA approved.

[26:21] **Speaker 6:** So There's other frameworks that have been in place for a long time to be very clear about what's detectability, what's probability. You know, ICHQ, ICHQ. Within here, they can be extended to other technologies, including AI.

[26:45] **Speaker 1:** So they're both on the call, but the room can't. The mic doesn't work.

[26:53] **Speaker 6:** To go through the frameworks that we have that's already in place in ICH as well as in GAMP, there are definitions for what risks are and how to evaluate them. And then, per every organization, you need to determine what your tolerance is for those risk categorizations. It's not just how I felt this morning when I woke up because I have a headache. It has to.

[27:26] **Speaker 1:** Yeah , And honestly, all of that should already be defined in your risk procedures and policies. So, yeah, it shouldn't be just kind of how that person felt at the point in time. So, when you're signing off, this is like a it comes up practically every conversation we have with folks. You're signing off. It's not the agent's decision; it's yours, as a quality person. So that's something that we have to reiterate over and over. And it's also why we built those checks into our system to prevent just allowing the agent to make quality decisions on behalf of people. So moving forward, so. How does that change kind of the way we deploy systems that are AI enabled? We really want to think about what we talked about already and how do we move quality forward in the process from a project perspective? And so we talked about observability and evaluation. That's something you need to bake into your implementations as early as possible. You don't wait till the end and then. Turn it on, and I will talk about why you don't want to do that. So, really, this is basically what we're calling evaluation-driven deployment. You've performed your observability and your evaluation against the agent before you deploy it into production. You're doing it during the implementation process, where you're defining and configuring and developing. So, what does that really mean? From an evaluation perspective, it means just like you would with any other project, you know, identifying what what are the failure modes, and we'll talk a bit a little bit more about this in detail. But now you've got a lot more failure modes, right? You've got the agent, you've got the data that it's consuming, you've got the prompt that was developed. You've got so many failure points. You're going to have to start identifying those and understanding, you know, what could actually happen during the process, and how are you going to mitigate that risk? And then you'll want to have kind of a golden set of data. I'll go back to something that I see a lot is when people start out with deploying AI. Data is key, right? But what you don't know, and it goes back to what Yari said, silent, silent failures, right? One of the biggest example I've seen is, and I deal with complaint systems a lot, is well, the data that you use to train the algorithm was like the happy path, and so you're going to continue to get happy path answers because you didn't provide. The data set that would have allowed it to train on, you know, when things go wrong, right? And so it's important to have a golden set that represents a variation of the possibilities in your in your data set. And then it mentions simple graders here, just kind of keeping it simple. It kind of contradicts what I said earlier about pass fail, but in reality, you do want to kind of. Dumb it down to pass bell initially because you don't want to over engineer your evaluators initially. You want to first understand how they work, get comfortable with them. So when I say pass bell, you think about that percentage accuracy. And I said, you know, what are you comfortable with? The pass bell is if it's ninety percent accurate, I'm happy. That's a pass. If it's not, then it's a bell. That way, people aren't having to do the mental. Exercises every time something something doesn't match a threshold. You don't have to figure out okay, what was the threshold and blah. You just know it passed or failed, right? So that's what I mean by keeping it simple. And then definitely reviewing the workflows means keeping human in the loop to confirm during that process when you're setting up your evaluations, and then having a baseline for regression testing. It all leads up to that. So let's talk about the framework itself. So, one thing that I always like to say to people, and the IT folks in the room will understand this: you're going to see that there are different technology vendors that provide this type of functionality out of the box. It it looks great, but It's not going to really solve your problem, right? It's going to be generic. It's going to apply generic graders to your, to your algorithms, to your LLMs. And so, although it may look great, it may look like a shiny new tool. You really need to think about what is the problem that you're trying to solve, and define metrics that make sense in your environment. So, kind of a high level of what we just talked about. the The process that you want to follow is, like I said, define your failure modes, build your evaluators, run them, and then cluster your failures. So you can look at trends. Right, where where am I most often seeing a problem with my evaluations? Is it that you know the agent is not getting enough information? To provide the proper response, okay, let's dive a little bit deeper. Why is that? Is it the quality of the data, or is there something that's failing along the way, and data is being dropped? Those kinds of things. And I have a question up front.

[34:04] **Speaker 5:** How would, when you're just beginning, how would you know what's failing?

[34:11] **Speaker 1:** And that so the question was in the beginning, how would you know what's failed? You've got to put the tools in place. So essentially, you're running these tools behind the scenes; they're telling you what failed. And we actually have a dashboard. Could probably pull it up at our booth if you want to see it. That shows you kind of here's all the prompts and the responses that we're receiving. Here's basically where the judge. Classified these particular prompts, giving them a passfail pass/fail rate, and it also says, by the way, to I think it was Jonathan's point. I think I got the name right. By the way, here's here's how you could improve that prompt that was sent to the element.

[35:00] **Speaker 7:** Yes. The one thing I didn't have to name is I just think about as building an employee, and then the instructions become. On like a job description for that employee, and then once you know the process, I think it makes it easier to to define what the failure modes could.

[35:16] **Speaker 1:** Be. That's a very good point. That was Jonathan in the back room. So one of the things he does is he always thinks of the agent and the prompt as you know an employee, right? And so he's defining the skill set for that particular employee and what they should and shouldn't do. Things like that. If I paraphrase correctly, yeah. So that's one way to think about.

[35:43] **Speaker 8:** It. So one thing I always get a little hung up on on the tools that are like AI that check the AI.

[35:51] **Speaker 6:** Is like, how does that ever end? Like, who's checking the AI that checks the AI, and then who's checking that AI that checks? You know, like how does that ever end exactly?

[36:01] **Speaker 1:** That's another common question. So who judges the judge? You yeah, you kind of have to provide. You have to think of it from the same perspective that this if it was a human, right? You can't, you know, it's endless, right? Yeah, so I would say at a minimum, your judge needs to be validated, right?

[36:25] **Speaker 2:** And just to add to it, there are practices where you align, measure the alignment of the judge against the human, and you again define an acceptable criteria for allowing it to deviate from the human five percent of the time.

[36:40] **Speaker 1:** Better you can say that.

[36:42] **Speaker 2:** Graders, right? I wasn't planning to.

[36:44] **Speaker 1:** You didn't look at this long enough. So three different types of judges, right? Code - based graders, which are basically the traditional ones, right? Very deterministic. You don't. It depends, right? It depends on the use case, right? But then model - based graders, which is another LLM, and then. Eric, Eric said upfront, human graders, right? The human grader is actually going to be confirming that the model - based grader was correct, and you do that kind of upfront in the beginning. You can't continuously.

[37:20] **Speaker 6:** I was going to say, is that just to get some interval, or you just kind of do it when you're getting it set up, and then you assume it stays, or you have to come off and you do?

[37:27] **Speaker 1:** You definitely want to make sure that that human is involved because that human is actually going to be providing information and feedback to the model. So that it's better trained up front, and then once it goes into production, you probably want to look more at exceptions, right? So, yeah. And and for that. Periodic.

[37:48] **Speaker 2:** And for that human grader, it is usually a subject matter expert.

[37:52] **Speaker 1:** Subject matter expert is the human grader. Someone in the back had a.

[37:56] **Speaker 8:** Yeah. Or one model checking another model, all very popular. It's about 76% effective right now. The fact that maybe both don't work, so that's where human players are important. It's still good to have.

[38:22] **Speaker 1:** That. Yeah, we definitely get to a point. So there was a comment in the back that you know we're not 100% there yet, so we still need to keep a human in the loop. But you know, there's a certain point where it's moving too fast and we can't keep up with it, right? So we kind of take it on an exception basis, and then also reviewing like model drift is something you have to review for, right, Yari? You know that very well, and so you definitely have to have periodic checks as well and exceptions. So. I think I might be at time, so I'll leave us with this kind of, you know, the judge qualification pack. So I think this has been said by multiple folks out in the audience today. Is really knowing the intended use and the boundaries, and that's kind of what Jonathan's been talking about in the pat in the back about making sure that when you're defining your prompts. And your agents that they understand the intended use of what of their role, right, and the data, and the use of the agent itself, and then defining your scoring and thresholds. We talked a little bit about that, but most importantly, what is the acceptance criteria? So as I mentioned, you know, twenty percent. I'm sorry, ninety percent, ninety-nine percent. What's best for you in your environment? And then one other thing I think I'll leave us with is basically the the calibration report, which is essentially statistics on how well the not only the agent but the judge and the statistics that are coming out that you can use as an exception report. Yeah, what do you do to act on? And I think I might be at time. Yes. So thank you. But if you want to do it real time.

## Related

- [[Home]]
- [[An LLM judge is a GxP system and needs its own qualification pack]] - the judge-qualification pack from this talk
- [[Validating an AI system in a regulated industry means validating a measurement system]] - the evaluation half of the stack
- [[AI Validation and Acceptance Criteria MOC]]

---

← [[2026-09-15-1024-gorani-ai-governance-human-risk-gxp.md|Gorani on human risk]] | [[Home]] | [[2026-09-15-1201-shelly-lapointe-data-foundation-for-ai-in-gxp.md|LaPointe on data foundation]] →
