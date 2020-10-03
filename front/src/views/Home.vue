<template>
  <div class="home">
    <ListVideos />
    <button @click="getVideos">Get videos</button>
  </div>
</template>

<script>
import axios from 'axios'
// @ is an alias to /src
import ListVideos from '@/components/ListVideos.vue'

export default {
  name: 'Home',
  components: {
    ListVideos
  },
  data() {
    return {
      videos: []
    }
  },
  methods: {
    getVideos() {
      axios.get('http://127.0.0.1:8000/videos/')
      .then(res => (this.videos = res.data))
      .catch(err => console.log(err)) ;
      console.log(this.videos) ;
    }
  }
}
</script>
