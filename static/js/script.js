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
    handleSlideShow();
  };

  // animation slideshow
  const handleSlideShow = () => {
    clearInterval(timer);
    timer = setInterval(() => {
      move(currentIndex - 1, "100%");
    }, 4000);
  };
  btnLeft.on("click", () => {
    clearInterval(timer);
    move(currentIndex - 1, "100%");
  });

  btnRight.on("click", () => {
    clearInterval(timer);
    move(currentIndex + 1, "-100%");
  });

  handleSlideShow();
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

  //******************** our blog  *************************/
  $("#blogPost").lightSlider({
    item: 3,
    loop: true,
    slideMargin: 30,
    // auto: true,
    slideMove: 2,
    easing: "cubic-bezier(0.25, 0, 0.25, 1)",
    speed: 1000,
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
  //******************** end of our blog  *************************/

  //******************** our partners  *************************/
  $("#our__partners").lightSlider({
    item: 6,
    loop: true,
    slideMargin: 30,
    auto: true,
    slideMove: 2,
    easing: "cubic-bezier(0.25, 0, 0.25, 1)",
    speed: 1000,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          item: 6,
          slideMove: 1,
          slideMargin: 20,
        },
      },
      {
        breakpoint: 800,
        settings: {
          item: 4,
          slideMove: 1,
          slideMargin: 20,
        },
      },
      {
        breakpoint: 600,
        settings: {
          item: 2,
          slideMove: 1,
        },
      },
    ],
  });
  //******************** end of our partners  *************************/

  //******************** footer section  *************************/
  const footerYear = $("#year");
  const date = new Date();
  footerYear.text(date.getFullYear()); // render year to footer year element

  // instagram gallery viewer

  const body = $("body");
  const modal = $('<div id="modal"></div>');
  const footerOverlay = $('<div class="footer__overlay"></div>');
  const footerIMGViewer = $('<div class="viewer"></div>'); // image viewer
  const footerIMGSlider = $('<div class="slider"></div>'); // image slider
  const footerSlideBtn = $(
    '<div class="slidBtn"><div class="prevBtn btn"><i class="fas fa-angle-double-left"></i></div><div class="nextBtn btn"><i class="fas fa-angle-double-right"></i></div></div>'
  );
  const counter = $('<span class="postCounter"></span>');
  const IGSlides = $(".instagram__post"); // instagram images
  let clonedSlides = null;
  let footerSlider = null;
  let footerIndex = 0;

  const footerMove = (newIndex, position) => {
    if (footerIndex > newIndex) {
      animate = "100%";
    } else {
      animate = "-100%";
    }

    if (newIndex < 0) {
      newIndex = 1;
    } else if (newIndex > clonedSlides.length - 1) {
      newIndex = 0;
    }

    clonedSlides.eq(newIndex).css({ display: "block", left: position });

    footerSlider.not(":animated").animate({ left: animate }, 800, () => {
      clonedSlides.eq(footerIndex).css({ display: "none" });
      clonedSlides.eq(newIndex).css({ left: "0" });
      footerSlider.css({ left: "0" });
      footerIndex = newIndex;
      postCounter(footerIndex);
    });
  };

  // post counter
  const postCounter = (index) => {
    // this render the number of post/posts length
    counter.text(`${index + 1}/${clonedSlides.length}`);
    footerIMGViewer.append(counter);
  };

  IGSlides.on("click", function () {
    modal.empty(); // first empty
    clonedSlides = IGSlides.clone(); // clone slides

    footerIndex = IGSlides.index(this);

    // join the div
    footerIMGSlider.append(clonedSlides);
    footerIMGViewer.append(footerIMGSlider);
    modal.prepend(footerSlideBtn);
    modal.append(footerIMGViewer);
    modal.prepend(footerOverlay);
    body.prepend(modal);
    footerSlider = $("#modal .slider");

    body.addClass("modal__open");
    clonedSlides.eq(footerIndex).css({ display: "block" });

    // call post counter
    postCounter(footerIndex); // from index for the first render to get accurate index
  });

  $(document).on("click", ".footer__overlay", function () {
    modal.empty();
    modal.remove();
    body.removeClass("modal__open");
  });

  $(document).on("click", "#modal .prevBtn", function () {
    footerMove(footerIndex - 1, "-100%");
  });

  $(document).on("click", "#modal .nextBtn", function () {
    footerMove(footerIndex + 1, "100%");
  });
  //******************** end of our footer section  *************************/

  //******************** section room detail  *************************/
  // image gallery
  $(document).ready(function () {
    $("#roomGallery").lightSlider({
      gallery: true,
      item: 1,
      loop: true,
      thumbItem: 5,
      slideMargin: 0,
      enableDrag: false,
      currentPagerPosition: "left",
      onSliderLoad: function (el) {
        el.lightGallery({
          selector: "#roomGallery .lslide",
        });
      },
    });
  });
  // tabbed panel
  $(".tab__list").each(function () {
    const $this = $(this);

    $this.on("click", ".tab__control", function (e) {
      e.preventDefault();

      const activeTab = $this.find("li.active");
      const activPanel = $("div.tab__panel.active");
      const tabControl = $(this);
      const id = this.hash;

      // panel
      activPanel.removeClass("active"); // remove active class from panel that's active
      $(id).addClass("active"); // add active class to this tab panel

      // tab
      activeTab.removeClass("active");
      tabControl.parent().addClass("active");
    });
  });

  // accordion

  $("ul.accordion").each(function () {
    const $this = $(this);
    $this.on("click", ".accodion__control", function (e) {
      // this code order must be maintained
      e.preventDefault();
      const activeControl = $(".accodion__control.active");
    
      // 1st: toggle active class
        $(this)
          .addClass("active")
          .next()
          .not(":animated")
          .slideToggle();

      // 2nd: remove previous active class
         activeControl // slide current active up
           .removeClass("active")
           .next()
           .slideUp()

    });
  });

  //******************** end of section room detail  *************************/
});
