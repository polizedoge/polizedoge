// Carousel Fade Animation
const carouselImages = document.querySelectorAll('.carousel-image');
let currentIndex = 0;

function showNextImage() {
    carouselImages.forEach((img, index) => {
        img.style.opacity = index === currentIndex ? '1' : '0';
    });
    currentIndex = (currentIndex + 1) % carouselImages.length;
}

setInterval(showNextImage, 3000);
