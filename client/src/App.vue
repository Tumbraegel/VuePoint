<template>
  <b-container fluid id="app">
    <b-row>
        <navbar/>
    </b-row>
    <b-row>
        <router-view/>
    </b-row>
  </b-container>
</template>

<script>
import Navbar from './components/NavBar';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.container-fluid {
  padding: 0 !important;
}
</style>
