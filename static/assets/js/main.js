import { filters, renderProducts, init } from './product.js';
import {initAuth, checkAuthenticated, logout } from './auth.js'

import { renderNavigation } from "./renders.js";



function initMain() {
  renderNavigation();
  init();
  initAuth();
  console.log('+')
}

window.addEventListener('DOMContentLoaded', initMain);
