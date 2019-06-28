<template>
  <div id="home">
    <router-link :to="'new'" append>New</router-link>
    <div id="active" v-show="active">
      <h2>Currently Running</h2>
      <button @click="stop_collection()">STOP ME</button>
    </div>
    <div id="list">
      <h2>Library</h2>
      <div v-for="collection in collections" :key="collection._id" @click="select(collection._id)">
        <collection-details :collection="collection" :selected="collection._id === selection"></collection-details>
      </div>
    </div>
  </div>
</template>
<script>
  import CollectionDetails from './Details.vue'
  export default {
    name: 'Home',
    data() {
      return {
        selection: undefined
      }
    },
    components: {
      CollectionDetails
    },
    mounted() {
    },
    created() {
    },
    methods: {
      select: function (id) {
        this.selection = this.selection === id ? undefined : id
        console.log(this.selection)
      },
      run_collection: function(id) {
        this.$store.dispatch("run_collection", {
          id
        }).then()
      },
      stop_collection: function() {
        this.$store.dispatch("stop_collection")
        .then()
      }
    },
    computed: {
      active() {
        return this.$store.getters.collections.find(e => {
          return e.active_flag
        })
      },
      collections() {
        return this.$store.getters.collections.filter(e => {
          return !e.active_flag
        })
      }
    },
    watch: {}
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#home {
  display: flex;
  flex-direction: column;
  background-color: white;
  padding: 10px 20px 10px 20px;
}

#active {

}
</style>