<template>
  <div>
    <b-button variant="outline-success" size="sm" @click="openAddModal()">Add Task</b-button>
    <b-button variant="outline-warning" size="sm">Work</b-button>
    <b-button variant="outline-warning" size="sm">Personal</b-button>
    <br><br>

        <!--ADD TASK MODAL-->
        <div id="wrapper" class="container">
          <modal v-if="showAddModal">
            <h3 slot="header" class="modal-title">Add Task</h3>
            <div slot="footer">
              <button type="button" class="btn btn-outline-info" @click="closeModal()">
                Close</button>
              <button type="button" class="btn btn-primary" data-dismiss="modal"
              @click="submitAndClose()">Submit</button>
            </div>
          </modal>
        </div>

        <div class="container weekday-table">
          <div class="row">
            <div class="col-sm weekday" v-for="day in days" :key="day">
              <h2 class="weekday-header">{{ day }}</h2>
              <ul class="task">
                <li id="task" v-for="task in getTasks()" :key="task.id" @click="openEditModal()">
                  <strong>{{ task.title }}</strong>
                  <div>{{ task.description }}</div>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!--EDIT TASK MODAL-->
        <div id="wrapper" class="container">
          <modal v-if="showEditModal">
            <h3 slot="header" class="modal-title">
              Edit Task #
            </h3>
            <div slot="footer">
              <button type="button" class="btn btn-outline-info" @click="closeModal()">
                Close</button>
              <button type="button" class="btn btn-primary" data-dismiss="modal"
              @click="submitAndClose()">Submit</button>
            </div>
          </modal>
        </div>

      <br>
      <b-button variant="outline-info" size="sm">Update</b-button>
      <b-button variant="outline-danger" size="sm">Delete</b-button>
    </div>
</template>

<script>
import axios from 'axios';
import Modal from './Modal';

export default {
  name: 'tasks',
  data() {
    return {
      days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Weekend'],
      tasks: '',
      showAddModal: false,
      showEditModal: false,
    };
  },

  components: {
    Modal,
  },

  computed: {
    localTasks() {
      return this.tasks;
    },
  },

  methods: {
    getAllTasks() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getTasks() {
      return this.tasks;
      // return this.localTasks.filter(task => task.date === day);
    },
    openAddModal() {
      this.showAddModal = true;
    },
    openEditModal() {
      this.showEditModal = true;
    },
    closeModal() {
      this.showEditModal = false;
      this.showAddModal = false;
    },
    submitAndClose() {
    // add stuff
    },
  },
  created() {
    this.getAllTasks();
    // eslint-disable-next-line
    console.log('created')
  },
};
</script>

<style>
.weekday-table {
  display: table;
  width: 100%;
  table-layout: fixed;
}

h2 {
  font-size: 3vh;
}

.weekday-header {
  color: seagreen;
}

.task {
  display: inline-block;
  font-size: 14px;
  list-style: none;
  text-align: center;
  padding: 0px;
  margin: 0px;
}

#task:hover, task:focus, task:active{
  background: rgb(51, 153, 95, 0.9);
  color: rgb(233, 233, 233);
  cursor: pointer;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

.weekday {
  font-size: 14px;
  display: table-cell;
  border: 1px solid seagreen;
  margin: 2px;
  padding: 5px;
  vertical-align: top;
  text-align: center;
  }
</style>
