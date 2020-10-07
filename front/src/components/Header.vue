<template>
    <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Youtube Rater</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
            <b-nav-item :to="{name: 'Home' }">Home</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <b-nav-form @submit="login" v-if="token === null">
                <b-form-input type="text" size="sm" class="mr-sm-2" placeholder="Username" v-model="form.username"></b-form-input>
                <b-form-input type="password" size="sm" class="mr-sm-2" placeholder="Password" v-model="form.password"></b-form-input>
                <b-button size="sm" class="mr-sm-2" type="submit">Login</b-button> 
                <b-button :to="{name: 'Register' }" size="sm" class="mr-sm-2" @click="logout">Register</b-button>            
            </b-nav-form>
            <div v-else >
                <span class="text-white pr-4">User : <strong>{{ username }}</strong></span>
                <b-button size="sm" class="my-2 my-sm-0" @click="logout">Logout</b-button>
            </div>
        </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    </div>
</template>

<script>
import axios from 'axios' ;
import Helper from '../helper/helper.js' ;
import { mapState, mapActions } from 'vuex' ;

export default {
  name: 'Header',
  data() {
      return {
          form: {
              username : '',
              passord: ''
          }
      }
  },
  computed: {
      ...mapState(['token', 'username'])
  },
  methods: {
      ...mapActions(['updateToken', 'setUsername']),
      login(){
          axios.post(`${Helper.apiURL}/auth/`, this.form)
          .then(res => {
              localStorage.setItem('user-token', res.data.token) ;
              localStorage.setItem('username', this.form.username) ;
              this.updateToken(localStorage.getItem('user-token'));
              this.setUsername(localStorage.getItem('username'));
              this.form = {
                  username: '',
                  password: ''
              }
          })
          .catch(err => console.log(err))
      },
      logout(){
            localStorage.removeItem('user-token') ;
            localStorage.removeItem('username') ;
            this.updateToken(null);
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
