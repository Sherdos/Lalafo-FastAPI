import { filters, renderProducts, init } from './product.js';
import {initAuth } from './auth.js'

let isAuthenticated = false;

function renderHeader() {
  const navBar = document.getElementById('nav');
  navBar.innerHTML = `
  <header class="bg-white shadow h-16 flex items-center px-6 justify-between">
      <h1 class="text-2xl font-bold">Dashboard</h1>
      <div class="p-4 border-b">
        <input 
          type="text" 
          id="search" 
          placeholder="Search ..." 
          class="w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
      </div>
      ${!isAuthenticated ? `<button class="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700">Login</button>` : ''}
  </header>`;
  
  // attach search listener
  document.getElementById('search').addEventListener('input', e => search(e.target.value));
}

async function search(q) {
  filters['q'] = q;
  await renderProducts();
}

async function logout() {
  isAuthenticated = false;
  renderNavigation();
}

function renderLogoutButton() {
  const logoutButton = document.getElementById('logout-button');
  if (isAuthenticated) {
    logoutButton.innerHTML = `
      <button id="logout-action" class="w-full px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700">
        Logout
      </button>
    `;
    document.getElementById('logout-action').addEventListener('click', logout);
  } else {
    logoutButton.innerHTML = '';
  }
}

function renderNavigation() {
  renderHeader();
  renderLogoutButton();
}

function initMain() {
  renderNavigation();
  init();
  initAuth();
  console.log('+')
}

window.addEventListener('DOMContentLoaded', initMain);
