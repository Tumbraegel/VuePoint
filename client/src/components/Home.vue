<template>
  <b-container id="home">
    <b-row class="justify-content-center">
      <add-task v-on:add-task="addTask"></add-task>
      <week-view :taskList="taskList" v-on:del-task="deleteTask"></week-view>
    </b-row>

    <b-row>
      <b-col>
        <p>SECTION FOR COMPLETED TASKS</p>
        <completed-tasks :taskList="taskList"></completed-tasks>
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

    deleteTask(id) {
      const path = `http://localhost:5000/list/${id}`;
      axios.delete(path, id)
        .then(() => {
          this.getAllTasks();
          // eslint-disable-next-line
          alert('Task was deleted');
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          // eslint-disable-next-line
          alert('NOPE');
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
.row {
  margin: 2em 0;
}
</style>
