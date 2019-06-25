<template>
  <b-container id="home">
    <b-row class="justify-content-center">
      <add-task v-on:add-task="addTask"></add-task>
      <week-view :taskList="taskList" v-on:del-task="deleteTask"
      v-on:compl-task="markTaskAsDone" v-on:edit-task="editTask"></week-view>
    </b-row>

    <b-row>
      <b-col>
        <h3>Completed Tasks</h3>
        <completed-tasks :taskList="taskList" v-on:incompl-task="editTask">
        </completed-tasks>
      </b-col>
    </b-row>

    <b-row>
      <b-col>
        <h3>History</h3>
        <task-history :taskList="taskList"></task-history>
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import axios from 'axios';
import sweetalert from 'sweetalert';
import WeekView from './WeekView';
import CompletedTasks from './CompletedTasks';
import AddTask from './AddTask';
import TaskHistory from './TaskHistory';

export default {
  name: 'Home',
  components: {
    'completed-tasks': CompletedTasks,
    'week-view': WeekView,
    'add-task': AddTask,
    'task-history': TaskHistory,
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
          sweetalert('Done!', 'Task created!', 'success', { buttons: false, timer: 1500 });
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
          sweetalert('Done!', 'Task deleted!', 'success', { buttons: false, timer: 1500 });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getAllTasks();
        });
    },

    editTask(payload) {
      const id = payload.id;
      const pathDel = `http://localhost:5000/list/${id}`;
      axios.post(pathDel, payload)
        .then(() => {
          this.getAllTasks();
          sweetalert('Done!', 'Task updated!', 'success', { buttons: false, timer: 1500 });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getAllTasks();
        });
    },

    markTaskAsDone(id) {
      const path = `http://localhost:5000/list/${id}`;
      axios.put(path, id)
        .then(() => {
          this.getAllTasks();
          sweetalert('Done!', 'Task completed!', 'success', { buttons: false, timer: 1500 });
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getAllTasks();
        });
    },
  },

  created() {
    this.getAllTasks();
  },
};
</script>

<style scoped>
.row {
  margin: 2em 0;
}
</style>
