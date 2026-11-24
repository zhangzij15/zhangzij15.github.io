// Citation text is already in the page; toggling and copying need no network request.
(() => {
  'use strict';

  function ensureCopyButton(panel) {
    const header = panel.querySelector('.citation-header');
    const textNode = panel.querySelector('.citation-text');
    if (!header || !textNode || header.querySelector('.citation-copy')) return;

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'citation-copy';
    button.textContent = 'Copy';
    button.setAttribute('aria-label', 'Copy IEEE citation');

    let resetTimer = null;
    button.addEventListener('click', () => {
      const citationText = textNode.textContent.trim();
      const markCopied = () => {
        button.textContent = 'Copied';
        button.dataset.copied = 'true';
        clearTimeout(resetTimer);
        resetTimer = setTimeout(() => {
          button.textContent = 'Copy';
          delete button.dataset.copied;
        }, 1800);
      };

      if (navigator.clipboard && typeof navigator.clipboard.writeText === 'function') {
        navigator.clipboard.writeText(citationText).then(markCopied, () => fallbackCopy(citationText, markCopied));
      } else {
        fallbackCopy(citationText, markCopied);
      }
    });

    header.appendChild(button);
  }

  function fallbackCopy(text, onSuccess) {
    const area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.position = 'fixed';
    area.style.opacity = '0';
    document.body.appendChild(area);
    area.select();
    try {
      if (document.execCommand('copy')) onSuccess();
    } finally {
      document.body.removeChild(area);
    }
  }

  document.addEventListener('click', event => {
    const button = event.target.closest('.citation-toggle');
    if (!button) return;

    const panel = document.getElementById(button.getAttribute('aria-controls'));
    if (!panel) return;

    const expanded = button.getAttribute('aria-expanded') === 'true';
    if (!expanded) ensureCopyButton(panel);
    panel.hidden = expanded;
    button.setAttribute('aria-expanded', String(!expanded));
  });
})();
