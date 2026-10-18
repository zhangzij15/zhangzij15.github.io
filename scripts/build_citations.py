"""Refresh static Citation controls without rebuilding the site's layout.

Run from any directory with Python 3.8+. Bibliographic facts come from the
audited publication metadata; display-only IEEE abbreviations are defined here.
"""

import html
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STYLE_VERSION = '20261018-red-recognition'
MONTHS = ("", "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.", "Jul.",
          "Aug.", "Sep.", "Oct.", "Nov.", "Dec.")
JOURNALS = {
    "IEEE Transactions on Communications": "IEEE Trans. Commun.",
    "IEEE Transactions on Signal Processing": "IEEE Trans. Signal Process.",
    "IEEE Journal on Selected Areas in Communications": "IEEE J. Sel. Areas Commun.",
    "IEEE Transactions on Wireless Communications": "IEEE Trans. Wireless Commun.",
    "Tsinghua Science and Technology": "Tsinghua Sci. Technol.",
    "IEEE Communications Standards Magazine": "IEEE Commun. Standards Mag.",
    "IEEE Transactions on Vehicular Technology": "IEEE Trans. Veh. Technol.",
    "IEEE Communications Letters": "IEEE Commun. Lett.",
    "IEEE Wireless Communications Letters": "IEEE Wireless Commun. Lett.",
    "IEEE Transactions on Intelligent Transportation Systems": "IEEE Trans. Intell. Transp. Syst.",
    "IEEE Communications Magazine": "IEEE Commun. Mag.",
}
CONFERENCES = {
    "C1": "IEEE Global Commun. Conf. (GLOBECOM)",
    "C2": "IEEE Int. Conf. Commun. (ICC)",
    "C3": "IEEE 21st Int. Workshop Signal Process. Adv. Wireless Commun. (SPAWC)",
    "C4": "11th Int. Conf. Wireless Commun. Signal Process. (WCSP)",
    "C5": "IEEE Wireless Commun. Netw. Conf. (WCNC)",
    "C6": "IEEE Int. Conf. Commun. (ICC)",
    "C7": "IEEE Global Commun. Conf. (GLOBECOM)",
    "C8": "IEEE 93rd Veh. Technol. Conf. (VTC-Spring)",
    "C9": "IEEE Int. Conf. Commun. Workshops (ICC Workshops)",
    "C10": "IEEE Int. Symp. Inf. Theory (ISIT)",
    "C11": "IEEE 97th Veh. Technol. Conf. (VTC-Spring)",
    "C12": "IEEE Global Commun. Conf. (GLOBECOM)",
    "C13": "IEEE 95th Veh. Technol. Conf. (VTC-Spring)",
    "C14": "IEEE Int. Conf. Commun. (ICC)",
}
# Preserve acronyms and proper names when converting article titles to sentence case.
TITLE_TERMS = {
    "irs": "IRS", "ris": "RIS", "riss": "RISs", "mimo": "MIMO",
    "xl-mimo": "XL-MIMO", "fas": "FAS", "6g": "6G", "2d": "2D",
    "3d": "3D", "bayesian": "Bayesian", "rydberg": "Rydberg",
    "tinker@home": "Tinker@Home",
}
ACTION_ROW = re.compile(r'<div class="publication-actions">(?P<links>.*?)</div>', re.S)
BUTTON_BLOCK = re.compile(r'<!-- citation-button:[^>]+ -->.*?<!-- /citation-button -->', re.S)
PANEL_BLOCK = re.compile(r'<!-- citation-panel:[^>]+ -->.*?<!-- /citation-panel -->', re.S)
SCRIPT_TAG = '<script src="assets/js/citations.js?v=20261017" defer></script>'
SCRIPT_BLOCK = re.compile(r'<script\b[^>]*src="assets/js/citations\.js(?:\?[^\"]*)?"[^>]*>\s*</script>\n?', re.I)
RECOGNITION_ROW = re.compile(r'<p class="publication-recognition">(.*?)</p>', re.S)
RECOGNITION_ICONS = {
    'esi': '<path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2-5.6-3-5.6 3 1.1-6.2L3 9.6l6.2-.9Z"/>',
    'hot': '<path d="M13 3c1 4-2 5-2 8 0 1.4 1 2.4 2.2 2.6 1.3-1.2 1.9-2.6 1.8-4.2 3.2 2.7 4 4.7 4 6.6a7 7 0 0 1-14 0c0-4.4 4.4-6.4 8-13Z"/>',
    'award': '<path d="M8 3h8v6a4 4 0 0 1-8 0V3Z"/><path d="M8 5H4v3a4 4 0 0 0 4 4m8-7h4v3a4 4 0 0 1-4 4M12 13v5m-4 3h8m-6-3h4v3h-4Z"/>',
    'support': '<path d="m3 8 9-5 9 5-9 5-9-5Zm4 3v6c3 3 7 3 10 0v-6m4-3v8"/>',
}


