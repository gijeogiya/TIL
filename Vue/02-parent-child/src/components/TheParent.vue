<template>
  <div class="border-box-red">
    <h2>The Parent</h2>
    <input type="text" v-model="parentInput" @input="onInput" />

    <p>From App => {{ appInput }}</p>
    <p>From Child => {{ childInput }}</p>

    <the-child
      :app-input="appInput"
      :parent-input="parentInput"
      @child-input-change="onChildInputChange"
    ></the-child>
  </div>
</template>

<script>
  import TheChild from '@/components/TheChild.vue'

  export default {
    name: 'TheParent',
    components: {
      TheChild,
    },
    props: {
      appInput: String,
    },

    data() {
      return {
        parentInput: '',
        childInput: '',
      }
    },

    methods: {
      onInput() {
        this.$emit('parent-input-change', this.parentInput)
      },
      onChildInputChange(childInput) {
        this.childInput = childInput
        this.$emit('child-input-change', this.childInput)
      },
    },

    // watch: {
    //   parentInput() {
    //     this.$emit('parent-input-change', this.parentInput)
    //   },
    // },
  }
</script>

<style scoped>
  /* scoped => 해당 컴포넌트에만 스타일 적용됨  */
  div.border-box-red {
    border: 3px solid red;
    margin: 5px;
  }
</style>
