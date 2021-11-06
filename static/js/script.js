$(document).ready(function () {
  const navLinks = $(".nav__link_wrapper");
  const toggleBtn = $("#toggle__btn");
  const navLink = $(".nav__link");

  // user info
  const userGreeting = $(".user__greeting");
  const userBtn = $(".user__greeting i");
  const userLinks = $(".user__links");

  const showLinkToggler = () => {
    navLinks.toggleClass("show__links");
    toggleBtn.toggleClass("turn");
  };
  // toggle button clicked
  toggleBtn.on("click", showLinkToggler);

  navLink.on("click", (e) => {
    if (window.innerWidth < 600) {
      showLinkToggler();
    }
  });

  // user info dropdown click
  userBtn.on("click", (e) => {
    userLinks.toggleClass("show__user_links");
    userGreeting.toggleClass("link__down");
  });

  // window resized
  window.addEventListener("resize", (e) => {
    // handleWindowResize(e);
    if (e.target.innerWidth > 600) {
    }
    if (navLinks.is(".show__links")) {
      navLinks.removeClass("show__links");
    }

    if (toggleBtn.is(".turn")) {
      toggleBtn.removeClass("turn");
    }
  });

  //******************** hero  *************************/
  const slider = $(".hero__photo_slider");
  const slides = $(".hero__photo_slide");
  const btnLeft = $(".hero .btn__left");
  const btnRight = $(".hero .btn__right");
  let currentIndex = 0;
  let timer;

  const move = (newIndex, position) => {
    if (currentIndex > newIndex) {
      animate = "-100%";
    } else {
      animate = "100%";
    }

    if (newIndex < 0) {
      newIndex = 1;
    } else if (newIndex > slides.length - 1) {
      newIndex = 0;
    }

    slides.eq(newIndex).css({ display: "block", left: position });

    slider.animate({ left: animate }, () => {
      slides.eq(currentIndex).css({ display: "none" });
      slides.eq(newIndex).css({ left: "0" });
      slider.css({ left: "0" });
      currentIndex = newIndex;
    });
    handleSlideShow()
  };

  // animation slideshow
  const handleSlideShow = () => {
      clearInterval(timer)
      timer = setInterval(() => {
        move(currentIndex -1, "100%");
      }, 4000);
  }
  btnLeft.on("click", () => {
    clearInterval(timer);
    move(currentIndex - 1, "100%");
    key = 1;
  });

  btnRight.on("click", () => {
    clearInterval(timer);
    move(currentIndex + 1, "-100%");
    key = 2;
  });

  handleSlideShow()
  slides.eq(currentIndex).css({ display: "block" });
  //******************** end of hero  *************************/

  //******************** our team  *************************/
  $("#lightSlider").lightSlider({
    item: 4,
    loop: true,
    slideMargin: 30,
    auto: true,
    slideMove: 2,
    easing: "cubic-bezier(0.25, 0, 0.25, 1)",
    speed: 600,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          item: 4,
          slideMove: 1,
          slideMargin: 20,
        },
      },
      {
        breakpoint: 800,
        settings: {
          item: 2,
          slideMove: 1,
          slideMargin: 20,
        },
      },
      {
        breakpoint: 600,
        settings: {
          item: 1,
          slideMove: 1,
        },
      },
    ],
  });  
  //******************** end of our team  *************************/
});