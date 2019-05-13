<template>
  <div id="details" v-if="record">
    <h1>{{record.desc ? record.desc : record._id}}</h1>
    <h2>{{record.active_flag}}</h2>
    <h3>{{record.keywords}}</h3>
    <div id="controls">
      <button @click="run_collection()" v-show="!record.active_flag">RUN ME</button>
      <button @click="stop_collection()" v-show="record.active_flag">STOP ME</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Details',
  data () {
    return {
    }
  },
  created () {
  },
  methods: {
    run_collection: function () {
      this.$store.dispatch("run_collection", {
        id: this.$route.params.id
      }).then(response => {
      })
    },
    stop_collection: function () {
      this.$store.dispatch("stop_collection")
      .then(response => {
      })
    }
  },
  computed: {
    record () {
      return this.$store.getters.collections.find(v => v._id === this.$route.params.id)
    }
  },
  watch: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#details {
}

#controls {
  margin: 0 10vw 10vh 0;
  position: fixed;
  right: 0;
  bottom: 0;
}
</style>
