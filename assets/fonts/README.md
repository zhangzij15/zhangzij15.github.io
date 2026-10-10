# Locally hosted fonts

The website serves these font files from its own `assets/fonts` directory. No visitor request to Google Fonts or another font CDN is needed.

Retrieved and checked on 2026-10-10. Both fonts are upright variable fonts distributed under the SIL Open Font License 1.1. Their complete upstream license notices are retained in this directory.

| File | Family | Weight axis | Subset | Size |
| --- | --- | --- | --- | --- |
| `eb-garamond-latin.woff2` | EB Garamond | 400–800 | Latin and common punctuation | 44,336 bytes |
| `source-sans-3-latin.woff2` | Source Sans 3 | 200–900 | Latin and common punctuation | 28,872 bytes |

## Sources

Google Fonts source repository revision: [`bd8f81ddb5c74d5c8897b36ad88b440266245103`](https://github.com/google/fonts/tree/bd8f81ddb5c74d5c8897b36ad88b440266245103).

The Google Fonts repository provides the upstream TTF, family metadata, and license. The deployed WOFF2 files are the official variable Latin subsets returned by the Google Fonts CSS service; they were copied without local font modification. They are not claimed to be byte-identical to a locally converted TTF.

[Official subset delivery manifest](https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400..800&family=Source+Sans+3:wght@200..900&display=swap)

### EB Garamond

- [Google Fonts source TTF](https://raw.githubusercontent.com/google/fonts/bd8f81ddb5c74d5c8897b36ad88b440266245103/ofl/ebgaramond/EBGaramond%5Bwght%5D.ttf)
- [Official WOFF2 file](https://fonts.gstatic.com/s/ebgaramond/v33/SlGUmQSNjdsmc35JDF1K5GR1SDk.woff2)
- Retained license: `ebgaramond-OFL.txt`
- Retained source metadata: `ebgaramond-METADATA.pb`
- WOFF2 SHA-256: `88603384163d301aebd5bd769832a8bfe3c9004ec24178417b9817f0ad32c63b`
- Source TTF SHA-256: `ef9512f92f6d579e5dc75af59a5a4b1b8b47d2eda89e00b954d44520e5369027`
- CSS Unicode range: `U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD`

### Source Sans 3

- [Google Fonts source TTF](https://raw.githubusercontent.com/google/fonts/bd8f81ddb5c74d5c8897b36ad88b440266245103/ofl/sourcesans3/SourceSans3%5Bwght%5D.ttf)
- [Official WOFF2 file](https://fonts.gstatic.com/s/sourcesans3/v20/nwpStKy2OAdR1K-IwhWudF-R3w8aZQ.woff2)
- Retained license: `sourcesans3-OFL.txt`
- Retained source metadata: `sourcesans3-METADATA.pb`
- WOFF2 SHA-256: `19143dca075972bc84e3fd9eab7416dd40cc565dccb2435a044bdfabe060c7d5`
- Source TTF SHA-256: `042fe2cc0b933e328410d7acbd0aa6a1873dca5aef81875f4bc214b08825c7b9`
- CSS Unicode range: `U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD`

The weight ranges were checked against the upstream TTF `fvar` table and the official delivery CSS. The WOFF2 signatures, header byte lengths, Brotli table stream, weight axes, and internal font identities were validated using Node.js built-ins. Further binary inspection is recorded in `font-manifest.json`.

Chinese, Greek, mathematical characters, and other characters outside the Latin subset use the website's fallback fonts.
