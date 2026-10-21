// Enhance full-size figure links with a native, keyboard-accessible modal.
(() => {
  'use strict';

  const viewer = document.getElementById('publication-figure-viewer');
  if (!viewer || typeof viewer.showModal !== 'function') return;

  const image = viewer.querySelector('.figure-viewer__image');
  const title = viewer.querySelector('.figure-viewer__title');
  const caption = viewer.querySelector('.figure-viewer__caption');
  const status = viewer.querySelector('.figure-viewer__status');
  const closeButton = viewer.querySelector('.figure-viewer__close');
  let opener = null;
  let pressedOnBackdrop = false;

  document.querySelectorAll('.publication-image-link').forEach(link => {
    link.setAttribute('aria-haspopup', 'dialog');
    link.setAttribute('aria-controls', viewer.id);
  });

  document.addEventListener('click', event => {
    const link = event.target.closest('.publication-image-link');
    if (!link || event.defaultPrevented || event.button !== 0 ||
        event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;

    const thumbnail = link.querySelector('img');
    if (!thumbnail || viewer.open) return;
    event.preventDefault();

    opener = link;
    const paper = link.closest('.publication-entry');
    const paperTitle = paper && paper.querySelector('.publication-title');
    const sourceCaption = link.closest('figure').querySelector('figcaption');
    title.textContent = paperTitle ? paperTitle.textContent.trim() : 'Publication figure';
    caption.replaceChildren();
    if (sourceCaption) {
      sourceCaption.childNodes.forEach(node => caption.append(node.cloneNode(true)));
    }
    status.textContent = 'Loading figure…';
    status.hidden = false;
    image.hidden = true;
    image.alt = thumbnail.alt;
    image.src = link.href;
    document.documentElement.classList.add('figure-viewer-open');
    viewer.showModal();
  });

  image.addEventListener('load', () => {
    if (!viewer.open) return;
    status.hidden = true;
    image.hidden = false;
  });

  image.addEventListener('error', () => {
    if (!viewer.open) return;
    image.hidden = true;
    status.textContent = 'The figure could not be loaded. Please close this window and try again.';
    status.hidden = false;
  });

  closeButton.addEventListener('click', () => viewer.close());

  // Keep both Tab directions within the viewer rather than browser chrome.
  viewer.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const controls = viewer.querySelectorAll('button:not([disabled]), a[href]');
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

  // Native Escape cancellation also emits close, so every exit follows this path.
  viewer.addEventListener('close', () => {
    document.documentElement.classList.remove('figure-viewer-open');
    image.removeAttribute('src');
    image.alt = '';
    pressedOnBackdrop = false;
    if (opener && opener.isConnected) opener.focus({preventScroll: true});
    opener = null;
  });
})();
