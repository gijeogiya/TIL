import Vue from 'vue'
import Vuex from 'vuex'

import _ from 'lodash'
import axios from 'axios'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

Vue.use(Vuex)

// 1. keyword 입력 => 2. AJAX 검색 => 3. videos 세팅 => 4. 클릭 => 5. selectedVideo
export default new Vuex.Store({
  state: {
    keyword: '',
    videos: [],
    selectedVideo: {},
  },
  getters: {
    isVideos: state => !!state.videos.length,
    isSelectedVideo: state => !_.isEmpty(state.selectedVideo),
    videoSrc: state => {
      const videoId = state.selectedVideo.id?.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
  mutations: {
    SET_KEYWORD: (state, keyword) => (state.keyword = keyword),
    SET_VIDEOS: (state, videos) => (state.videos = videos),
    SET_SELECTED_VIDEO: (state, video) => (state.selectedVideo = video),
  },
  actions: {
    setKeywordAndFetchVideos({ commit, dispatch }, keyword) {
      commit('SET_KEYWORD', keyword)
      dispatch('fetchVideos')
    },

    fetchVideos({ state, commit }) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: state.keyword,
      }

      axios
        .get(API_URL, { params: params })
        .then(res => commit('SET_VIDEOS', res.data.items))
        .catch(err => console.error(err))
    },

    setSelectedVideo({ commit }, video) {
      commit('SET_SELECTED_VIDEO', video)
    },
  },
})
