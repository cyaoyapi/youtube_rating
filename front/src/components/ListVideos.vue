<template>
  <div class="">
    <div class="row">
      <div class="col-md-5 text-center nicefont">
            <h1>Welcome to youtube videos rating</h1>
            <hr>
            <div v-for="video in videos" :key="video.id">
              <h4>{{ video.title }}</h4>
              <p>Rating : {{ video.ratings_average }}</p>
              <p></p>{{ video.comments_list }}</p>
              <button class="btn-sm btn-primary mt-2 mb-3">Details</button>
            </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ListVideos',
  data() {
    return {
      videos: []
    }
  },
  methods: {
    getVideos() {
      axios.get('http://127.0.0.1:8000/api/videos/')
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err)) ;
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
