<template>
  <li class="list-group-item" @click="setSelectedVideo(video)">
    <img :src="videoImgSrc" :alt="video.title" />
    {{ video.snippet.title | strUnescape }}
  </li>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'VideoListItem',
    props: {
      video: Object,
    },
    methods: {
      ...mapActions(['setSelectedVideo']),
    },
    computed: {
      videoImgSrc() {
        return this.video.snippet.thumbnails.default.url
      },
    },
  }
</script>

<style>
  .list-group-item {
    display: flex;
    margin-bottom: 1rem;
    cursor: pointer;
  }
  .list-group-item:hover {
    background-color: #eee;
  }
  .list-group-item img {
    height: fit-content;
    margin-right: 0.5rem;
  }
</style>
