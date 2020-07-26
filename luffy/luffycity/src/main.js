import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false


import '@/assets/css/global.css'

import axios from 'axios'
Vue.prototype.$axios = axios;


import cookies from 'vue-cookies'
Vue.prototype.$cookies = cookies;

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// 配置全局自定义设置
import settings from '@/assets/js/settings'
Vue.prototype.$settings = settings;
// 在所有需要与后台交互的组件中：this.$settings.base_url + '再拼接具体后台路由'


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
