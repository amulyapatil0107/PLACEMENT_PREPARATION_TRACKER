document.addEventListener('DOMContentLoaded', () => {
    const mobileToggle = document.querySelector('.mobile-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    if (mobileToggle && sidebar) {
        mobileToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }

    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    
    if (themeToggle) {
        const savedTheme = localStorage.getItem('theme') || 'dark';
        if (savedTheme === 'light') {
            body.classList.remove('dark-theme');
            body.classList.add('light-theme');
            themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
        } else {
            body.classList.add('dark-theme');
            body.classList.remove('light-theme');
            themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
        }

        themeToggle.addEventListener('click', () => {
            if (body.classList.contains('dark-theme')) {
                body.classList.remove('dark-theme');
                body.classList.add('light-theme');
                themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
                localStorage.setItem('theme', 'light');
            } else {
                body.classList.add('dark-theme');
                body.classList.remove('light-theme');
                themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
                localStorage.setItem('theme', 'dark');
            }
        });
    }

    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(toast => {
        const closeBtn = toast.querySelector('.toast-close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                toast.style.animation = 'slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1) reverse forwards';
                setTimeout(() => toast.remove(), 300);
            });
        }
    });
});