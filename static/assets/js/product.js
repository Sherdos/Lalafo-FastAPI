const ROOT_URL = "http://localhost:8000/";
const ROOT_API_URL = "http://localhost:8000/api/v1";

let filters = {};

async function fetchProductData() {
  const response = await fetch(`${ROOT_API_URL}/search/products`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(filters),
  });
  return response.json();
}

async function fetchCategoryData() {
  const response = await fetch(`${ROOT_API_URL}/categories/tree`);
  return response.json();
}

async function renderProducts() {
  const products = await fetchProductData();
  const container = document.getElementById("products");
  if (container){

      let result = '';
      if (products.length > 0) {
        result = `
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          ${products.map(product => `
            <div class="bg-white rounded-2xl shadow p-4 flex flex-col">
              <img src="${ROOT_URL}${product.image}" class="w-full h-40 object-cover rounded-xl mb-4" />
              <h2 class="text-lg font-medium mb-1">${product.name}</h2>
              <p class="text-sm text-gray-500 mb-4">${product.description}</p>
              <div class="mt-auto flex items-center justify-between">
                <span class="font-semibold">$${product.price}</span>
                <button class="px-3 py-1.5 text-sm rounded-xl bg-gray-900 text-white hover:bg-gray-800 transition">
                  Add to Cart
                </button>
              </div>
            </div>
          `).join("")}
        </div>`;
      } else {
        result = '<h2 class="font-semibold">Ничего не найдено </h2>';
      }
      container.innerHTML = result;
  }
}

function renderCategories(categories, container_name = 'categories') {
  const container = document.getElementById(container_name);

  container.innerHTML = categories.map(category => {
    if (category.childer && category.childer.length > 0) {
      return `
        <div>
          <button 
            onclick="toggleDropdown(${category.id})" 
            class="flex justify-between items-center w-full px-3 py-2 text-gray-700 rounded hover:bg-gray-200"
          >
            ${category.name}
            <svg class="w-4 h-4 transition-transform" id="icon-${category.id}" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
            </svg>
          </button>
          <div id="dropdown-${category.id}" class="ml-4 mt-1 space-y-1 hidden"></div>
        </div>
      `;
    } else {
      return `
        <button onclick="changeCategory(${category.id}, '${category.name}')" class="block px-3 py-2 text-gray-600 rounded hover:bg-gray-100">${category.name}</button>
      `;
    }
  }).join("");

  categories.forEach(category => {
    if (category.childer && category.childer.length > 0) {
      renderCategories(category.childer, `dropdown-${category.id}`);
    }
  });
}

function changeTitle(newTitle) {
  const container = document.getElementById('title');
  container.textContent = newTitle;
}

async function changeCategory(category_id, category_name) {
  filters['category_id'] = category_id;
  changeTitle(category_name);
  await renderProducts();
}

async function init() {
  await renderProducts();
  const categories = await fetchCategoryData();
  renderCategories(categories);
  // renderNavigation() will come from main.js
}

// 👇 Export only what main.js needs
export { filters, renderProducts, renderCategories, changeCategory, init };
