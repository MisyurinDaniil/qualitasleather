'use strict';

window.onload = function() {
    
    // Управление кнопками (close button and toggle button) 
    // в меню на мобильной версии проекрта 
    let navMain = document.querySelector('.main-nav__list');
    let navToggleBurger = document.querySelector('.burger-toggle');
    
    navMain.classList.remove('main-nav__list--nojs');
    
    navToggleBurger.addEventListener('click', function() {
        if (navMain.classList.contains('main-nav__list--closed')) {
            navMain.classList.remove('main-nav__list--closed');
            navMain.classList.add('main-nav__list--opened');
        } else {
            navMain.classList.add('main-nav__list--closed');
            navMain.classList.remove('main-nav__list--opened');
        }
    });
    
    let goodsBigLeftArrow = document.querySelector('.goods-image__big-left-arrow');
    let goodsMediumImageList = document.querySelectorAll('.goods-image__medium-image-link');
    goodsBigLeftArrow.addEventListener('click', function() {   
//        console.log (goodsMediumImageList);
        for (let i = 0; i < goodsMediumImageList.length; i++) {
//            console.log (goodsMediumImageList[i]);
//            console.log (goodsMediumImageList[i].classList);      
            if (!goodsMediumImageList[i].classList.contains('display-none') && i >= 1) {
                goodsMediumImageList[i].classList.add('display-none');
                goodsMediumImageList[i-1].classList.remove('display-none');
                return;
            }
        }
    });
    
    let goodsBigRightArrow = document.querySelector('.goods-image__big-right-arrow');
    goodsBigRightArrow.addEventListener('click', function() {
        console.log (goodsMediumImageList);
        for (let i = 0; i < goodsMediumImageList.length; i++) {
            console.log (goodsMediumImageList[i]);
            console.log (goodsMediumImageList[i].classList);      
            if (!goodsMediumImageList[i].classList.contains('display-none') && 
            i < goodsMediumImageList.length-1) {
                goodsMediumImageList[i].classList.add('display-none');
                goodsMediumImageList[i+1].classList.remove('display-none');
                return;
            }
        }
    });
     
}; 
