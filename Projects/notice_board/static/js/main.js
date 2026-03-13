// ========================================
// 1. Dark Mode Toggle
// ========================================
const themeToggle = document.getElementById('themeToggle');
const htmlElement = document.documentElement;
const iconElement = themeToggle ? themeToggle.querySelector('i') : null;

// Check for saved theme preference
const savedTheme = localStorage.getItem('theme') || 'dark';
htmlElement.setAttribute('data-bs-theme', savedTheme);
updateThemeIcon(savedTheme);

if (themeToggle) {
    themeToggle.addEventListener('click', function() {
        const currentTheme = htmlElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        htmlElement.setAttribute('data-bs-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
        
        // Show toast notification
        showToast(`Switched to ${newTheme} mode`, 'info');
    });
}

function updateThemeIcon(theme) {
    if (iconElement) {
        iconElement.className = theme === 'dark' ? 'fas fa-moon' : 'fas fa-sun';
    }
}

// ========================================
// 2. Real-time Clock (Dashboard)
// ========================================
const clockElement = document.getElementById('realtimeClock');

function updateClock() {
    if (clockElement) {
        const now = new Date();
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        const seconds = String(now.getSeconds()).padStart(2, '0');
        const timeString = `${hours}:${minutes}:${seconds}`;
        
        clockElement.textContent = timeString;
    }
}

if (clockElement) {
    updateClock();
    setInterval(updateClock, 1000);
}

// ========================================
// 3. Toast Notifications
// ========================================
function showToast(message, type = 'success') {
    const toastEl = document.getElementById('liveToast');
    if (toastEl) {
        const toastBody = toastEl.querySelector('.toast-body');
        const toast = new bootstrap.Toast(toastEl);
        
        // Remove old bg classes
        toastEl.classList.remove('bg-success', 'bg-danger', 'bg-warning', 'bg-info', 'bg-primary');
        
        // Add new bg class
        toastEl.classList.add(`bg-${type}`, 'text-white');
        
        toastBody.textContent = message;
        toast.show();
    }
}

// Make showToast available globally
window.showToast = showToast;

// ========================================
// 4. Delete Confirmation
// ========================================
const deleteButtons = document.querySelectorAll('.delete-btn');

deleteButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        if (!confirm('Are you sure you want to delete this notice? This action cannot be undone.')) {
            e.preventDefault();
        }
    });
});

// ========================================
// 5. Search Functionality (Dashboard Table)
// ========================================
const searchInput = document.getElementById('searchInput');
const tableBody = document.querySelector('tbody');

if (searchInput && tableBody) {
    searchInput.addEventListener('keyup', function() {
        const searchTerm = this.value.toLowerCase();
        const rows = tableBody.querySelectorAll('tr');
        
        rows.forEach(row => {
            const text = row.textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });
}

// ========================================
// 6. Search Functionality (User Panel Cards)
// ========================================
const userSearchInput = document.getElementById('userSearch');
const noticeCards = document.querySelectorAll('.notice-card');

if (userSearchInput) {
    userSearchInput.addEventListener('keyup', function() {
        const searchTerm = this.value.toLowerCase();
        
        noticeCards.forEach(card => {
            const title = card.querySelector('.card-title');
            const content = card.querySelector('.card-text');
            
            if (title && content) {
                const titleText = title.textContent.toLowerCase();
                const contentText = content.textContent.toLowerCase();
                
                if (titleText.includes(searchTerm) || contentText.includes(searchTerm)) {
                    card.style.display = '';
                    card.style.animation = 'slideIn 0.5s ease-out';
                } else {
                    card.style.display = 'none';
                }
            }
        });
        
        // Show/hide no results message
        const visibleCards = Array.from(noticeCards).filter(card => card.style.display !== 'none');
        const existingNoResults = document.getElementById('noResults');
        const cardsContainer = document.querySelector('.row.g-4');
        
        if (existingNoResults) {
            existingNoResults.remove();
        }
        
        if (visibleCards.length === 0 && cardsContainer) {
            const message = document.createElement('div');
            message.id = 'noResults';
            message.className = 'col-12 text-center py-5';
            message.innerHTML = '<h4 class="text-muted">No notices found</h4>';
            cardsContainer.appendChild(message);
        }
    });
}

// ========================================
// 7. Auto-dismiss Alerts
// ========================================
const alerts = document.querySelectorAll('.alert');

alerts.forEach(alert => {
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    }, 5000); // Auto-dismiss after 5 seconds
});

// ========================================
// 8. Form Validation Feedback
// ========================================
const forms = document.querySelectorAll('.needs-validation');

forms.forEach(form => {
    form.addEventListener('submit', function(event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add('was-validated');
    }, false);
});

// ========================================
// 9. Category Filter (User Panel)
// ========================================
const categoryButtons = document.querySelectorAll('.category-filter');

