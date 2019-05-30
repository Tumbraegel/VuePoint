<template>
  <div>
    <b-button variant="outline-primary" size="sm" v-b-modal.addNew>
      Add New
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

    <!-- Tasks table  -->
    <b-container fluid class="weekday-table">
      <b-row>
        <b-col size="sm" class="weekday" v-for="day in days" :key="day">
          <h2 class="weekday-header">{{ day }}</h2>
          <ul class="task">
            <li id="task" v-for="task in getCorrectTaskboard(day)" :key="task.id"
            @click="openEditModal()">
              <strong>{{ task.title }}</strong>
              <div>{{ task.taskDescription }}</div>
            </li>
          </ul>
        </b-col>
      </b-row>
    </b-container>

        <!--ADD TASK MODAL-->
        <b-modal id="addNew" centered scrollable hide-footer title="Add New Task">
          <div id="form-add">
            <b-form @submit="onsubmit" @onreset="onReset">
              <b-form-group id="form-title" label="Task Title:">
                <b-form-input id="form-title_input" v-model="text" placeholder="Enter task title">
                </b-form-input>
              </b-form-group>
              <b-form-group id="form-date" label="Due Date">
                <b-form-input id="form-date_input" v-model="date" placeholder="Enter task due date">
                </b-form-input>
              </b-form-group>
              <b-form-group id="form-descr" label="Description:">
                <b-form-input id="form-desc_input" v-model="text" placeholder="Enter description">
                </b-form-input>
              </b-form-group>
              <b-form-group id="form-flag" label="Flag:">
                <b-form-input id="form-flag_input" v-model="text" placeholder="Choose a flag">
                </b-form-input>
              </b-form-group>
            </b-form>
          </div>
          <div id="btn">
            <b-button id="btn-cancel" @click="$bvModal.hide('addNew')">Cancel</b-button>
            <b-button variant="success" id="btn-create">Create</b-button>
          </div>
        </b-modal>

        <!--EDIT TASK MODAL-->
        <b-container id="wrapper">
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
        </b-container>

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
            <em v-b-popover.hover.right="task.taskDescription" title="Details">{{task.title}}</em>
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
      addTaskForm: {
        title: '',
        taskDescription: '',
      },
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
      const path = 'http://localhost:5000/list';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
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

    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.taskDescription = '';
    },

    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      let read = false;
      if (this.addTaskForm.read[0]) read = true;
      const payload = {
        title: this.addTaskForm.title,
        taskDescription: this.addTaskForm.taskDescription,
        read, // property shorthand
      };
      this.addTask(payload);
      this.initForm();
    },

    onReset(evt) {
      evt.preventDefault();
      this.$refs.addTaskModal.hide();
      this.initForm();
    },

    getAllTasksPer(day) {
      // jb: I just print the days to get rid of the linter warning of an unused variable
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

h2 {
  font-size: 1.5rem;;
}

.task {
  list-style: none;
  text-align: center;
  padding: 0px;
  margin: 0px;
  width: 100%;
}

#task:hover, task:focus, task:active{
  color: seagreen;
  cursor: pointer;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

.weekday {
  font-size: 0.9rem;
  background-color: seagreen;
  border-radius: 5px;
  margin: 5px;
  padding: 10px 5px;
  text-align: center;
  color: white;
  box-shadow: 0 0 3px rgba(0, 0, 0, 0.6);
  }

.task li {
    background-color: white;
    border-radius: 5px;
    margin: 5px;
    color: black;
    padding: 5%;
  }
</style>

<style scoped>
#btn {
  float: right;
}

</style>
