document
  .getElementById("data-page")
  .addEventListener("click", function (event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith("data.html")) {
      // Scroll to the top of the page
      window.scrollTo(0, 0);
    } else {
      // Change the URL and navigate to a new page
      window.location.href = "data.html";
    }
  });

document
  .getElementById("home-page")
  .addEventListener("click", function (event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith("index.html")) {
      // Scroll to the top of the page
      window.scrollTo(0, 0);
    } else {
      // Change the URL and navigate to a new page
      window.location.href = "index.html";
    }
  });

document
  .getElementById("music-page")
  .addEventListener("click", function (event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith("music.html")) {
      // Scroll to the top of the page
      window.scrollTo(0, 0);
    } else {
      // Change the URL and navigate to a new page
      window.location.href = "music.html";
    }
  });

document
  .getElementById("navbar__logo")
  .addEventListener("click", function (event) {
    // Prevent the default behavior of the link
    event.preventDefault();

    // Check if the current page is 'data.html'
    if (window.location.href.endsWith("index.html")) {
      // Scroll to the top of the page
      window.scrollTo(0, 0);
    } else {
      // Change the URL and navigate to a new page
      window.location.href = "index.html";
    }
  });

document
  .getElementById("service-card-4")
  .addEventListener("click", function (event) {
    // Prevent the default behavior of the link
    event.preventDefault();
    // IKEA website Blahaj
    window.open(
      "https://www.ikea.com/us/en/p/blahaj-soft-toy-shark-90373590/",
      "_blank"
    );
  });
