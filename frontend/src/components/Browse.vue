<template>
  <div id="browse">
    <div id="browse-nav">
      <div id="logo">
        Test
      </div>
      <div id="browse-collections">
        <router-link :to="'new'" class="nav-object">
          <p class="qs">New Collection</p>
        </router-link>
        <router-link v-for="col in collections" :key="col._id" :to="col._id" class="nav-object" :class="{'active': col.active_flag}" @mouseenter.native="active = col._id" @mouseleave.native="active = null">
          <p v-show="col._id !== active" class="qs">{{ col.desc }}</p>
          <p v-show="col._id === active" class="qs">{{ col.keywords.join(',') }}</p>
        </router-link>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'Browse',
  data () {
    return {
      active: null
    }
  },
  mounted () {
    this.$store.dispatch('load_collections')
  },
  created () {
  },
  methods: {
    toggle_display: function (id) {
      if (this.activity[id]) {
        this.activity[id] = !this.activity[id]
      } else {
        this.activity[id] = true
      }
    }
  },
  computed: {
    collections () {
      return this.$store.getters.collections.sort((a, b) => {
        if (a.active_flag && !b.active_flag) {
          return -1
        }
        if (!a.active_flag && b.active_flag) {
          return 1
        }
        return 0
      })
    }
  },
  watch: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#browse {
  height: 100%;
  width: 100%;
  display: flex;
}
#browse-nav {
  flex: 0 0 400px;
}
#logo {
  height: 20%;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}
#browse-collections {
  height: 80%;
  box-sizing: border-box;
  padding: 20px 0 50px 0;
  overflow-y: scroll;
  display: flex;
  flex-direction: column;
}
#browse-collections::-webkit-scrollbar { 
  width: 0 !important
}
.nav-object {
  padding-left: 20px;
  justify-content: center;
  flex: 0 0 100px;
  display: flex;
  flex-direction: column;
  color: black;
  border-top: solid;
  border-top-width: 1px;
  text-decoration: none;
  background-color: white;
  box-shadow: none;
  transition: all .1s linear;
  overflow: none;
}
.nav-object:hover {
  background-color: black;
  color: white;
  box-shadow: 5px 10px white;
}
.nav-object::-webkit-scrollbar { 
  width: 0 !important
}
</style>
