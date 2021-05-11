<script lang="ts">
    import axios from 'axios'
    import _ from 'lodash'
    import { mapGetters } from 'vuex'

    export default {
        data() {
            return {
                loading: true,
                forms: [],
                selectedFormId: '',
                entryDetail: {},
                searchTerm: ''
            }
        },
        methods : {
            selectForm: function(id) {
                this.selectedFormId = id
            },
            showDetail: function(index) {
                this.entryDetail = this.selectedForm.entries[index]
            },
            deleteForm: function() {
                confirm( `Are you sure you want to delete form - ${this.selectedFormId} ?`)
                let delete_url = this.providerURLS.deleteForm
                axios.delete(delete_url.replace('{id}', this.selectedFormId))
                .then((results) => {
                    console.log(results)
                })
            }
        },
        computed : {
            ...mapGetters([
                'providerURLS'
            ]),
            selectedForm: function() {
                return this.forms[this.selectedFormId]
            }
        },
        watch:  {
            searchTerm : _.debounce(function(newVal) {

                axios.get(this.providerURLS.getFormsFiltered.replace('{title}', encodeURI(newVal)))
                .then((results) => {
                    console.log(results)
                    this.forms = results.data.forms
                    this.selectedFormId = Object.keys(this.forms)[0]

                    console.log(this.selectedForm.entries)
                    let data = []
                    _.each(this.selectedForm.entries, function() {
                    
                        data.push(['action', 'data'])
                    })
                    
                })
                    
            }, 500, { 'maxWait': 1000 })
        },
        mounted() {
            axios.get(this.providerURLS.getForms)
            .then((results) => {
                console.log(results)
                this.forms = results.data.forms
                this.selectedFormId = Object.keys(this.forms)[0]

                console.log(this.selectedForm.entries)
                let data = []
                _.each(this.selectedForm.entries, function() {
                
                    data.push(['action', 'data'])
                })
                
            })
        }
    }
</script>

<template>
    <div class="col-10 pt-4">
        <div class="row">
            <div class="col-md-10">
                <h1>Forms</h1>
            </div>
            <div class="col-md-2">
                <div class="form-group">
                  <label for="searchTerm">Search by Title</label>
                  <input type="text" name="" id="searchTerm" class="form-control" placeholder="" aria-describedby="helpId" v-model="searchTerm">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-3">
                <ul class="list-group">
                    <li v-for="(form, index) in forms" v-bind:key="index" v-on:click="selectForm(form.id)" class="list-group-item" :class="(form.id == selectedFormId)? 'active' : ''" style="cursor: pointer">{{ form.title }}</li>
                </ul>
            </div>
            <div class="col-9">
                <template v-if="selectedForm != undefined">
                    <h2>{{ selectedForm.title }} Entries</h2>
                    <table class="table table-bordered table-striped"  v-if="selectedForm.entries.length > 0">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Data</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(entry, index) in this.selectedForm.entries" v-bind:key="index" class="mb-2">
                                <td scope="row">
                                    <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#modelId" v-on:click="showDetail(index)">
                                        Details
                                    </button>
                                </td>
                                <td>
                                    <template v-for="(field) in selectedForm.fields">
                                        {{ field['label'] }} : {{ entry[field['id']] }} 
                                    </template>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div v-if="selectedForm.entries.length == 0">No Entries Yet</div>
                    <button class="btn btn-danger" v-on:click="deleteForm">Delete Form</button>
                </template>
                <template v-else>
                    <p>No form selected</p>
                </template>
            </div>
        </div>

        <!-- Modal -->
        <div class="modal fade" id="modelId" tabindex="-1" role="dialog" aria-labelledby="modelTitleId" aria-hidden="true">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Entry Details</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <template v-if="(typeof selectedForm !== 'undefined')? true : false" >
                            <table class="table table-striped table-bordered">
                                <thead>
                                    <tr>
                                        <td>Label</td>
                                        <td>Data</td>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>id</td>
                                        <td>{{ entryDetail['id'] }}</td>
                                    </tr>
                                    <tr v-for="(field, index) in selectedForm.fields" :key="index">
                                        <td>{{ field['label'] }}</td>
                                        <td>{{ entryDetail[field['id']] }}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </template>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>