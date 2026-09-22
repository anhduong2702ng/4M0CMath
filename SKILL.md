---
name: cmath-learning-materials
description: Convert CMath PPTX presentations or scanned PDF worksheets into responsive, menu-linked HTML in this repository.
---

# CMath Learning Materials

Route by source format and load only the matching local skill:

- **PPTX:** read [`.agents/skills/pptx-to-html-v8/SKILL.md`](.agents/skills/pptx-to-html-v8/SKILL.md).
- **PDF or page images:** read [`.agents/skills/pdf_to_html_ocr_skill/SKILL.md`](.agents/skills/pdf_to_html_ocr_skill/SKILL.md).
- Use [`.agents/skills/pptx-to-html-qa/SKILL.md`](.agents/skills/pptx-to-html-qa/SKILL.md) only for PPTX visual-regression or conversion QA.

Do not introduce a planning framework for ordinary conversion or UI changes. Inspect the source, implement directly, run proportional QA, and give the user the review link.

## Repository invariants

- Generated lessons live at `outputdata/<DDMMYYYY>/`; their link back to the root menu is `../../index.html`.
- Every lesson page exposes a visible **Back to Main Menu** control. Keep it in the shared generator/template, not as a one-off edit.
- PDF worksheets use `scripts/generate_v2.py`, `styles/shared.css`, and a data-driven `scripts/content_<date>_<type>.py` module.
- Keep the root `index.html` synchronized with generated lessons. Each date group shows **Nội dung buổi học** outside the card grid and contains all available NDBH/BTVN cards.
- Preserve source wording and mathematical content. If the source contradicts itself, reproduce both statements and add a short source note; never silently invent a correction.
- Answers remain protected through the existing `mode-locked` flow. Printing and E-ink behavior must continue to work.
- Use fluid readable typography. Mobile must not shrink the root font below 17px; wide tables may scroll inside their own bounds without making the whole page overflow.

## Finish

Regenerate from source, verify menu/back links and page completeness, render at one desktop and one narrow viewport, run `git diff --check`, then provide clickable links to `index.html` and the new lesson.
