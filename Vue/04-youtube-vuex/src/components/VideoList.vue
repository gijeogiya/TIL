<template>
  <div class="col">
    <ul class="list-group">
      <video-list-item
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
      >
      </video-list-item>
    </ul>
  </div>
</template>

<script>
  import VideoListItem from '@/components/VideoListItem.vue'

  import { mapState } from 'vuex'

  export default {
    name: 'VideoList',
    components: { VideoListItem },
    computed: {
      ...mapState(['videos']),
    },
  }
</script>

<style></style>
