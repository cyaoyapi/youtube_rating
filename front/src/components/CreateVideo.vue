<template>
    <b-modal id="new-video" ref="new-video" title="Add new video" hide-footer>
        <p class="text-success">{{ controlMessage }}</p>
        <b-form @submit.prevent="onSubmit" @submit="$emit('update-list-videos')" @reset.prevent="onReset">
            <b-form-group
                id="group-1"
                label="Title:"
                label-for="title"
                description="The video title"
            >
                <b-form-input
                id="title"
                v-model="form.title"
                type="text"
                required
                placeholder="Enter the video title" 
                @focus="resetControlMessage"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="group-2"
                label="Description:"
                label-for="description"
                description="The video description"
            >
                <b-form-textarea
                    id="description"
                    v-model="form.description"
                    placeholder="Enter at most 300 characters"
                    rows="10"
                    ></b-form-textarea>            
            </b-form-group>

            <b-form-group
                id="group-3"
                label="Url:"
                label-for="url"
                description="The video url"
            >
                <b-form-input
                id="url"
                v-model="form.url"
                type="url"
                required
                placeholder="Enter the video url"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="group-4"
                label="Category:"
                label-for="category"
                description="The video category"
            >
                <b-form-select v-model="form.category" :options="categoryOptions"></b-form-select>
            </b-form-group>

            <b-form-group
                id="group-5"
                label="Sub Category:"
                label-for="subcategory"
                description="The video Sub category"
            >
                <b-form-input
                id="subcategory"
                v-model="form.subcategory"
                type="text"
                required
                placeholder="Enter the video sub category"
                ></b-form-input>            
            </b-form-group>

            <b-form-group
                id="group-6"
                label="Author:"
                label-for="author"
                description="The video author"
            >
                <b-form-input
                id="author"
                v-model="form.author"
                type="text"
                required
                placeholder="Enter the video author"
                ></b-form-input>
            </b-form-group>


            <b-button type="submit" variant="primary">Submit</b-button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
            <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>    
    </b-modal>
</template>

<script>
import axios from 'axios' ;
import Helper from '../helper/helper.js' ;

export default {
  name: 'CreateVideo',
  data() {
      return {
          form: {
              title: '',
              description: '',
              url: '',
              category: null,
              subcategory: '',
              author: ''
          },
          categoryOptions: [
            { value: null, text: 'Please select an option' },
            { value: 'Programming', text: 'Programming' },
            { value: 'Data Science', text: 'Data Science' },
        ],
        controlMessage: '',
      }
  },
  methods: {
      onSubmit() {
        console.log("Submit form") ;
        axios.post(`${Helper.apiURL}/api/videos/`, this.form)
        .then(res => {
            console.log(res) ;
            this.onReset();
            this.controlMessage = 'Video successfully added' ;
        })
        .catch(err => console.log(err)) ;
      },
      onReset() {
        this. form = {
              title: '',
              description: '',
              url: '',
              category: null,
              subcategory: '',
              author: ''
        }
      },
      resetControlMessage(){
          this.controlMessage = '' ;
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
