# Zenford Phase 1 prototype

This guide is the starting point for changes to the prototype. It records the project context, the decisions behind the UI, the three walkthroughs, and where to find any additional requirements. Routine UI changes can use this guide and `index.html`.

## Product

Zenford is VENEXUS's online language-learning platform. The initial offerings are English, Chinese, Japanese, Korean, and Vietnamese for non-native speakers. Language is configurable in the product. An account can hold independent entitlements for Basic self-study and Học với AI. An expired entitlement affects its own product access. The learner's progress and competency profile carry across learning environments.

- **Learning.** Placement and competency profile, individualized planning, booking, Pre-class, live teacher-led class, Post-class verification, daily practice, AI notebook, and progress. Basic includes self-study courses, exercises, and assessments.
- **Public website and sales.** Discover programs, take a placement test, request consultation, shop for products, and enter account, checkout, and enrollment. Sales and finance workflows cover leads, orders, contracts, payments, refunds, accounting, and commissions.
- **Role-specific portals.** Learners see their work and schedule. Parents see connected learners, attendance, reports, and fees. Teachers see assigned classes, Pre-class reports, grade work, and track their schedule and earnings. Collaborators (CTV and affiliates) see referrals, commission, and wallet.
- **Staff operations.** Admin CRM is the workspace for sales, academics, teaching, marketing, customer support, HR and recruitment, finance, and system/AI configuration. Học thuật owns the learning material used by teaching, Basic, and marketing. AI provides drafts, evidence, or recommendations. The relevant human role approves consequential steps.

The customer learner draft supplies the current learning experience and fee examples. The Phase 1 package is business analysis and design. This repository's deliverable is a local HTML presentation of that design. The same UI can be demonstrated offline with fictional users, files, scores, and statuses.

## Customer learner portal

