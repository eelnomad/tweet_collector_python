<template>
  <div id="app">
    <div id="title">
      Title
    </div>
    <div id="top-nav">
    </div>
    <div id="content">
      <div id="side-nav">
        <router-link v-for="route in routes" :to="route.path" :key="route.path">{{ route.desc }}</router-link>
      </div>
      <router-view></router-view>
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
  background: linear-gradient(to right, #C1CDCD 0%, azure 100%) no-repeat left;
  flex: 0 0 50px;
  display: flex;
  align-items: center;
  padding: 0 0 0 20px;
}

#top-nav {
  background-color: azure;
  flex: 0 0 60px;
}

#content {
  flex: 1 1 auto;
  display: flex;
  flex-direction: row;
}

#side-nav {
  flex: 0 1 300px;
}

a {
  display: flex;
  align-items: center;
  list-style-type: none;
  transition: all 0.3s ease-in-out;
  padding: 0 0 0 20px;
  height: 50px;
  text-decoration: none;
  color: black;
}

a:hover {
  color: black;
  text-decoration: line;
}

.router-link-active {/*
  background-color: black;
  color: white;
  box-shadow: inset 0 0 10px black;*/
}
</style>
