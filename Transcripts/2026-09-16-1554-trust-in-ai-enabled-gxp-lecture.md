date: 2026-09-16
recorded_at: 2026-09-16T15:54:45-04:00
duration_seconds: 804
type: transcript
conference: "KENX AI in GxP East 2026"
source: plaud
plaud_id: of_22028b45df37099ad2faac79afc42819
plaud_name: "09-16 Lecture: Trust in AI-Enabled GxP Environments"
speakers:
  - Speaker 1
  - Speaker 2
  - Speaker 3
presenter: Aarti (Amy) Arora
affiliation: "Principal, RxT"
session: "Strengthening AI Systems with Built-In Cybersecurity and Access Control, part 2 (day two)"
tags:
  - kenx-gxp-east-2026
  - transcript

# Trust in AI-enabled GxP environments lecture, part 2

> Recorded 2026-09-16 at 1554 via Plaud. 13:24.

## Summary

> Part 2 and conclusion of Aarti (Amy) Arora's lecture, resuming the moment part 1's recording cut off (SailPoint as quality's frenemy, since security teams get the budget). The talk's four trust checks: the system works as intended, unauthorized users cannot act, records and prompts and models cannot change unnoticed, and monitoring runs continuously. Responsibility splits by strength rather than merger: quality leads GxP risk assessments and CSA validation while security supports to test trust; security leads vendor and architecture reviews and access-control design while quality layers in nuance; monitoring belongs to everyone.
>
> She introduces the S.H.A.R.E. tabletop framework for AI use cases: Scope the intended use, name what could go wrong (and right), Align on which controls can be shared with a named owner, Reuse existing evidence so each control is tested once, and Exercise failure in a safe space. Her three takeaways: build security in as early as quality, share the design, and test trust rather than just functionality; quality builds confidence, security sustains trust. Q&A covers harmonizing evidence across GxP, SOX, cyber, and ESG audits (the working answer: a non-qualified platform holding the steps to recreate testing, with GxP steps layered on top, borrowing SOX's testing discipline), and consolidating role sprawl using license cost, training burden, and usage-log levers, with read-only study access as the main proliferation driver and no observed correlation between access roles and human-in-the-loop qualification.

## Plaud AI notes
<!-- markdownlint-disable MD033 MD026 -->

<App-generated notes from the Plaud cloud, verbatim.>

> Date Time: 2026-09-16 15:54:45
> Location: [Insert Location]
> Instructor: [Insert Name]

### Plaud summary

This lecture, recorded on 2026-09-16, focuses on building and sustaining trust in AI-enabled GxP environments by positioning Quality and Security as collaborative partners throughout the lifecycle—from early design through continuous monitoring. It introduces a practical, tabletop-style S.H.A.R.E. framework to align cross-functional controls, evidence, owners, and next actions; advocates “testing trust” beyond functionality; and clarifies shared responsibilities between Quality and Security without forcing role mergers. The latter portion covers implementation realities: harmonizing evidence for audits across GxP, SOX, cybersecurity, and ESG; managing access-control sprawl with consolidation strategies; leveraging role-based training and cost levers; and noting that “human-in-the-loop” training labels are generally not tied to specific access roles.

### Knowledge Points

### <mark style="background-color: #F9EDD4">1. Shared Trust Responsibilities between Quality and Security</mark>

- Risk Assessment and Controls Leadership Balance
  - Quality typically leads GxP risk assessments due to process and compliance context; Security partners by framing impact and aligning with control frameworks (e.g., NIST), where Security is better positioned to lead.
  - Vendor and architecture reviews are best led by Security (architecture, control requirements), with Quality partnering to ensure QMS presence and compliance readiness; the aim is to “choose wisely” so vendors meet control requirements.
- Access-Control Design and Validation Roles
  - Security should lead access-control design to ensure controls are testable; Quality adds GxP nuances and ensures traceability and validation suitability.
  - CSA (Computer Software Assurance) and validation are led by Quality, with Security supporting to “test trust” (beyond functionality), ensuring controls perform as intended and unauthorized actions are prevented.
- Monitoring and Continuous Assurance
  - Periodic reviews and incident handling are shared across Business, IT, Security, and Quality; the aspiration is to evolve from periodic to continuous monitoring.
  - Monitoring is “super critical” in AI-enabled environments, ensuring records, prompts, and AI models cannot change unnoticed and that unauthorized users cannot act.

### 2. “Everyone Owns Trust” Mindset and Partnership Model

- Partnership over Merger
  - Core principle: Quality does not need to become Security; Security does not need to become Quality; they must be strong partners.
  - Quality builds confidence through design and validation; Security sustains trust through controls, monitoring, and architecture; together they protect patients and enable innovation.
- Patient-Centric Alignment Technique
  - When disagreements arise, start with shared truths: serving patients and ensuring products are safe and effective.
  - Trace back from this common ground to locate misalignment, then identify a common control to realign teams.

### <mark style="background-color: #F9EDD4">3. S.H.A.R.E. Tabletop Framework for AI Use Cases</mark>

- Framework Steps and Timing
  - S (Scope, 5 min): Define the AI use case and intended use. Use existing intake models to select a problem with clear ROI and shared business value.
  - H (Harm, 5 min): Identify what could go wrong (and what could go right). Quality, Cyber, Business, and IT contribute risk perspectives relevant to AI and GxP.
  - A (Align, 10 min): Determine which controls can be shared; assign a named owner for each shared control to avoid diffusion of responsibility. Test the control once and reuse the evidence across functions (Security, Quality, IT).
  - R (Reuse, 5 min): Leverage existing evidence repositories and prior test artifacts to avoid redundant testing across domains (e.g., reuse for SOX, cybersecurity, ESG).
  - E (Exercise, 5 min): Test failure modes via safe-space failure prompts and tabletop injections, rehearse cross-silo responses, and document exceptions and accepted risks.
- Outputs and Ownership
  - Conclude with: shared control, named owner, evidence link, next action + date. Track after-actions or exceptions, explicitly documenting risk acceptance and planned mitigations.

### 4. Build Security Early, Share Design, and Test Trust

- <mark style="background-color: #F9EDD4">3 Key Takeaways
  - Start Early: Build Security in as early as Quality—“quality by design” and “secure by design” together.</mark>
  - Share the Design: Make shared risks and decisions explicit; establish shared ownership and clear RACI-like guidance without rigid enforcement.
  - Test Trust: Test controls and monitor together, focusing on protecting patients while enabling innovation. Validate permissions and ensure proper segregation of duties and access behaviors.

### 5. Practical Evidence Harmonization Across Audit Regimes

- Challenge and Iterative Solutions
  - GxP evidence and documentation often differ from cybersecurity and software-control evidence expectations; harmonization is non-trivial and may require multiple iterations.
  - Initial attempts: start with “lowest-touch” evidence, then build up; alternatively, start with “highest-touch” GxP and extract lower-touch elements. The final approach lands in the middle.
- Final Approach
  - Use a non-qualified platform to store all steps needed to recreate testing and evidence. For SOX, cybersecurity, or ESG audits, evidence can be retrieved directly. For GxP, follow specific steps layered on top of the shared evidence.
  - Leverage SOX discipline for control testing methodology (“how do you test your control”), strengthening GxP practice. Expect some rework across both sides to achieve sustainable, shareable evidence across countries.

### 6. Access-Control Sprawl and Consolidation Strategies

- Managing Role Proliferation
  - As features expand, granular permissions multiply, enlarging the role matrix. Apply a “cyber lens” to rationalize.
  - Use levers: license cost analysis (advanced roles may cost more), role-based training burden (e.g., 19 training items tied to a role), and actual usage logs to assess necessity.
  - When the matrix becomes unwieldy (e.g., far-right columns in Excel like “AA”), pause to consolidate: analyze license costs, training load, and usage frequency; eliminate or merge roles accordingly.
- <mark style="background-color: #F9EDD4">Read-Only and Study Access Nuances
  - Role proliferation often comes from restricting access to specific studies even for read-only needs.</mark> Where appropriate (e.g., non-confidential studies, non-M&A contexts), simplify by allowing read-only access, significantly reducing the number of roles.
- Human-in-the-Loop Association
  - Observed practice: training programs may label “human-in-the-loop,” but this labeling is typically not correlated to specific user role combinations in access-control systems.

### 7. Trust Controls and Questions of Unauthorized Actions

- Core Trust Checks
  - Verify systems work as intended; ensure unauthorized users cannot act.
  - Detect whether records, prompts, or AI models can change unnoticed; implement monitoring to capture such changes.
  - Reinforce that monitoring is a shared responsibility and central to sustaining trust in AI-enabled GxP operations.

### Questions

- [Insert Question/Confusion]

### Assignments

- [ ] 1. Convene a cross-functional tabletop S.H.A.R.E. exercise (Quality, Cyber, Business, IT) to select a common ROI-positive AI use case; document scope, harms, shared controls with a named owner, evidence link, next action, and date.
- [ ] 2. Define a shared control framework with explicit owners; establish a single-test, multi-reuse evidence policy across Quality, Security, IT, SOX, ESG audits.
- [ ] 3. Implement continuous monitoring for AI systems to detect unauthorized actions, unnoticed changes to records/prompts/models, and permission misuse; plan migration from periodic reviews to continuous assurance.
- [ ] 4. Rationalize access-control roles: analyze license costs, role-based training requirements, and usage logs; consolidate roles where feasible, especially for study read-only scenarios.
- [ ] 5. Create or update an evidence repository on a non-qualified platform with documented steps to recreate tests; define additional GxP steps required when evidence is used for GxP audits; ensure global shareability.
- [ ] 6. Establish “secure by design” alongside “quality by design” in early lifecycle stages for AI-enabled GxP systems; integrate Security in design reviews and Quality in validation planning.
- [ ] 7. Develop failure-prompt scenarios and run tabletop exercises to “test failure” in a safe environment; record exceptions, accepted risks, and mitigation plans with dates and owners.

### Highlights (button-flagged moments)

#### this is part two, last recording was truncated

• Context: The analysis did not identify any substantive discussion, decisions, or action items in the provided content.

#### Speaker Outlines Collaborative Framework for Quality and Security Responsibilities

The speaker explains the presented slide, detailing a flexible framework for shared responsibilities between Quality and Security teams across various activities, emphasizing it is a 'conversation starter, not a rigid RACI.'
• Visual Context: The slide displays a chart assigning 'Lead', 'Partner', or 'Shared' roles to Quality and Security for tasks like 'Risk assessment', 'Vendor + architecture review', and 'Periodic review'.
• Discussion Insight: The speaker clarifies that for GXP, Quality leads risk assessments, while Security is better suited to lead on vendor architecture reviews and access-control design.
• Key Takeaway: The proposed model is not a strict RACI chart but a flexible guide to foster partnership, ensuring that both Quality and Security contribute to their strengths without needing to become experts in the other's domain.

#### Presenter Details the "S.H.A.R.E." Framework for Cross-Functional AI Governance

The speaker presents a slide detailing the "S.H.A.R.E." framework and explains it as a tabletop exercise designed to align Quality, Cyber, Business, and IT teams by defining scope, assessing harm, aligning on controls, reusing evidence, and testing for failure.
• Visual Context: The slide outlines a five-step framework called S.H.A.R.E.: Scope (What is the intended use?), Harm (What could go wrong?), Align (Which controls can we share?), Reuse (What evidence already exists?), and Exercise (How will we test failure?).
• Discussion Insight: The speaker explains that the 'Align' step is crucial because while controls are shared, each must have a specific owner, and the goal is to 'test it once, and use the evidence once' across different departments like security and quality.
• Key Takeaway: The S.H.A.R.E. exercise is designed to break down departmental silos, resulting in actionable outcomes: a shared control, a named owner, a link to the evidence, and a defined next action with a date.

#### Speaker Summarizes Key Takeaways for Integrating Security and Quality

As the presentation concludes, the speaker verbally reiterates the three key takeaways displayed on the slide: starting early, sharing the design, and testing trust, emphasizing the core message that Security and Quality must become effective partners.
• Visual Context: The slide presents '3 Key Takeaways': building security in early, making shared risk explicit, and testing controls by monitoring together.
• Discussion Insight: The speaker explicitly walks through the three takeaways on the slide, reinforcing the idea that while Quality and Security don't need to become experts in each other's fields, they must partner effectively.
• Key Takeaway: The central theme is that Quality builds confidence and Security sustains trust, and their collaboration is essential to serve patients and ensure product safety.

#### Role proliferation is often driven by a desire to restrict access to specific studies, even for read-only roles.

• Speaker 1 explains that a common reason for creating excessive roles is when someone wants to prevent access to a particular study, even if it's not a sensitive topic like a merger and acquisition.
• The justification for creating these new roles is often that they are 'read-only' and the study is not confidential, so the perceived risk is low.
• While Speaker 1 has not seen a direct correlation between user roles and a 'qualified human in the loop' status, they have seen training programs label their training as 'human in the loop'.

<!-- markdownlint-enable MD033 MD026 -->
## Transcript

[00:00] **Speaker 1:** Salepoint, other cybersecurity tools—they have the money. Oftentimes, quality like we don't get the budget that cybersecurity gets. So then you can start using their tools if you qualify. I'm in the in the GXP life. So Salepoint became like a frenemy of mine over time. So does it work as intended? Can unauthorized users act? Can records, prompts, or AI models change unnoticed? And lastly, this is the one I'm going to beat this dead horse because it's a passion point of mine. Is monitoring, monitoring becomes super critical in this world that we're stepping into. And the cheesy part of me that was ingrained—I think I was brainwashed—is everyone owns trust, just like everyone owns quality. Everyone owns trust, and yes, there's going to be some areas where quality takes a lead role, and security takes a partner role. Vice versa. This isn't like a rigid racey that I want you to go back and be like, "Hey, look what I learned." Like security has to lead this, and quality has to lead this. But there's areas where risk assessments for GXP, it makes sense for us to lead that. There, the NIST controls make sense for them to lead it. But the vendor and architecture review to have security review their architecture makes way more sense than someone in quality. And Sure, we need to make sure they have their QMS in place. So there's a partner, but ultimately we need to choose wisely, someone who can meet all of our control requirements, access and control design. I let security lead those conversations. I go for the ride, as quality, and then like layer in if there's any nuances. But security, at least our security team did a way better job at leading these conversations than I did. CSA validation, obviously, quality would lead that, but security. Supporting it so that we test the trust, not just the functionality, and then periodic review. We know this the fun time where if we get away from periodic to continuous, but everyone has a role in that. The business, IT, security, quality, everybody has a role. So as I promised, a good party or like a total nerd nerd event. This where I think it's I'm adorable. We come up with a share share what you learned. So this is something I learned when we took on the business. I took on the business continuity practice as well. So all of this was like a huge, do these things, and I had no idea how to do them. But the concept of a tabletop exercise, I know we do them in a lot of functions. I will say, business continuity teams do this better than anyone I've seen, where they come up with a base scenario. They start injecting like what could go wrong, and you have to react. And it could be like in any situation, not an IT situation. COVID was a great example, where we would talk through what would happen in these different scenarios. But imagine if we took that rigor and that like same framework and mindset, and did it with all of our use cases. And I want to quote Anand from Simicon earlier. He said, "You know what would be cool? It's for ROI. It's for everyone in the room to like." Unanimously, come up with a business problem that they want to solve. So that becomes the you. The you share. If I were to change this, I actually submitted my slides on time this time, which never happens. So I couldn't change it. But if you share, ubiquitously, come up with a business problem that everyone wants to solve, and that you're going to get ROI from, then this is the share. Bring together quality, cyber, business, IT. What's the AI use case? Once you figured out what the problem is, what's the intended use? Spend like five minutes on that. You probably already have like an intake model where you have like a bunch of them, a bank that you can choose from. Pick one. Then you talk about what could go wrong. And I heard earlier someone say, "But what could go right?" I think that's a great lens to add: is what could go right? Why we want to try this? But then what could go wrong? And this is where it's fun because quality will bring in what could go wrong from Quality perspective, cyber will bring in theirs, business IT, and like flipping to the back of the book. What's funny? It's the same controls that actually prevent what could go wrong, that harm. Even though we have different things that could go wrong, the same controls prevent that harm. Which controls can we share? And this the A and the align, and I put this in my favorite color because this important. Is while you have a shared control framework, you do have an owner for the control. That if you start doing this, like you might miss it entirely. So this A, which controls, can we share? That means you test it once, and you use the evidence once. You don't have to test it four times, one for security, one for quality, one for IT. Just test it once. Reuse what evidence already exists. That's the R and share, and then exercise. How will we test failure? So just in a safe space, inject some failure prompts and figure out how you can work through it. Really cool framework to talk across silos and come up with an end-to-end, very rarely used case. So how can we have the shared control? Who owns it? How we're going to evidence it? Like we can all link to it, and then if there is an after-action that comes up or an exception, track that to say we're accepting this risk. This this going to happen, and then what are we going to do? So. If I could just leave with three takeaways: number one, build security as early as quality; have that protection by design, not just quality by design. Share that design, like with the share framework we just went through, and then test the trust. Don't just test the system; test the ability to do things with different permissions. And my biggest takeaway: this is I think, if I knew this when I started the journey, I thought I had to become like a security expert. And I'm like, you know, you guys have been doing this for 20 years. I've been doing it for like 20 minutes. But I felt the pressure. Like I thought I had to become quality, a security expert. So, my therapy notes, if I were to journal this, like what the, what people do these days. Quality does not need to become security. Security does not need to become quality. You just like need to become good partners. And talk to each other, not like. Think your control is worded better than their control. Like pick the fights that matter, and ultimately, quality builds confidence, security sustains trust, and then together, this is any time you disagree with anyone at work. My favorite thing to do is like start at the one thing we know to be true, which is like, are we here to serve the patients? If anyone answers that no, just walk out of the room because like, that's just they just want to be combative. But if you start with okay. Is it fair to say we all want to serve patients? Okay, cool. Is it fair to say that we want to make sure the product is safe and effective? Yeah, okay, that's cool too. And then you trace it all the way back and figure out where you like no longer align, and then find a way to get that common control to get you back into alignment. But that's really that's really all about protection by design, and happy to engage in any dialogue or use cases or anything around.

[07:37] **Speaker 2:** Good question on the controls and the evidences, right? So in a GxP world, there is certain rules of, you know, how you have to have a documentation to be able to present it to auditors and, you know, audit, you know, B and everybody. Whereas in a software controls, whereas in such a security controls related, right, the level of evidence is not exactly. How you use it in the FDI? Yep. Or even for in a GXP environment, so how did you manage to come together to that single setup for evidence in a platform when we do that testing? Like when you say that we you know test it together, you know if you talk to the cybersecurity even in the soft and say, hey, I don't need to do all this you know this format and you know what you expose, what you exposing in GXP environment, hey, we need to have this certain format and it to be presentable. So how did you bring it together to. Make it sustainable and shareable across the countries.

[08:43] **Speaker 1:** You know, it's a great question. My like short answer is it wasn't easy, and I got it wrong like five times. Right, so the first time was okay. Let's first try it with the lowest common denominator. Let's do it with like the least touch, and then see if we can use that as a Lego to build the highest touch. And then we said, wait, wait, that's like weird. Then we said, okay, let's try it with the GXP, the highest touch, and then extract. The lower-touch stuff, and we landed somewhere in the middle, which is we landed in a non-qualified platform that held all the steps to recreate and in evidence. So, like, if you needed to use it for SOX, cybersecurity, or ESG audit, you could grab it from there. If you're going to GXP, follow these steps, and it had like that. That's the discipline that SOX brings in, as it tells you how do you test your control. That I feel GXP could use a little bit more. But it, we did, we tried all of them and it ended up somewhere in the middle with a little bit of rework on both sides. Any other questions or similar stories that you guys have gone through?

[09:50] **Speaker 3:** Shouldn't it be an online question?

[10:08] **Speaker 1:** Here we go. Just a lot of good call out though. Anything else? I know I'm standing between you and the airport. I'm standing between me and the airport. But anything else?

[10:24] **Speaker 3:** Uh, for for access management, uh, you mentioned there was a one point you had like 200 roles, and then you ended up consolidating down. Um. I think we've seen as as new features come out, the rate of technology will change, the pace will change. There's always new features, there's always new capabilities, and the trend seems to be that because everyone likes these granular permissions, that every time there's a new feature, there's a new separate permission for that feature. Yeah. As well. So, how do you manage? What's the best way to manage access controls when your matrix is just going to continue to grow?

[11:03] **Speaker 1:** Yeah, like my joke answers very carefully, but it would be honestly. That's where like I would say the cyber lens really came in, and the what the one hand I said is also like role based training. I was I was almost able to say like, hey, if you give if I give you this role, you got to train on these nineteen things. But like, how often are you really going to do it? And does this like really make sense? And is this a point in time? Because also the licenses cost more for some of those advanced roles. So we I use different levers like cost. And training and what's in it for me, but I highly recommend. Like once you start seeing that matrix get like to the double A on the Excel spreadsheet, like when you start going far right, take a minute to look at it, consolidate it. Look at your license costs. Look at how much you're training people, and say, and then look at the usage logs and say, how often do you actually do it, and consolidate as much as you can from there.

[11:56] **Speaker 3:** Do you see a a particular, Access group combination being associated with a qualified human in the loop, perhaps like where someone says that this person is qualified human in the loop if they have been given this particular level of access because that's been governed by this training program. Is there a correlation?

[12:18] **Speaker 1:** I haven't seen. Well, not to say it doesn't exist. I haven't looked at it through that lens. What I can say is where I see the roles proliferate often is like. Oh well, I don't want someone to look at that study, so I'm gonna create a new role. Why not? It's a read-only. It's not a merger and acquisition. It's a study. No one's like likely gonna go in there. It's nothing confidential, and they have read-only. I've been able to reduce roles a ton that way, but I haven't seen a human a qualifier for human in the loop. What I have seen is training programs start to label their training human in the loop, but not correlated to a user role. Anything else before we wrap up? And of course, you know how to find me if you have any questions. Obviously, this is going to stay on your mind for like the rest of the week. If anything comes up later, just let me know. Okay. Cool. Thanks, guys.

## Related

- [[Home]]
- [[2026-09-16-1521-ai-protection-by-design-gxp-lecture|Part 1]]
- [[Governance Risk and Human Factors MOC]]
