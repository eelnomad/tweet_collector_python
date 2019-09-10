<template>
  <div id="pending" v-if="pending">
    <font-awesome-icon icon="circle-notch" class="fa-7x" spin />
  </div>
  <div id="home" v-else>
    <router-link tag="div" :to="'new'" id="new-button" append>
      <h3>New Collection</h3>
    </router-link>
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
      },
      pending() {
        return this.$store.getters.collections ? false : true
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
  padding: 50px 10%;
  flex-grow: 1;
}

#pending {
  display: flex;
  width: 100%;
  justify-content: center;
  align-items: center;
}

h3 {
  line-height: 0px;
}

#new-button {
  padding: 10px 30px;
  border: solid 1px;
  border-color: gray;
  color: gray;
  border-radius: 10px;
  transition: all .2s ease-in-out;
  cursor: pointer;
  width: 145px;
}

#new-button:hover {
  border-color: white;
  color: white;
  background-color: gray;
}
</style>