<template>
  <div>
    <b-button variant="outline-success" size="sm" @click="openAddModal()">
      Add Task
    </b-button>
    <b-button variant="outline-warning" size="sm" @click="setWorkTaskboard('work')">
      Work
    </b-button>
    <b-button variant="outline-warning" size="sm" @click="setWorkTaskboard('personal')">
      Personal
    </b-button>
    <b-button v-if="!showAllTasks" variant="outline-warning" size="sm"
    @click="setWorkTaskboard('all')">
    All
    </b-button>
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
                <li id="task" v-for="task in getCorrectTaskboard(day)" :key="task.id"
                @click="openEditModal()">
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
        flag: 'work',
        importance: 'high',
        state: 'complete',
      },
      {
        id: '2',
        title: 'Ticket #25',
        date: 'Tuesday',
        description: 'Needs to be done ASAP',
        flag: 'work',
        importance: 'high',
        state: 'incomplete',
      },
      {
        id: '3',
        title: 'Grocery Shopping',
        date: 'Weekend',
        description: '@fancy supermarket',
        flag: 'personal',
        importance: 'low',
        state: 'incomplete',
      },
      {
        id: '4',
        title: 'Sprint 34 Deadline',
        date: 'Wednesday',
        description: 'To-Do: Tickets #73, #75, #79',
        flag: 'work',
        importance: 'high',
        state: 'incomplete',
      },
      {
        id: '5',
        title: 'Sprint Review',
        date: 'Wednesday',
        description: 'Having an existential crisis',
        flag: 'work',
        important: 'high',
        state: 'incomplete',
      }],
      showAddModal: false,
      showEditModal: false,
      showAllTasks: true,
      showWorkTasks: false,
      showPersonalTasks: false,
    };
  },

  components: {
    Modal,
  },

  computed: {
    allTasks() {
      return this.tasks;
    },
    workTasks() {
      return this.tasks.filter(task => task.flag === 'work');
    },
    personalTasks() {
      return this.tasks.filter(task => task.flag === 'personal');
    },
  },

  methods: {
    getAllTasks(day) {
      return this.allTasks.filter(task => task.date === day);
    },
    getWorkTasks(day) {
      return this.workTasks.filter(task => task.date === day);
    },
    getPersonalTasks(day) {
      return this.personalTasks.filter(task => task.date === day);
    },
    getCorrectTaskboard(day) {
      if (this.showWorkTasks) {
        return this.getWorkTasks(day);
      } else if (this.showPersonalTasks) {
        return this.getPersonalTasks(day);
      }
      return this.getAllTasks(day);
    },
    setWorkTaskboard(expr) {
      switch (expr) {
        case 'all': {
          this.showWorkTasks = false;
          this.showPersonalTasks = false;
          this.showAllTasks = true;
          break;
        }
        case 'work': {
          this.showWorkTasks = true;
          this.showPersonalTasks = false;
          this.showAllTasks = false;
          break;
        }
        case 'personal': {
          this.showWorkTasks = false;
          this.showPersonalTasks = true;
          this.showAllTasks = false;
          break;
        }
        default: {
          this.showWorkTasks = false;
          this.showPersonalTasks = false;
          this.showAllTasks = true;
          break;
        }
      }
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
