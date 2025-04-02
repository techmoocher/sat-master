// Main JavaScript file for SAT Master

document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Add smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Sidebar functionality
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.querySelector('.sidebar');
    const closeBtn = document.querySelector('.btn-close-sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    
    // Function to open sidebar with improved animation
    function openSidebar() {
        // Add active class with slight delay for smoother appearance
        overlay.classList.add('active');
        setTimeout(() => {
            sidebar.classList.add('active');
            document.body.classList.add('sidebar-open');
        }, 50);
        document.body.style.overflow = 'hidden'; // Prevent scrolling when sidebar is open
    }
    
    // Function to close sidebar with improved animation
    function closeSidebar() {
        sidebar.classList.remove('active');
        setTimeout(() => {
            overlay.classList.remove('active');
        }, 300); // Match this with the sidebar transition duration
        document.body.classList.remove('sidebar-open');
        document.body.style.overflow = ''; // Restore scrolling
    }
    
    // Toggle sidebar when burger button is clicked
    sidebarToggle.addEventListener('click', function() {
        if (sidebar.classList.contains('active')) {
            closeSidebar();
        } else {
            openSidebar();
        }
    });
    
    // Close sidebar when close button is clicked
    closeBtn.addEventListener('click', closeSidebar);
    
    // Close sidebar when overlay is clicked
    overlay.addEventListener('click', closeSidebar);
    
    // Close sidebar when escape key is pressed
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && sidebar.classList.contains('active')) {
            closeSidebar();
        }
    });
    
    // Add hover effect to navigation items
    const navItems = document.querySelectorAll('.nav-link, .sidebar-link');
    navItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.querySelector('i').classList.add('fa-beat');
        });
        item.addEventListener('mouseleave', function() {
            this.querySelector('i').classList.remove('fa-beat');
        });
    });

    // Add active class to current navigation item
    const currentPage = window.location.pathname.split('/').pop();
    document.querySelectorAll('.navbar-nav .nav-link').forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
});

// Function to include HTML content
function includeHTML() {
    const includes = document.getElementsByTagName('include');
    for (let i = 0; i < includes.length; i++) {
        const element = includes[i];
        const file = element.getAttribute("src");
        if (file) {
            const xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4) {
                    if (this.status == 200) {element.innerHTML = this.responseText;}
                    if (this.status == 404) {element.innerHTML = "Page not found.";}
                    element.replaceWith(...element.childNodes);
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            return;
        }
    }
}
