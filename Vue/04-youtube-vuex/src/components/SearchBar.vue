<template>
  <div class="search-bar" :style="{ margin: isVideos ? '0' : '40vh 0' }">
    <input
      v-model="inputKeyword"
      @keydown.enter="setKeywordAndFetchVideos(inputKeyword)"
      type="text"
      placeholder="Search"
      autofocus
    />
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'SearchBar',
    data() {
      return {
        inputKeyword: '',
      }
    },
    methods: {
      // 1. 사용자가 입력한 내용을 (v-model="inputKeyword")
      // 2. Enter 입력했을 때, (@keydown.enter=)
      // 3. action을 통해 넘긴다 ("setKeywordAndFetchVideos(inputKeyword)")
      ...mapActions(['setKeywordAndFetchVideos']),
    },
    computed: {
      ...mapGetters(['isVideos']),
    },
  }
</script>

<style>
  .search-bar > input {
    width: 100%;
    padding: 0.5rem;
    font-size: 2rem;
  }
  .search-bar {
    transition: margin 0.5s;
  }
</style>
