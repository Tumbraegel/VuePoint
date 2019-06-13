<template>
<b-container class="row-margin" id="home">
    <b-row>
      <b-col>
        <task-list :taskList="taskList" :addTask="addTask"></task-list>
      </b-col>
    </b-row>

    <b-row class="row-margin">
      <b-col>
        <p>SECTION FOR COMPLETED TASKS</p>
        <completed-tasks :taskList="taskList"></completed-tasks>
      </b-col>
    </b-row>

    <b-row class="row-margin" align-v="end">
      <b-col>
        <p>FOOTER SECTION</p>
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import axios from 'axios';
import TaskList from './TaskList';
import CompletedTasks from './CompletedTasks';

export default {
  name: 'Home',
  components: {
    'completed-tasks': CompletedTasks,
    'task-list': TaskList,
  },
  data() {
    return {
      taskList: [],
    };
  },
  methods: {
    getAllTasks() {
      const path = 'http://localhost:5000/list';
      axios.get(path)
        .then((res) => {
          this.taskList = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    // adapted from https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ up to onReset() method
    addTask(payload) {
      const path = 'http://localhost:5000/list';
      axios.post(path, payload)
        .then(() => {
          this.getAllTasks();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getAllTasks();
        });
    },
  },
  created() {
    this.getAllTasks();
    // eslint-disable-next-line
    console.log('created')
  },
};
</script>

<style scoped>
.row-margin {
  margin-top: 3em;
}
</style>
