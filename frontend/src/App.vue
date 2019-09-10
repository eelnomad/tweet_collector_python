<template>
  <div id="app">
    <div id="title">
      <h2>Random Utilities</h2>
      <span/>
      <div id="top-nav-links" @click="to_git()">
        <font-awesome-icon :icon="['fab', 'github']" /> GitHub
      </div>
    </div>
    <div id="top-nav">
    </div>
    <div id="content">
      <div id="side-nav">
        <router-link v-for="route in routes" :to="route.path" :key="route.path">
          <h4 :style="{ color: route.color}">{{ route.desc }}</h4>
          <span></span>
          <font-awesome-icon :icon="route.icon" :style="{ color: route.color}"/>
        </router-link>
      </div>
      <transition name="fade">
        <router-view></router-view>
      </transition>
    </div>
  </div>
</template>

<script>
  import 'normalize.css/normalize.css'
  import './assets/css/custom.css'

  export default {
    name: 'app',
    data () {
      return {
      }
    },
    mounted () {
    },
    created () {
    },
    methods: {
      to_git: function () {
        window.open('https://github.com/eelnomad/tweet_collector_python')
      }
    },
    computed: {
      routes() {
        return this.$router.options.routes.filter(e => {
          return "desc" in e
        })
      }
    }
  }
</script>

<style scoped>
#app {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

#title {
  background-color: green;
  background: linear-gradient(to right, #168254 0%, #1CA369 100%) no-repeat left;
  flex: 0 0 50px;
  display: flex;
  align-items: center;
  padding: 0 0 0 20px;
  display: flex;
}

span {
  flex: 1 1 auto;
}

#title > h2, h3 {
  margin: 0;
}

#top-nav-links {
  margin: 0 10px 0 10px;
  cursor: pointer;
}

#top-nav {
  background-color: #1CA369;
  flex: 0 0 60px;
}

#content {
  flex: 1 1 auto;
  display: flex;
  flex-direction: row;
}

#side-nav {
  flex: 0 1 300px;
  border-right: 2px solid whitesmoke;
}

#side-nav > a {
  display: flex;
  align-items: center;
  padding: 0 20px 0 20px;
  height: 50px;
  text-decoration: none;
  color: black;
}

.router-link-active {
  color: transparent;
}

.fade-enter-active, .fade-leave-active {
  transition: all .1s ease-in;
  overflow-x: hidden;
}
.fade-enter {
  z-index: -1;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
