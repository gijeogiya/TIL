<template>
  <div class="search-bar" :style="{ margin: isVideos ? '0' : '40vh 0' }">
    <input type="text" @keyup.enter="onEnter" placeholder="Search" autofocus />
  </div>
</template>

<script>
  export default {
    name: 'SearchBar',
    props: {
      isVideos: Boolean,
    },
    methods: {
      onEnter(event) {
        this.$emit('keyword-input', event.target.value)
      },
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
