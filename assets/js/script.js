// Developer Xperience - page behaviors
// 1. Banner "more options" dropdown menus (with module search)
// 2. Current-page highlighting in nav menus
// 3. Demo contact form (no backend)

/* 1. Dropdown menus -------------------------------------- */

// Offset-based visibility: elements hidden via [hidden], display: none on an
// ancestor (.search-hidden groups), or a closed dropdown report null.
function isVisible(el) {
  return el.offsetParent !== null;
}

// Close a single dropdown, reset its button state, and clear its search filter
function closeDropdown(dropdown) {
  dropdown.classList.remove('open');
  const button = dropdown.querySelector('.dropdown-toggle');
  if (button) {
    button.setAttribute('aria-expanded', 'false');
  }
  resetMenuSearch(dropdown);
}

// Clear the dropdown's module search filter, if it has one and it is active
function resetMenuSearch(dropdown) {
  const input = dropdown.querySelector('.menu-search-input');
  if (!input || input.value === '') return;
  input.value = '';
  filterModuleNav(dropdown, '');
}

// Filter the module nav inside a dropdown. A group stays visible when its
// module title matches; otherwise only matching section links are shown.
function filterModuleNav(dropdown, query) {
  const nav = dropdown.querySelector('.module-navigation');
  if (!nav) return;

  const term = query.trim().toLowerCase();
  const filtering = term.length > 0;

  let moduleCount = 0;
  let sectionCount = 0;

  nav.querySelectorAll('.module-group').forEach((group) => {
    const moduleLink = group.querySelector(':scope > a');
    const sectionLinks = group.querySelectorAll('.submodule-aside a');
    const moduleMatch =
      filtering &&
      moduleLink &&
      moduleLink.textContent.toLowerCase().includes(term);

    let sectionsShown = 0;
    sectionLinks.forEach((link) => {
      // A module-title match reveals all of its sections; otherwise only
      // sections whose own text matches stay visible.
      const hit = filtering && (moduleMatch || link.textContent.toLowerCase().includes(term));
      link.hidden = filtering && !hit;
      if (hit) {
        sectionCount += 1;
        sectionsShown += 1;
      }
    });

    const showGroup = !filtering || Boolean(moduleMatch) || sectionsShown > 0;
    group.classList.toggle('search-hidden', !showGroup);
    if (showGroup) moduleCount += 1;
  });

  // Announce result counts to assistive tech via the role="status" line
  const status = dropdown.querySelector('.menu-search-status');
  if (status) {
    if (!filtering) {
      status.textContent = '';
    } else if (moduleCount === 0) {
      status.textContent = 'No matches - press Escape to clear.';
    } else {
      const modules = `${moduleCount} module${moduleCount === 1 ? '' : 's'}`;
      const sections = sectionCount
        ? `, ${sectionCount} section${sectionCount === 1 ? '' : 's'}`
        : '';
      status.textContent = `Matches: ${modules}${sections}`;
    }
  }
}

// Live-filter the module list while the user types
function watchMenuSearch(dropdown) {
  const input = dropdown.querySelector('.menu-search-input');
  if (!input) return;
  input.addEventListener('input', () => {
    filterModuleNav(dropdown, input.value);
  });
}

// Toggle a dropdown when its button is clicked
document.querySelectorAll('.dropdown-toggle').forEach((button) => {
  button.addEventListener('click', (event) => {
    event.stopPropagation();
    const dropdown = button.closest('.dropdown');
    const isOpen = dropdown.classList.toggle('open');
    button.setAttribute('aria-expanded', String(isOpen));
    // Open the menu with focus on the search box, when there is one
    if (isOpen) {
      const input = dropdown.querySelector('.menu-search-input');
      if (input) input.focus();
    }
  });
});

// Arrow keys cycle through the visible links of an open dropdown
document.querySelectorAll('.dropdown').forEach((dropdown) => {
  watchMenuSearch(dropdown);

  dropdown.addEventListener('keydown', (event) => {
    if (!dropdown.classList.contains('open')) return;
    if (event.key !== 'ArrowDown' && event.key !== 'ArrowUp') return;

    // Only cycle through links that survive the active search filter
    const links = Array.from(dropdown.querySelectorAll('a')).filter(isVisible);
    if (links.length === 0) return;

    event.preventDefault();
    const current = links.indexOf(document.activeElement);
    const step = event.key === 'ArrowDown' ? 1 : -1;
    // Nothing focused yet: ArrowDown lands on the first link, ArrowUp on the last
    const next =
      current === -1
        ? step === 1
          ? 0
          : links.length - 1
        : (current + step + links.length) % links.length;
    links[next].focus();
  });

  // Close when keyboard focus leaves the dropdown entirely
  dropdown.addEventListener('focusout', (event) => {
    if (!dropdown.contains(event.relatedTarget)) closeDropdown(dropdown);
  });
});

// Close the dropdown when a menu link is chosen
document.querySelectorAll('.dropdown-menu a').forEach((link) => {
  link.addEventListener('click', () => closeDropdown(link.closest('.dropdown')));
});

// Close any open dropdown when clicking elsewhere
document.addEventListener('click', (event) => {
  if (!event.target.closest('.dropdown')) closeAllOpen();
});

// Close every open dropdown
function closeAllOpen() {
  document.querySelectorAll('.dropdown.open').forEach(closeDropdown);
}

// Escape: first press clears an active search, second press closes the menu
document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;

  const activeInput = Array.from(
    document.querySelectorAll('.dropdown.open .menu-search-input')
  ).find((input) => input.value !== '');
  if (activeInput) {
    activeInput.value = '';
    filterModuleNav(activeInput.closest('.dropdown'), '');
    activeInput.focus();
    return;
  }

  const open = document.querySelectorAll('.dropdown.open');
  if (open.length === 0) return;
  const toggle = open[0].querySelector('.dropdown-toggle');
  closeAllOpen();
  if (toggle) toggle.focus();
});

/* 2. Current-page highlighting --------------------------- */

// Static pages can't server-render aria-current, so mark matching links here.
const currentPage = location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('nav a[href], footer nav a[href]').forEach((link) => {
  const href = link.getAttribute('href');
  if (!href.includes('#') && href.split('#')[0] === currentPage) {
    link.setAttribute('aria-current', 'page');
  }
});

/* 3. Demo contact form ------------------------------------ */

const contactForm = document.getElementById('contact-form');
if (contactForm) {
  const status = contactForm.querySelector('.form-status');

  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    // Let the browser's native validation UI handle invalid fields
    if (!contactForm.checkValidity()) return;

    if (status) {
      status.textContent =
        'Thanks for your message! (Demo form - no backend, so nothing was actually sent.)';
      status.hidden = false;
    }
    contactForm.reset();
  });
}
