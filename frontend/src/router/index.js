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
    desc: 'Twitter Collector',
    icon: ['fab', 'twitter'],
    color: '#00aced',
    component: Collection,
    children: [
    {
      path: 'new',
      name: 'New Collection',
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