def recognition_kind(label):
    if label.startswith('ESI '):
        return 'hot' if 'hot paper' in label.lower() else 'esi'
    return 'award' if 'award' in label.lower() else 'support'


def recognition_labels(content):
    # Badge icons contain SVG paths, with no text or nested span elements.
    return [html.unescape(re.sub(r'<[^>]+>', '', label)).strip()
            for label in re.findall(r'<span\b[^>]*>(.*?)</span>', content, re.S)]


def recognition_badge_html(label, compact=False):
    kind = recognition_kind(label)
    legacy_kind = 'esi' if kind == 'hot' else kind
    classes = ('reference-badge reference-badge--' + legacy_kind
               if compact else 'recognition-label')
    classes += ' recognition-badge recognition-badge--' + kind
    icon = ('<svg class="recognition-icon" viewBox="0 0 24 24" width="14" height="14" '
            'aria-hidden="true" focusable="false">' + RECOGNITION_ICONS[kind] + '</svg>')
    return f'<span class="{classes}">{icon}{html.escape(label)}</span>'


def refresh_recognition_row(match):
    labels = recognition_labels(match[1])
    if not labels or any(not label for label in labels):
        raise ValueError('Unrecognized publication-recognition markup')
    return '<p class="publication-recognition">' + ''.join(
        recognition_badge_html(label) for label in labels) + '</p>'


def sentence_title(title):
    words = re.split(r'(\s+)', title.lower())
    for i, word in enumerate(words):
        # Match punctuation separately so "RIS-aided" retains its acronym.
        words[i] = re.sub(r'[\w]+(?:[-@][\w]+)*',
                          lambda m: TITLE_TERMS.get(m[0], re.sub(
                              r'\bris\b', 'RIS', m[0])), word)
    result = ''.join(words)
    result = re.sub(r'(:\s+)([a-z])', lambda m: m[1] + m[2].upper(), result)
    return result[0].upper() + result[1:]


def marked_owner_name(name, corresponding=False):
    marker = '<sup title="Corresponding author">*</sup>' if corresponding else ''
    return '<strong>' + name + '</strong>' + marker


def emphasize_supplied_owner(authors):
    """Use only for audited bylines with exactly one Z. Zhang occurrence."""
    marked, count = re.subn(r'(?<![\w.])Z\.\s*Zhang(?![\w-])',
                            lambda m: marked_owner_name(m[0]), authors)
    if count != 1:
        raise ValueError('Ambiguous supplied author name: ' + authors)
    return marked


def author_name(author, record_id, personalize=False, corresponding=False):
    initials = []
    for part in author['given'].split():
        initials.append('-'.join(piece[0].upper() + '.' for piece in part.split('-') if piece))
    name = ' '.join(initials) + ' ' + author['family']
    # The bylines in the linked J6/C5 papers explicitly include the suffix.
    if record_id in ('J6', 'C5') and author['family'] == 'Heath':
        name += ', Jr.'
    name_html = html.escape(name)
    if (personalize and author['given'].strip().casefold() == 'zijian'
            and author['family'].strip().casefold() == 'zhang'):
        return marked_owner_name(name_html, corresponding)
    return name_html


def author_list(record, personalize=False, corresponding=False):
    names = [author_name(a, record['id'], personalize, corresponding) for a in record['authors']]
    # The personal reading list retains every author so the owner's name is visible.
    if len(names) > 6 and not personalize:
        return names[0] + ' <i>et al.</i>'
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return ' and '.join(names)
    return ', '.join(names[:-1]) + ', and ' + names[-1]


def date_text(record):
    return ((MONTHS[record['month']] + ' ') if record.get('month') else '') + str(record['year'])


def page_text(pages):
    # Some publisher records use zero-padded proceedings page ranges.
    return re.sub(r'\d+', lambda m: str(int(m[0])), pages).replace('-', '–')


