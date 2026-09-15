/* ==========================================================================
   AQCA — Sidebar enhancements
   Builds the sidebar header (collapse button + live filter), swaps the text
   chevrons for SVG icons, and keeps the active item in view.
   Loaded after js/navigation.js.
   ========================================================================== */
(function () {
  var CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>';
  var CHEVRON_LEFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>';
  var SEARCH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"></circle><line x1="20" y1="20" x2="16.2" y2="16.2"></line></svg>';

  function norm(s) {
    return (s || '').replace(/\s+/g, ' ').trim().toLowerCase();
  }

  function isNarrow() {
    return typeof window.matchMedia === 'function' && window.matchMedia('(max-width: 768px)').matches;
  }

  document.addEventListener('DOMContentLoaded', function () {
    var sidebar = document.getElementById('sidebar');
    if (!sidebar) return;
    var nav = sidebar.querySelector('.nav-menu');
    if (!nav) return;

    /* --- 1. Header: collapse button + filter ------------------------------ */
    var header = document.createElement('div');
    header.className = 'sidebar-header';
    sidebar.insertBefore(header, sidebar.firstChild);

    var legacy = sidebar.querySelector('.sidebar-squeeze-toggle');
    if (legacy) legacy.parentNode.removeChild(legacy);

    header.innerHTML =
      '<div class="sidebar-brand">' +
        '<span class="sidebar-brand-label">Navigate</span>' +
        '<button type="button" class="sidebar-collapse" title="Collapse sidebar" aria-label="Collapse sidebar" aria-expanded="true">' + CHEVRON_LEFT + '</button>' +
      '</div>' +
      '<div class="sidebar-search">' + SEARCH +
        '<input type="search" class="sidebar-search-input" placeholder="Filter pages…" aria-label="Filter navigation" autocomplete="off" spellcheck="false">' +
      '</div>';

    var collapseBtn = header.querySelector('.sidebar-collapse');
    var input = header.querySelector('.sidebar-search-input');

    if (isNarrow()) {
      document.body.classList.remove('squeezed');
    }
    collapseBtn.setAttribute('aria-expanded', document.body.classList.contains('squeezed') ? 'false' : 'true');

    collapseBtn.addEventListener('click', function () {
      var squeezed = document.body.classList.toggle('squeezed');
      try { localStorage.setItem('sidebar-squeezed', squeezed ? 'true' : 'false'); } catch (e) {}
      collapseBtn.setAttribute('aria-expanded', squeezed ? 'false' : 'true');
      Array.prototype.forEach.call(document.querySelectorAll('.nav-subgroup.flyout'), function (f) {
        f.classList.remove('flyout');
      });
    });

    /* --- 2. SVG chevrons --------------------------------------------------- */
    Array.prototype.forEach.call(sidebar.querySelectorAll('.nav-group-icon, .nav-group-icon-nested'), function (el) {
      el.innerHTML = CHEVRON;
    });

    /* --- 3. Live filter ---------------------------------------------------- */
    var empty = document.createElement('div');
    empty.className = 'sidebar-empty';
    empty.textContent = 'No pages match your filter.';
    nav.parentNode.insertBefore(empty, nav.nextSibling);

    var footer = document.createElement('div');
    footer.className = 'sidebar-footer';
    footer.innerHTML = '<kbd>/</kbd><span>to filter pages</span>';
    empty.parentNode.insertBefore(footer, empty.nextSibling);

    var items = Array.prototype.filter.call(nav.children, function (el) {
      return el.classList.contains('nav-item');
    });

    function applyFilter(raw) {
      var q = norm(raw);
      var on = q.length > 0;
      sidebar.classList.toggle('is-filtering', on);
      var visible = 0;

      items.forEach(function (item) {
        var toggle = item.querySelector('.nav-group-toggle');
        var link = item.querySelector('.nav-link');
        var label = norm(toggle ? toggle.textContent : (link ? link.textContent : ''));
        var groupHit = on && !!toggle && label.indexOf(q) !== -1;
        var childHits = 0;

        Array.prototype.forEach.call(item.querySelectorAll('.nav-subgroup .nav-link'), function (l) {
          var li = l.parentNode;
          var hit = !on || groupHit || norm(l.textContent).indexOf(q) !== -1;
          li.style.display = hit ? '' : 'none';
          if (hit && on) childHits++;
        });

        Array.prototype.forEach.call(item.querySelectorAll('.nav-item-nested'), function (n) {
          var any = Array.prototype.some.call(n.querySelectorAll('.nav-link'), function (l) {
            return l.parentNode.style.display !== 'none';
          });
          n.style.display = (!on || any) ? '' : 'none';
        });

        Array.prototype.forEach.call(item.querySelectorAll('.nav-subgroup > li.nav-category-label'), function (li) {
          li.style.display = on ? 'none' : '';
        });

        var ownHit = on && !toggle && label.indexOf(q) !== -1;
        var show = !on || ownHit || childHits > 0;
        item.style.display = show ? '' : 'none';
        if (on) visible += childHits + (ownHit ? 1 : 0);
      });

      empty.classList.toggle('visible', on && visible === 0);
    }

    input.addEventListener('input', function () { applyFilter(input.value); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        input.value = '';
        applyFilter('');
        input.blur();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== '/' || e.metaKey || e.ctrlKey || e.altKey) return;
      var t = e.target;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
      if (window.getComputedStyle(input).display === 'none') return;
      e.preventDefault();
      input.focus();
      input.select();
    });

    /* --- 4. Keep the active item visible ------------------------------------ */
    setTimeout(function () {
      var active = sidebar.querySelector('.nav-link.active');
      if (!active) return;
      var r = active.getBoundingClientRect();
      var sr = sidebar.getBoundingClientRect();
      if (r.height === 0) return;
      if (r.top < sr.top + 70 || r.bottom > sr.bottom - 12) {
        sidebar.scrollTop += (r.top - sr.top) - (sidebar.clientHeight / 2) + (r.height / 2);
      }
    }, 120);
  });
})();
