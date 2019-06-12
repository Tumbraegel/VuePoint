<template>
  <b-container fluid id="home">
    <b-row>
      <task-list></task-list>
    </b-row>

    <b-row>
      <p>Completed Taks</p>
      <completed-tasks></completed-tasks>
    </b-row>
  </b-container>
</template>

<script>
import TaskList from './TaskList.vue';
import CompletedTasks from './CompletedTasks.vue';

export default {
  name: 'Home',
  components: {
    'completed-tasks': CompletedTasks,
    'task-list': TaskList,
  }
};
</script>

<style scoped>
  #home {
    margin: 0 50px 0 ;
  }

  .row {
    margin: 2em 0;
  }
</style>
