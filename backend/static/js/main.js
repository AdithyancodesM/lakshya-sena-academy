function toggleMenu() {
    const nav = document.getElementById("navLinks");
    nav.classList.toggle("show");
}
let currentIndex = 0;
let images = [];

document.addEventListener("DOMContentLoaded", () => {
    images = Array.from(document.querySelectorAll(".gallery-img"));

    images.forEach((img, index) => {
        img.addEventListener("click", () => openModal(index));
    });

    document.querySelector(".close").addEventListener("click", closeModal);
    document.querySelector(".prev").addEventListener("click", showPrev);
    document.querySelector(".next").addEventListener("click", showNext);

    // Keyboard controls
    document.addEventListener("keydown", (e) => {
        if (document.getElementById("imageModal").style.display === "block") {
            if (e.key === "Escape") closeModal();
            if (e.key === "ArrowLeft") showPrev();
            if (e.key === "ArrowRight") showNext();
        }
    });

    // Swipe support
    let startX = 0;

    document.getElementById("imageModal").addEventListener("touchstart", e => {
        startX = e.touches[0].clientX;
    });

    document.getElementById("imageModal").addEventListener("touchend", e => {
        let endX = e.changedTouches[0].clientX;
        if (startX - endX > 50) showNext();
        if (endX - startX > 50) showPrev();
    });

    // Click outside image closes modal
    document.getElementById("imageModal").addEventListener("click", e => {
        if (e.target.id === "imageModal") closeModal();
    });
});

function openModal(index) {
    currentIndex = index;
    const modal = document.getElementById("imageModal");
    const modalImg = document.getElementById("modalImage");

    modal.style.display = "block";
    modalImg.src = images[currentIndex].src;
}

function closeModal() {
    document.getElementById("imageModal").style.display = "none";
}

function showNext() {
    currentIndex = (currentIndex + 1) % images.length;
    document.getElementById("modalImage").src = images[currentIndex].src;
}

function showPrev() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    document.getElementById("modalImage").src = images[currentIndex].src;
}
