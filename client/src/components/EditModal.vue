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
