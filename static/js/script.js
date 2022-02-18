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
    //  If current slide is showing or a slide is animating, then do nothing
    if (slider.is(":animated")) {
      return;
    }

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
    move(currentIndex - 1, "100%");
  });

  btnRight.on("click", () => {
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
  const galleryViewHandler = (photos, index) => {
    const body = $("body");
    const modal = $('<div id="modal"></div>');
    const overlayEl = $('<div class="footer__overlay"></div>');
    const viewerEl = $('<div class="viewer"></div>'); // image viewer
    const sliderEl = $('<ul class="slider"></ul>'); // image slider
    const slideBtns = $(
      '<div class="slidBtn"><div class="prevBtn btn"><i class="fas fa-angle-double-left"></i></div><div class="nextBtn btn"><i class="fas fa-angle-double-right"></i></div></div>'
    );
    const counter = $('<span class="postCounter"></span>');
    let currentIndex = index;

    const clonedSlides = photos.clone(); // clone slides

    // remove styles that's already present in the photos :- this is for room detail gallery
    clonedSlides.each(function () {
      $(this).removeAttr("style");
    });

    modal.empty(); // first empty

    // join the div
    sliderEl.append(clonedSlides);
    viewerEl.append(sliderEl);
    modal.prepend(slideBtns);
    modal.append(viewerEl);
    modal.prepend(overlayEl);
    body.prepend(modal);

    const slider = $("#modal .slider");

    body.addClass("modal__open");
    clonedSlides.eq(currentIndex).css({ display: "block" });

    // post counter
    const postCounter = (index) => {
      // this render the number of post/posts length
      counter.text(`${index + 1}/${clonedSlides.length}`);
      viewerEl.append(counter);
    };

    const moveHandler = (newIndex, position) => {
      if (currentIndex > newIndex) {
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

      slider.not(":animated").animate({ left: animate }, 800, () => {
        clonedSlides.eq(currentIndex).css({ display: "none" });
        clonedSlides.eq(newIndex).css({ left: "0" });
        slider.css({ left: "0" });
        currentIndex = newIndex;
        postCounter(currentIndex);
      });
    };

    // call post counter
    postCounter(currentIndex); // from index for the first render to get accurate index

    $(document).on("click", ".footer__overlay", function () {
      modal.empty();
      modal.remove();
      body.removeClass("modal__open");
    });

    $(document).on("click", "#modal .prevBtn", function () {
      moveHandler(currentIndex - 1, "-100%");
    });

    $(document).on("click", "#modal .nextBtn", function () {
      moveHandler(currentIndex + 1, "100%");
    });
  };

  // instagram image gallery
  const IGSlides = $(".instagram__post");
  IGSlides.on("click", function () {
    const IGIndex = IGSlides.index(this);
    galleryViewHandler(IGSlides, IGIndex);
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
      // onSliderLoad: function (el) {
      //   el.lightGallery({
      //     selector: "#roomGallery .lslide",
      //   });
      // },
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
    $this.on("click", ".accordion__control", function (e) {
      // this code order must be maintained
      e.preventDefault();
      const activeControl = $(".accordion__control.active");

      // 1st: toggle active class
      $(this).addClass("active").next().not(":animated").slideToggle();

      // 2nd: remove previous active class
      activeControl // slide current active up
        .removeClass("active")
        .next()
        .slideUp();
    });
  });

  // room detail gallery viewer
  const roomIMGgallery = $("#roomGallery .room__detail_img");
  roomIMGgallery.on("click", function () {
    const roomIMGIndex = roomIMGgallery.index(this); // room image index
    galleryViewHandler(roomIMGgallery, roomIMGIndex);
  });

  //******************** end of section room detail  *************************/
});

// messages
setTimeout(() => {
  $(".messages").fadeOut("slow"); // remove message after 4sec
  $(".errorlist").fadeOut("slow"); // remove error message after 4sec
}, 5000);

// password
$(".form__group").each(function () {
  // loop through all form group
  const $this = $(this); // this is current group
  const faPass = $this.find(".fa__pass"); // get the icons
  faPass.on("click", function () {
    const passInput = $this.find("input");
    const inputType = passInput.attr("type");

    faPass.toggleClass("show"); // toggle icon

    switch (inputType) {
      case "password":
        passInput.attr("type", "text");
        break;
      case "text":
        passInput.attr("type", "password");
        break;
      default:
        passInput.attr("type", "password");
        break;
    }
  });
});

// check button
const all = $("#all");
const options = $(".option");

all.on("change", function (e) {
  if (e.target.checked) {
    options.each(function () {
      this.checked = all.prop("checked");
    });
  }
});

options.each(function () {
  $(this).on("change", function (e) {
    if (!this.checked) {
      all[0].checked = false;
    }
  });
});
