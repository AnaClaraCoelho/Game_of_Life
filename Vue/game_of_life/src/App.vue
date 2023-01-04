<template>
  <div id="app">
    <GameLife></GameLife>
  </div>
</template>

<script>
import GameLife from './components/GameLife.vue'

export default {
  name: 'App',
  components: {
    GameLife
  }
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
</style>
