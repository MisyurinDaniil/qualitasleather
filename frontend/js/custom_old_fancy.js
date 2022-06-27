// Управление кнопками (close button and toggle button) 
// в меню на мобильной версии проекрта для меню с группами товара 
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
// 
// 
// Куча строк говнокода для кастомизированного мною слайдера
// Два объекьа galleryBigBlock, gallerySmallBlock
// My Custom Huyastam gallery
// 
// 
let galleryBigBlock = {

    settings: {
        leftArrowClass: 'goods-image__big-left-arrow',
        rightArrowClass: 'goods-image__big-right-arrow',
        imageBlockClass: 'goods-image__medium-image-block',
        noneDisplayClass: 'display-none',
    },

    init() {
        this.eventNextImage();
        this.eventPreviusImage();
    },
    eventNextImage() {
        this.getRightArrowTag().addEventListener('click', () => this.rightArrowHandler());
    },
    eventPreviusImage() {
        this.getLeftArrowTag().addEventListener('click', () => this.leftArrowHandler());
    },
    getLeftArrowTag() {
        return document.querySelector(`.${this.settings.leftArrowClass}`);
    },

    getRightArrowTag() {
        return document.querySelector(`.${this.settings.rightArrowClass}`);
    },
    rightArrowHandler() {
        let allImageBlock = this.getAllImageBlock();
        for (let i =0; i < allImageBlock.length; i++) {
            if (allImageBlock[i].dataset.src === this.getCurrentImageBlock().dataset.src && i !== allImageBlock.length-1) {
                this.getCurrentImageBlock().classList.add(this.settings.noneDisplayClass);
                allImageBlock[i+1].classList.remove(this.settings.noneDisplayClass);
                break;
            }
            else if (allImageBlock[i].dataset.src === this.getCurrentImageBlock().dataset.src && i == allImageBlock.length-1) {
                this.getCurrentImageBlock().classList.add(this.settings.noneDisplayClass);
                allImageBlock[0].classList.remove(this.settings.noneDisplayClass);
                break;
            }
            
        }
    },
    leftArrowHandler() {
        let allImageBlock = this.getAllImageBlock();
        for (let i =0; i < allImageBlock.length; i++) {
            if (allImageBlock[i].dataset.src === this.getCurrentImageBlock().dataset.src && i !== 0) {
                this.getCurrentImageBlock().classList.add(this.settings.noneDisplayClass);
                allImageBlock[i-1].classList.remove(this.settings.noneDisplayClass);
                break;
            }
            else if (allImageBlock[i].dataset.src === this.getCurrentImageBlock().dataset.src && i == 0) {
                this.getCurrentImageBlock().classList.add(this.settings.noneDisplayClass);
                allImageBlock[allImageBlock.length-1].classList.remove(this.settings.noneDisplayClass);
                break;
            }
            
        }
    },
    getAllImageBlock() {
        return document.querySelectorAll(`.${this.settings.imageBlockClass}`);
    },
    getCurrentImageBlock() {
        let allImageBlock = this.getAllImageBlock();
        for (let i =0; i < allImageBlock.length; i++) {
            if(!allImageBlock[i].classList.contains(this.settings.noneDisplayClass)) {
                return allImageBlock[i];
            } 
        }
    },
};

