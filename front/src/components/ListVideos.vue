<template>
  <div class="container  nicefont">
    <h1>Welcome to youtube rater</h1>
    <hr>
    <div class="row">
      <div class="col-md-5 text-center border-right">
            <h2>List of videos</h2>
            <p class="text-right">
              <b-button v-b-modal.new-video variant="primary">Add new video</b-button>
            </p>
            <table class="table">
              <thead class="thead-dark">
                <tr>
                  <th>Title</th>
                  <th>Rating average</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="video in videos" :key="video.id">
                  <td class="text-left">{{ video.title }}</td>
                  <td>{{ video.ratings_average }}</td>
                  <td><button class="btn-sm btn-primary mt-2 mb-3" @click="getVideoDetails(video)">Details</button></td>
                </tr>
              </tbody>
            </table>
      </div>
      <div class="col-md-7 p-5">
        <h2>Selected video details</h2>
        <DetailsVideo :videoToDisplay="videoDetails" @update-list-videos="updateListVideos" @reset-details-video="resetDetailsVideo" />
      </div>
    </div>
    <CreateVideo @update-list-videos="updateListVideos" />
  </div>
</template>

<script>
import axios from 'axios' ;
import Helper from '../helper/helper.js' ;
import DetailsVideo from './DetailsVideo' ;
import CreateVideo from './CreateVideo' ;

export default {
  name: 'ListVideos',
  components: {
    DetailsVideo,
    CreateVideo
  },
  data() {
    return {
      videos: [],
      videoDetails: {
        id: "None"
      },
    }
  },
  methods: {
    getVideos() {
      axios.get(`${Helper.apiURL}/api/videos/`)
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err)) ;
    },
    getVideoDetails(video) {
      this.videoDetails = video ;
    },
    resetDetailsVideo() {
      this.videoDetails = {
        id: "None"
      }
    },
    updateListVideos() {
      this.timer = setTimeout(() => {
      axios.get(`${Helper.apiURL}/api/videos/`)
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err)) ;
      }, 600) ;
    }
  },
  created(){
    this.getVideos() ;
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Mukta:wght@300&display=swap');

.nicefont {
  font-family: 'Mukta', sans-serif;
}

</style>
