<script lang="ts">
    import axios from 'axios'
    import { v4 as uuidv4 } from 'uuid'
    import { mapGetters } from 'vuex'

    export default {

        data() {
            return {
                fieldTypes: [
                    {
                        "type" : "text",
                        "icon" : ""
                    },
                    {
                        "type" : "email",
                        "icon" : ""
                    }
                ],
                form: {
                    title: '',
                    fields: [],
                    entries: []
                },
                enabled: true
            }
        },
        computed:  {
            ...mapGetters([
                'providerURLS'
            ])
        },
        methods: {
            addField: function() {
                this.form.fields.push({
                    'id' : uuidv4(),
                    'label' : '', 
                    'placeholder' : 'Enter label name', 
                    'type' : 'text' 
                })
            },
            removeField: function(index) {
                this.form.fields.splice(index, 1)
                console.log(index)
            },
            createForm: function() {
                axios.post(this.providerURLS.createForm,
                        { 'form' : this.form }
                    ).then((results) => {
                        alert('new form created')
                        this.form = {
                            title: '',
                            fields: [],
                            entries: []
                        }
                        console.log(results)
                    })
            },
            toId: function(label) {
                return label
            }
        }
    }
</script>

<template>
    <div class="col-10 pt-4">
        <div class="row">
            <div class="col-12">
                <div class="form-group">
                <label for="">Form Title</label>
                <input type="text"
                    class="form-control" name="form_title" id="" aria-describedby="helpId" placeholder="" v-model="form.title">
                </div>
                <div v-for="(field, index) in this.form.fields" v-bind:key="index" class="row mb-4">
                    <div class="col">
                        <input type="text" v-model="field.label" :placeholder="field.placeholder" class="form-control">
                    </div>
                    <div class="col">
                        <select name="" id="" v-model="field.type" class="form-control">
                            <option value="text">text</option>
                            <option value="email">email</option>
                        </select>
                    </div>
                    <div class="col">
                        <button class="btn btn-danger" v-on:click="removeField(index)">delete</button>
                    </div>
                </div>
                <hr>
                <div class="mb-4">
                    <button class="btn btn-primary" v-on:click="addField">Add Field</button>
                </div>
                <div>
                    <button class="btn btn-primary" v-on:click="createForm">Create Form</button>
                </div>
            </div>
        </div>
    </div>
</template>