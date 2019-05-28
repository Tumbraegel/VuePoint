<template>
  <div>
    <b-button variant="outline-success" size="sm" @click="openAddModal()">
      Add Task
    </b-button>
    <b-button variant="outline-warning" size="sm" @click="setCategory('work')">
      Work
    </b-button>
    <b-button variant="outline-warning" size="sm" @click="setCategory('personal')">
      Personal
    </b-button>
    <b-button v-if="!showAllTasks" variant="outline-warning" size="sm"
    @click="setCategory('all')">
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
      <br><br>
      <div>
        <h2>COMPLETED TASKS</h2> <hr>
      </div><!--
      <b-list-group v-for="task in completedTasks" :key="task.id">
        <div class="text-left">
          <b-list-group-item variant="secondary">Task:
            <em v-b-popover.hover.right="task.description" title="Details">{{task.title}}</em>
            </b-list-group-item>
        </div>
      </b-list-group> -->
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
      showAllTasks: true,
      showWorkTasks: false,
      showPersonalTasks: false,
      showingCompleted: false,
      done: 1,
    };
  },

  components: {
    Modal,
  },

  computed: {
    allTasks() {
      return this.tasks;
    },
    // workTasks() {
    //   return this.tasks.filter(task => task.flag === 'work');
    // },
    // personalTasks() {
    //   return this.tasks.filter(task => task.flag === 'personal');
    // },
    // completedTasks() {
    //   return this.tasks.filter(task => task.state === this.done);
    // },
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
    getAllTasksPer(day) {
      // eslint-disable-next-line
      console.log(this.tasks)
      // eslint-disable-next-line
      console.log(day);
      return this.allTasks;
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
      return this.getAllTasksPer(day);
    },
    setCategory(expr) {
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
