# Zijian Zhang — Academic Homepage

Personal academic website: [zhangzij15.github.io](https://zhangzij15.github.io/).

The five main pages use the shared typography and responsive layout defined in `acad-homepage.css`:

- `index.html` — biography, education, research interests, and academic service
- `publications.html` — publications and patents
- `projects.html` — research projects
- `demos.html` — robotics and localization demonstrations
- `awards.html` — honors and certificates

The site consists of static files and requires no build step. For local preview, run `python -m http.server 8765 --bind 127.0.0.1` from this directory and open `http://127.0.0.1:8765/`.

The shared theme uses navy and ocean blue as its main colors, with teal, coral, and restrained champagne accents. Gradient title panels, category tabs, and figure frames add visual depth while bibliographic text remains on white backgrounds. EB Garamond is used for page headings and Source Sans 3 for body text. The variable fonts are hosted locally in `assets/fonts`; their licenses and source records are retained there. System fonts provide fallbacks for Chinese and other characters outside the Latin subsets.

Maintain the current site by editing the HTML pages directly. The `.jemdoc` files and the original generator are retained as legacy content sources. Regenerating them with `jemdoc.py` will replace the current HTML layout, so do not run that generator for routine updates.

Paper downloads, code archives, certificates, and media use their original paths. Journal-paper figures are stored in `assets/publications/`; `figure-manifest.json` records each source PDF, figure number, PDF page, and crop coordinates. The original PDFs are unchanged. Figure thumbnails link to the full-size images, and their captions link to the source PDF page.

The Projects page is organized into seven research areas, each with up to three selected journal papers and links to available code. The Publications page provides the complete list. `preview-templates/` contains the earlier design options. The shared layout is adapted from AcadHomepage by RayeRen.

Publication metadata and patent records were checked on October 10, 2026. Sources, field changes, and unresolved details are recorded in [`docs/metadata-audit-2026-10-10.md`](docs/metadata-audit-2026-10-10.md), with structured records in `data/`. The `Granted` label identifies a documented grant event; it does not assert that a patent is currently in force. Update verified citations in both Publications and the selected Projects entries.
