
document.getElementById('data-page').addEventListener('click', function(event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith('data.html')) {
        // Scroll to the top of the page
        window.scrollTo(0, 0);
    } else {
        // Change the URL and navigate to a new page
        window.location.href = 'data.html';
    }
});

document.getElementById('home-page').addEventListener('click', function(event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith('index.html')) {
        // Scroll to the top of the page
        window.scrollTo(0, 0);
    } else {
        // Change the URL and navigate to a new page
        window.location.href = 'index.html';
    }
});

document.getElementById('navbar__logo').addEventListener('click', function(event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith('index.html')) {
        // Scroll to the top of the page
        window.scrollTo(0, 0);
    } else {
        // Change the URL and navigate to a new page
        window.location.href = 'index.html';
    }
});
