---
name: zenford-neo-pop
description: Apply the Zenford Neo-Pop Sticker visual system when building, changing, or reviewing Zenford HTML screens, components, mascot use, and Vietnamese UI copy.
---

# Zenford Neo-Pop

Start with the root project guide for the product, palette, brand voice and walkthrough fixtures. Edit the existing hash route in `index.html`. The `custom` map holds authored screens. `genericScreen` chooses a task view or populated record table. Use `userRoutes` for a dedicated route, `routeRecords` for its rows and `collections` for shared domain data. Keep related actions connected through in-session state. Leave the `ux-data` JSON as the verbatim Phase 1 inventory. [Project guide](../../../AGENT.md)

## Compose a screen

1. Identify the task, audience and action. For public discovery, use the homepage (`home`) as the example for yellow, ink, section-level pastels and large Zen. For focused learning, use `preLesson` or `labHint` for a white surface, small Zen and immediate feedback. For CRM, use `academicPipeline` and `cvReview` for a readable timeline or comparison table.
2. Compose with `pageHeading`, `card`, `link`, `button`, `pill`, `metric` and `table` where appropriate. Match the `zf-` component classes already embedded in the file. Preserve hash destinations, native field labels, focus handling and the mock’s in-memory state.
3. Select colors by purpose. Read the `neo-pop-tokens` style block for exact values. Keep cobalt in the logo, use one strong focal area of yellow, and use ink text on pastel. Use an ink action with a white shadow on the yellow hero. In a workspace reserve color for the action, small hints and meaningful states.
4. Write the label in the language the person using the screen would use. For instance, “Nghe lại câu mẫu” identifies what plays. For incorrect answers, pair “Chưa đúng” with a clue. Use the Vietnamese forms of address and commercial wording in the project guide.

## Component recipes

| Need | HTML contract |
| --- | --- |
| Action or navigation | Use `button(action, label, style)` or `link(id, label, style)`. `primary` is yellow, `dark` is ink and the default is white. The kit supplies the press/focus states. |
| Static or linked card | Use `card` for a panel. Use an anchor and `zf-card zf-card--hover` for a linked sticker. Reserve tilt for marketing illustrations. |
| Status or filter | Use `pill` / `zf-tag` for a read-only state. For a filter use a labeled `button.zf-pill` and update `aria-pressed` with the selection. For a binary setting use a native checkbox or `button.zf-switch[role=switch]` with an accessible name and synchronized `aria-checked`. |
| Answer or progress | Use `label.zf-answer` with a native radio. After checking, apply `is-ok` or `is-no` and expose the result as text. Use `zf-bar` with a child `i` for a fill. Supply the value and total in the accessible label or native progress semantics. |
| Language tile | Give the link `zf-lang` and `data-lang`, call `glyph(code)`, and print the full language name. Use the EN/ZH/JA/KO/VI mappings in the guide. CJK glyphs use the system font. |
| Marketing heading | Use `zf-overline` for a short uppercase label, `zf-kick` for a tilted introductory tag and `zf-hl` for a marker stroke. Keep each heading meaningful when read on its own. |
| Speaking Zen | Use `zf-say` containing a `zf-zen` and a `zf-bubble`. Use the `labHint` implementation for a small, contextual prompt. |
| Wordmark and illustration | Preserve the supplied SVG proportions. The normal and reverse wordmarks are embedded in header and footer. `data-zen` takes `state|hood color|outfit`. Use a pastel hex value for the shirt. The bundle mounts placeholders after each route render. |

For example, a listening hint uses this structure:

```html
<aside class="zf-say">
  <span class="zf-zen" data-zen="think|#BFE4FF|phones"></span>
  <p class="zf-bubble"><strong>Zen</strong><br>Nghe lần đầu để nắm ý chính.</p>
</aside>
```

Zen’s expressions are `normal`, `happy`, `wow`, `wink`, `think`, `love`, `sad` and `fierce`. Use `phones`, `mic`, `book` or `pencil` for the four Labs. Keep eye tracking and blinking optional for reduced-motion users. Use labeled Lucide symbols for functional icons.

## Verify a change

Open `index.html` directly from disk with network access disabled. Check the changed screen at phone and desktop widths, navigate away and back, and exercise its selected, error or success state with the keyboard. Check Vietnamese accents, explicitly named statuses, visible focus, logo contrast, and reduced motion. Confirm that fonts, Zen, and any relevant audio still work offline. Use `python tests/audit_sources.py` for catalog fidelity and `python tests/audit_mock.py` for route, viewport and fixture checks.

For exact variants, the supplied kit has a README per component, a rendered example, SVG originals, and the CSS/JS bundles. The runtime in this repository uses the standalone `zf-` classes and `ZenfordNP` renderer. [Component guides](<../../../Zenford Neo-pop 1/Zenford Neo-Pop/components/>) · [Asset guides](<../../../Zenford Neo-pop 1/Zenford Neo-Pop/assets/>) · [Token source](<../../../Zenford Neo-pop 1/Zenford Neo-Pop/tokens.css>)
