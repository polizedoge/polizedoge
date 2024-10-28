<script>
let currentIndex = 0;
const images = document.querySelectorAll('.carousel img');

function showNextImage() {
    images.forEach((img, index) => {
        img.classList.remove('fade');
        img.style.opacity = '0';
    });
    images[currentIndex].classList.add('fade');
    images[currentIndex].style.opacity = '1';
    currentIndex = (currentIndex + 1) % images.length;
}

setInterval(showNextImage, 3000); // Adjust the interval as needed
showNextImage(); // Initial call
</script>
