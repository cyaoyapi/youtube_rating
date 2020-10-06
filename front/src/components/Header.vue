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
            <b-button v-else size="sm" class="my-2 my-sm-0" type="button" @click="logout">Logout</b-button>
        </b-navbar-nav>
        </b-collapse>
    </b-navbar>
    </div>
</template>

<script>
import axios from 'axios' ;

export default {
  name: 'Header',
  data() {
      return {
          form: {
              username : '',
              passord: ''
          },
          token: localStorage.getItem('user-token') || null,
      }
  },
  methods: {
      login(){
          axios.post('http://127.0.0.1:8000/auth/', this.form)
          .then(res => {
              localStorage.setItem('user-token', res.data.token) ;
              this.token = localStorage.getItem('user-token') ;
          })
          .catch(err => console.log(err))
      },
      logout(){
            localStorage.removeItem('user-token') ;
            this.token = null ;
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
