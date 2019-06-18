<template>
    <!-- Tasks table  -->
    <b-container fluid class="week-view">
      <b-row class="day-container">
        <b-col class="weekday" v-for="day in weekdays" :key="day">
          <div class="weekday-header">
            <h2>{{ day }}</h2>
          </div>

          <ul class="tasks">
            <li class="task" v-for="task in getCorrectTaskboard(day)" :key="task.id" v-on:click="showDetail(task.id)">
            <b-button class="close" aria-label="Close" v-on:click="$emit('del-task', task.id)">
              <span aria-hidden="true">&times;</span>
            </b-button>
            <h3>{{ task.title }}</h3>
            <div class="descr">{{ task.taskDescription }}</div>
            <input type="checkbox" name="complete_checkbox"
            v-on:change="$emit('compl-task', task.id)">
          </li>
          </ul>
        </b-col>
      </b-row>

      <!-- <b-modal v-model="showEdit" id="edit-modal" title="Edit Task" hide-footer>
        <b-form @submit="editTask">
          <label class="sr-only" for="form-input-title-edit">Title</label>
          <b-form-input id="form-input-title-edit"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Title" v-model="editTaskForm.title"
          ></b-form-input>

          <label class="sr-only" for="form-input-date-edit">Date</label>
          <b-input-group prepend="Due on:" class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-input id="form-input-date-edit" type="date" v-model="editTaskForm.dueDate">
          </b-input>
          </b-input-group>

          <label class="sr-only" for="form-input-decsription-edit">Description</label>
          <b-form-input id="form-input-description-edit"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Description" v-model="editTaskForm.taskDescription"
          ></b-form-input>

          <label class="sr-only" for="form-input-flag-edit">Flag: </label>
          <b-input-group prepend="Flag: " class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-form-select id="form-input-flag-edit" class="mb-2 mr-sm-2 mb-sm-0"
          :options = "flags" v-model="editTaskForm.flag">
          </b-form-select></b-input-group>

          <div class="modal-footer">
            <b-button variant="secondary" id="btn-cancel" v-on:click="hideModal">
            Cancel</b-button>
            <b-button type="submit" variant="primary" id="btn-save" @click="hideModal">
            Save</b-button>
          </div>
        </b-form>
      </b-modal> -->

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

export default {
  name: 'tasks',
  props: ['taskList'],
  data() {
    return {
      showModal: false,
      isEditing: false,
      weekdays: [],
      showAllTasks: true,
      showWorkTasks: false,
      showPersonalTasks: false,
      showStudyTasks: false,
    };
  },

  methods: {
    showDetail(id) {
      // some code
    },

   /*  hideModal() {
      this.showEdit = false;
    },

    editTask(evt) {
      evt.preventDefault();
      const payload = {
        title: this.editTaskForm.title,
        dueDate: this.editTaskForm.dueDate,
        taskDescription: this.editTaskForm.taskDescription,
        flag: this.editTaskForm.flag,
      };
      this.$emit('edit-task', payload, this.editTaskForm.id);
      this.initForm();
    },
 */
    getThisWeekDates() {
      for (let i = 1; i <= 7; i += 1) {
        this.weekdays.push(moment().day(i).format('YYYY-MM-DD'));
      }
      return this.weekdays;
    },

    getAllTasksPer(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.taskState === 0);
    },

    getWorkTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'work'
      && task.taskState === 0);
    },

    getStudyTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'studies'
      && task.taskState === 0);
    },

    getPersonalTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'personal'
      && task.taskState === 0);
    },

    getCorrectTaskboard(day) {
      if (this.showWorkTasks) {
        return this.getWorkTasks(day);
      } else if (this.showPersonalTasks) {
        return this.getPersonalTasks(day);
      } else if (this.showStudyTasks) {
        return this.getStudyTasks(day);
      }
      return this.getAllTasksPer(day);
    },

    setCategory(expr) {
      switch (expr) {
        case 'all': {
          this.showWorkTasks = false;
          this.showPersonalTasks = false;
          this.showStudyTasks = false;
          this.showAllTasks = true;
          break;
        }
        case 'work': {
          this.showWorkTasks = true;
          this.showPersonalTasks = false;
          this.showStudyTasks = false;
          this.showAllTasks = false;
          break;
        }
        case 'personal': {
          this.showWorkTasks = false;
          this.showPersonalTasks = true;
          this.showStudyTasks = false;
          this.showAllTasks = false;
          break;
        }
        case 'studies': {
          this.showWorkTasks = false;
          this.showPersonalTasks = false;
          this.showStudyTasks = true;
          this.showAllTasks = false;
          break;
        }
        default: {
          this.showWorkTasks = false;
          this.showPersonalTasks = false;
          this.showStudyTasks = false;
          this.showAllTasks = true;
          break;
        }
      }
    },
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

.task:hover, task:focus, task:active{
color: seagreen;
cursor: pointer;
box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

.task {
  background-color: white;
  border-radius: 5px;
  margin: 10px 5px;
  font-size: 1em;
  color: black;
  word-wrap: break-word;
  padding: 0.4em;
  position: relative;
}

.close {
  background-color: lightgray;
  width: 16px;
  height: 16px;
  font-size: 1rem;
  border-radius: 50%;
  color: white;
  top: -5px;
  right: -5px;
  opacity: 1;
  font-weight: 400;
  line-height: 0.5;
  padding-bottom: 5px;
  text-shadow: 1px 1px 2px grey; 
  position: absolute;
}

.checkbox {
  margin-left: 5px;
}


h3 {
  margin-top: 0.1em;
  font-size: 1em;
  font-weight: 500;
}

.descr {
  margin: 0
}

.flag-btn button {
  margin-right: 0.5em;
}
</style>
