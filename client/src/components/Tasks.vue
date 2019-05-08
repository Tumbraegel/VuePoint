<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>VuePoint</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Task</button>
        <br><br>

        <!--
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col" v-for="day in days">{{ day }}</th>
            </tr>
          </thead>
          <tbody>
          <tr>
            <td v-for="task in tasks" v-bind:key="task.id">{{ task.title }}</td>
          </tr>
          </tbody>
        </table>
        -->

        <div class="weekday-table">
          <li class="weekday" v-for="day in days" :key="day">
            <h2 class="weekday-header">{{ day }}</h2>
            <ul class="task">
              <li v-for="task in getTasks(day)" :key="task.id">
                <strong>{{ task.title }}</strong>
                <div>{{ task.description }}</div>
              </li>
            </ul>
          </li>
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
 </style>

<script>
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
      }],
    };
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
  },
};
</script>
