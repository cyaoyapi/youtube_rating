<template>
    <div id="container" class="container">
        <b-form @submit.prevent="onSubmit" @reset.prevent="onReset">
            <b-form-group
                id="group-1"
                label="Username:"
                label-for="username"
                description="The username"
            >
                <b-form-input
                id="username"
                v-model="form.username"
                type="text"
                required
                placeholder="Enter username" 
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="group-2"
                label="Password:"
                label-for="password"
                description="The password"
            >
                <b-form-input
                id="password"
                v-model="form.password"
                type="password"
                required
                ></b-form-input>
            </b-form-group>
            
            <b-button type="submit" variant="primary">Submit</b-button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>  
        </div>
</template>

<script>
import axios from 'axios' ;
import Helper from '../helper/helper.js' ;

export default {
  name: 'Register',
  data() {
      return {
          form: {
              username: '',
              password: ''
          }
      }
  },
  methods: {
      onSubmit() {
        console.log("Submit form") ;
        axios.post(`${Helper.apiURL}/api/users/`, this.form)
        .then(res => {
            console.log(res) ;
            this.$router.push("/");
        })
        .catch(err => console.log(err)) ;
      },
      onReset() {
        this. form = {
              username: '',
              password: ''
        }
      }  
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#container {
    width: 25rem;
}
</style>
