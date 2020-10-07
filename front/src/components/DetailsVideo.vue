<template>
    <div class="row">
        <div v-if="videoToDisplay.id === 'None'" class="col">
            <p class="text-warning text-center">No selected video</p>
        </div>
        <div v-else class="col">
            <p><strong>Title</strong> : {{ videoToDisplay.title }}</p>
            <b-embed
                type="iframe"
                aspect="16by9"
                :src="videoToDisplay.url"
                allowfullscreen
            ></b-embed>            
            <p><strong>Url</strong> : {{ videoToDisplay.url }}</p>
            <p><strong>Author</strong> : {{ videoToDisplay.author }}</p>
            <p><strong>Description</strong> : {{ videoToDisplay.description }}</p>
            <p><strong>Category</strong> : {{ videoToDisplay.category }}</p>
            <p><strong>Subcategory</strong> : {{ videoToDisplay.subcategory }}</p>
            <p v-if="videoToDisplay.ratings_average > 0"><strong>Rating average </strong> : {{ videoToDisplay.ratings_average }}</p>
            <p v-if="videoToDisplay.comments_list.length > 0"><strong>Comments</strong> : </p>
            <ul v-if="videoToDisplay.comments_list.length > 0">
                <li v-for="[key, obj_comment] in Object.entries(videoToDisplay.comments_list)" :key="key" class="text-left"><strong>{{ obj_comment.username }}</strong> => Stars : {{ obj_comment.stars }} => <q>{{ obj_comment.comment }}</q></li>
            </ul>
            <b-form @submit.prevent="giveRating(videoToDisplay.id)" v-if="token !== null">
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
            <hr v-if="token !== null">
            <div v-if="token !== null">
            Clic here <b-button  size="sm" 
                class="btn btn-danger my-2 my-sm-0" 
                type="button"
                @click="deleteVideo(videoToDisplay.id)">
                Delete
            </b-button> to delete this video !</div>
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
          axios.delete(`${Helper.apiURL}/api/videos/${id}`, this.axiosConfig)
          .then(res => {
              this.$emit('update-list-videos') ;
              this.$emit('reset-details-video') ; 
          })
          .catch(err => console.log(err)) ;
      },
      giveRating(id){

          axios.post(`${Helper.apiURL}/api/videos/${id}/rate_video/`, this.form, this.axiosConfig)
          .then(res => {
              this.$emit('update-list-videos') ;
              this.$emit('update-details-video', { videoId: this.videoToDisplay.id }) ;
              this.onReset() ;
          })
          .catch(err => console.log(err)) ;
      },
      onReset(){
          this.form = {
              stars: null,
              comments: ''
          }
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
