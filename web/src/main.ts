import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import store from './store'
import router from './router'


Vue.config.productionTip = false

window.vm = new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
