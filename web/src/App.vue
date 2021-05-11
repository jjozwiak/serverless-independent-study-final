<script lang="ts">
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        platform : 'aws'
      }
    },
    watch: {
      platform: function() {
        console.log('platform changed')
        this.$store.commit('setProvider', this.platform)
      }
    },
    computed: {
      ...mapGetters([
        'provider'
      ])
    }
  }
</script>

<template>
  <div id="app">
    <nav class="navbar navbar-dark sticky-top bg-dark flex-md-nowrap p-0">
      <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="#">Simple Form App</a>
    </nav>
    <div class="container-fluid fh">
      <div class="row fh">
        <nav class="col-md-2 d-none d-md-block bg-gray sidebar pt-4">
          <div class="sidebar-sticky">
            <ul class="nav flex-column">
              <li class="nav-item">
                <div class="nav-link">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-file-text"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                  <router-link to="/forms">Forms</router-link>
                </div>
              </li>
              <li class="nav-item">
                <div class="nav-link">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-file-text"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                  <router-link to="/form/create">Create New Form</router-link>
                </div>
              </li>
              <li class="nav-item">
                <div class="nav-link">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-file-text"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                  <router-link to="/form/test">Form Test</router-link>
                </div>  
              </li>
              <li class="nav-item">
                <div class="nav-link">
                  <label for="aws-platform">
                    <img src="https://www.clipartkey.com/mpngs/m/169-1697212_amazon-aws-aws-svg.png" width="50px" alt="">
                  </label>               
                  
                  <input id="aws-platform" type="radio" value="aws" v-model="platform">
                </div>
              </li>
              <li>
                <div class="nav-link">                
                  <label for="azure-platform">
                    <img src="https://www.kindpng.com/picc/m/299-2994956_azure-logo-microsoft-azure-logo-svg-hd-png.png" width="50px" alt="">
                  </label>
                  <input id="azure-platform" type="radio" value="azure" v-model="platform">
                </div>
              </li>
            </ul>
          </div>
        </nav>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
  @import 'assets/scss/typography.scss';

  body, html, #app, .fh {
      height: 100%;
  }

  .bg-gray {
    background-color: #ddd;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }

  .nav-link {
    img {
      &:hover {
        cursor: pointer;
      }
    }
  }
</style>
