<template>
    <div class="row">
        <div v-if="videoToDisplay.id === 'None'" class="col">
            <p class="text-warning text-center">No selected video</p>
        </div>
        <div v-else class="col">
            <p><strong>Title</strong> : {{ videoToDisplay.title }}</p>
            <p><strong>Url</strong> : {{ videoToDisplay.url }}</p>
            <p><strong>Author</strong> : {{ videoToDisplay.author }}</p>
            <p><strong>Description</strong> : {{ videoToDisplay.description }}</p>
            <p><strong>Category</strong> : {{ videoToDisplay.category }}</p>
            <p><strong>Subcategory</strong> : {{ videoToDisplay.subcategory }}</p>
            <p><strong>Rating average </strong> : {{ videoToDisplay.ratings_average }}</p>
            <p><strong>Comments</strong> : </p>
            <ul>
                <li v-for="[key, text] in Object.entries(videoToDisplay.comments_list)" :key="key">{{ text }}</li>
            </ul>
            <b-form @submit="giveRating" @reset="onReset">
                <legend>Rate this video</legend>
                <b-form-group
                    id="input-group-1"
                    label-for="stars"
                >
                    <b-form-rating
                    id="stars"
                    v-model="form.stars"
                    required
                    ></b-form-rating>
                    {{ form.stars }}
                </b-form-group>
                <b-form-group
                    id="input-group-2"
                    label="Comments:"
                    label-for="comments"
                >
                    <b-form-textarea
                    id="comments"
                    v-model="form.comments"
                    required
                    ></b-form-textarea>
                </b-form-group>
                <b-button type="submit" variant="primary">Give rating</b-button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            </b-form>
            <hr>
            Clic here <b-button v-if="token !== null" 
                size="sm" class="btn btn-danger my-2 my-sm-0" 
                type="button"
                @click="deleteVideo(videoToDisplay.id)">
                Delete
            </b-button> to delete this video !
        </div>
    </div>
</template>

<script>
import axios from 'axios' ;
import Helper from '../helper/helper.js' ;
import { mapState, mapGetters } from 'vuex' ;

export default {
  name: 'DetailsVideo',
  props: {
      videoToDisplay: {
          type: Object,
          required: true
      }
  },
  data() {
      return {
          form: {
              stars: null,
              comments: ''
          }
      }
  },
  computed: {
      ...mapState(['token']),
      ...mapGetters(['axiosConfig'])
  },
  methods: {
      deleteVideo(id){
          axios.delete(`${Helper.apiURL}/api/videos/${id}`, axiosConfig)
          .then(res => {
              this.$emit('update-list-videos') ;
              this.$emit('reset-details-video') ; 
          })
          .catch(err => console.log(err)) ;
      },
      giveRating(){

      },
      onReset(){

      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
