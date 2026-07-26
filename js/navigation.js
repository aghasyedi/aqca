/* js/navigation.js */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Handle Expandable/Collapsible Navigation Groups
    const groupToggles = document.querySelectorAll('.nav-group-toggle');
    
    groupToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const isExpanded = toggle.getAttribute('aria-expanded') === 'true';
            toggle.setAttribute('aria-expanded', !isExpanded);
        });
    });

    // 2. Handle Mobile Drawer Toggle
    const menuToggle = document.getElementById('mobile-menu-toggle');
    const sidebar = document.getElementById('sidebar');
    
    if (menuToggle && sidebar) {
        // Create overlay element
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
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        // Simple matching logic (could be improved for complex paths)
        if (linkPath && currentPath.endsWith(linkPath) && linkPath !== '/' && linkPath !== '#') {
            link.classList.add('active');
            
            // Expand parent group if inside a subgroup
            const subgroup = link.closest('.nav-subgroup');
            if (subgroup) {
                const toggle = subgroup.previousElementSibling;
                if (toggle && toggle.classList.contains('nav-group-toggle')) {
                    toggle.setAttribute('aria-expanded', 'true');
                }
            }
        }
    });

    // 4. Persist Sidebar Scroll Position
    if (sidebar) {
        // Restore scroll position on load
        const savedScrollPos = sessionStorage.getItem('sidebar-scroll-pos');
        if (savedScrollPos) {
            sidebar.scrollTop = parseInt(savedScrollPos, 10);
        }
        
        // Save scroll position before leaving page
        window.addEventListener('beforeunload', () => {
            sessionStorage.setItem('sidebar-scroll-pos', sidebar.scrollTop);
        });
    }
});
