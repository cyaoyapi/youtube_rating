<template>
  <div class="">
    <div class="row">
      <div class="col-md-5 text-center">
            <h1>Welcome to youtube videos rating</h1>
            <button @click="getVideos">Get videos</button>
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
      .then(res => (console.log(res.data)))
      .catch(err => console.log(err)) ;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
