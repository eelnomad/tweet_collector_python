<template>
  <div id="collection">
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>
<script>
  export default {
    name: 'Collection',
    data() {
      return {
      }
    },
    mounted() {
      this.$store.dispatch('load_collections')
    },
    created() {},
    methods: {
    },
    computed: {
    },
    watch: {}
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#collection {
  width: 100%;
  display: flex;
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