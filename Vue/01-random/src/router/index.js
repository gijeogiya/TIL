import Vue from 'vue'
import VueRouter from 'vue-router'

import LunchView from '../views/LunchView.vue'
import LottoView from '@/views/LottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    // URL
    path: '/lunch',
    // 별명
    name: 'lunch',
    // 어떤 컴포넌트와 매핑되는가
    component: LunchView,
  },
  {
    path: '/lotto/:count',
    name: 'lotto',
    component: LottoView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
