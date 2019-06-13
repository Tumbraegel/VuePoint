<template>
<b-container class="row-margin" id="home">
    <b-row class="justify-content-center">
      <add-task v-on:add-task="addTask"></add-task>
      <week-view :taskList="taskList"></week-view>
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
import WeekView from './WeekView';
import CompletedTasks from './CompletedTasks';
import AddTask from './AddTask';

export default {
  name: 'Home',
  components: {
    'completed-tasks': CompletedTasks,
    'week-view': WeekView,
    'add-task': AddTask,
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

    addTask(payload) {
      const path = 'http://localhost:5000/list';
      axios.post(path, payload)
        .then(() => {
          this.getAllTasks();
          // this.show = false;
          // eslint-disable-next-line
        alert('New Task added');
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