def citation_html(record, personalize=False, corresponding=False):
    record_id = record['id']
    title = sentence_title(record['title'])
    if record_id in ('O1', 'O2'):
        # These are demonstrations, not verified paginated proceedings papers.
        authors = re.sub(r'\s+,', ',', record['authors_supplied'])
        venue = re.sub(r'^Demonstration at ', '', record['recommended_venue_html']).rstrip('.')
        authors_html = html.escape(authors)
        if personalize:
            authors_html = emphasize_supplied_owner(authors_html)
        return (authors_html + ', “' + html.escape(title)
                + ',” demonstration presented at ' + venue + '.')
    lead = author_list(record, personalize, corresponding) + ', “' + html.escape(title) + ',” '
    if record_id.startswith('J'):
        fields = ['<i>' + JOURNALS[record['venue']] + '</i>']
        if record['publication_status'] == 'early_access':
            # IEEE Xplore abstract/document/11535312/ reports 26 May 2026.
            # PP/99 and pp. 1–6 are provisional, so omit them from this citation.
            fields += ['early access', 'May 26, 2026'] if record_id == 'J9' else ['early access', date_text(record)]
        else:
            if record.get('volume'):
                fields.append('vol. ' + str(record['volume']))
            if record.get('issue'):
                fields.append('no. ' + str(record['issue']))
            if record.get('pages'):
                fields.append('pp. ' + page_text(record['pages']))
            elif record.get('article_number'):
                fields.append('Art. no. ' + str(record['article_number']))
            fields.append(date_text(record))
        body = ', '.join(fields)
    elif record_id.startswith('C'):
        location = re.search(r'</i>, (.*?), pp\.', record['recommended_venue_html'])
        if not location:
            raise ValueError('Missing verified conference location: ' + record_id)
        body = ('in <i>Proc. ' + CONFERENCES[record_id] + '</i>, '
                + html.escape(html.unescape(location[1])) + ', ' + date_text(record)
                + ', pp. ' + page_text(record['pages']))
    elif record_id == 'B1':
        body = ('in <i>' + html.escape(record['venue'])
                + '</i>. Wiley-IEEE Press, ' + date_text(record)
                + ', ch. 2, pp. ' + page_text(record['pages']))
    elif record_id == 'O3':
        return (lead + '<i>RoboCup@Home 2019, Open Platform League</i>, team description paper, '
                + '2019. [Online]. Available: '
                + 'https://tdp.robocup.org/tdp/2019-tdp-tinker-robocuphome-open-platform/')
    else:
        raise ValueError('Unsupported citable record: ' + record_id)
    return lead + body + ', doi: ' + html.escape(record['doi']) + '.'


def refresh_page(path, records):
    original = path.read_text(encoding='utf-8')
    source = PANEL_BLOCK.sub('', BUTTON_BLOCK.sub('', original))
    source = RECOGNITION_ROW.sub(refresh_recognition_row, source)
    by_doi = {r['doi'].lower(): r for r in records if r.get('doi')}
    counts = Counter()

    def replace_row(match):
        links = match['links']
        doi = re.search(r'href="https://doi.org/([^\"]+)"', links)
        record = by_doi.get(html.unescape(doi[1]).lower()) if doi else None
        if not record and 'href="pubs/Conference_paper/Tinker.pdf"' in links:
            record = next(r for r in records if r['id'] == 'O3')
        if not record:
            return match[0]
        record_id = record['id']
        counts[record_id] += 1
        panel_id = 'citation-' + path.stem + '-' + record_id.lower() + '-' + str(counts[record_id])
        title = html.escape(record['title'], quote=True)
        button = (f'<!-- citation-button:{record_id} -->'
                  f'<button type="button" class="citation-toggle" aria-expanded="false" '
                  f'aria-controls="{panel_id}" aria-label="Citation for {title}">'
                  '<span class="decorative-emoji" aria-hidden="true">📑</span>'
                  'Citation<span class="citation-chevron" aria-hidden="true"></span></button>'
                  '<!-- /citation-button -->')
        panel = (f'<!-- citation-panel:{record_id} -->'
                 f'<div class="citation-panel" id="{panel_id}" hidden>'
                 '<span class="citation-label">IEEE citation</span>'
                 f'<p class="citation-text">{citation_html(record)}</p></div>'
                 '<!-- /citation-panel -->')
        return '<div class="publication-actions">' + links + button + '</div>' + panel

    source = ACTION_ROW.sub(replace_row, source)
    if path.stem == 'publications':
        expected = {r['id'] for r in records if r.get('doi') or r['id'] == 'O3'}
        if set(counts) != expected or any(n != 1 for n in counts.values()):
            raise ValueError('Publications citation coverage mismatch: ' + str(counts))
    if path.stem == 'projects' and sum(counts.values()) != len(ACTION_ROW.findall(source)):
        raise ValueError('A selected project paper has no citation')
    source = re.sub(r'acad-homepage\.css\?v=[^\"]+', 'acad-homepage.css?v=' + STYLE_VERSION, source)
    source = SCRIPT_BLOCK.sub('', source)
    source = source.replace('</head>', SCRIPT_TAG + '\n</head>')
    if source != original:
        with path.open('w', encoding='utf-8', newline='\n') as output:
            output.write(source)
    print(f'{path.name}: {sum(counts.values())} citations')


