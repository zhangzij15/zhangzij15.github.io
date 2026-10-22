# Zijian Zhang — Academic Homepage

Personal academic website: [zhangzij15.github.io](https://zhangzij15.github.io/).

The main pages and compact publication list use the shared typography and responsive layout defined in `acad-homepage.css`:

- `index.html` — biography, education, research interests, and academic service
- `publications.html` — publications and patents
- `publication-list.html` — compact, continuously numbered publication and patent references
- `projects.html` — research projects
- `demos.html` — robotics and localization demonstrations
- `awards.html` — honors and certificates

The site consists of static files and requires no build step. For local preview, run `python -m http.server 8765 --bind 127.0.0.1` from this directory and open `http://127.0.0.1:8765/`.

The shared theme uses navy and ocean blue as its main colors, with teal, coral, and restrained champagne accents. Gradient title panels, category tabs, and figure frames add visual depth while bibliographic text remains on white backgrounds. EB Garamond is used for page headings and Source Sans 3 for body text. The variable fonts are hosted locally in `assets/fonts`; their licenses and source records are retained there. System fonts provide fallbacks for Chinese and other characters outside the Latin subsets.

Small decorative emoji accent selected headings, category tabs, and Citation buttons. They use system emoji fonts, are hidden from assistive technology and print, and are excluded from bibliographic text.

Maintain the current site by editing the HTML pages directly. The `.jemdoc` files and the original generator are retained as legacy content sources. Regenerating them with `jemdoc.py` will replace the current HTML layout, so do not run that generator for routine updates.

Publications and Projects include independent Citation buttons that expand an IEEE-style reference beneath each paper. The reference text is embedded in the HTML; `assets/js/citations.js` only handles opening and closing. After updating verified publication metadata, run `python scripts/build_citations.py` to refresh these generated controls in both pages. This optional maintenance helper preserves the surrounding layout and links. It uses sentence-case article titles, abbreviated periodicals and months, and IEEE's first-author-plus-et-al. convention for more than six authors. See [`docs/citation-controls.md`](docs/citation-controls.md) for the formatting and source notes.

The same helper generates `publication-list.html`, linked near the top of Publications. This reading view has no figures. It follows the detailed page's book/journal/conference/other-contribution/international-patent/Chinese-patent order with continuous reference numbers. Compact Paper/Code links (and Book/Slides where applicable), ESI labels, awards, and grants reuse the detailed entries' existing URLs and recognition text. Missing resources have no placeholder. Demonstrations remain explicitly identified as demonstrations. Patent citations use `data/patent-status.json`: verified grants cite the grant publication and issue date, while application publications cite their publication number and date. Chinese patents retain their official Chinese titles. Each national or international record is cited separately, including members of the same patent family.

In the compact list, Zijian Zhang's name is bold in every reference. All authors are retained so the name remains visible in long bylines. Corresponding-author stars follow the explicitly marked bylines on Publications; keep those source markers current when maintaining author roles. Namesake abbreviations are distinguished using the full structured author names. The expandable Citation text keeps its standard reference formatting.

Paper downloads, code archives, certificates, and media use their original paths. Journal-paper figures are stored in `assets/publications/`; `figure-manifest.json` records each source PDF, figure number, PDF page, crop coordinates, and high-resolution rendition. The original PDFs and PNG thumbnails are unchanged. On Publications, figure thumbnails open a native modal with the paper title, original source caption, and a separate lossless WebP image rendered directly from the PDF at approximately 3200 pixels on its longer edge. These larger images in `assets/publications/full/` load only when opened; regenerate them with `python scripts/build_publication_figures.py` (requires pypdfium2 and Pillow). PDF vector content renders at the higher resolution; embedded photographs and raster artwork retain their original detail limits. Close the modal with the × button, Escape, or a click outside the window; focus returns to the thumbnail. `assets/js/publication-figures.js` handles this interaction independently of Citation controls. Without JavaScript or native dialog support, the high-resolution image link opens in the same tab. Captions retain their links to the source PDF page.

The Projects page is organized into seven research areas, each with up to three selected journal papers and links to available code. The Publications page provides the complete list. `preview-templates/` contains the earlier design options. The shared layout is adapted from AcadHomepage by RayeRen.

Publication metadata and patent records were checked on October 10–11, 2026. Sources and unresolved details are recorded in [`docs/metadata-recheck-2026-10-11.md`](docs/metadata-recheck-2026-10-11.md), with structured records in `data/`. Follow-up display corrections are documented in [`docs/metadata-corrections-2026-10-17.md`](docs/metadata-corrections-2026-10-17.md). The `Granted` label identifies a documented grant event; it does not assert that a patent is currently in force. Update verified citations in both Publications and the selected Projects entries.

An [October 22, 2026 check of all 21 journal papers](docs/journal-publication-status-2026-10-22.md) confirmed their final volume/page assignments against publisher-deposited DOI records. J9 was updated from Early Access to vol. 75, no. 10, pp. 25198–25203, Oct. 2026; no other journal entry required a status conversion.

An October 18, 2026 public-source check of the 17 journal papers without an ESI Highly Cited Paper label found no independently confirmable additions. This is an inconclusive public-source result, not proof of non-selection in the latest ESI release. Coverage, the dated institutional evidence, and access limits are documented in [`docs/esi-audit-2026-10-18.md`](docs/esi-audit-2026-10-18.md).
