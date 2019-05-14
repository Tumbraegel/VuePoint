<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>VuePoint</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" @click="openAddModal()">
          Add Task
        </button>
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

        <div class="weekday-table">
          <li class="weekday" v-for="day in days" :key="day">
            <h2 class="weekday-header">{{ day }}</h2>
            <ul class="task">
              <li id="task" v-for="task in getTasks(day)" :key="task.id" @click="openEditModal()">
                <strong>{{ task.title }}</strong>
                <div>{{ task.description }}</div>
              </li>
            </ul>
          </li>
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
        <button type="button" class="btn btn-warning btn-sm">Update</button>
        <button type="button" class="btn btn-danger btn-sm">Delete</button>
      </div>
    </div>
  </div>
</template>

<style>
.weekday-table {
  display: table;
  width: 115%;
  table-layout: fixed;
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

.btn-success {
  background-color: seagreen;
}

.btn-success:hover {
  background-color:rgb(38, 115, 71);
}
</style>

<script>
import Modal from './Modal';

export default {
  data() {
    return {
      days: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Weekend'],
      tasks:
      [{
        id: '1',
        title: 'Office Party',
        date: 'Friday',
        description: 'Buy Cookies',
        importance: 'high',
      },
      {
        id: '2',
        title: 'Meeting',
        date: 'Tuesday',
        description: 'with Jacob from HR',
        importance: 'high',
      },
      {
        id: '3',
        title: 'Coffee Date',
        date: 'Weekend',
        description: '@Starbucks',
        importance: 'low',
      },
      {
        id: '4',
        title: 'Sprint 34 Deadline',
        date: 'Wednesday',
        description: 'To-Do: Tickets #73, #75, #79',
        importance: 'high',
      },
      {
        id: '5',
        title: 'Sprint Review',
        date: 'Wednesday',
        description: 'Having an existential crisis',
        important: 'high',
      }],
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
    getTasks(day) {
      return this.localTasks.filter(task => task.date === day);
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
};
</script>
