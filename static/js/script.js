$(function(){
    const navLinks = $(".nav__link_wrapper");
    const toggleBtn = $("#toggle__btn");
    const navLink = $(".nav__link")

    // user info
    const userGreeting = $(".user__greeting");
    const userBtn = $('.user__greeting i');
    const userLinks = $(".user__links");

    const showLinkToggler = () => {
        navLinks.toggleClass("show__links");
        toggleBtn.toggleClass('turn')
    }
    // toggle button clicked
    toggleBtn.on('click', showLinkToggler);

    navLink.on("click", (e)=>{
        if(window.innerWidth < 600){
            showLinkToggler()
        }
    });

    // user info dropdown click
    userBtn.on('click', (e)=>{
        userLinks.toggleClass('show__user_links');
        userGreeting.toggleClass('link__down');
    })

    // window resized
    window.addEventListener('resize', (e)=>{
        // handleWindowResize(e);
        if (e.target.innerWidth > 600) {
        }
        if (navLinks.is(".show__links")) {
          navLinks.removeClass("show__links");
        }

        if (toggleBtn.is(".turn")) {
          toggleBtn.removeClass("turn");
        } 

    })


})