class ThemeSwitcher {
    constructor() {
        this.themeToggle = document.getElementById('theme-toggle');
        this.darkIcon = document.querySelector('.dark-icon');
        this.lightIcon = document.querySelector('.light-icon');
        this.htmlElement = document.documentElement;
        
        this.currentTheme = localStorage.getItem('theme') || 'dark';
        this.setTheme(this.currentTheme);
        
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
    }
    
    setTheme(theme) {
        this.htmlElement.setAttribute('data-bs-theme', theme);
        this.darkIcon.classList.toggle('d-none', theme === 'light');
        this.lightIcon.classList.toggle('d-none', theme === 'dark');
        localStorage.setItem('theme', theme);
    }
    
    toggleTheme() {
        const newTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        this.currentTheme = newTheme;
        this.setTheme(newTheme);
    }
}

// Initialize theme switcher when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ThemeSwitcher();
});
