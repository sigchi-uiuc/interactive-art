import { createRouter, createWebHistory } from 'vue-router'
import ArtView from '../views/ArtView.vue'
import CarouselView from '@/views/CarouselView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: CarouselView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/art-view/:id',
    name: 'ArtView',
    component: ArtView,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
