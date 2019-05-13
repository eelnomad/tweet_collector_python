<template>
  <div id="create">
    Title: <input v-model="desc" type="text" placeholder="Default Value">
    Capture Groups: <input v-model="new_word" @keyup.enter="add_keyword()">
    <div id="word-list">
      <div class="word" v-for="(keyword, index) in keywords" :key="index">
        {{keyword}}
        <button @click="keywords.splice(index, 1)">X</button>
      </div>
    </div>
    <button @click="create_collection()" :disabled="keywords.length === 0">Create</button>
  </div>
</template>

<script>
export default {
  name: 'Create',
  data () {
    return {
      desc: '',
      new_word: '',
      invalid: false,
      keywords: []
    }
  },
  created () {
  },
  methods: {
    add_keyword: function () {
      var words = this.new_word.split(',')
      for (var i = 0; i < words.length; i++) {
        var normalized = words[i].toLowerCase().split(' ').filter((v, i, a) => a.indexOf(v) === i && v.length > 0).sort().join(' ')
        if (normalized.length === 0 || this.keywords.indexOf(normalized) > -1) {
          continue
        } else {
          this.keywords.push(normalized)
        }
      }
      this.new_word = ''
    },
    create_collection: function () {
      this.$store.dispatch("create_collection", {
        keywords: this.keywords,
        desc: this.desc.length > 0 ? this.desc : null
      }).then(response => {
        this.$router.push({ name: 'Details', params: { id: response.data.id }})
      })
    }
  },
  computed: {
  },
  watch: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#create {
  display: flex;
  flex-direction: column;
}
</style>
