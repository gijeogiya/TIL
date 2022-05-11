<template>
  <div>
    <h1>Pick Lunch</h1>
    <div>
      <h2>{{ menu }}</h2>
      <button @click="pickMenu">점심 뽑기</button>
    </div>
    <div>
      <h2>Lotto 뽑기 고고(6)</h2>
      <button @click="moveToLotto">GOGO</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data() {
    return {
      menus: ['부대찌개', '잡채', '풀떼기', '밥',],
      menu: ''
    }
  },
  methods: {
    pickMenu() { this.menu = _.sample(this.menus) },
    moveToLotto() { 
      this.$router.push({
        name: 'lotto',
        params: { count: 6 } 
      }) 
    },
  },
  created() {
    this.pickMenu()
  }
}
</script>

<style>

</style>
