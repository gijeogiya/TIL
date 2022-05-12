<template>
  <div v-if="isSelectedVideo" class="video-detail">
    <div class="video-container">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>

    <div class="video-info">
      <h2>{{ selectedVideo.snippet.title | strUnescape }}</h2>
      <p>{{ selectedVideo.snippet.description | strUnescape }}</p>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapState } from 'vuex'

  export default {
    name: 'VideoDetail',
    computed: {
      ...mapState(['selectedVideo']),
      ...mapGetters(['isSelectedVideo', 'videoSrc']),
    },
  }
</script>

<style>
  .video-detail {
    width: 70%;
    padding-right: 1rem;
  }

  .video-container {
    position: relative;
    padding-top: 56.28%;
  }

  .video-container > iframe {
    position: absolute;
    top: 0;
    bottom: 0;
    width: 100%;
    height: 100%;
  }

  .video-info {
    margin-top: 20px;
    padding: 20px;
    border: solid 1px lightgray;
    border-radius: 10px;
  }
</style>
