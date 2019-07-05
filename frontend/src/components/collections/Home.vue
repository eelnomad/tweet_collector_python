<template>
  <div id="home">
    <router-link :to="'new'" append>New</router-link>
    <div id="active" v-if="active">
      <h2>Currently Running</h2>
      <div @click="select(active._id)">
        <collection-details :collection="active" :selected="active._id === selection"></collection-details>
      </div>
    </div>
    <div id="list">
      <h2>Collections</h2>
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
      if (this.collections.length === 0) {
        this.$router.push({ name: 'New Collection' })
      }
    },
    created() {
    },
    methods: {
      select: function (id) {
        // this.selection = this.selection === id ? undefined : id
        this.selection = id
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
  padding: 2% 10%;
  flex-grow: 1;
}
</style>