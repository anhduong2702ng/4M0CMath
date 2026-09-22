---
name: pdf-to-html-ocr
description: Convert scanned or photographed worksheet PDFs into faithful, responsive CMath HTML using page-image inspection and the repository's data-driven generator.
---

# PDF Worksheet to Responsive HTML

Use this skill for scanned PDFs or page images. It is optimized for this repository's vertical worksheets, not fixed 16:9 slide decks.

## Source preparation

1. Identify the input PDF, date, lesson topic, and whether it is NDBH or BTVN.
2. Check whether PyMuPDF is available before installing anything.
3. Register reusable inputs in `scripts/extract_pdf.py`.
4. Render every page at 3× into:
   - `outputdata/<DDMMYYYY>/images_ndbh_<date>/`, or
   - `outputdata/<DDMMYYYY>/images_btvn_<date>/`.

Reuse `extract_pdf()`; do not create another extractor unless the source needs different processing.

## OCR and content modeling

Inspect every rendered page with the image viewer. For each page:

- Count the visible regions: header, exercise blocks, tables/diagrams, and footer.
- Transcribe printed wording exactly and in reading order. Do not summarize or paraphrase.
- Treat clear handwriting as answer data, not as printed question text.
- Verify mathematical answers independently when practical.
- If the printed source is internally inconsistent, preserve the conflicting wording and add a concise **Lưu ý từ bản gốc**. Do not silently rewrite it.
- Reconstruct meaningful tables and diagrams semantically. Embed a source image only when HTML/CSS would lose essential meaning.

Create one data-driven content module such as `scripts/content_12_btvn.py`. Reuse helpers from `scripts/generate_v2.py`:

- `hdr()` and `foot()` for one `.page-card` per source page.
- `A()` and `Ablk()` for protected answers.
- `gen_theory()`, `gen_debai()`, or `gen_btvn()` for the required access mode.

Do not duplicate the full HTML shell or shared CSS inside each content module.

## Responsive and navigation requirements

- Output to `outputdata/<DDMMYYYY>/<class>_<type>_<date>.html`.
- Inherit `styles/shared.css`; preserve font smoothing and the fluid 17–19px root scale.
- Grids collapse to one column on narrow screens.
- Wide tables scroll horizontally inside the table area.
- Controls have touch-friendly sizing.
- Every page includes the generator-provided `../../index.html` **Back to Main Menu** link.
- Print mode hides navigation and preserves readable worksheet layout.

Update `index.html` in the same change:

- Add the lesson card to the correct date group.
- Ensure that date group has a visible `session-topic` outside the card grid.
- Keep all card targets valid.

## QA

Before delivery:

1. Confirm extracted image count equals PDF page count.
2. Confirm generated `.page-card` count equals PDF page count.
3. Check a list of distinctive sentences from every page against the generated HTML.
4. Confirm answer and blank markup exists where expected.
5. Confirm all Main Menu card targets exist and the lesson's back link resolves.
6. Render the lesson and Main Menu at a desktop width and a narrow width (about 500px); inspect for clipping, page-wide overflow, and unreadable text.
7. Run `git diff --check`.
8. Remove temporary screenshots/profiles; keep the extracted OCR page images.

Return clickable links to the root Main Menu and the generated lesson.

## Conditional reference

Read `examples/manual_results.html` only when the source is genuinely slide-like and requires a fixed 16:9 container or complex chart reconstruction. Ordinary worksheets do not need this large example.
