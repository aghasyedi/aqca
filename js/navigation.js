/* js/navigation.js */
document.addEventListener('DOMContentLoaded', () => {
    
    // Icon mappings for sidebar items
    const icons = {
        'About AQCA': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>',
        'Preface': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>',
        'Quantum Computing Basics': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20"></path><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
        'Algorithms': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
        'Visualise': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>',
        'Analysis Centre': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>',
        'Resources': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>',
        'References': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
        'Appendix': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>',
        'Developer': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>'
    };

    const sidebar = document.getElementById('sidebar');
    
    // Inject Icons & Tooltips
    if (sidebar) {
        const topLevelItems = sidebar.querySelectorAll('.nav-item > .nav-link, .nav-item > .nav-group-toggle');
        topLevelItems.forEach(item => {
            const text = item.textContent.trim();
            let label = "";
            if (item.classList.contains('nav-group-toggle')) {
                // Algorithms toggle
                label = item.querySelector('span:first-child').textContent.trim();
                item.title = label;
                if (icons[label]) {
                    item.insertAdjacentHTML('afterbegin', icons[label]);
                }
            } else {
                // Regular links
                // Ignore Home since it has .step-num
                if (text === "✦Home" || text === "Home") {
                    item.title = "Home";
                    return;
                }
                label = text;
                item.title = label;
                if (icons[label]) {
                    // Wrap text in a span so we can hide it in CSS
                    item.innerHTML = `${icons[label]} <span>${label}</span>`;
                }
            }
        });

        // Add Squeeze toggle button at the top of the sidebar
        const squeezeBtn = document.createElement('button');
        squeezeBtn.className = 'sidebar-squeeze-toggle';
        squeezeBtn.innerHTML = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>';
        squeezeBtn.title = "Toggle Sidebar";
        sidebar.insertBefore(squeezeBtn, sidebar.firstChild);

        // Load squeezed state
        if (localStorage.getItem('sidebar-squeezed') === 'true') {
            document.body.classList.add('squeezed');
        }

        // Squeeze Toggle Logic
        squeezeBtn.addEventListener('click', () => {
            const isSqueezed = document.body.classList.toggle('squeezed');
            localStorage.setItem('sidebar-squeezed', isSqueezed);
            
            // Close flyout if any is open
            const openFlyouts = document.querySelectorAll('.nav-subgroup.flyout');
            openFlyouts.forEach(f => f.classList.remove('flyout'));
        });
    }

    // 1. Handle Expandable/Collapsible Navigation Groups & Flyouts
    const groupToggles = document.querySelectorAll('.nav-group-toggle');
    
    groupToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            const isSqueezed = document.body.classList.contains('squeezed');
            const subgroup = toggle.nextElementSibling;
            
            if (isSqueezed && subgroup) {
                // Flyout logic
                if (subgroup.classList.contains('flyout')) {
                    subgroup.classList.remove('flyout');
                } else {
                    // Close others
                    document.querySelectorAll('.nav-subgroup.flyout').forEach(f => f.classList.remove('flyout'));
                    
                    // Open this one as flyout
                    subgroup.classList.add('flyout');
                    
                    // Position it precisely next to the toggle button
                    const rect = toggle.getBoundingClientRect();
                    subgroup.style.top = `${rect.top}px`;
                    
                    // Close on outside click
                    const closeFlyout = (event) => {
                        if (!toggle.contains(event.target) && !subgroup.contains(event.target)) {
                            subgroup.classList.remove('flyout');
                            document.removeEventListener('click', closeFlyout);
                        }
                    };
                    setTimeout(() => {
                        document.addEventListener('click', closeFlyout);
                    }, 0);
                }
            } else {
                // Normal accordion logic
                const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
                toggle.setAttribute('aria-expanded', !isExpanded);
            }
        });
    });

    // 2. Handle Mobile Drawer Toggle
    const menuToggle = document.getElementById('mobile-menu-toggle');
    
    if (menuToggle && sidebar) {
        const overlay = document.createElement('div');
        overlay.className = 'sidebar-overlay';
        document.body.appendChild(overlay);
        
        const toggleSidebar = () => {
            const isOpen = sidebar.classList.contains('open');
            if (isOpen) {
                sidebar.classList.remove('open');
                overlay.classList.remove('active');
            } else {
                sidebar.classList.add('open');
                overlay.classList.add('active');
            }
        };

        menuToggle.addEventListener('click', toggleSidebar);
        overlay.addEventListener('click', toggleSidebar);
    }
    
    // 3. Highlight current page
    const currentUrl = window.location.href.split('#')[0].split('?')[0];
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (!link.href) return;
        const linkUrl = link.href.split('#')[0].split('?')[0];
        
        if (linkUrl === currentUrl) {
            link.classList.add('active');
            
            // Expand parent group if inside a subgroup
            const subgroup = link.closest('.nav-subgroup');
            if (subgroup) {
                // If it's the normal view, we expand it
                subgroup.style.display = 'block'; 
                const toggle = subgroup.previousElementSibling;
                if (toggle && toggle.classList.contains('nav-group-toggle')) {
                    toggle.setAttribute('aria-expanded', 'true');
                }
            }
        }
    });

    // 4. Persist Sidebar Scroll Position
    if (sidebar) {
        const savedScrollPos = sessionStorage.getItem('sidebar-scroll-pos');
        if (savedScrollPos) {
            sidebar.scrollTop = parseInt(savedScrollPos, 10);
        }
        
        window.addEventListener('beforeunload', () => {
            sessionStorage.setItem('sidebar-scroll-pos', sidebar.scrollTop);
        });
    }
});
