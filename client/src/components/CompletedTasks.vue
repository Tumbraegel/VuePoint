<template>
 <div>
      <b-list-group v-for="task in completedTasks()" :key="task.id">
        <div class="text-left">
          <b-list-group-item variant="secondary">Task:
            <em v-b-popover.hover.right="task.taskDescription" title="Details">{{task.title}}</em>
            </b-list-group-item>
        </div>
      </b-list-group>
 </div>
</template>

<script>
export default {
  name: 'completedTasks',
  props: ['taskList'],
  data() {
    return {
      // showingCompleted: false,
      done: 1,
    };
  },
  methods: {
    completedTasks() {
      return this.taskList.filter(task => task.taskState === this.done);
    },
    getCompletedTasks() {
      // stuff
    },
  },
};
</script>

<style scoped>
</style>
