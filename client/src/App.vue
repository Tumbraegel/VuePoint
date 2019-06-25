<template>
  <b-container fluid id="app">
    <b-row>
      <b-col>
        <navbar/>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <router-view/>
      </b-col>
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
#app {
  width: 100vw;
}

* {
  box-sizing: border-box;
}

.container-fluid {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

</style>
