<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>VuePoint</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Monday</th>
              <th scope="col">Tuesday</th>
              <th scope="col">Wednesday</th>
              <th scope="col">Thursday</th>
              <th scope="col">Friday</th>
              <th scope="col">Weekend</th>
            </tr>
          </thead>
          <tbody>
          <tr>
            <td v-for="(task, index) in tasks[0]" :key="index">{{ task.title }}</td>
            <td></td>
            <td></td>
            <td></td>
            <td v-for="(task, index) in tasks[1]" :key="index">{{ task.title }}</td>
            <td></td>
          </tr>
          </tbody>
        </table>
        <button type="button" class="btn btn-warning btn-sm">Update</button>
        <button type="button" class="btn btn-danger btn-sm">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
    };
  },
  methods: {
    getTasks() {
      const path = 'http://localhost:5000/tasks';
      axios.get(path)
        .then((res) => {
          this.tasks = res.data.tasks;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getTasks();
  },
};
</script>
