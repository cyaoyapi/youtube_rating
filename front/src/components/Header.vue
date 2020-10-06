<template>
    <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">Youtube Rater</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
        <!-- <b-navbar-nav>
            <b-nav-item href="/">Home</b-nav-item>
            <b-nav-item href="/about">About</b-nav-item>
        </b-navbar-nav> -->

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
            <b-nav-form @submit="login" v-if="token === null">
            <b-form-input type="text" size="sm" class="mr-sm-2" placeholder="Username" v-model="form.username"></b-form-input>
            <b-form-input type="password" size="sm" class="mr-sm-2" placeholder="Password" v-model="form.password"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Login</b-button>
            </b-nav-form>
            <b-button v-else size="sm" class="my-2 my-sm-0" @click="logout">Logout</b-button>
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
      ...mapState(['token'])
  },
  methods: {
      ...mapActions(['updateToken']),
      login(){
          axios.post(`${Helper.apiURL}/auth/`, this.form)
          .then(res => {
              localStorage.setItem('user-token', res.data.token) ;
              this.updateToken(localStorage.getItem('user-token'));
          })
          .catch(err => console.log(err))
      },
      logout(){
            localStorage.removeItem('user-token') ;
            this.updateToken(null);
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
