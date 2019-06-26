<template>
    <!-- Tasks table  -->
    <b-container fluid>

      <b-row class="justify-content-center flag-btn">
      <b-button @click="toggleWeek('last', $event)" variant="outline-secondary" size="sm"
      >&laquo; Last</b-button>
      <b-button @click="toggleWeek('current')" variant="outline-secondary" size="sm">
        Current Week</b-button>
      <b-button @click="toggleWeek('next', $event)" variant="outline-secondary" size="sm"
      >Next &raquo;</b-button>
      </b-row>

      <b-row class="day-container">
        <b-col class="weekday" v-for="day in weekdays" :key="day">
          <div class="weekday-header">
            <h2>{{ day }}</h2>
          </div>
          <ul class="tasks">
            <li class="task" v-for="task in getCorrectTaskboard(day)" :key="task.id">
              <b-button class="close" aria-label="Close" v-on:click="$emit('del-task', task.id)">
                <span aria-hidden="true">&times;</span>
              </b-button>
              <h3 v-on:click="showDetail(task)">{{ task.title }}</h3>
              <div class="descr" v-on:click="showDetail(task)">
                {{ task.taskDescription }}
              </div>
              <div class="flag">
                {{ task.flag }}
              </div>
              <input type="checkbox" name="complete_checkbox"
              v-on:change="markDone(task.id)" class="weekview_checkbox">
            </li>
          </ul>
        </b-col>
      </b-row>

      <b-modal v-model="showDetailModal" hide-footer>
        <div class="modal-body">
          <h4>{{ taskDetail.title }}</h4>
          <p>Due on {{ taskDetail.dueDate }}
            <b-button class="flag" variant="outline-warning"
            size="sm">{{ taskDetail.flag }}</b-button>
          </p>
          <h5>Description:</h5><p>{{ taskDetail.taskDescription }}</p>
          <p>Done? <input type="checkbox" name="complete_checkbox"
          v-on:change="markDone(taskDetail.id)"></p>
        </div>
        <div class="modal-footer">
          <b-button variant="danger" id="btn-edit"
          v-on:click="openEditModal(taskDetail)">Edit</b-button>
          <b-button variant="secondary" id="btn-cancel"
          v-on:click="showDetailModal = !showDetailModal">
          Cancel</b-button>
        </div>
      </b-modal>

      <b-modal v-model="showEditModal" title="Edit Task" hide-footer>
        <b-form @submit="onSubmit">
          <label class="sr-only" for="form-edit-title">Title</label>
          <b-form-input v-bind:class="{ 'warning': isEmpty }" id="form-edit-title"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Title" v-model="editTaskForm.title"
          ></b-form-input>
          <p class="error" v-if="error">{{ error }}</p>

          <label class="sr-only" for="form-edit-date">Date</label>
          <b-input-group prepend="Due on:" class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-input id="form-edit-date" type="date" v-model="editTaskForm.dueDate">
          </b-input>
          </b-input-group>

          <label class="sr-only" for="form-edit-decsription">Description</label>
          <b-form-input id="form-edit-description"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Description" v-model="editTaskForm.taskDescription"
          ></b-form-input>

          <label class="sr-only" for="form-edit-flag">Flag: </label>
          <b-input-group prepend="Flag: " class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-form-select id="form-edit-flag" class="mb-2 mr-sm-2 mb-sm-0"
          :options = "flags" v-model="editTaskForm.flag">
          </b-form-select></b-input-group>
          <div class="modal-footer">
            <b-button variant="success" type="submit" id="btn-edit"
            v-on:click="showEditModal = !showEditModal">Save</b-button>
            <b-button variant="secondary" id="btn-cancel"
            v-on:click="showEditModal = !showEditModal">Cancel</b-button>
          </div>
        </b-form>
      </b-modal>

      <b-row class="justify-content-center flag-btn">
         <b-button class="flag"
         :class="{ active: showWorkTasks }"
         @click="setCategory('work')">Work</b-button>
        <b-button class="flag"
        :class="{ active: showStudyTasks }"
        @click="setCategory('studies')">Studies</b-button>
        <b-button class="flag"
        :class="{ active: showPersonalTasks }"
        @click="setCategory('personal')">Personal</b-button>
        <b-button v-if="!showAllTasks" class="flag"
        :class="{ active: showAllTasks }"
        @click="setCategory('all')">All</b-button>
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
      showDetailModal: false,
      showEditModal: false,
      weekdays: [],
      nextWeek: false,
      lastWeek: false,
      enableDisable: false,
      showAllTasks: true,
      showWorkTasks: false,
      showPersonalTasks: false,
      showStudyTasks: false,
      taskDetail: {
        id: '',
        title: '',
        dueDate: '',
        taskDescription: '',
        flag: '',
      },
      editTaskForm: {
        id: '',
        title: '',
        dueDate: '',
        taskDescription: '',
        flag: '',
      },
      flags: [
        { value: 'Work', text: 'Work' },
        { value: 'Personal', text: 'Personal' },
        { value: 'Studies', text: 'Studies' },
      ],
      error: '',
      isEmpty: false,
      allActive: false,
      workActive: false,
      studiesActive: false,
      personalActive: false,
    };
  },

  methods: {
    showDetail(task) {
      this.showDetailModal = true;
      this.taskDetail.id = task.id;
      this.taskDetail.title = task.title;
      this.taskDetail.dueDate = task.dueDate;
      this.taskDetail.taskDescription = task.taskDescription;
      this.taskDetail.flag = task.flag;
    },

    markDone(id) {
      this.$emit('compl-task', id);
      this.showDetailModal = false;
    },

    openEditModal(taskDetail) {
      this.showDetailModal = false;
      this.showEditModal = true;
      this.editTaskForm.id = taskDetail.id;
      this.editTaskForm.title = taskDetail.title;
      this.editTaskForm.dueDate = taskDetail.dueDate;
      this.editTaskForm.taskDescription = taskDetail.taskDescription;
      this.editTaskForm.flag = taskDetail.flag;
    },

    onSubmit(evt) {
      evt.preventDefault();
      if (this.editTaskForm.title === '') {
        this.error = 'Please enter a title';
        this.isEmpty = true;
      } else {
        const payload = {
          id: this.editTaskForm.id,
          title: this.editTaskForm.title,
          taskDescription: this.editTaskForm.taskDescription,
          dueDate: this.editTaskForm.dueDate,
          flag: this.editTaskForm.flag,
        };
        this.$emit('edit-task', payload);
        this.error = '';
        this.showEditModal = false;
      }
    },

    toggleWeek(week) {
      if (week === 'next') {
        this.nextWeek = true;
        this.lastWeek = false;
      } else if (week === 'last') {
        this.lastWeek = true;
        this.nextWeek = false;
      } else if (week === 'current') {
        this.lastWeek = false;
        this.nextWeek = false;
      }
      return this.getThisWeekDates();
    },

    clearArray() {
      for (let i = this.weekdays.length; i > 0; i -= 1) {
        this.weekdays.pop();
      }
    },

    getThisWeekDates() {
      this.clearArray();
      if (this.nextWeek) {
        for (let i = 1; i <= 7; i += 1) {
          this.weekdays.push(moment().add(1, 'week').day(i).format('YYYY-MM-DD'));
        }
      } else if (this.lastWeek) {
        for (let i = 1; i <= 7; i += 1) {
          this.weekdays.push(moment().subtract(1, 'week').day(i).format('YYYY-MM-DD'));
        }
      } else {
        for (let i = 1; i <= 7; i += 1) {
          this.weekdays.push(moment().day(i).format('YYYY-MM-DD'));
        }
      }
      return this.weekdays;
    },

    getAllTasksPer(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.taskState === 0);
    },

    getWorkTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'Work'
      && task.taskState === 0);
    },

    getStudyTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'Studies'
      && task.taskState === 0);
    },

    getPersonalTasks(day) {
      return this.taskList.filter(task => task.dueDate.includes(day) && task.flag === 'Personal'
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

.flag {
  margin-top: 0.3em;
  margin-bottom: 0.3em;
}

.weekday {
  font-size: 0.9rem;
  border-radius: 5px;
  margin: 5px 0px 5px 0px;
  padding: 5px;
  text-align: center;
}

.weekday-header {
  padding: 3px;
  background: #f6f6f6;
  border-radius: 5px;
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
color: gray;
cursor: pointer;
box-shadow: 0 0 8px rgba(0, 0, 0, 0.6);
}

.task {
  border-style: solid;
  border-width: medium;
  border-color: lightgray;
  border-radius: 5px;
  margin: 10px 5px;
  font-size: 1em;
  color: black;
  word-wrap: break-word;
  padding: 0.6em;
  position: relative;
}

.close {
  width: 16px;
  height: 16px;
  font-size: 1rem;
  border-radius: 50%;
  color: gray;
  top: 1px;
  right: -1px;
  opacity: 1;
  font-weight: 400;
  line-height: 0.5;
  padding-bottom: 5px;
  position: absolute;
}

h3 {
  margin-top: 0.1em;
  font-size: 1em;
  font-weight: 500;
}

.descr {
  margin: 0
}

.flag{
  border-style: solid;
  border-width: thin;
  border-color: seagreen;
  border-radius: 5px;
  color: seagreen;
  background-color: white;
}

.flag-btn button {
  margin-right: 0.5em;
}

.modal-body {
  text-align: center;
  padding: 0 !important;
}

h4 {
  font-size: 1.5em;
}
</style>