def patent_citation_html(record, personalize=False):
    """Cite the specific grant or application publication, with its own date."""
    identifiers = record['verified_identifiers']
    number = identifiers.get('grant_publication_number')
    granted = bool(number)
    issued = record['date']['granted'] if granted else record['date']['published_application']
    number = number or identifiers['publication_number']
    if not issued:
        raise ValueError('Missing patent publication/issue date: ' + record['id'])
    published = date.fromisoformat(issued)
    patent_date = MONTHS[published.month] + f' {published.day}, {published.year}'
    if number.startswith('WO'):
        if granted:
            raise ValueError('A PCT publication cannot be an issued patent')
        kind = 'PCT Int. Patent Appl.'
    elif number.startswith('US'):
        kind = 'U.S. Patent' if granted else 'U.S. Patent Appl.'
    elif number.startswith('EP'):
        kind = 'European Patent' if granted else 'European Patent Appl.'
    elif number.startswith('CN'):
        kind = 'Chinese Patent' if granted else 'Chinese Patent Appl.'
    else:
        raise ValueError('Unknown patent jurisdiction: ' + number)
    title = record['official_title']
    chinese = record['id'].startswith('CN')
    language = '(in Chinese), ' if chinese else ''
    title_html = html.escape(title)
    if chinese:
        title_html = '<span lang="zh-CN">' + title_html + '</span>'
    inventors = html.escape(record['inventors'])
    if personalize:
        inventors = emphasize_supplied_owner(inventors)
    return (inventors + ', “' + title_html
            + ',” ' + language + kind + ' ' + html.escape(number)
            + ', ' + patent_date + '.')


def reference_resources_html(entry, title):
    """Reuse existing resource URLs and recognitions from the detailed entry."""
    actions = ACTION_ROW.search(entry)
    links = []
    if actions:
        for attributes, caption in re.findall(r'<a\b([^>]+)>(.*?)</a>', actions['links'], re.S):
            label = html.unescape(re.sub(r'<[^>]+>', '', caption)).strip()
            if label not in ('Paper', 'Code', 'Book', 'Slides'):
                continue
            source_attributes = dict(re.findall(r'([\w-]+)="([^\"]*)"', attributes))
            href = html.escape(html.unescape(source_attributes['href']), quote=True)
            extras = ''.join(' ' + key + '="' + html.escape(html.unescape(source_attributes[key]), quote=True) + '"'
                             for key in ('target', 'rel') if key in source_attributes)
            accessible_name = html.escape(label + ' for ' + title, quote=True)
            links.append(f'<a href="{href}"{extras} aria-label="{accessible_name}">{label}</a>')
    links_html = ' <span class="reference-links">' + ''.join(links) + '</span>' if links else ''
    recognition = RECOGNITION_ROW.search(entry)
    badges = []
    if recognition:
        for label in recognition_labels(recognition[1]):
            badges.append(recognition_badge_html(label, compact=True))
        if not badges:
            raise ValueError('Unrecognized publication-recognition markup: ' + title)
    badges_html = '<div class="reference-recognition">' + ''.join(badges) + '</div>' if badges else ''
    return links_html, badges_html


