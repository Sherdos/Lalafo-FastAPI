import { renderNavigation } from "./renders.js";

const ROOT_URL = "http://localhost:8000/";
const ROOT_API_URL = "http://localhost:8000/api/v1";

async function sendDataToLogin(email, password) {
  const response = await fetch(`${ROOT_API_URL}/auth/token`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({email:email, password:password}),
  });
  return response.json();
}

async function login(e) {
  e.preventDefault(); 
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const result = await sendDataToLogin(email, password);
    console.log(result);
    sessionStorage.setItem("access_token", result.access_token);
  } catch (err) {
    console.error("Login failed:", err);
  }
  renderNavigation()
}

function checkAuthenticated(){
    const result = sessionStorage.getItem('access_token')
    if (result){
        return true
    }else{
        return false
    }
}


async function logout() {
  sessionStorage.removeItem("access_token")
}

function renderLoginForm() {
    const form = document.getElementById('login')
    form.innerHTML = `
        <div class="flex items-center justify-center min-h-screen bg-gray-100">
  <div class="w-full max-w-md bg-white rounded-2xl shadow p-8">
    <h2 class="text-2xl font-bold mb-6 text-center">Login</h2>

    <form class="space-y-5" id="login-form">
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700">email</label>
        <input 
          type="text" 
          id="email" 
          name="email" 
          required 
          class="mt-1 block w-full px-3 py-2 border rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        >
      </div>

      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input 
          type="password" 
          id="password" 
          name="password" 
          required 
          class="mt-1 block w-full px-3 py-2 border rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
        >
      </div>

      <button 
        type="submit" 
        class="w-full py-2 px-4 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition">
        Login
      </button>
    </form>

    <p class="text-sm text-gray-600 mt-4 text-center">
      Don’t have an account? 
      <a href="#" class="text-blue-600 hover:underline">Register</a>
    </p>
  </div>
</div>
    `
}



async function initAuth() {
  renderLoginForm()
  const form = document.getElementById("login-form");
  form.addEventListener("submit", login);
  
}

export {initAuth, checkAuthenticated, logout}
