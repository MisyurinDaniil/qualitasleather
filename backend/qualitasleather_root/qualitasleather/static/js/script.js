
document.addEventListener('DOMContentLoaded', function(){

    // Управление кнопками (close button and toggle button) 
    // в меню мобильной версии проекрта (меню с группами товара)
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
    /********************************************/
    /*************Отправка формы заказа *********/
    /********************************************/
    document.querySelector('.main-button').addEventListener('click', () => {
        document.querySelector(".modal-window__content").classList.remove('display-none');
        document.querySelector(".modal-window__order-true").classList.add('display-none');
        document.querySelector(".modal-window__order-false").classList.add('display-none');
    });

    if (document.querySelector("form")) {

        const ajaxSend = async (formData) => {
            const response = await fetch('/makeorder/', {
                method: "POST",
                body: formData
            });
            if (!response.ok) {
                throw new Error(`Ошибка по адресу /makeorder/, статус ошибки ${response.status}`);
            }
            return await response.text();
        };

        const forms = document.querySelectorAll("form");

        forms.forEach(form => {
            form.addEventListener("submit", function (e) {
                e.preventDefault();
                const formData = new FormData(this);
                ajaxSend(formData)
                    .then((response) => {
                        console.log(response);
                        // form.reset(); // очищаем поля формы
                        document.querySelector(".modal-window__content").classList.add('display-none')
                        document.querySelector(".modal-window__order-true").classList.remove('display-none')
                    })
                    .catch((err) => {
                        console.error(err)
                        document.querySelector(".modal-window__content").classList.add('display-none')
                        document.querySelector(".modal-window__order-false").classList.remove('display-none')
                    });
            });
        });
    }


}, false);


