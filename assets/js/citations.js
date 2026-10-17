// Citation text is already in the page; toggling needs no network request.
document.addEventListener('click', function (event) {
  const button = event.target.closest('.citation-toggle');
  if (!button) return;

  const panel = document.getElementById(button.getAttribute('aria-controls'));
  if (!panel) return;

  const expanded = button.getAttribute('aria-expanded') === 'true';
  panel.hidden = expanded;
  button.setAttribute('aria-expanded', String(!expanded));
});
