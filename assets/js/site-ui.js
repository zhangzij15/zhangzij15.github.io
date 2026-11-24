// Progressive UI enhancements: theme toggle, back-to-top, publication search/filter, and unified lightbox.
(() => {
  'use strict';

  const THEME_KEY = 'zhangzij15-theme';
  const MOON_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8Z"/></svg>';
  const SUN_ICON = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 2v2.2M12 19.8V22M4.9 4.9l1.6 1.6M17.5 17.5l1.6 1.6M2 12h2.2M19.8 12H22M4.9 19.1l1.6-1.6M17.5 6.5l1.6-1.6"/></svg>';
  const UP_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M12 19V5M6 11l6-6 6 6"/></svg>';
  const SEARCH_ICON = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';

  function getSavedTheme() {
    try {
      const value = localStorage.getItem(THEME_KEY);
      return value === 'dark' || value === 'light' ? value : null;
    } catch (_) {
      return null;
    }
  }

  function saveTheme(theme) {
    try {
      localStorage.setItem(THEME_KEY, theme);
    } catch (_) {}
  }

  function applyTheme(theme) {
    const isDark = theme === 'dark';
    document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
    let meta = document.querySelector('meta[name="theme-color"]');
    if (!meta) {
      meta = document.createElement('meta');
      meta.name = 'theme-color';
      document.head.appendChild(meta);
    }
    meta.content = isDark ? '#0b1524' : '#0e2238';
  }

  function initThemeToggle() {
    const inner = document.querySelector('.site-masthead__inner');
    if (!inner || inner.querySelector('.theme-toggle')) return;

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'theme-toggle';

    const syncButton = () => {
      const isDark = document.documentElement.dataset.theme === 'dark';
      button.innerHTML = isDark ? SUN_ICON : MOON_ICON;
      button.setAttribute('aria-pressed', String(isDark));
      button.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
      button.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
    };

    syncButton();
    button.addEventListener('click', () => {
      const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      saveTheme(next);
      syncButton();
    });

    if (window.matchMedia) {
      const media = window.matchMedia('(prefers-color-scheme: dark)');
      const onSystemChange = event => {
        if (!getSavedTheme()) {
          applyTheme(event.matches ? 'dark' : 'light');
          syncButton();
        }
      };
      if (typeof media.addEventListener === 'function') {
        media.addEventListener('change', onSystemChange);
      }
    }

    inner.appendChild(button);
  }

  function initBackToTop() {
    if (document.querySelector('.floating-top')) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'floating-top';
    button.setAttribute('aria-label', 'Back to top');
    button.title = 'Back to top';
    button.innerHTML = UP_ICON;
    button.hidden = true;

    const update = () => {
      const show = window.scrollY > 420;
      if (button.hidden === show) {
        button.hidden = !show;
      }
    };

    button.addEventListener('click', () => {
      const reduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, behavior: reduced ? 'auto' : 'smooth' });
    });

    window.addEventListener('scroll', update, { passive: true });
    document.body.appendChild(button);
    update();
  }

  function initPublicationFilter() {
    if (!document.body.classList.contains('publications-page') ||
        document.body.classList.contains('publication-list-page')) return;

    const nav = document.querySelector('#layout-content > .section-nav');
    const sections = Array.from(document.querySelectorAll('.publication-section'));
    if (!nav || !sections.length) return;

    const items = [];
    sections.forEach(section => {
      section.querySelectorAll('.publication-entry').forEach(entry => {
        const authorsEl = entry.querySelector('.publication-authors');
        const authorsText = authorsEl ? authorsEl.textContent.trim() : '';
        items.push({
          section,
          entry,
          searchable: entry.textContent.toLowerCase().replace(/\s+/g, ' '),
          firstAuthor: /^Z\.\s*Zhang\b/.test(authorsText),
          withCode: Boolean(entry.querySelector('.publication-actions a[href^="codes/"]')),
          honors: Boolean(entry.querySelector('.publication-recognition')),
        });
      });
    });
    if (!items.length) return;

    const toolbar = document.createElement('div');
    toolbar.className = 'pub-toolbar';
    toolbar.setAttribute('role', 'region');
    toolbar.setAttribute('aria-label', 'Filter publications');
    toolbar.innerHTML =
      '<div class="pub-search">' +
        '<span class="pub-search__icon">' + SEARCH_ICON + '</span>' +
        '<input type="search" class="pub-search__input" placeholder="Search title, author, venue, or patent…" aria-label="Search publications and patents">' +
        '<button type="button" class="pub-search__clear" aria-label="Clear search" hidden>×</button>' +
      '</div>' +
      '<div class="pub-filters" role="group" aria-label="Quick filters">' +
        '<button type="button" class="pub-filter is-active" data-filter="all" aria-pressed="true">All</button>' +
        '<button type="button" class="pub-filter" data-filter="first" aria-pressed="false">First Author</button>' +
        '<button type="button" class="pub-filter" data-filter="code" aria-pressed="false">With Code</button>' +
        '<button type="button" class="pub-filter" data-filter="honors" aria-pressed="false">Honors / ESI</button>' +
      '</div>' +
      '<p class="pub-toolbar__count" role="status" aria-live="polite"></p>';

    const emptyNotice = document.createElement('div');
    emptyNotice.className = 'pub-empty';
    emptyNotice.hidden = true;
    emptyNotice.innerHTML =
      '<p>No publications or patents match the current filter.</p>' +
      '<button type="button" class="pub-empty__reset">Reset filters</button>';

    nav.insertAdjacentElement('afterend', toolbar);
    sections[sections.length - 1].insertAdjacentElement('afterend', emptyNotice);

    const input = toolbar.querySelector('.pub-search__input');
    const clearBtn = toolbar.querySelector('.pub-search__clear');
    const filterButtons = Array.from(toolbar.querySelectorAll('.pub-filter'));
    const countEl = toolbar.querySelector('.pub-toolbar__count');
    const resetBtn = emptyNotice.querySelector('.pub-empty__reset');
    let activeFilter = 'all';

    const applyFilter = () => {
      const query = input.value.trim().toLowerCase();
      const tokens = query ? query.split(/\s+/) : [];
      clearBtn.hidden = !query;

      let visibleTotal = 0;
      const sectionCounts = new Map(sections.map(s => [s, 0]));

      items.forEach(item => {
        let ok = true;
        if (activeFilter === 'first') ok = item.firstAuthor;
        else if (activeFilter === 'code') ok = item.withCode;
        else if (activeFilter === 'honors') ok = item.honors;

        if (ok && tokens.length) {
          ok = tokens.every(tok => item.searchable.includes(tok));
        }

        item.entry.hidden = !ok;
        if (ok) {
          visibleTotal += 1;
          sectionCounts.set(item.section, sectionCounts.get(item.section) + 1);
        }
      });

      sections.forEach(section => {
        section.hidden = sectionCounts.get(section) === 0;
      });

      const isFiltered = activeFilter !== 'all' || tokens.length > 0;
      countEl.textContent = isFiltered
        ? `Showing ${visibleTotal} of ${items.length} entries`
        : `${items.length} entries`;
      emptyNotice.hidden = visibleTotal > 0;
    };

    const resetAll = () => {
      input.value = '';
      activeFilter = 'all';
      filterButtons.forEach(btn => {
        const active = btn.dataset.filter === 'all';
        btn.classList.toggle('is-active', active);
        btn.setAttribute('aria-pressed', String(active));
      });
      applyFilter();
    };

    input.addEventListener('input', applyFilter);
    clearBtn.addEventListener('click', () => {
      input.value = '';
      applyFilter();
      input.focus();
    });
    resetBtn.addEventListener('click', () => {
      resetAll();
      input.focus();
    });

    filterButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        activeFilter = btn.dataset.filter;
        filterButtons.forEach(other => {
          const active = other === btn;
          other.classList.toggle('is-active', active);
          other.setAttribute('aria-pressed', String(active));
        });
        applyFilter();
      });
    });

    // If a user clicks a category anchor that is currently hidden by filters, clear filters first.
    nav.addEventListener('click', event => {
      const link = event.target.closest('a[href^="#"]');
      if (!link) return;
      const target = document.getElementById(link.getAttribute('href').slice(1));
      if (target && target.hidden) {
        resetAll();
      }
    });

    applyFilter();
  }

  function ensureViewerDialog() {
    let viewer = document.getElementById('publication-figure-viewer');
    if (viewer) return viewer;
    viewer = document.createElement('dialog');
    viewer.className = 'figure-viewer';
    viewer.id = 'publication-figure-viewer';
    viewer.setAttribute('aria-labelledby', 'figure-viewer-title');
    viewer.setAttribute('aria-describedby', 'figure-viewer-caption');
    viewer.innerHTML =
      '<div class="figure-viewer__panel">' +
        '<div class="figure-viewer__header">' +
          '<h2 class="figure-viewer__title" id="figure-viewer-title">Preview</h2>' +
          '<button class="figure-viewer__close" type="button" aria-label="Close image preview" autofocus><span aria-hidden="true">×</span></button>' +
        '</div>' +
        '<div class="figure-viewer__stage">' +
          '<img class="figure-viewer__image" alt="" hidden>' +
          '<p class="figure-viewer__status" role="status" hidden></p>' +
        '</div>' +
        '<div class="figure-viewer__caption" id="figure-viewer-caption"></div>' +
      '</div>';
    document.body.appendChild(viewer);
    return viewer;
  }

  function initUnifiedLightbox() {
    // Publications page already initializes its dedicated publication-figures.js controller.
    const isAwards = document.body.classList.contains('awards-page');
    const isProjects = document.body.classList.contains('projects-page');
    if (!isAwards && !isProjects) return;

    const viewer = ensureViewerDialog();
    if (!viewer || typeof viewer.showModal !== 'function') return;

    const image = viewer.querySelector('.figure-viewer__image');
    const title = viewer.querySelector('.figure-viewer__title');
    const caption = viewer.querySelector('.figure-viewer__caption');
    const status = viewer.querySelector('.figure-viewer__status');
    const closeButton = viewer.querySelector('.figure-viewer__close');
    let opener = null;
    let fallbackSrc = null;
    let pressedOnBackdrop = false;

    const IMAGE_LINK_RE = /\.(png|jpe?g|webp|gif)(?:$|\?)/i;

    if (isAwards) {
      document.querySelectorAll('.award-resources a').forEach(link => {
        if (IMAGE_LINK_RE.test(link.getAttribute('href') || '')) {
          link.classList.add('lightbox-trigger');
          link.setAttribute('aria-haspopup', 'dialog');
          link.setAttribute('aria-controls', viewer.id);
        }
      });
    }

    if (isProjects) {
      document.querySelectorAll('.project-figure > a').forEach(link => {
        link.classList.add('lightbox-trigger');
        link.setAttribute('aria-haspopup', 'dialog');
        link.setAttribute('aria-controls', viewer.id);
      });
    }

    const openViewer = (trigger, headingText, primarySrc, altText, captionNodes, fallback) => {
      if (viewer.open) return;
      opener = trigger;
      fallbackSrc = fallback || null;
      title.textContent = headingText;
      caption.replaceChildren(...captionNodes);
      status.textContent = 'Loading image…';
      status.hidden = false;
      image.hidden = true;
      image.alt = altText;
      image.src = primarySrc;
      document.documentElement.classList.add('figure-viewer-open');
      viewer.showModal();
    };

    document.addEventListener('click', event => {
      const link = event.target.closest('a.lightbox-trigger');
      if (!link || event.defaultPrevented || event.button !== 0 ||
          event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;

      if (isAwards) {
        event.preventDefault();
        const item = link.closest('li');
        const year = item && item.querySelector('.award-year');
        const desc = item && item.querySelector('.award-content > p');
        const label = desc ? desc.textContent.trim().replace(/\.$/, '') : 'Award Certificate';
        const heading = year ? `${year.textContent.trim()} · ${label}` : label;
        const openLink = document.createElement('a');
        openLink.href = link.href;
        openLink.target = '_blank';
        openLink.rel = 'noopener';
        openLink.textContent = 'Open original image';
        openViewer(link, heading, link.href, `${label} certificate`, [openLink]);
        return;
      }

      if (isProjects) {
        const thumb = link.querySelector('img');
        if (!thumb) return;
        event.preventDefault();
        const entry = link.closest('.project-entry');
        const headingEl = entry && entry.querySelector('.project-title');
        const heading = headingEl ? headingEl.textContent.trim() : 'Research Figure';
        const rawSrc = thumb.getAttribute('src') || '';
        const pubMatch = rawSrc.match(/^assets\/publications\/([^/]+)\.png$/);
        const hiResSrc = pubMatch ? `assets/publications/full/${pubMatch[1]}.webp` : thumb.src;

        const nodes = [];
        if (thumb.alt) {
          nodes.push(document.createTextNode(thumb.alt + ' · '));
        }
        const pdfLink = document.createElement('a');
        pdfLink.href = link.href;
        pdfLink.target = '_blank';
        pdfLink.rel = 'noopener';
        pdfLink.textContent = 'Read source paper (PDF)';
        nodes.push(pdfLink);

        openViewer(link, heading, hiResSrc, thumb.alt || heading, nodes, pubMatch ? thumb.src : null);
      }
    });

    image.addEventListener('load', () => {
      if (!viewer.open) return;
      status.hidden = true;
      image.hidden = false;
    });

    image.addEventListener('error', () => {
      if (!viewer.open) return;
      if (fallbackSrc) {
        const next = fallbackSrc;
        fallbackSrc = null;
        image.src = next;
        return;
      }
      image.hidden = true;
      status.textContent = 'The image could not be loaded. Please close this window and try again.';
      status.hidden = false;
    });

    closeButton.addEventListener('click', () => viewer.close());

    viewer.addEventListener('keydown', event => {
      if (event.key !== 'Tab') return;
      const controls = viewer.querySelectorAll('button:not([disabled]), a[href]');
      if (!controls.length) return;
      const first = controls[0];
      const last = controls[controls.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });

    const isOutside = event => {
      const bounds = viewer.getBoundingClientRect();
      return event.clientX < bounds.left || event.clientX > bounds.right ||
             event.clientY < bounds.top || event.clientY > bounds.bottom;
    };
    viewer.addEventListener('pointerdown', event => {
      pressedOnBackdrop = isOutside(event);
    });
    viewer.addEventListener('click', event => {
      if (pressedOnBackdrop && isOutside(event)) viewer.close();
      pressedOnBackdrop = false;
    });

    viewer.addEventListener('close', () => {
      document.documentElement.classList.remove('figure-viewer-open');
      image.removeAttribute('src');
      image.alt = '';
      fallbackSrc = null;
      pressedOnBackdrop = false;
      if (opener && opener.isConnected) opener.focus({ preventScroll: true });
      opener = null;
    });
  }

  initThemeToggle();
  initBackToTop();
  initPublicationFilter();
  initUnifiedLightbox();
})();
