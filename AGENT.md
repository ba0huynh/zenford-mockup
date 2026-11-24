# Zenford Phase 1 prototype

This guide is the starting point for changes to the prototype. It records the project context, the decisions behind the UI, the three walkthroughs, and where to find any additional requirements. Routine UI changes can use this guide and `index.html`.

## Product

Zenford is VENEXUS's online language-learning platform. The initial offerings are English, Chinese, Japanese, Korean, and Vietnamese for non-native speakers. Language is configurable in the product. An account can hold independent entitlements for Basic self-study and Học với AI. An expired entitlement affects its own product access. The learner's progress and competency profile carry across learning environments.

- **Learning.** Placement and competency profile, individualized planning, booking, Pre-class, live teacher-led class, Post-class verification, daily practice, AI notebook, and progress. Basic includes self-study courses, exercises, and assessments.
- **Public website and sales.** Discover programs, take a placement test, request consultation, shop for products, and enter account, checkout, and enrollment. Sales and finance workflows cover leads, orders, contracts, payments, refunds, accounting, and commissions.
- **Role-specific portals.** Learners see their work and schedule. Parents see connected learners, attendance, reports, and fees. Teachers see assigned classes, Pre-class reports, grade work, and track their schedule and earnings. Collaborators (CTV and affiliates) see referrals, commission, and wallet.
- **Staff operations.** Admin CRM is the workspace for sales, academics, teaching, marketing, customer support, HR and recruitment, finance, and system/AI configuration. Học thuật owns the learning material used by teaching, Basic, and marketing. AI provides drafts, evidence, or recommendations. The relevant human role approves consequential steps.

The Phase 1 package is business analysis and design. This repository's deliverable is a local HTML presentation of that design. The same UI can be demonstrated offline with fictional users, files, scores, and statuses.

## Files and architecture

- Open [index.html](index.html) directly in a current browser. CSS, JavaScript, screen catalog, artwork, and the spoken sample are embedded. There is no install or build step.
- The `ux-data` JSON block copies the screen metadata and navigation from UX-02. It contains 614 screen IDs across eight areas: public website (38), learner portal (66), AI learning workspace (28), parent portal (25), teacher portal (38), collaborator portal (8), Admin CRM (381), and email/PDF previews (30).
- `#SCR-Mxx-nn` is a stable URL fragment. `#danh-muc` opens the searchable catalog. `#pre-done` is a prototype-only completion view. Preserve the `SCR` IDs and keep catalog and deep links usable directly from `file://`.
- The `custom` map assigns authored views to priority screens. Everything else uses `genericScreen` to render wireframe components, illustrative fixtures, and links to nearby screens. When a screen needs more fidelity, add an authored view and register it under its existing ID.
- `preState`, `academic`, and `cv` hold temporary demonstration state in memory. Hash navigation preserves it in the current document. A full reload resets it. Helpers such as `pageHeading`, `workspace`, `card`, `table`, `pill`, `link`, and `button` keep repeated UI consistent.
- Keep the deliverable buildless and self-contained for mockup requests. Use anchors for navigation, native form controls, and small vanilla JavaScript handlers for UI state and prewritten outcomes. Keep live AI, APIs, accounts, real file processing, user-data storage, and communications outside this prototype scope.

## Walkthroughs

### Học với AI · Pre-class

