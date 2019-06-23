<template>
    <div id="task-modal">
      <b-button class="add-btn" variant="outline-primary" size="sm"
      v-on:click="openModal">&plus; Add new task</b-button>
      <b-modal v-model="show" id="add-modal" title="New Task" hide-footer>
        <b-form @submit="onSubmit">
          <label class="sr-only" for="form-input-title">Title</label>
          <b-form-input v-bind:class="{ 'warning': isEmpty }" id="form-input-title"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Title" v-model="addTaskForm.title"
          ></b-form-input>
          <p class="error" v-if="error">{{ error }}</p>

          <label class="sr-only" for="form-input-date">Date</label>
          <b-input-group prepend="Due on:" class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-input id="form-input-date" type="date" v-model="addTaskForm.dueDate">
          </b-input>
          </b-input-group>

          <label class="sr-only" for="form-input-decsription">Description</label>
          <b-form-input id="form-input-description"
          class="mb-2 mr-sm-2 mb-sm-0 input-field"
          placeholder="Task Description" v-model="addTaskForm.taskDescription"
          ></b-form-input>

          <label class="sr-only" for="form-input-flag">Flag: </label>
          <b-input-group prepend="Flag: " class="mb-2 mr-sm-2 mb-sm-0 input-field">
          <b-form-select id="form-input-flag" class="mb-2 mr-sm-2 mb-sm-0"
          :options = "flags" v-model="addTaskForm.flag">
          </b-form-select></b-input-group>

          <div class="modal-footer" id="btn">
            <b-button variant="secondary" id="btn-cancel" v-on:click="show =!show">
            Cancel</b-button>
            <b-button type="submit" variant="primary" id="btn-create">
            Add Task</b-button>
        </div>
      </b-form>
    </b-modal>
    </div>
</template>

<script>
// import axios from 'axios';

export default {
  props: ['taskList'],
  data() {
    return {
      show: false,
      flags: [
        { value: 'Work', text: 'Work' },
        { value: 'Personal', text: 'Personal' },
        { value: 'Studies', text: 'Studies' },
      ],
      addTaskForm: {
        title: '',
        taskDescription: '',
        dueDate: '',
        flag: '',
      },
      error: '',
      isEmpty: false
    };
  },

  methods: {
    openModal() {
      if (this.error) {
        this.error = '';
        this.isEmpty = false;
        this.show = true;
      }
      this.show = true;
    },

    initForm() {
      this.addTaskForm.title = '';
      this.addTaskForm.taskDescription = '';
      this.addTaskForm.dueDate = '';
      this.addTaskForm.flag = '';
    },

    onSubmit(evt) {
      evt.preventDefault();
      if (this.addTaskForm.title == '') {
        this.error = 'Please enter a title';
        this.isEmpty = true;
      }
      else {
        const payload = {
        title: this.addTaskForm.title,
        taskDescription: this.addTaskForm.taskDescription,
        dueDate: this.addTaskForm.dueDate,
        flag: this.addTaskForm.flag,
        };
        this.$emit('add-task', payload);
        this.error = '';
        this.initForm();
        this.show = false;
      }
    },

    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },

    created() {
      this.initform();
      // eslint-disable-next-line
      console.log('created');
    },
  }
};
</script>

<style scoped>
#task-modal {
    text-align: center;
}

.new-task {
    width: 100%;
    margin: 0;
    font-size: 1.5em;
    border-bottom: 1px solid #4285F4;
}

.input-field {
    margin-top: 1em;
}

.modal-footer {
    margin-top: 2em;
    text-align: right;
    padding-bottom: 0;
}

@keyframes bounce {
  0% {
    transform: translateX(0px);
    timing-function: ease-in;
  }
  37% {
    transform: translateX(5px);
    timing-function: ease-out;
  }
  55% {
    transform: translateX(-5px);
    timing-function: ease-in;
  }
  73% {
    transform: translateX(4px);
    timing-function: ease-out;
  }
  82% {
    transform: translateX(-4px);
    timing-function: ease-in;
  }
  91% {
    transform: translateX(2px);
    timing-function: ease-out;
  }
  96% {
    transform: translateX(-2px);
    timing-function: ease-in;
  }
  100% {
    transform: translateX(0px);
    timing-function: ease-in;
  }
}

.warning {
  border-color: red;
  animation-name: bounce;
  animation-duration: .5s;
  animation-delay: 0.25s;
}

.error {
  color: red;
  animation-name: bounce;
  animation-duration: .5s;
  animation-delay: 0.25s;
}
</style>
