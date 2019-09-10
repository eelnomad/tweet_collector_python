<template>
    <div id="create">
        <h1>Title:</h1>
        <input v-model="desc" type="text" placeholder="Default: <Collection ID>">
        <h2>Capture Groups:</h2>
        <input v-model="new_word" @keyup.enter="add_keyword()">
        <div id="word-list">
            <div class="word" v-for="(keyword, index) in keywords" :key="index" @click="keywords.splice(index, 1)">
                <font-awesome-icon style="margin: 0 5px 0 0;" icon="times" />
                {{keyword}}
            </div>
        </div>
        <button id="new-collection" @click="create_collection()" :disabled="keywords.length === 0">Create Collection</button>
    </div>
</template>
<script>
export default {
    name: 'Create',
    data() {
        return {
            desc: '',
            new_word: '',
            invalid: false,
            keywords: []
        }
    },
    created() {},
    methods: {
        add_keyword: function() {
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
        create_collection: function() {
            this.$store.dispatch("create_collection", {
                keywords: this.keywords,
                desc: this.desc.length > 0 ? this.desc : null
            }).then(response => {
                this.$router.push({ name: 'Collections', params: { id: response.data.id } })
            })
        }
    },
    computed: {},
    watch: {}
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#create {
    flex-grow: 1;
    padding: 5% 10%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

input {
    border-radius: 5px;
    line-height: 20px;
    padding: 10px 15px;
    border: solid 1px;
    border-color: gray;
}

#word-list {
  flex: 1 1 auto;
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
}

.word {
    display: flex;
    height: 20px;
    align-items: center;
    list-style: none;
    border-radius: 10px;
    margin: 20px 10px 0 0;
    padding: 10px 15px;
    background-color: whitesmoke;
    color: gray;
    transition: all .2s ease;
    border: 1px solid gray;
    cursor: pointer;
}

.word:hover {
    background-color: gray;
    color: whitesmoke;
}

#new-collection {
    padding: 10px 30px;
    border: solid 1px;
    border-color: gray;
    color: gray;
    border-radius: 10px;
    transition: all .2s ease-in-out;
    cursor: pointer;
    width: 100%;
}

#new-collection:enabled {
    background-color: white;
}

#new-collection:hover:enabled {
    border-color: white;
    color: white;
    background-color: gray;
}
</style>