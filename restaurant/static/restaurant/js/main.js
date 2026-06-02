const hamburger = document.getElementById("hamburger");
const navLinks = document.getElementById("navLinks");
const mobileMenuOverlay = document.getElementById("mobileMenuOverlay");

if (hamburger && navLinks) {
    const closeMenu = () => {
        hamburger.classList.remove("active");
        navLinks.classList.remove("active");
        document.body.classList.remove("menu-open");
        if (mobileMenuOverlay) {
            mobileMenuOverlay.classList.remove("active");
        }
    };

    hamburger.addEventListener("click", function () {
        hamburger.classList.toggle("active");
        navLinks.classList.toggle("active");
        document.body.classList.toggle("menu-open");

        if (mobileMenuOverlay) {
            mobileMenuOverlay.classList.toggle("active");
        }
    });

    const navItems = navLinks.querySelectorAll("a");
    navItems.forEach(link => {
        link.addEventListener("click", closeMenu);
    });

    if (mobileMenuOverlay) {
        mobileMenuOverlay.addEventListener("click", closeMenu);
    }
}