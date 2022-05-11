<template>
  <div id="app" class="border-box-blue">
    <h1>App</h1>
    <input type="text" v-model="appInput" />

    <p>From Parent => {{ parentInput }}</p>
    <p>From Child => {{ childInput }}</p>
    <!-- 3. print -->
    <the-parent
      :app-input="appInput"
      @parent-input-change="onParentInputChange"
      @child-input-change="onChildInputChange"
    ></the-parent>
  </div>
</template>

<script>
  // 1. import
  import TheParent from './components/TheParent.vue'

  export default {
    name: 'App',
    // 2. register
    components: {
      // template에서 사용할 이름 : 컴포넌트 이름
      TheParent: TheParent,
    },
    data() {
      return {
        appInput: '',
        parentInput: '',
        childInput: '',
      }
    },
    methods: {
      onParentInputChange(parentInput) {
        this.parentInput = parentInput
      },
      onChildInputChange(childInput) {
        this.childInput = childInput
      },
    },
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  .border-box-blue {
    border: 3px solid blue;
    margin: 5px;
  }
</style>
