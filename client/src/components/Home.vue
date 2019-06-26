<template>
  <b-container id="home">
    <b-row class="justify-content-center">
      <add-task v-on:add-task="addTask"></add-task>
      <week-view :taskList="taskList" v-on:del-task="deleteTask"
      v-on:compl-task="markTaskAsDone" v-on:edit-task="editTask"></week-view>
    </b-row>

    <b-row class="justify-content-center">
      <b-col>
      <div role="tablist">
        <b-card no-body class="mb-1">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button class="acc-btn" block href="#" v-b-toggle.accordion-1
            variant="light">
              Completed Tasks
            </b-button>
          </b-card-header>
          <b-collapse id="accordion-1" accordion="my-accordion" role="tabpanel">
            <b-card-body>
              <b-card-text>
                <completed-tasks :taskList="taskList" v-on:incompl-task="editTask">
                </completed-tasks>
              </b-card-text>
            </b-card-body>
          </b-collapse>
        </b-card>

        <b-card no-body class="mb-1">
          <b-card-header header-tag="header" class="p-1" role="tab">
            <b-button class="acc-btn" block href="#" v-b-toggle.accordion-2
            variant="light">
              History of all Tasks
            </b-button>
          </b-card-header>
          <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
            <b-card-body>
              <task-history :taskList="taskList"></task-history>
            </b-card-body>
          </b-collapse>
        </b-card>
      </div>
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
.acc-btn, .acc-btn:active, acc-btn:focus {
  outline: none !important;
  box-shadow: none;
}

.p-1 {
    background-color: transparent;
    letter-spacing: 1px;
}

.row {
  margin: 2em 0;
}
</style>