categoryButtons.forEach(btn => {
    btn.addEventListener('click', function() {
        const category = this.dataset.category;
        
        // Update active state
        categoryButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        // Filter cards
        noticeCards.forEach(card => {
            const cardCategory = card.dataset.category;
            
            if (category === 'All' || cardCategory === category) {
                card.style.display = '';
                card.style.animation = 'slideIn 0.5s ease-out';
            } else {
                card.style.display = 'none';
            }
        });
        
        // Update URL without reload
        const url = new URL(window.location);
        if (category === 'All') {
            url.searchParams.delete('category');
        } else {
            url.searchParams.set('category', category);
        }
        window.history.pushState({}, '', url);
    });
});

// ========================================
// 10. Sort Functionality
// ========================================
const sortButtons = document.querySelectorAll('.sort-btn');

sortButtons.forEach(btn => {
    btn.addEventListener('click', function() {
        const sortOrder = this.dataset.sort;
        
        // Update active state
        sortButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        
        // Sort cards
        const container = document.querySelector('.row.g-4');
        const cardsArray = Array.from(noticeCards);
        
        cardsArray.sort((a, b) => {
            const dateA = new Date(a.querySelector('.text-muted.small')?.textContent || 0);
            const dateB = new Date(b.querySelector('.text-muted.small')?.textContent || 0);
            
            return sortOrder === 'newest' ? dateB - dateA : dateA - dateB;
        });
        
        // Re-append sorted cards
        cardsArray.forEach(card => {
            card.style.display = '';
            container.appendChild(card);
        });
        
        // Update URL
        const url = new URL(window.location);
        url.searchParams.set('sort', sortOrder);
        window.history.pushState({}, '', url);
    });
});

// ========================================
// 11. Smooth Scroll for Anchor Links
// ========================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ========================================
// 12. Dynamic Year Update
// ========================================
const yearElement = document.getElementById('currentYear');
if (yearElement) {
    yearElement.textContent = new Date().getFullYear();
}

// ========================================
// 13. Card Hover Effects
// ========================================
const cards = document.querySelectorAll('.notice-card');

cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// ========================================
// 14. Modal Reset on Close
// ========================================
const modals = document.querySelectorAll('.modal');

modals.forEach(modal => {
    modal.addEventListener('hidden.bs.modal', function() {
        const form = modal.querySelector('form');
        if (form) {
            form.reset();
            form.classList.remove('was-validated');
        }
    });
});

// ========================================
// 15. Edit Notice - Populate Modal Data
// ========================================
const editButtons = document.querySelectorAll('.edit-btn');

editButtons.forEach(button => {
    button.addEventListener('click', function() {
        const id = this.dataset.id;
        const title = this.dataset.title;
        const content = this.dataset.content;
        const category = this.dataset.category;
        
        const modal = document.getElementById('editNoticeModal');
        if (modal) {
            const form = modal.querySelector('form');
            modal.querySelector('#editId').value = id;
            modal.querySelector('#editTitle').value = title;
            modal.querySelector('#editContent').value = content;
            modal.querySelector('#editCategory').value = category;
            // Set form action to the edit endpoint
            form.action = '/dashboard/edit/' + id;
        }
    });
});

// ========================================
// 16. Pagination Active State
// ========================================
const paginationLinks = document.querySelectorAll('.page-link');
const currentParams = new URLSearchParams(window.location.search);
const currentPage = currentParams.get('page') || 1;

paginationLinks.forEach(link => {
    const linkPage = link.textContent.trim();
    if (linkPage === currentPage) {
        link.parentElement.classList.add('active');
    }
});

// ========================================
// 17. Keyboard Shortcuts
// ========================================
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + D = Toggle Dark Mode
    if ((e.ctrlKey || e.metaKey) && e.key === 'd') {
        e.preventDefault();
        themeToggle.click();
    }
    
    // Escape = Close Modals
    if (e.key === 'Escape') {
        const openModals = document.querySelectorAll('.modal.show');
        openModals.forEach(modal => {
            const modalInstance = bootstrap.Modal.getInstance(modal);
            if (modalInstance) {
                modalInstance.hide();
            }
        });
    }
});

// ========================================
// 18. Notice Card Animation on Scroll
// ========================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(card);
});

// ========================================
// 19. Search Focus (Home Page)
// ========================================
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.has('q')) {
    const searchInput = document.getElementById('userSearch');
    if (searchInput) {
        searchInput.focus();
    }
}

// ========================================
// 20. Pre-fill Edit Form (if data attributes exist)
// ========================================
// This handles the case where edit data is embedded in the button
const editModal = document.getElementById('editNoticeModal');
if (editModal) {
    const form = editModal.querySelector('form');
    const submitBtn = form.querySelector('button[type="submit"]');
    
    // Update form action based on notice ID
    const noticeId = document.getElementById('editId')?.value;
    if (noticeId) {
        form.action = `/dashboard/edit/${noticeId}`;
    }
}