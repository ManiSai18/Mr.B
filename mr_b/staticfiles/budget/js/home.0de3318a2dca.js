// Menu Dropdown
document.querySelector(".btn-dropdown").addEventListener("click", function () {
  document.querySelector(".main-nav-menu").classList.toggle("show-toggle");
  document.querySelector(".line-1").classList.toggle("line-1-toggleLine");
  document.querySelector(".line-2").classList.toggle("line-2-toggleLine");
  document.querySelector(".line-3").classList.toggle("line-3-toggleLine");
});

// Carousel Slider
const slides = document.querySelectorAll(".slide");
const slider = document.querySelector(".slider");
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");

let currentIndex = 0;
const totalSlides = slides.length;

function showSlide(index) {
  slides.forEach(slide => slide.classList.remove("active"));
  slides[index].classList.add("active");
  slider.style.transform = `translateX(-${index * 100}vw)`;
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % totalSlides;
  showSlide(currentIndex);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
  showSlide(currentIndex);
}

next.addEventListener("click", nextSlide);
prev.addEventListener("click", prevSlide);
setInterval(nextSlide, 4000);

showSlide(currentIndex);
