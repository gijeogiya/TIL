<template>
  <div class="border-box-green">
    <h2>The Child</h2>
    <input type="text" v-model="childInput" @input="onInput" />
    <p>From App => {{ appInput }}</p>
    <p>From Parent => {{ parentInput }}</p>
  </div>
</template>

<script>
  export default {
    name: 'TheChild',
    props: {
      appInput: String,
      parentInput: String,
    },
    data() {
      return {
        childInput: '',
      }
    },
    methods: {
      onInput() {
        this.$emit('child-input-change', this.childInput)
      },
    },
  }
</script>

<style>
  .border-box-green {
    border: 3px solid green;
    margin: 5px;
  }
</style>
