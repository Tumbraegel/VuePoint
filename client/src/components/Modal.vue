<template>
<transition name="modal">
 <div class="modal modal-mask" style="display: block" @click='close'>
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <slot name="header"></slot>
      </div>
      <div class="modal-body">
        <slot name="body">
          <form class="form">
            <div class="form-group">
              <label for="title">Title</label>
              <input type="text" class="form-control" name="title">
            </div>

            <div class="form-group">
              <label for="description">Description</label>
              <input type="text" class="form-control" name="description">
            </div>

            <div class="form-group">
              <label for="date">Due Date</label>
              <input type="date" class="form-control" name="date">
            </div>

            <div class="form-group">
              <label for="importance">Importance</label>
                <select multiple class="form-control" name="importance">
                  <option value="hight">High</option>
                  <option value="medium">Medium</option>
                  <option value="low">Low</option>
              </select>
            </div>
          </form>
        </slot>
      </div>
      <div class="modal-footer">
        <slot name="footer"></slot>
      </div>
    </div>
  </div>
</div>
</transition>
</template>

<script>
export default {
  name: 'Modal',

  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

</style>
