import Vue from 'vue'
import VueRouter from 'vue-router'
import DoctorDash from '../components/DoctorDash'

Vue.use(VueRouter)

const routes = [
  {
    path: '/doctor',
    name: 'Doctor',
    component: DoctorDash
  },
  {
    path: '/',
    redirect: {
      name: 'Doctor'
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router