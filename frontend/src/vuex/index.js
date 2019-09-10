import Vue from 'vue'
import Vuex from 'vuex/dist/vuex.js'
import axios from 'axios/dist/axios.js'

axios.defaults.baseURL = ''
Vue.prototype.$http = axios


Vue.use(Vuex)

const state = {
  collections: null
}

const getters = {
  collections (state) {
    return state.collections
  }
}

const mutations = {
  set_collections (state, payload) {
    state.collections = payload
  }
}

const actions = {
  load_collections (context) {
    axios.get('/api/list')
    .then(r => {
      context.commit('set_collections', r.data)
    })
  },
  create_collection (context, payload) {
    return new Promise((resolve, reject) => {
      axios.get('/api/new', {
        params: payload
      }).then(r => {
        context.dispatch('load_collections')
        resolve(r)
      }).catch(e => {
        reject(e)
      })
    })
  },
  delete_collection (context, payload) {
    return new Promise((resolve, reject) => {
      axios.get('/api/delete', {
        params: payload
      }).then(r => {
        context.dispatch('load_collections')
        resolve(r)
      }).catch(e => {
        reject(e)
      })
    })
  },
  run_collection (context, payload) {
    return new Promise((resolve, reject) => {
      axios.get('/api/run', {
        params: payload
      }).then(r => {
        context.dispatch('load_collections')
        resolve(r)
      }).catch(e => {
        reject(e)
      })
    })
  },
  stop_collection (context) {
    return new Promise((resolve, reject) => {
      axios.get('/api/stop')
      .then(r => {
        context.dispatch('load_collections')
        resolve(r)
      }).catch(e => {
        reject(e)
      })
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
