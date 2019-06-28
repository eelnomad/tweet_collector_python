import Vue from 'vue'
import Router from 'vue-router'
import Collection from '@/components/collections/Collection'
import CollectionHome from '@/components/collections/Home'
import CollectionCreate from '@/components/collections/Create'

Vue.use(Router)

const router = new Router({
  routes: [
  {
    path: '*',
    redirect: { name: 'Collections'}
  },
  {
    path: '/collections',
    desc: 'Collections',
    component: Collection,
    children: [
    {
      path: 'new',
      component: CollectionCreate
    },
    {
      path: '',
      name: 'Collections',
      component: CollectionHome
    },
    ]
  }
  ]
})



export default router