// Family Background Data

// Fetch family data from JSON file
async function loadData() {
  const res = await fetch("/static/data/data.json");
  data = await res.json();

  // Setup family backgroun data
  const testimonialsList = document.querySelector(".testimonials-list");
  testimonialsList.innerHTML = "";

  for (const t of data.familyData) {
    testimonialsList.innerHTML += `
    <li class="testimonials-item">
      <div class="content-card" data-testimonials-item>
        <figure class="testimonials-avatar-box">
          <img
            src="${t.avatar}"
            alt="${t.name}"
            width="60"
            data-testimonials-avatar
          />
        </figure>
        <h4 class="h4 testimonials-item-title" data-testimonials-title>
          ${t.name}
        </h4>
        <p data-testimonials-relationship hidden>${t.relationship}</p>
        <div class="testimonials-text" data-testimonials-text>
          <p>${t.text}</p>
        </div>
      </div>
    </li>
  `;
  }

  // Setup hobbies data
  const hobbiesList = document.querySelector(".service-list");
  hobbiesList.innerHTML = "";

  for (const hobby of data.hobbiesData) {
    hobbiesList.innerHTML += `
    <li class="service-item">
        <div class="service-icon-box">
            <img
            src="${hobby.icon}"
        "
            alt="${hobby.title} Icon"
            width="40"
            />
        </div>

        <div class="service-content-box">
            <h4 class="h4 service-item-title">${hobby.title}</h4>

            <p class="service-item-text">
            ${hobby.text}
            </p>
        </div>
    </li>
  `;
  }
}

loadData();
