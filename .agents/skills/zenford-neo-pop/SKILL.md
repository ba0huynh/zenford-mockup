---
name: zenford-neo-pop
description: Build and review Zenford HTML screens using the customer’s learner portal design, Vietnamese copy, shared learning fixtures and offline navigation. Use for learner flows and for applying Zenford styling to the public site and other portals.
---

# Zenford interface design

Use the customer’s **Cổng học viên Zenford - nháp1.html** as the primary learner design reference. Its `SCR` inventory names HV-01 through HV-23. Its `COMMON` and `NOTES` explain the design decisions. The root guide summarizes the fixtures and routes for everyday edits. The older Neo-Pop kit supplies the logo, Zen, fonts and reusable tokens. [Customer reference](<../../../Cổng học viên Zenford - nháp1.html>) · [Project guide](../../../AGENT.md)

## Compose a learner screen

1. Find the slug in `studentScreens` in `index.html`. Edit `V[slug]` inside `student-views` and add screen styles to `student-styles`. Reuse `PH` for the heading, `zsay` for hints, `.c` for panels, `.btn` for actions and `.tag` for status. Send internal navigation through the portal bridge. The parent owns bookmarks and back/forward history.
2. Keep the study canvas paper white, type ink and the primary action yellow `#FDE047`. Use sky for listening, peach for speaking, mint for reading and lavender for writing. Give the yellow, pastel and dark surfaces readable foregrounds. Use Bricolage Grotesque for titles and Be Vietnam Pro for Vietnamese text. Preserve the customer’s compact 76 px rail, 256 px expanded state, clear outlines, short hard shadows and mobile bottom tabs: Hôm nay, Lịch, Lab, Hỏi Zen, Thêm.
3. Use one mascot identity, Zen the robot cat. Tie its expression to a specific prompt, hint or outcome. Address the learner as **bạn**. Name the action and show its result beside the relevant work. Keep focus visible, label buttons and inputs, provide plain-text status with color, support dark mode and reduced motion, and let a narrow calendar stack above its details.
4. Use the shared `D` data for minutes, blocks, class time, allowance and language. Derive counts and scores from the learner’s actions. The progress measure is the weekly study clock. A competency block tracks learning, while a monthly plan grants lessons and minutes. Put fees and purchasing controls in **Gói và học phí**. Learning screens can link to owned material. Keep streaks, rankings, coins and sales banners out of the study area.
5. Preserve the learning loop. Check-in collects mood, recap, preview and warm-up evidence. Check-out compares against that baseline. Reading requires evidence, writing asks the learner to revise, and Hỏi Zen offers increasingly specific hints. Route useful feedback to Vở AI. Use the learner’s language context in every view. Display an explicit sample-data empty state when a language has no lesson.
6. Test the affected flow from its user entry point and directly by bookmark. Check return navigation, mobile and desktop layouts, repeated actions, session state and an offline reload. The prototype ships as a single `index.html` with embedded assets. Simulate recording, grading, account changes and payments locally.

## Other Zenford surfaces

The customer reference covers the learner portal. For public discovery, use the existing home and shop layouts. For teacher, parent, CRM and recruitment, keep role-specific workflows and reuse `pageHeading`, `card`, `link`, `button`, `pill` and `table`. Read the matching section of the project guide for the academic agent roadmap, approval gates or CV rubric. Preserve the Phase 1 `ux-data` inventory and stable SCR links. [Project guide](../../../AGENT.md)
