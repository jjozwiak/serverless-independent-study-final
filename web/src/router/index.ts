import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/forms',
    name: 'Forms',
    component: () => import('../views/Forms.vue')
  },
  {
    path: '/form/create',
    name: 'CreateForm',
    component: () => import('../views/CreateForm.vue')
  },
  {
    path: '/form/test',
    name: 'FormTest',
    component: () => import('../views/FormTest.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
