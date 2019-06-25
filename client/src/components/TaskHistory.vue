<template>
 <div>
      <b-list-group v-for="task in getTaskHistory()" :key="task.id">
        <div class="text-left">
          <b-list-group-item variant="secondary">Task:
            <em v-b-popover.hover.right="task.taskDescription" title="Details">{{task.title}}</em>
            <input v-if="task.taskState == 1" checked type="checkbox" disabled>
            <input v-else type="checkbox" disabled>
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
    getTaskHistory() {
      // prevSunday method from: https://stackoverflow.com/questions/35088088/javascript-for-getting-the-previous-monday#46544455
      // and https://answers.yahoo.com/question/index?qid=20100510160009AAeC42w&guccounter=1&guce_referrer=aHR0cHM6Ly9ndWNlLnlhaG9vLmNvbS8&guce_referrer_sig=AQAAAICsaJVpkUMTE6PUPDSmdVn7t1GOCJsNSAJ0gJv-tXvfIKrmKmAYd0EYxRE_6ZXh5eN5dq3ptdayqqwZPwWvdTq_ad4JrDdAwV5OM4nfL0qk5UCJHlP1t6Xk1TjyGFCFnQlSFYm5OHu7H4CeUo9e9x8P_igeAv-xhMxRXxbSh_2-
      const prevSunday = new Date();
      prevSunday.setDate(prevSunday.getDate() - ((prevSunday.getDay()) % 7));
      return this.taskList.filter(task => new Date(task.dueDate) < prevSunday);
    },
  },
};
</script>

<style scoped>
</style>
