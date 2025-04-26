const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
}, { threshold: 0.5 });

document.addEventListener('DOMContentLoaded', () => {
    const storyText = document.querySelector('.story-text');
    const categoriesSection = document.querySelector('.categories-section');
    const categoryItems = document.querySelectorAll('.category-item');
    
    observer.observe(storyText);
    observer.observe(categoriesSection);
    categoryItems.forEach(item => observer.observe(item));

    // User menu dropdown
    const userMenuTrigger = document.querySelector('.user-menu-trigger');
    const dropdownMenu = document.querySelector('.dropdown-menu');

    if (userMenuTrigger && dropdownMenu) {
        userMenuTrigger.addEventListener('click', () => {
            dropdownMenu.classList.toggle('active');
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (!userMenuTrigger.contains(e.target)) {
                dropdownMenu.classList.remove('active');
            }
        });
    }
});