import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    provider: 'aws',
    awsURLS : {
      getForms : process.env.VUE_APP_AWS_FORMS_URL,
      getFormsFiltered : process.env.VUE_APP_AWS_FORMS_FILTERED_URL,
      createForm : process.env.VUE_APP_AWS_FORM_CREATE_URL,
      submitData: process.env.VUE_APP_AWS_FORM_SUBMIT_URL,
      deleteForm: process.env.VUE_APP_AWS_FORM_DELETE_URL
    },
    azureURLS : {
      getForms : process.env.VUE_APP_AZURE_FORMS_URL,
      getFormsFiltered : process.env.VUE_APP_AZURE_FORMS_FILTERED_URL,
      createForm : process.env.VUE_APP_AZURE_FORM_CREATE_URL,
      submitData: process.env.VUE_APP_AZURE_FORM_SUBMIT_URL,
      deleteForm: process.env.VUE_APP_AZURE_FORM_DELETE_URL
    }
  },
  getters: {
    provider: state => {
      return state.provider
    },
    providerURLS: state => {
      if (state.provider == 'aws') {
        return state.awsURLS
      }
      if (state.provider == 'azure') {
        return state.azureURLS
      }
    }
  },
  mutations: {
    setProvider(state, val) {
      state.provider = val
    }
  },
  actions: {
  },
  modules: {
  }
})
