import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'
import router from './router'

Vue.use(VueResource);
Vue.use(VueCookies);

Vue.config.productionTip = false
Vue.prototype.$api = 'http://127.0.0.1:5000/api'

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')