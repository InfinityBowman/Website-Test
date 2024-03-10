const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');
const navLogo = document.querySelector('#navbar__logo');


// Display Mobile Menu
const mobileMenu = () => {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
};

menu.addEventListener('click', mobileMenu);

// Show active menu when scrolling
const highlightMenu = () => {
    const elem = document.querySelector('.highlight');
    const homeMenu = document.querySelector('#home-page');
    const aboutMenu = document.querySelector('#about-page');
    const dataMenu = document.querySelector('#data-page');
    let scrollPos = window.scrollY;

    if (window.location.href.endsWith('data.html')) {
        dataMenu.classList.add('highlight');
        homeMenu.classList.remove('highlight');
        aboutMenu.classList.remove('highlight');
        return;
    }

    // Adds 'highlight' class to menu items
    if (window.innerWidth > 960 && scrollPos < 600) {
        homeMenu.classList.add('highlight');
        aboutMenu.classList.remove('highlight');
        return;
    }
    else if (window.innerWidth > 960 && scrollPos < 1400) {
        aboutMenu.classList.add('highlight');
        homeMenu.classList.remove('highlight');
        dataMenu.classList.remove('highlight');
        return;
    }
    else if (window.innerWidth > 960 && scrollPos < 2345) {
        dataMenu.classList.add('highlight');
        aboutMenu.classList.remove('highlight');
        return;
    }

    if((elem && window.innerWidth > 960 && scrollPos < 600) || elem) {
        elem.classList.remove('highlight');
    }
}

window.addEventListener('scroll', highlightMenu);
window.addEventListener('load', highlightMenu);
window.addEventListener('click', highlightMenu);

// Close mobile nav after click
const hideMobileMenu = () => {
    const menuBars = document.querySelector('.is-active');
    if (window.innerWidth <= 768 && menuBars) {
        menu.classList.toggle('is-active');
        menuLinks.classList.remove('active');
    }
}

menuLinks.addEventListener('click', hideMobileMenu);
navLogo.addEventListener('click', hideMobileMenu);

// Button gradient animations
const button = document.querySelector('.button');
const mainBtn = document.querySelector('.main__btn');

  function updateGradient() {
    const currentTime = new Date().getTime();
    const position = (currentTime % 5000) / (50); // Change the divisor to adjust speed

    button.style.backgroundPosition = position + '% 0%';
    mainBtn.style.backgroundPosition = position + '% 0%';

    requestAnimationFrame(updateGradient);
  }
  updateGradient();

  // Try for logo
