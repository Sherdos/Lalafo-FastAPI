const ROOT_URL = "http://localhost:8000/";
const ROOT_API_URL = "http://localhost:8000/api/v1";

async function fetchData() {
  const response = await fetch(`${ROOT_API_URL}/products`);
  return response.json();
}

async function init() {
  const products = await fetchData();
  console.log(products);

  const container = document.getElementById("products");
  container.innerHTML = `
    <h1 class="text-2xl font-semibold mb-6">Products</h1>
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
    </div>
  `;
}

window.addEventListener('DOMContentLoaded', init);
