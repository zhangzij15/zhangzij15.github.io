"""Render lossless, high-resolution modal figures from the original paper PDFs.

Requires pypdfium2 and Pillow. Existing PNG thumbnails and source PDFs are kept.
Run from any directory: python scripts/build_publication_figures.py
"""

import json
from pathlib import Path

import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "assets/publications/figure-manifest.json"
LONG_EDGE = 3200


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for paper in manifest["papers"]:
        source = ROOT / paper["pdf"]
        output = ROOT / "assets/publications/full" / (source.stem + ".webp")
        left, top, right, bottom = paper["crop"]
        scale = LONG_EDGE / max(right - left, bottom - top)
        with pdfium.PdfDocument(source) as pdf:
            page = pdf[paper["page"] - 1]
            width, height = page.get_size()
            if not (0 <= left < right <= width and 0 <= top < bottom <= height):
                raise ValueError("Figure crop outside PDF page: " + str(source))
            # PDFium crop is the amount removed from left/bottom/right/top.
            bitmap = page.render(
                scale=scale,
                crop=(left, height - bottom, width - right, top),
                draw_annots=False,
                rev_byteorder=True,
            )
            image = bitmap.to_pil()
            output.parent.mkdir(parents=True, exist_ok=True)
            image.save(output, format="WEBP", lossless=True, method=6)
            paper["full_size"] = {
                "image": output.relative_to(ROOT).as_posix(),
                "width": image.width,
                "height": image.height,
                "encoding": "lossless WebP rendered directly from the source PDF crop",
            }
            print("J{}: {}x{} ({:.0f} KB)".format(
                paper["journal_number"], image.width, image.height,
                output.stat().st_size / 1024,
            ))
            image.close()
            bitmap.close()
            page.close()
    MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