Open [Việc hôm nay](index.html#SCR-M42-01). The fixture is **Ordering at a café**, Tiếng Anh A2, class ENG-A2-07. Show the lesson time, deadline, estimate, and three stages. Learners can re-enter the preview at the last visited stage.

1. [Chẩn đoán](index.html#SCR-M42-02). Show the question count, sample multiple-choice, written, and spoken questions, then separate concepts already understood from areas that need practice.
2. [Dạy nền](index.html#SCR-M42-03). Teach the gaps in the learner's explanation language, show a worked example, offer another explanation, and let the learner explain it back or flag that a teacher should help.
3. [Luyện tập](index.html#SCR-M42-04). Present café role-play, an embedded sample recording, a simulated spoken answer, pronunciation feedback, and retry. Finish with a note in [Vở học AI](index.html#SCR-M45-07).
4. [Teacher progress](index.html#SCR-M42-05) links to the [teacher report](index.html#SCR-M42-07) and [email preview](index.html#SCR-M42-08). The report shows class-level errors, pairing or activity suggestions, individual results, and “Chưa đủ dữ liệu” where needed.

In the product, known material can skip re-teaching, repeated difficulty can be flagged for the teacher, and quota or service interruptions preserve progress. Live class and Post-class are separate stages. Sources: SRS-06 M42, BF-M42-02/03, UX-01 learner and teacher journeys.

### Xưởng học thuật · Academic AI

Open [Đề bài học thuật](index.html#SCR-M16-03), then [Tạo đề bài](index.html#SCR-M16-04). A brief includes a topic, language, level, deliverables, permitted sources, a quality checklist, and an appropriate final reviewer. The default topic is **Giao tiếp tại quán cà phê**. Changing it updates the simulated run context.

- [Cấu hình agent](index.html#SCR-M17-03) keeps an independent provider/model pair for each agent and production branch. Providers are Claude, ChatGPT, and Gemini. Changing the provider refreshes the model list for that role. Model labels are demonstration fixtures.
- [Pipeline](index.html#SCR-M17-04) shows the currently active stage, waiting and completed stages, version, and handoff log. The stage sequence is research, curriculum design, script, production, independent AI QA, manual QA, then final academic approval. Research, curriculum, and script have expert approval gates in the walkthrough.
- Production runs four parallel branches in the product: books and exercises, assessments and rubrics, audio, visuals/slides/video. The HTML shows the branches and their selected models. Walk through **Chạy bước**, **Hoàn thành bước**, and **Chuyên gia duyệt** where shown.
- At **Kiểm định**, select **Mô phỏng kiểm định trả về** to send the run back to **Sản xuất**, with a reason and a new version on retry. The demo defect is a missing phrase at the end of audio sentence 3. The log shows the correction and the return to QA. [Báo cáo kiểm định](index.html#SCR-M17-07) and [So sánh lần chạy](index.html#SCR-M17-06) show the review and version fixtures.
- After passing AI QA, the language expert confirms [Kiểm định thủ công](index.html#SCR-M17-08). The academic lead approves publication in [Phê duyệt và phát hành](index.html#SCR-M16-12). A return records the affected stage, reason and version. Published material appears in [Kho học liệu](index.html#SCR-M16-08).

Sources: SRS-04 M16/M17, BF-M17-01 to BF-M17-04, UX-02 SCR-M16 and SCR-M17. Shared provider configuration is M04.

### AI review CV · Recruitment

Start at [Tin tuyển dụng](index.html#SCR-M29-02) or [Xếp hạng CV](index.html#SCR-M29-04). The fixture is a vacancy for an online English teacher. The [application preview](index.html#SCR-M29-01) uses a sample CV and shows the consent step. The same fictional candidate IDs connect ranking, evidence, and the [candidate pipeline](index.html#SCR-M29-07).

- Show the [job-specific rubric](index.html#SCR-M29-03), version, weights, mandatory criteria, invitation threshold, and near-threshold band. The sample uses 40/30/20/10 weights, a threshold of 75, and a band of ±5.
- In the ranking, show the AI scores and the **Cần xem lại** filter. Nguyễn An has a complete sample result, Trần Bình is near the threshold, and Lê Chi has an unreadable file with no AI score. Keep missing evidence explicit.
- Put criterion-by-criterion explanations and CV excerpts near the original CV preview. Use job-relevant experience, qualifications, skills, and education as evidence. The SRS excludes age, gender, marital status, hometown, and portrait from scoring.
- **Điều chỉnh điểm** records a mock HR score and reason beside the original AI score. **Mời phỏng vấn AI** and **Dừng hồ sơ** require human input and show the selected transition in the pipeline. Recruitment decisions belong to HR and the department lead.

Sources: SRS-05 M29, FR-M29-02/03/04/05, BF-M29-01, UX-01 recruitment journey.

## UI skills and visual rules

- **Sites skill.** For a website or prototype change, consult the Sites skill for local static implementation and browser verification. This HTML deliverable uses the local-only workflow. Use the existing entry point and scope.
- **imagegen skill.** Use for new project raster illustrations when they make the experience clearer. The original fox reading a yellow book is embedded in `hero-asset`. The UI diagrams and timelines are HTML/CSS.
- Use the [Zenford sample](http://demo.citgroup.vn/Zenford-web/mau1/) for visual direction. The mockup draws on indigo text, bright yellow raised primary actions, pale lavender, mint and sky accents, rounded containers, and friendly typography. It uses Baloo 2 for the hero and brand, and system text for dense screens.
- Use the same tokens in the public, learning, and admin views. Give the public site and study moments space and friendly illustration. Keep CRM tables and workflow views compact enough for comparing items. On small screens, stack panels and allow horizontal scrolling inside tables and nav.
- Keep interface labels in Vietnamese, with native-language lesson examples where appropriate. Put a single clear primary action near the content it affects. Use text as well as color for states such as **Cần chạy lại**, **Chờ người duyệt**, and **Cần xem lại**. Keep focus visible and associate fields with labels.

## Verification

See [the Phase 1 audit](AUDIT.md) for coverage by portal, fixture assumptions, known gaps and repeatable checks.

Open `index.html` offline and run each walkthrough end to end. Test with a desktop viewport and a phone-width viewport. Check direct links and browser back navigation. For the catalog, search `kiem dinh thu cong`, filter by area, open a result, and check the 614-screen total when filters are clear. For the academic path, change one provider, verify its model choices, trigger a QA return, run the correction, and finish both approvals. For CV review, inspect a flagged CV, edit a score, and confirm the original score stays visible and the human decision appears in the pipeline.

## Source lookup

The source package is `Zenford_Ho_so_Giai_doan_1_v1.0-20261124T044003Z-1-001/Zenford_Ho_so_Giai_doan_1_v1.0/`. Use the precise ID to find an unresolved detail in one source.

| Source | Look here for |
| --- | --- |
| `00_Zenford_Huong_dan_bo_ho_so_GD1.docx` | Package map, document precedence, traceability, and outstanding project decisions |
| SRS-00, SRS-01 | Product overview, shared architecture, access, configuration, AI providers, audit, integrations, and handover |
| SRS-02, SRS-03, CT-01 | Public website, commercial workflows, finance rules, Basic, learner and parent portals |
| SRS-04 / SRS-05 / SRS-06 | Academic and marketing AI / internal operations and AI recruitment / learning cycle and teacher workflows |
| SRS-07, SRS-08 | Sitemap and screens, roles, configuration, notifications, reports, open questions, and traceability |
| UX-01, `02_Trai_nghiem_nguoi_dung/Zenford_UX-02_Wireframe.html` | Role journeys, screen relationships, components, and the source catalog |
| TK-01/02/03, schema JSON, OpenAPI YAML, BM-01 | Production architecture, data, API contracts, privacy and access boundaries |
| KH-01/02/03 | Delivery sequencing, test strategy, and formal acceptance cases |

`FR` identifies a functional requirement, `BF` a flow, `BR` a business rule, `SCR` a screen, `CFG` a configurable setting, `OI` an open issue, and `AC` an acceptance case. Sample dates, thresholds, models, scores, and staffing details in the HTML are fixtures. For production changes, confirm open configuration decisions in SRS-08 and use the applicable SRS and acceptance case.
