<template>
 <div class="completed_tasks_view">
      <b-list-group v-for="task in completedTasks()" :key="task.id">
        <div class="text-left">
          <b-list-group-item variant="secondary">Task:
            <em v-b-popover.hover.right="task.taskDescription" title="Details">{{task.title}}</em>
            <input checked type="checkbox" v-on:change="$emit('incompl-task', task)">
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
    };
  },
  methods: {
    completedTasks() {
      return this.taskList.filter(task => task.taskState === 1);
    },
  },
};
</script>

<style scoped>
.completed_tasks_view {
  width: 95vw;
}
</style>
