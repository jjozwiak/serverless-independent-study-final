<template>
  <div class="col-10 pt-4 about">
    <div class="form-group">    
      <select name="" id="" v-model="form_id" class="form-control">
        <option v-for="(form, index) in forms" :value="form.id" :key="index">{{ form.title }}</option>
      </select>
    </div>
    <form action="" method="POST">
      <template v-if="selectedForm">
        <div v-for="(field, index) in selectedForm.fields" :key="index" class="form-group">
          <label :for="field.id">{{ field.label }}</label>
          <input :type="field.type" :id="field.id" :name="field.id" class="form-control">
        </div>
      </template>
      <div class="form-group">
        <label for="">Form ID</label>
        <input type="text" name="form_id" id="form_id" v-model="form_id" class="form-control" placeholder="" aria-describedby="helpId">
      </div>
      <div class="form-group">
        <input type="submit" v-on:click.prevent="submitForm" class="btn btn-primary">
      </div>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import { v4 as uuidv4 } from 'uuid'
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        form_id: '',
        forms: []
      }
    },
    computed: {
      ...mapGetters([
        'providerURLS'
      ]),
      selectedForm: function() {
        return this.forms[this.form_id]
      }
    },
    methods : {
      getData: function() {
        let inputs = document.getElementsByTagName('input')
        let data = {}
        for (var index = 0; index < inputs.length; ++index) {
          let currInput = inputs[index]
          if (currInput.type == 'text') {
            data[currInput.name] = currInput.value
          }
        }
        data['id'] = uuidv4()
        return data
      },
      submitForm: function() {
        let submit_data_url = this.providerURLS.submitData
        axios.post(submit_data_url.replace('{id}', this.form_id), { 'data' : this.getData() })
        .then((results) => {
          console.log(results)
        })
      }
    },
    mounted() {
      axios.get(this.providerURLS.getForms)
        .then((results) => {
          console.log(results)
          this.forms = results.data.forms
          this.form_id = Object.keys(this.forms)[0]
        })
    }
  }
</script>
