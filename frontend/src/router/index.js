import Vue from 'vue'
import Router from 'vue-router'
import Browse from '@/components/Browse'
import Details from '@/components/Details'
import Create from '@/components/Create'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Browse,
      children: [
        {
          path: 'new',
          component: Create
        },
        {
          path: ':id',
          name: 'Details',
          component: Details
        },
      ]
    }
  ]
})