The customer’s 24 November 2026 draft is the design and behavior reference for learner-facing work. Start at **Không gian của tôi** on the public site. In the portal, **Mục lục học tập** opens all 23 screens and links to support, orders, activated plans and the café Pre-class exercise. On phones use **Thêm**. The customer’s HTML stays at the repository root as the original reference. [Customer draft](<Cổng học viên Zenford - nháp1.html>) · [Learner portal](index.html#SCR-M14-02) · [Design skill](.agents/skills/zenford-neo-pop/SKILL.md)

| Customer screens | Learner experience |
| --- | --- |
| HV-01–04 | Daily tasks with reasons and time estimates, feeling and readiness check, class preparation, and check-out compared with the baseline. |
| HV-05–07 | Weekly calendar, booking and availability, 12 competency blocks with evidence, before/after progress and the weekly study clock. |
| HV-08–14 | The Lab hub, listening transcript/dictation, speaking role-play, reading evidence, guided writing corrections, Hỏi Zen and Vở AI with flashcards. |
| HV-15–18 | Owned library and activation, video lesson with anonymous Q&A, exercise and results, and a watermarked reader with word lookup. |
| HV-19–21 | Per-language tuition, renewals and mock invoices, dated notifications, privacy, guardian reports and night mode. |
| HV-22–23 | Four-step onboarding and a resumable placement assessment example opened at the writing section. |

The shared learner fixture is **Minh Anh, Tuesday 24/11/2026**. English A2 → B1 uses Kết hợp. Japanese N5 → N4 uses Học với AI and has billing data. The full lesson fixture teaches English. Gia Hân is the guardian’s second learner, with a paused Japanese course and no current payment due. Start the English study clock at 186/210 minutes this week, with 3/12 blocks passed, block 4 needing help and block 5 in practice. The B1 forecast moved from June to August 2027. Tonight’s class with cô Lan runs 19:30–20:30 with check-in due at 19:15. The English billing period has 5 of 8 sessions used and 372 of 600 Zen minutes used. Monthly illustrative prices are 390,000, 1,590,000, 2,290,000 and 3,990,000 ₫ for AI, group, mixed and 1-to-1 respectively. One month is full price, three months save 5% and six save 10%. Auto-renewal starts off for each language.

In `index.html`, edit `student-styles` and `student-views` for the learner portal. `studentScreens` maps each customer slug, HV identifier and stable SCR bookmark. The outer router owns browser history and mounts one sandboxed `srcdoc` frame that shares the embedded fonts and mascot runtime. Messages synchronize navigation, café practice evidence and purchased books. Keep messages limited to recognized destinations and the active frame. Forms and all simulation data stay local. Use `V[slug]` for a view, `V[slug].after` for its handlers and `D` for shared learner data. Refresh resets the demo. For a focused review, open `index.html#HV-01` through `#HV-23`. Run `python tests/audit_student.py` for the customer portal and the existing audits for other roles.

## Files and architecture

- Open [index.html](index.html) directly in a current browser. CSS, JavaScript, screen catalog, artwork, and the spoken sample are embedded. There is no install or build step.
- The `ux-data` JSON block copies the screen metadata and navigation from UX-02. It contains 614 screen IDs across eight areas: public website (38), learner portal (66), AI learning workspace (28), parent portal (25), teacher portal (38), collaborator portal (8), Admin CRM (381), and email/PDF previews (30).
- `#SCR-Mxx-nn` is a stable URL fragment. `#danh-muc` opens the searchable catalog. `#pre-class-cafe` opens the supplementary café exercise overview and `#pre-done` opens its completion view. Preserve the `SCR` IDs and keep catalog and deep links usable directly from `file://`.
- `custom` holds the original priority walkthroughs. For other routes, `genericScreen` chooses an authored entry from `userRoutes`, a task renderer via `viewTypes` and `specialViews`, or a populated `recordList`. `routeRecords` contains per-screen fixtures, and `collections` holds reusable domain records. Each dataset starts with column names and follows with rows. Stable hash IDs stay in `ux-data`. Use its requirements as design input. Write the visible interface in end-user language.
- For a new screen, choose a realistic starting state, provide data with consistent units and dates, and link the result of each primary action to its destination. Test empty and changed states. Forms, filtered tables, conversations, checkouts, and dashboards have separate templates. Rendering a wireframe paragraph as a card leaves the task unfinished.
- `preState`, `academic`, and `cv` hold temporary demonstration state in memory. Hash navigation preserves it in the current document. A full reload resets it. Helpers such as `pageHeading`, `workspace`, `card`, `table`, `pill`, `link`, and `button` keep repeated UI consistent.
- Keep the deliverable buildless and self-contained for mockup requests. Use anchors for navigation, native form controls, and small vanilla JavaScript handlers for UI state and prewritten outcomes. Keep live AI, APIs, accounts, real file processing, user-data storage, and communications outside this prototype scope.

## Populated site walkthroughs

- **Shop and payment.** Open [Cửa hàng](index.html#SCR-M10-01), search `cafe`, open the title, expand the preview, and add the printed book. The eight products span five languages. Search, four filters, sort order and pagination work together. Digital quantities are one per product. Printed books support multiple copies. `ZEN10` gives a 10% illustrative discount on items, with a 25,000 ₫ delivery charge for an order containing print. Checkout creates one pending order. Confirming simulated payment adds it to [order history](index.html#SCR-M13-04) and grants access in [the library](index.html#SCR-M11-09). The separate [plan selector](index.html#SCR-M13-01) delivers a paid plan to the learner’s entitlements.
- **Learner forecast.** The [competency roadmap](index.html#SCR-M46-01) opens the 12 blocks, evidence and August 2027 target. The [prior-week log](index.html#SCR-M46-03) details 150 minutes for 16–22 November. The [parent forecast](index.html#SCR-M46-04) includes the separate paused learner, Gia Hân.
- **Other entry points.** Use the learner, parent, teacher and collaborator home pages to reach daily work. Try booking a class, checking a certificate with `ZF-A2-024`, completing the short placement activity in any of five languages, or sending a support request. Contact enquiries become CRM leads. A lead’s detail link carries the selected person and their notes. The browser’s full reload starts a fresh demonstration.
- **Authoring and checks.** `storeState` connects shopping, totals, payment and entitlements. `road` and `milestones` connect forecast views. `localView` holds page state, while related tasks share their records explicitly. Keep user-entered text escaped and derive totals from the same rows shown in the interface. Run `python tests/audit_populated_views.py` for the populated journeys, alongside the source and all-route audits.

## Walkthroughs

### Học với AI · Pre-class

Open [Check-in](index.html#SCR-M42-01) and choose **Luyện thêm trước buổi**, or open the [café exercise](index.html#SCR-M42-02) directly. This supplementary fixture is **Ordering at a café**, Tiếng Anh A2, class ENG-A2-07. Show the lesson time, deadline, estimate, and three stages. Learners can re-enter the preview at the last visited stage.

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

Use the customer’s learner portal draft for layout, navigation, copy, study behavior and tuition examples. The Zenford Neo-Pop kit supplies shared brand assets. Use the Phase 1 wireframe for the screen catalog and for workflows outside the customer draft. [Zenford design skill](.agents/skills/zenford-neo-pop/SKILL.md)

### Page treatments outside the customer learner portal

- **Public and sales.** Start with white paper. Use one large cyber-yellow area on the homepage, ink text and a dark primary action with a white offset shadow. The learning journey uses a mint section with white cards. The language section uses sky with five labeled language glyphs. Teacher features use peach. An order summary can use ink with white text, a yellow heading and a yellow shadow. Aim for roughly 60% white, 25% pastel, 10% ink and 5% yellow across a sales page. Group up to three adjacent pastel card colors, with the five language glyphs retaining their assigned colors.
- **Learner, teacher and operations workspaces.** Keep the canvas and large panels white. Use pastel on small hints, the active step, skill markers and status tags. Keep tables upright and dense enough to compare rows. The primary task action is yellow. Put feedback next to the response and identify it in words. A QA return should remain legible in the timeline, and both the original and adjusted CV scores should remain visible.
- **Color tokens.** Ink `#141414` for type, outlines and hard shadows. Paper `#FFFFFF`, soft `#F6F7F9`, divider `#E4E7EE`, muted text `#555B68`, yellow `#FDE047`. Pastels are mint `#BDEFD8`, lavender `#D8CCFF`, peach `#FFD2B8`, sky `#BFE4FF` and butter `#FFF1A8`. Reserve cobalt `#2F4BD8` for the logo. Success uses `--good` for outlines and `--good-text` for text on white. An incorrect answer gets a dashed `--bad` border and “✕ Chưa đúng”.
- **Semantic colors.** English `A` / sky, Chinese `中` / peach, Japanese `あ` / lavender, Korean `한` / mint, Vietnamese `Ă` / butter. Show the language name with the glyph and use the `--lang-*` aliases. Listening uses sky, speaking peach, reading mint and writing lavender through `--lab-nghe`, `--lab-noi`, `--lab-doc` and `--lab-viet`.
- **Typography and shapes.** Use Bricolage Grotesque 800 for headings and large numbers (20px minimum), Be Vietnam Pro for body, labels and captions (12px minimum), and system fonts for CJK glyphs. Use tabular digits for scores, times and money. Keep prose near 60 characters per line. Ink borders are 2.5px on controls/cards and 2px on tags/progress. Use hard shadows of 3/4/5px, growing to 8px on hoverable cards. A pressed button travels its shadow distance. Corner radii are 10/14/20/26px or pill-shaped. The kit supplies a 28px notebook grid and a race checker pattern.
- **Identity.** Use the supplied horizontal SVG logos at 110px or wider, or a mark at 24px or wider. Allow clear space of a quarter of the mark height. Use the cobalt logo on white/pastel and the reverse logo on ink. The rotation is built into the asset. Zen is a robot cat with a white head, yellow ears and LED eyes, a black face screen and a pastel shirt. Use the supplied artwork or runtime. Limit each screen to one speaking Zen and one decorative Zen. Place a small Zen beside a study hint. Pair headphones/microphone/book/pencil with listening/speaking/reading/writing, a cape with success, a helmet with racing and a TV with notices.
- **Voice and controls.** Address learners as “bạn”, parents as “ba mẹ” or “phụ huynh”. Zen speaks as “Zen”. Use short Vietnamese sentences, sentence-case titles and action labels. Uppercase is reserved for short marketing overlines. Zen gives a clue and lets the learner try. Mark illustrative fees “minh họa”. For renewal, default to a reminder with a payment link and QR. The outcome commitment offers one repeat of the unmet section. Use Lucide line icons at 20/24px with a 2.5px stroke and a text label, except for menu/cart. Keep emoji, pink, decorative color gradients and floating confetti out of the UI.
- **Motion and access.** Use 100–200ms for presses and hover, 500–800ms for reveals and 1–1.6s for progress. Keep slight sticker tilt on marketing illustrations only. Honor reduced motion with a static final state. Preserve visible keyboard focus, native controls, labeled states, phone stacking and scrollable tables.

The single-file runtime embeds both fonts, their licenses, the supplied CSS tokens and component bundle, the logo assets and Zen’s SVG renderer. Call `ZenfordNP.mount(main)` after inserting a route. Reuse the existing helpers and design skill when editing the prototype. The full kit is available for precise component or asset lookups. [Design kit](<Zenford Neo-pop 1/Zenford Neo-Pop/README.md>)

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
