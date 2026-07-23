document.addEventListener('DOMContentLoaded', function () {
  const toc = document.getElementById('TOC');
  if (!toc) return;

  const btn = document.createElement('button');
  btn.id = 'toc-toggle-btn';
  btn.setAttribute('aria-label', 'Recolher sumário');
  btn.innerHTML = '&#8249;';
  toc.appendChild(btn);

  const stored = localStorage.getItem('toc-collapsed');
  if (stored === 'true') {
    toc.classList.add('toc-collapsed');
    btn.innerHTML = '&#8250;';
    btn.setAttribute('aria-label', 'Expandir sumário');
  }

  btn.addEventListener('click', function () {
    const collapsed = toc.classList.toggle('toc-collapsed');
    btn.innerHTML = collapsed ? '&#8250;' : '&#8249;';
    btn.setAttribute('aria-label', collapsed ? 'Expandir sumário' : 'Recolher sumário');
    localStorage.setItem('toc-collapsed', collapsed);
  });
});
