<template>
<b-container class="row-margin" id="home">
    <b-row>
      <b-col>
        <tasks/>
      </b-col>
    </b-row>

    <!--<b-row class="row-margin">
      <b-col>
        <p>SECTION FOR COMPLETED TASKS</p>
        <done/>
      </b-col>
    </b-row>-->

    <b-row class="row-margin" align-v="end">
      <b-col>
        <p>FOOTER SECTION</p>
      </b-col>
    </b-row>

  </b-container>
</template>

<script>
import Tasks from './Tasks';
import Done from './Done';

export default {
  name: 'Home',
  components: {
    Tasks,
    Done,
  },
};
</script>

<style scoped>
.row-margin {
  margin-top: 3em;
}
</style>
