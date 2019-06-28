<template>
  <div id="collection-details">
    <div id="detail-header">
      <h3>{{collection.desc ? collection.desc : collection._id}}</h3>
    </div>
    <transition name="fade">
      <div id="detail-body" v-show="selected">
        <h4>{{collection.active_flag}}</h4>
        <h5>{{collection.keywords}}</h5>
      </div>
    </transition>
  </div>
</template>
<script>
  export default {
    name: 'CollectionDetails',
    data() {
      return {
      }
    },
    props: ['collection', 'selected'],
    created() {},
    methods: {
      toggle: function () {
        this.active = !this.active
      },
      run_collection: function() {
        this.$store.dispatch("run_collection", {
          id: this.$route.params.id
        }).then()
      },
      stop_collection: function() {
        this.$store.dispatch("stop_collection")
        .then()
      }
    },
    computed: {
      record() {
        return this.$store.getters.collections.find(v => v._id === this.$route.params.id)
      }
    },
    watch: {}
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#collection-details {
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease-in-out;
}

#detail-header {
  background-color: whitesmoke;
}

#detail-body {
  background-color: transparent;
}

#controls {
  margin: 0 10vw 10vh 0;
  position: fixed;
  right: 0;
  bottom: 0;
}
.fade-enter-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>