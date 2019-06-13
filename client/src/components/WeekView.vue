<template>
    <!-- Tasks table  -->
    <b-container fluid class="week-view">
      <b-row class="day-container">
        <b-col class="weekday" v-for="day in weekdays" :key="day">
          <div class="weekday-header">
            <h2>{{ day }}</h2>
          </div>

          <ul class="tasks">
            <li id="task" v-for="task in getAllTasksPer(day)" :key="task.id"
          @click="openEditModal()">
            <b-button class="close" aria-label="Close" v-on:click="deleteTask(task.id)">
              <span aria-hidden="true">&times;</span>
            </b-button>
            <h3>{{ task.title }}</h3>  
            <div class="descr">{{ task.taskDescription }}</div>
          </li>
          </ul>
        </b-col>
      </b-row>

      <b-row class="justify-content-center flag-btn">
         <b-button variant="outline-warning" size="sm" @click="setCategory('work')">
        Work
        </b-button>
        <b-button variant="outline-warning" size="sm" @click="setCategory('studies')">
          Studies
        </b-button>
        <b-button variant="outline-warning" size="sm" @click="setCategory('personal')">
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
  },

  deleteTask(id) {
    this.$emit('delete-task', this.id);
  },

  created() {
    this.getThisWeekDates();
  },
};
</script>

<style scoped>
.day-container, .flag-btn {
    margin-top: 1em;
  }

  .weekday {
    font-size: 0.9rem;
    background-color: seagreen;
    border-radius: 5px;
    margin: 5px;
    padding: 10px 5px;
    text-align: center;
    color: white;
  }

  .weekday-header {
    height: 30px;
  }

  h2 {
    font-size: 1.1rem;
  }
  
  .tasks {
    list-style: none;
    text-align: center;
    padding: 0px;
    margin: 20px 0 0;
    width: 100%;
  }

  #task:hover, task:focus, task:active{
  color: seagreen;
  cursor: pointer;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
  }

  #task {
    background-color: white;
    border-radius: 5px;
    margin: 8px 4px;
    font-size: 1em;
    color: black;
    word-wrap: break-word;
    position: relative;
    padding: 0.2em;
  }

  .close {
    font-size: 1.2em;
    padding: 1px 2px 2px; 
  }

  h3 {
    font-size: 1em;
    font-weight: 500;
    padding: 0.2em;
  }

  .descr {
    padding: 0.2em;
    margin: 0;
  }

  .flag-btn button {
    margin-right: 0.5em;
  }
</style>
