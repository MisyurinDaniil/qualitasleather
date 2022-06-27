// Управление кнопками (close button and toggle button) 
// в меню на мобильной версии проекрта для меню с группами товара 
let navMain = document.querySelector('.main-nav__list');
let navToggleBurger = document.querySelector('.burger-toggle');

if (navMain) navMain.classList.remove('main-nav__list--nojs');
if (navToggleBurger) {
    navToggleBurger.addEventListener('click', function() {
        if (navMain.classList.contains('main-nav__list--closed')) {
            navMain.classList.remove('main-nav__list--closed');
            navMain.classList.add('main-nav__list--opened');
        } else {
            navMain.classList.add('main-nav__list--closed');
            navMain.classList.remove('main-nav__list--opened');
        }
    });
}
//
//Fancybox product slider  
// Initialise Carousel
const mainCarouselEl = document.querySelector("#mainCarousel");
const thumbCarouselEl = document.querySelector("#thumbCarousel");

if (mainCarouselEl && thumbCarouselEl) {
    const mainCarousel = new Carousel(mainCarouselEl, {
        Dots: false,
    });

    //Fancybox product slider
    // Thumbnails
    const thumbCarousel = new Carousel(thumbCarouselEl, {
        Sync: {
        target: mainCarousel,
        friction: 0,
        },
        Dots: false,
        Navigation: false,
        center: true,
        slidesPerPage: 1,
        infinite: false,
    });
        //
    //Fancybox product slider  
    // Customize Fancybox
    Fancybox.bind('[data-fancybox="gallery"]', {
        Carousel: {
        on: {
            change: (that) => {
            mainCarousel.slideTo(mainCarousel.findPageForSlide(that.page), {
                friction: 0,
            });
            },
        },
        },
    });
}