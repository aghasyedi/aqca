/* js/navigation.js */
document.addEventListener('DOMContentLoaded', () => {
    
    // Icon mappings for sidebar items
    const icons = {
        'About AQCA': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 22 7.5 22 16.5 12 22 2 16.5 2 7.5 12 2"></polygon><text x="12" y="14" font-size="8" text-anchor="middle" font-family="sans-serif" font-weight="bold" fill="currentColor" stroke="none">AQ</text><circle cx="12" cy="7" r="1.5" fill="currentColor" stroke="none"></circle></svg>',
        'Preface': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"></path><path d="M15 2l5 5v-5z"></path></svg>',
        'QC Basics': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><ellipse cx="12" cy="12" rx="10" ry="4" stroke-dasharray="2 2"></ellipse><path d="M12 2v20"></path><path d="M2 12h20"></path><path d="M5 19l14-14"></path></svg>',
        'Algorithms': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="5" height="5"></rect><text x="4.5" y="8.5" font-size="4" text-anchor="middle" font-family="sans-serif" stroke="none" fill="currentColor">H</text><line x1="7" y1="7.5" x2="11" y2="7.5"></line><circle cx="13" cy="7.5" r="2"></circle><line x1="13" y1="5.5" x2="13" y2="15"></line><circle cx="13" cy="15" r="1" fill="currentColor"></circle><line x1="15" y1="7.5" x2="18" y2="7.5"></line><rect x="18" y="5" width="5" height="5"></rect><path d="M19 8.5a1.5 1.5 0 0 0 3 0"></path><line x1="20.5" y1="8.5" x2="22" y2="6.5"></line></svg>',
        'Visualise': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><ellipse cx="12" cy="12" rx="10" ry="4" stroke-dasharray="2 2"></ellipse><path d="M12 2a10 10 0 0 0 0 20"></path><path d="M7 12c1.5-2 3.5-3 5-3s3.5 1 5 3c-1.5 2-3.5 3-5 3s-3.5-1-5-3z" fill="currentColor" stroke="none"></path><circle cx="12" cy="12" r="1.5" fill="var(--background)"></circle></svg>',
        'Analysis Centre': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="10" r="6"></circle><line x1="14.24" y1="14.24" x2="20" y2="20"></line><path d="M7 10c1-1.5 2-1.5 3 0s2 1.5 3 0"></path></svg>',
        'Resources': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2z"></path><path d="M4 6v-2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v2"></path><path d="M14 6v6l-2-1.5L10 12V6"></path></svg>',
        'References': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="3"></circle><circle cx="6" cy="12" r="3"></circle><circle cx="18" cy="19" r="3"></circle><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line></svg>',
        'Appendix': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><path d="M8 11h3m-1.5-1.5v3"></path><path d="M16 13v4a2 2 0 0 1-4 0v-5a3 3 0 0 1 6 0v5" stroke-linecap="round"></path></svg>',
        'Developer': '<svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10z"></path><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><polyline points="16 11 18 13 16 15"></polyline><polyline points="8 11 6 13 8 15"></polyline></svg>'
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
                item.setAttribute('data-tooltip', label);
                item.removeAttribute('title');
                if (icons[label]) {
                    const arrow = item.querySelector('.nav-group-icon');
                    item.innerHTML = `<div style="display: flex; align-items: center; gap: 0.75rem;">${icons[label]} <span>${label}</span></div>`;
                    if (arrow) item.appendChild(arrow);
                }
            } else {
                // Regular links
                // Wrap Home so its text hides when squeezed
                if (text === "✦Home" || text === "Home") {
                    item.setAttribute('data-tooltip', 'Home');
                    item.removeAttribute('title');
                    // Remove any existing inner text and recreate cleanly
                    item.innerHTML = `<span class="step-num nav-icon" style="background: var(--primary); color:#ffffff; font-size:12px;">✦</span> <span>Home</span>`;
                    return;
                }
                label = text;
                item.setAttribute('data-tooltip', label);
                item.removeAttribute('title');
                if (icons[label]) {
                    // Wrap text in a span so we can hide it in CSS
                    item.innerHTML = `${icons[label]} <span>${label}</span>`;
                }
            }
        });

        // Setup fixed tooltip for squeezed mode
        const tooltip = document.createElement('div');
        tooltip.className = 'sidebar-tooltip';
        document.body.appendChild(tooltip);

        topLevelItems.forEach(item => {
            item.addEventListener('mouseenter', () => {
                if (document.body.classList.contains('squeezed')) {
                    const label = item.getAttribute('data-tooltip');
                    if (label) {
                        tooltip.textContent = label;
                        const rect = item.getBoundingClientRect();
                        tooltip.style.top = `${rect.top + (rect.height / 2)}px`;
                        tooltip.style.left = `${rect.right + 15}px`;
                        tooltip.classList.add('visible');
                    }
                }
            });
            item.addEventListener('mouseleave', () => {
                tooltip.classList.remove('visible');
            });
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

    const algoSubgroups = document.querySelectorAll('.nav-subgroup');
    algoSubgroups.forEach(subgroup => {
        if (subgroup.querySelector('.nav-category-label')) {
            const items = Array.from(subgroup.children);
            let currentNestedLi = null;
            let currentNestedUl = null;
            
            subgroup.innerHTML = '';
            
            items.forEach(li => {
                if (li.classList.contains('nav-category-label')) {
                    currentNestedLi = document.createElement('li');
                    currentNestedLi.className = 'nav-item-nested';
                    
                    const btn = document.createElement('button');
                    btn.className = 'nav-group-toggle-nested';
                    btn.innerHTML = `<span style="flex:1;">${li.innerHTML}</span> <span class="nav-group-icon-nested">▼</span>`;
                    
                    currentNestedUl = document.createElement('ul');
                    currentNestedUl.className = 'nav-subgroup-nested';
                    
                    currentNestedLi.appendChild(btn);
                    currentNestedLi.appendChild(currentNestedUl);
                    subgroup.appendChild(currentNestedLi);
                    
                    btn.addEventListener('click', (e) => {
                        e.stopPropagation(); 
                        if (!document.body.classList.contains('squeezed') || !subgroup.classList.contains('flyout')) {
                            const isExpanded = btn.getAttribute('aria-expanded') === 'true';
                            btn.setAttribute('aria-expanded', !isExpanded);
                        }
                    });
                    
                } else if (currentNestedUl) {
                    const link = li.querySelector('.nav-link');
                    if (link && link.textContent.trim().startsWith('•')) {
                        link.textContent = link.textContent.replace('•', '').trim();
                    }
                    currentNestedUl.appendChild(li);
                } else {
                    subgroup.appendChild(li);
                }
            });
        }
    });

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
                    subgroup.style.bottom = 'auto'; // reset in case it was modified before
                    
                    // Force a reflow check to ensure it doesn't clip off the bottom
                    requestAnimationFrame(() => {
                        const subgroupHeight = subgroup.offsetHeight;
                        if (rect.top + subgroupHeight > window.innerHeight) {
                            subgroup.style.top = 'auto';
                            subgroup.style.bottom = '10px';
                        }
                    });
                    
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
            
            // Expand nested subgroup if any
            const nestedSubgroup = link.closest('.nav-subgroup-nested');
            if (nestedSubgroup) {
                nestedSubgroup.style.display = 'block';
                const nestedToggle = nestedSubgroup.previousElementSibling;
                if (nestedToggle) {
                    nestedToggle.setAttribute('aria-expanded', 'true');
                }
            }
            
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
