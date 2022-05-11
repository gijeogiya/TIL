<template>
  <div>
    <h1>Pick {{ count }} Lotto</h1>
    <div>
      <h2>{{ luckyNumbers }}</h2>
      <button @click="pickLotto">뽑기!</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data() {
    return {
      count: this.$route.params.count,
      luckyNumbers: []
    }
  },
  methods: {
    pickLotto() {
      const numbers = _.range(1, 46)
      this.luckyNumbers = _.sampleSize(numbers, this.count)
    },
  },
  created() {
    this.pickLotto()
  }
}
</script>

<style>

</style>
