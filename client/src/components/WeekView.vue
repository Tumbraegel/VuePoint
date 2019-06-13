<template>
    <!-- Tasks table  -->
    <b-container fluid class="weekday-table">
      <b-row class="day-container">
        <b-col size="md" class="weekday" v-for="day in weekdays" :key="day">
          <div class="weekday-header">
            <h2>{{ day }}</h2>
          </div>

          <ul class="tasks">
            <li id="task" v-for="task in getCorrectTaskboard(day)" :key="task.id"
            @click="openEditModal()">
              <strong>{{ task.title }}</strong>
              <div>{{ task.taskDescription }}</div>
            </li>
          </ul>
        </b-col>
      </b-row>

      <b-row class="justify-content-center">
         <b-button variant="outline-warning" size="sm" @click="setCategory('work')">
        Work
        </b-button>
        <b-button variant="outline-warning" size="sm" @click="setCategory('studies')">
          Personal
        </b-button>
        <b-button v-if="!showAllTasks" variant="outline-warning" size="sm"
        @click="setCategory('all')">
        All
        </b-button>
      </b-row>
    </b-container>
</template>

<script>
import moment from 'moment';
import Modal from './Modal';

export default {
  name: 'tasks',
  props: ['taskList'],
  data() {
    return {
      weekdays: [],
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

  methods: {
    getThisWeekDates() {
      for (let i = 1; i <= 7; i += 1) {
        this.weekdays.push(moment().day(i).format('ddd, DD MMM'));
      }
      return this.weekdays;
    },

    getAllTasksPer(day) {
      return this.taskList.filter(task => task.dueDate.includes(day));
    },

    getWorkTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'work');
    },

    getPersonalTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'studies');
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
        case 'studies': {
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
    this.getThisWeekDates();
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
