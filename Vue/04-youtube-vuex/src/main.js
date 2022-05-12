import Vue from 'vue'
import App from './App.vue'
import store from './store'

import _ from 'lodash'

Vue.config.productionTip = false

Vue.filter('strUnescape', rawText => _.unescape(rawText))

new Vue({
  store,
  render: h => h(App),
}).$mount('#app')