def refresh_publication_list(records, patents):
    """Build an image-free reading view with the same order as Publications."""
    source = (ROOT / 'publications.html').read_text(encoding='utf-8')
    # The detailed page's explicitly marked bylines are the source of author roles.
    corresponding_ids = set()
    entries = {}
    for entry in re.findall(r'<li class="publication-entry[^\"]*">.*?</li>', source, re.S):
        record_id = re.search(r'<span class="publication-number">([^<]+)</span>', entry)
        byline = re.search(r'<p class="publication-authors">(.*?)</p>', entry, re.S)
        if record_id:
            entries[record_id[1]] = entry
        if record_id and byline and re.search(
                r'<(?:b|strong)(?:\s[^>]*)?>Z\.\s*Zhang</(?:b|strong)>\s*(?:<sup\b[^>]*>\s*)?\*',
                byline[1]):
            corresponding_ids.add(record_id[1])
    header = re.search(r'<header class="site-masthead">.*?</header>', source, re.S)[0]
    header = header.replace('aria-current="page"', 'aria-current="location"')
    footer = re.search(r'<footer class="site-footer">.*?</footer>', source, re.S)[0]
    groups = [
        ('book-chapters', 'Book Chapters', [r for r in records if r['id'].startswith('B')]),
        ('journal-papers', 'Journal Papers', [r for r in records if r['id'].startswith('J')]),
        ('conference-papers', 'Conference Papers', [r for r in records if r['id'].startswith('C')]),
        ('other-publications', 'Demos &amp; Other Contributions', [r for r in records if r['id'].startswith('O')]),
        ('international-patents', 'International Patents', [r for r in patents if r['id'].startswith('IP')]),
        ('chinese-patents', 'Chinese Patents', [r for r in patents if r['id'].startswith('CN')]),
    ]
    sections = []
    expected_ids = []
    number = 0
    for anchor, label, group in groups:
        if not group:
            continue
        items = []
        start = number + 1
        for record in group:
            number += 1
            expected_ids.append(record['id'])
            reference = (patent_citation_html(record, personalize=True)
                         if record['id'].startswith(('IP', 'CN'))
                         else citation_html(record, personalize=True,
                                            corresponding=record['id'] in corresponding_ids))
            links, recognition = reference_resources_html(entries[record['id']], record['title'])
            items.append(f'<li id="reference-{record["id"].lower()}" data-publication-id="{record["id"]}">'
                         f'<span class="reference-number">[{number}]</span>'
                         f'<div class="reference-content"><p class="reference-text">{reference}</p>'
                         f'{links}{recognition}</div></li>')
        sections.append(f'<section class="reference-section" id="{anchor}" aria-labelledby="{anchor}-heading">\n'
                        f'<h2 id="{anchor}-heading">{label}</h2>\n'
                        f'<ol class="reference-list" start="{start}">\n'
                        + '\n'.join(items) + '\n</ol>\n</section>')
    # Catch an accidental mismatch with the detailed page instead of silently dropping papers.
    page_order = re.findall(r'<span class="publication-number">((?:B|J|C|O|IP|CN)\d+)</span>', source)
    if expected_ids != page_order:
        raise ValueError('Publication-list order differs from the detailed Publications page')
    body = '\n'.join(sections)
    output = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="The complete publication and patent list of Zijian Zhang, presented as IEEE-style references.">
<link rel="stylesheet" href="acad-homepage.css?v={STYLE_VERSION}">
<link rel="shortcut icon" type="image/x-icon" href="Tsinghua.ico">
<title>Publication List | Zijian Zhang</title>
</head>
<body class="publications-page publication-list-page">
<a class="skip-link" href="#main-content">Skip to main content</a>
{header}
<main class="site-main reference-main">
<article class="site-content" id="main-content" tabindex="-1"><div id="layout-content">
<p class="reference-back"><a href="publications.html">← Back to Publications</a></p>
<div id="toptitle"><h1>Publication List</h1><p class="reference-byline"><strong>Zijian Zhang · 张子健</strong></p></div>
<p class="page-intro">Book chapters, journal and conference papers, other contributions, and patents, in the same order as the Publications page.</p>
<p class="publication-note">* denotes the corresponding author.</p>
{body}
</div>{footer}</article>
</main>
</body>
</html>
'''
    path = ROOT / 'publication-list.html'
    if not path.exists() or path.read_text(encoding='utf-8') != output:
        with path.open('w', encoding='utf-8', newline='\n') as target:
            target.write(output)
    print(f'{path.name}: {number} references')


if __name__ == '__main__':
    metadata = json.loads((ROOT / 'data/publication-metadata.json').read_text(encoding='utf-8'))
    patent_metadata = json.loads((ROOT / 'data/patent-status.json').read_text(encoding='utf-8'))
    for page in ('publications.html', 'projects.html'):
        refresh_page(ROOT / page, metadata['records'])
    refresh_publication_list(metadata['records'], patent_metadata['records'])
