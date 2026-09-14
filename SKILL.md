---
name: pptx-to-html-v8
description: Convert a Microsoft PowerPoint presentation (.pptx) to a native HTML/CSS interactive web presentation.
---

# PPTX to HTML Converter (V8 Table Engine)

**The canonical version of this skill lives in
[.agents/skills/pptx-to-html-v8/SKILL.md](.agents/skills/pptx-to-html-v8/SKILL.md) — read that one.**
It carries the full conversion rules (Rule 1-17), the QA workflow and the known limitations;
this file used to hold an older copy of the instructions that had silently fallen out of date.

## Layout of this repository

| Path | Role |
|---|---|
| `.agents/skills/pptx-to-html-v8/` | The skill itself: instructions, converter, QA. **Source of truth.** |
| `scripts/`, `qa/` | Working copy of the converter used from the repository root. Must stay byte-identical to the skill's copy — change one, copy to the other. |
| `inputdata/<bài>/` | Source .pptx decks. |
| `outputdata/<bai_N>/` | Generated presentations, two levels below the root so the page's `../../index.html` menu link resolves. |
| `index.html` | Menu listing every converted lesson. Add a card for each new deck. |

## Quick start

```bash
cd scripts
python pptx2html.py -i <absolute-path-to-input.pptx> -o <repo>/outputdata/bai_N

cd ..
python qa/check_underlines.py outputdata/bai_N/presentation.html --pptx <absolute-path-to-input.pptx>
```

If a run fails midway PowerPoint can stay open as a ghost process — clear it with
`taskkill /F /IM POWERPNT.EXE` before retrying.
