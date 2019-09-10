<template>
  <div id="collection-details">
    <div id="detail-header" :class="{'selected': selected}">
      <h3>{{collection.desc ? collection.desc : collection._id}}</h3>
      <transition name="fade">
        <div id="collection-actions" v-show="selected" @click="collection.active_flag ? stop_collection() : run_collection()" >
          <font-awesome-icon v-if="pending" icon="circle-notch" spin />
          <font-awesome-icon v-else-if="collection.active_flag" icon="stop"/>
          <font-awesome-icon v-else icon="play" />
        </div>
      </transition>
    </div>
    <div id="detail-body" v-show="selected">
      <li class="keyword" v-for="(keyword, index) in collection.keywords" :key="index">
        {{keyword}}
      </li>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'CollectionDetails',
    data() {
      return {
        pending: false
      }
    },
    props: ['collection', 'selected'],
    created() {},
    methods: {
      toggle: function () {
        this.active = !this.active
      },
      run_collection: function() {
        this.pending = true
        this.$store.dispatch("run_collection", {
          id: this.collection._id
        }).then(() => {
          setTimeout(function () {
            this.pending = false
          }, 1000)
        })
      },
      stop_collection: function() {
        this.pending = true
        this.$store.dispatch("stop_collection")
        .then(() => {
          setTimeout(function () {
            this.pending = false
          }, 1000)
        })
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
  padding: 0 30px;
  background-color: whitesmoke;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: all .5s ease;
}

#detail-header:hover, #detail-header.selected:hover {
  background-color: lightgray;
}

#detail-header.selected {
  background-color: #e8e8e8;
}

#detail-body {
  background-color: transparent;
  display: flex;
  flex-wrap: wrap;
  padding: 10px 15px;
  border-width: 1px;
  border-color: #e8e8e8;
  border-style: solid;
}

.keyword {
  flex: 0 1 auto;
  list-style: none;
  border-radius: 10px;
  margin: 10px 5px;
  padding: 10px 15px;
  background-color: whitesmoke;
  transition: all .5s ease;
}

.keyword:hover {
  background-color: lightgray;
}

.fade-enter-active {
  transition: opacity 0s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

#collection-actions {
  padding: 10px 30px;
  border: solid 1px;
  border-color: white;
  border-radius: 10px;
  /*filter: brightness(1);*/
  color: white;
  transition: all .2s ease-in-out;
  cursor: pointer;
  width: 14px;
}

#collection-actions:hover {
  /*filter: brightness(.5);*/
  background-color: gray;
  border-color: gray;
  color: whitesmoke;
}
</style>