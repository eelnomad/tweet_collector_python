<template>
  <div id="collection">
    <router-view></router-view>
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
}
</style>