let gallerySmallBlock = {

    nextArrowClass: 'goods-image__small-right-arrow',
    previousArrowClass: 'goods-image__small-left-arrow',
    blockGalleryClass: 'goods-image__small-image-wrap',
    imageBlockClass: 'goods-image__small-image-block',
    blockBorderClass: 'goods-image__small-image-block-border',
    galleryBigBlock,
    nextShowImageUrl: null,

    init() {
        this.clickBlockGallery();
        this.clickNextArrow();
        this.clickPreviousArrow();
    },
    clickBlockGallery() {
        this.getBlockGallery().addEventListener('click', (event) => this.blockGalleyHandler(event));
    },
    getBlockGallery() {
        return document.querySelector(`.${this.blockGalleryClass}`);
    },
    blockGalleyHandler(event) {
        if (event.target.tagName !== 'IMG') {
            return;
        }
        this.setNextShowImageUrl(event);
        this.showNextImageBlock();
        
    },
    setNextShowImageUrl(event) {
        this.nextShowImageUrl = event.target.dataset.mediumSrc;
        let allLi = this.getAllSmallImageBlock();
        for (let li of allLi) {
            li.classList.remove(this.blockBorderClass);
        }
        event.target.parentElement.classList.add(this.blockBorderClass);
    },

    getNextShowImageUrl() {
        return this.nextShowImageUrl;
    },

    getAllSmallImageBlock() {
        return document.querySelectorAll('.goods-image__small-image-block');
    },

    showNextImageBlock() {
        let allImageBlock = this.galleryBigBlock.getAllImageBlock();
        for (let i = 0; i < allImageBlock.length; i++) {
            if(allImageBlock[i].firstElementChild.attributes.src.value === this.getNextShowImageUrl()) {
                this.setDisplayNoneCurrentImage();
                allImageBlock[i].classList.remove('display-none');
                return;
            }
        }
    },
    setDisplayNoneCurrentImage() {
        this.galleryBigBlock.getCurrentImageBlock().classList.add('display-none');
    },

    clickNextArrow() {
        document.querySelector(`.${this.nextArrowClass}`).addEventListener('click', () => {
            let smallImageBlocks = this.getAllSmallImageBlock();
            let nextPictureBlock = null;
            for (let i = 0; i < smallImageBlocks.length; i++){
                if ((smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && !smallImageBlocks[i - 1])
                    || (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && smallImageBlocks[i + 1] && i === 1)) {

                    smallImageBlocks[i].classList.remove(this.blockBorderClass);

                    nextPictureBlock =  smallImageBlocks[i + 1];
                    nextPictureBlock.classList.add(this.blockBorderClass);

                    this.showMediumPicture(nextPictureBlock);
                    break;
                }
                else if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && smallImageBlocks[i + 1] && i > 1) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);

                    nextPictureBlock = smallImageBlocks[i + 1]
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    nextPictureBlock.style.marginLeft = '10px';

                    smallImageBlocks[i - 1].style.marginLeft = '0';
                    smallImageBlocks[i - 2].classList.add('display-none');

                    this.showMediumPicture(nextPictureBlock);
                    break;
                }
                else if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && !smallImageBlocks[i + 1]) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);
                    smallImageBlocks[i - 1].style.marginLeft = '0';
                    smallImageBlocks[i - 2].classList.add('display-none');

                    nextPictureBlock = smallImageBlocks[0];
                    nextPictureBlock.classList.remove('display-none');
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    nextPictureBlock.style.marginLeft = '10px';

                    this.showMediumPicture(nextPictureBlock);

                    document.querySelector('.goods-image__small-image-list')
                        .append(nextPictureBlock.cloneNode(true));
                    nextPictureBlock.remove();
                    break;
                }
            }
        });
    },

    clickPreviousArrow() {
        document.querySelector(`.${this.previousArrowClass}`).addEventListener('click', () => {
            let smallImageBlocks = this.getAllSmallImageBlock();
            let nextPictureBlock = null;
            for (let i = 0; i < smallImageBlocks.length; i++) {
                if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && !smallImageBlocks[i - 1]) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);
                    smallImageBlocks[i].style.marginLeft = '10px';

                    nextPictureBlock = smallImageBlocks[smallImageBlocks.length - 1];
                    nextPictureBlock.classList.remove('display-none');
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    nextPictureBlock.style.marginLeft = '0px';
                    this.showMediumPicture(nextPictureBlock);

                    document.querySelector('.goods-image__small-image-list')
                        .prepend(nextPictureBlock.cloneNode(true));
                    smallImageBlocks[smallImageBlocks.length - 1].remove();
                    break;
                }
                else if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && smallImageBlocks[i + 1]
                    && smallImageBlocks[i - 1].classList.contains('display-none')) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);
                    smallImageBlocks[i].style.marginLeft = '10px';

                    nextPictureBlock = smallImageBlocks[i - 1];
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    nextPictureBlock.classList.remove('display-none');
                    nextPictureBlock.style.marginLeft = '0px';
                    this.showMediumPicture(nextPictureBlock);
                    break;
                }
                else if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && smallImageBlocks[i + 1]) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);

                    nextPictureBlock = smallImageBlocks[i - 1];
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    this.showMediumPicture(nextPictureBlock);

                    break;
                }
                else if (smallImageBlocks[i].classList.contains(this.blockBorderClass)
                    && smallImageBlocks[i - 1] && !smallImageBlocks[i + 1]) {
                    smallImageBlocks[i].classList.remove(this.blockBorderClass);

                    nextPictureBlock = smallImageBlocks[i - 1];
                    nextPictureBlock.classList.add(this.blockBorderClass);
                    this.showMediumPicture(nextPictureBlock);
                    break;
                }
            }
        });
    },

    showMediumPicture(nextPictureBlock){
        let nextPictureImgUrl = nextPictureBlock.children[0].dataset.mediumSrc;
        let allMediumImageBlock = this.galleryBigBlock.getAllImageBlock();

        for (let i =0; i < allMediumImageBlock.length; i++) {
            allMediumImageBlock[i].classList.add('display-none');
        }
        for (let i =0; i < allMediumImageBlock.length; i++) {
            if (allMediumImageBlock[i].children[0].attributes.src.value === nextPictureImgUrl) {
                allMediumImageBlock[i].classList.remove('display-none');
            }
        }
    },
};

/*********************************
 * Init My Custom Huyastam gallery
 */
galleryBigBlock.init();
gallerySmallBlock.init();
