"use strict";

// --- General Utility ---
const elementToggleFunc = function (elem) {
  elem.classList.toggle("active");
  console.log(
    `Element ${elem.classList.contains("active") ? "activated" : "deactivated"}`
  );
};

// --- Sidebar Functionality ---
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");
if (sidebar && sidebarBtn) {
  sidebarBtn.addEventListener("click", function () {
    elementToggleFunc(sidebar);
  });
}

// --- Testimonials Modal (Only on About Page) ---
const testimonialsItem = document.querySelectorAll("[data-testimonials-item]");
const modalContainer = document.querySelector("[data-modal-container]");
const modalCloseBtn = document.querySelector("[data-modal-close-btn]");
const overlay = document.querySelector("[data-overlay]");

if (testimonialsItem.length > 0 && modalContainer && modalCloseBtn && overlay) {
  const modalImg = document.querySelector("[data-modal-img]");
  const modalTitle = document.querySelector("[data-modal-title]");
  const modalText = document.querySelector("[data-modal-text]");
  const modalRelationship = document.querySelector("[data-modal-relationship]");

  const testimonialsModalFunc = function () {
    elementToggleFunc(modalContainer);
    elementToggleFunc(overlay);
  };

  for (let i = 0; i < testimonialsItem.length; i++) {
    testimonialsItem[i].addEventListener("click", function () {
      if (modalImg) modalImg.src = this.querySelector("[data-testimonials-avatar]").src;
      if (modalImg) modalImg.alt = this.querySelector("[data-testimonials-avatar]").alt;
      if (modalTitle) modalTitle.innerHTML = this.querySelector("[data-testimonials-title]").innerHTML;
      if (modalText) modalText.innerHTML = this.querySelector("[data-testimonials-text]").innerHTML;
      if (modalRelationship) modalRelationship.innerHTML = this.querySelector("[data-testimonials-relationship]").innerHTML;
      testimonialsModalFunc();
    });
  }

  modalCloseBtn.addEventListener("click", testimonialsModalFunc);
  overlay.addEventListener("click", testimonialsModalFunc);
}

// --- Project Filter (Only on Projects Page) ---
const select = document.querySelector("[data-select]");
const selectItems = document.querySelectorAll("[data-select-item]");
const selectValue = document.querySelector("[data-select-value]");
const filterBtns = document.querySelectorAll("[data-filter-btn]");

if (select && selectItems.length > 0 && selectValue && filterBtns.length > 0) {
  select.addEventListener("click", function () {
    elementToggleFunc(this);
  });

  for (let i = 0; i < selectItems.length; i++) {
    selectItems[i].addEventListener("click", function () {
      let selectedValue = this.innerText.toLowerCase();
      selectValue.innerText = this.innerText;
      elementToggleFunc(select);
      filterFunc(selectedValue);
    });
  }

  const filterItems = document.querySelectorAll("[data-filter-item]");

  const filterFunc = function (selectedValue) {
    for (let i = 0; i < filterItems.length; i++) {
      if (selectedValue === "all") {
        filterItems[i].classList.add("active");
      } else if (
        selectedValue === filterItems[i].dataset.category.toLowerCase()
      ) {
        filterItems[i].classList.add("active");
      } else {
        filterItems[i].classList.remove("active");
      }
    }
  };

  let lastClickedBtn = filterBtns[0];

  for (let i = 0; i < filterBtns.length; i++) {
    filterBtns[i].addEventListener("click", function () {
      let selectedValue = this.innerText.toLowerCase();
      if (selectValue) selectValue.innerText = this.innerText;

      filterFunc(selectedValue);

      if (lastClickedBtn) {
        lastClickedBtn.classList.remove("active");
      }
      this.classList.add("active");
      lastClickedBtn = this;
    });
  }
}

// --- Contact Form (Only on Contact Page) ---
const form = document.querySelector("[data-form]");
const formInputs = document.querySelectorAll("[data-form-input]");
const formBtn = document.querySelector("[data-form-btn]");

if (form && formInputs.length > 0 && formBtn) {
  for (let i = 0; i < formInputs.length; i++) {
    formInputs[i].addEventListener("input", function () {
      if (form.checkValidity()) {
        formBtn.removeAttribute("disabled");
      } else {
        formBtn.setAttribute("disabled", "");
      }
    });
  }
}

// --- Page Navigation ---
const navigationLinks = document.querySelectorAll("[data-nav-link]");

if (navigationLinks.length > 0) {
  for (let i = 0; i < navigationLinks.length; i++) {
    navigationLinks[i].addEventListener("click", function (event) {
      event.preventDefault();
      const pageName = this.dataset.pageName;

      if (pageName) {
        const url = pageName === "about" ? "/" : `/${pageName}`;
        window.location.href = url;
      } else {
        console.warn("data-page-name attribute missing on navigation link.");
        window.location.href = "/";
      }
    });
  }
}

// --- About Text Indentation (Only on About Page) ---
document.addEventListener("DOMContentLoaded", function() {
    const indentParagraphs = document.querySelectorAll(".about-text p");
    const indentFiller = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";

    if (indentParagraphs.length > 0) {
        indentParagraphs.forEach(p => {
            if (!p.textContent.startsWith(indentFiller.replace(/&nbsp;/g, ' '))) {
                p.innerHTML = indentFiller + p.innerHTML;
            }
        });
    }

    // Modal Date (for testimonials, if present)
    const modalDate = document.querySelector(".modal-date");
    if (modalDate) {
        const now = new Date();
        const options = { year: "numeric", month: "long", day: "numeric" };
        modalDate.textContent = now.toLocaleDateString("en-US", options);
    }

    // Call the lazy loading function on DOMContentLoaded
    addLazyLoadingToImages();
});

// --- Lazy Loading Images Function ---
function addLazyLoadingToImages() {
  const images = document.querySelectorAll("img");
  images.forEach(img => {
    // Only add lazy loading if it's not already present or explicitly set to "eager"
    if (!img.getAttribute("loading")) {
      img.setAttribute("loading", "lazy");
    }
  });
  console.log("Lazy loading attribute added to all images.");
}


// --- Resume Download Function ---
window.downloadResume = function() {
  const url = "/static/pdf/Jade Atyla Madigal - Resume.pdf";
  const link = document.createElement("a");
  link.href = url;
  link.download = "Jade Atyla Madigal - Resume.pdf";
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};


// --- Burger Menu Functionality ---
const burgerMenuBtn = document.querySelector("[data-burger-menu-btn]");
const navbar = document.querySelector(".navbar");

function toggleNavbar(active) {
  if (navbar && burgerMenuBtn) {
    if (active) {
      navbar.classList.add("active");
      burgerMenuBtn.querySelector("ion-icon")?.setAttribute("name", "close-sharp");
    } else {
      navbar.classList.remove("active");
      burgerMenuBtn.querySelector("ion-icon")?.setAttribute("name", "menu-outline");
    }
  }
}

if (burgerMenuBtn && navbar) {
  burgerMenuBtn.addEventListener("click", () => {
    const isActive = navbar.classList.contains("active");
    toggleNavbar(!isActive);
  });

  navigationLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (navbar.classList.contains("active") && window.innerWidth < 1024) {
        toggleNavbar(false);
      }
    });
  });
}