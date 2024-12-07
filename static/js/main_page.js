let currentSlide = 0;
const slides = document.querySelector('.slides');
const dots = document.querySelectorAll('.dots button');

function showSlide(index) {
    currentSlide = index;
    slides.style.transform = `translateX(-${index * 100}%)`;
    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
}

setInterval(() => {
    currentSlide = (currentSlide + 1) % dots.length;
    showSlide(currentSlide);
}, 5000);
