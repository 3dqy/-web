function toggleDarkMode() {
    const body = document.body;
    const lightLogo = document.getElementById('lightLogo');
    const darkLogo = document.getElementById('darkLogo');

    // Toggle dark mode by adding/removing a dark-mode class to the body
    body.classList.toggle('dark-mode');

    // Toggle between light and dark mode logos
    lightLogo.style.display = body.classList.contains('dark-mode') ? 'none' : 'inline';
    darkLogo.style.display = body.classList.contains('dark-mode') ? 'inline' : 'none';

    // Save the user's preference to local storage
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Check if the user has a dark mode preference and apply it
const savedDarkMode = localStorage.getItem('darkMode');
if (savedDarkMode === 'true') {
    toggleDarkMode();
}

