# Zenford Phase 1 mockup audit

## Verdict

The HTML preserves all 614 UX-02 screen records and the original eight-area navigation. The purpose and ordered component list of every screen agree with the corresponding screen definition in SRS-01 through SRS-06. That comparison covers 3,622 purpose and component entries. SRS-07 independently contains the same 614 screen IDs.

Every screen has an explicit fixture mapping. The original 27 priority screens retain their authored walkthroughs. Additional routes use task-specific shop, learning, finance, family, communications and operations views or searchable record tables. The tables use per-screen or domain datasets. The extra `#pre-done` route is a completion state outside the 614-screen inventory.

## Findings corrected

| Source | Previous behavior | Corrected demonstration |
| --- | --- | --- |
| SRS-06 FR-M42-02/03, BR-M42-02 | Every set of responses produced the same strengths and weaknesses. | The choice, written answer, and selected speech sample determine the concepts marked understood. A fully correct attempt can go directly to practice. |
| SRS-06 FR-M42-04/05/06, BR-M42-04/06 | The roster initially showed a learner halfway through teaching and the teacher report assigned that learner strengths. | Starting, practicing, and finishing update the sample state. The report withholds conclusions for unfinished learners. The roster marks overdue work at the displayed sample time. The practice error appears in the notebook when the feedback is shown. |
| SRS-04 BF-M17-01/02/03, SCR-M17-06 | A returned curriculum or script appeared as an audio correction, and the comparison could lose intervening revisions. | Each return records the affected item and reason. Rerunning records the next version. Earlier corrections remain available in the comparison. |
| SRS-04 SCR-M17-08 and SCR-M16-12 | Final approval shared the manual-QA route and the library status stopped at approval. | Manual QA hands the item to the academic lead's release screen. Publication updates the library fixture. |
| SRS-04 SCR-M16-04 and SCR-M17-03 | Japanese and English could share mismatched level choices. The reviewer was labeled English even for other languages. | The brief offers language-specific example levels, program, competency block, output type and deadline. The pipeline shows the selected review language and the agent configuration explains the four academic AI groups. |
| SRS-05 FR-M29-03, SCR-M29-04 | Some quoted evidence was absent from the displayed CV. A filter could leave details for a hidden candidate on screen. | The CV preview and quotations share the same source text. Scores have candidate-specific rationales. The score band and review filter apply together, including empty results. |

## What the sample values establish

- The three CV records use fictional names and files. The criterion maxima are 40, 30, 20 and 10. The two scored CVs total 86 and 73 points. The unreadable file has a blank score. The demo threshold of 75 and band of ±5 place the 73-point CV under human review. SRS-05 assigns these settings to VNS through CFG-M29-02/03.
- The café lesson, ENG-A2-07, sample deadline of 17:30, class time of 18:30, pronunciation score of 82, and example recordings are fixtures. SRS-06 defines the relationship between booking, deadline, evidence and reporting. It leaves timing and attempt limits configurable.
- The academic topic, model menu, sample returns, and people are illustrative. SRS-04 defines the research, script, production, independent QA, and human review responsibilities. The screenshot brief additionally requests Claude, ChatGPT and Gemini choices per agent.
- Currency amounts, course durations, IDs and dates in the preview illustrate display formats. Commercial policy and formulas have separate ownership in CT-01, SRS-02 and SRS-08. The mockup does not establish approved prices, fees, refund rules, or live model availability.

## Remaining fidelity limits

The shop, checkout, learner forecast, placement, class booking, selected CRM tasks and original guided demonstrations support linked interactions. Many secondary staff screens share a record-table layout with filtering and details. The document comparison verifies the source inventory. Browser checks verify navigation, width and representative workflows. Individual source controls, approval policies and service errors across all 614 screens have separate production acceptance cases.

The authored workflows also cover selected cases. Academic QA and version screens omit full run-cost accounting, side-by-side artifact diffs, and editing individual checklist items. The recruitment form uses a fixed sample CV and identity. The rubric view displays one fixed version. The interview uses three written prompts and saves typed responses during the session. Pre-class uses deterministic answers and prerecorded speech. Provider errors, quota enforcement, and persistence across reloads are outside the demonstration.

Use the mockup to review navigation, handoffs, selected screen states and fixture consistency. Production acceptance, role-based access enforcement, integrations, and complete business-rule coverage require separate verification against the applicable SRS and KH-03 cases.

## Customer learner update

The customer draft supplies the 23 learner views and their shared November 2026 fixture. The Phase 1 audit above describes the original source inventory. Use the [project guide](AGENT.md) for the current competency blocks, tuition examples and English lesson data. The customer’s archival review annotations are available in the original HTML. Learners see a menu of activities and services.

## Repeating the checks

- Run `python tests/audit_student.py` to compare the learner inventory with the customer HTML and exercise its bookmarks, check-in, booking, learning evidence, notebook, fees, library and phone navigation offline.
- Run `python tests/audit_sources.py` from the repository. It compares the original local DOCX, UX-02 and HTML without network access.
- Run `python tests/audit_mock.py` with Python Playwright and Edge installed. The browser context runs offline. Set `ZENFORD_BROWSER` to another installed Chromium channel if needed. The checks exercise every screen at 390px and 1440px, inspect internal links, and cover the data regressions above with selected interactions.
- Run `python tests/audit_populated_views.py` to check a two-copy print order, discount and shipping arithmetic, payment history, milestone evidence, a paused course, CRM notes and a submitted support ticket.
- For a stakeholder walkthrough, follow the three paths in [AGENT.md](AGENT.md). The audit also exercised source-rights validation, per-agent model selection, a QA return through the next approval and release, the teacher report, and HR score adjustment and candidate decisions.
