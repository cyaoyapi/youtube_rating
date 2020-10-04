<template>
    <div class="row">
        <div v-if="videoToDisplay.id === 'None'" class="col">
            <p class="text-warning text-center">Aucune vidéo n'est selectionnée</p>
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
        </div>
    </div>
</template>

<script>

export default {
  name: 'DetailsVideo',
  props: {
      videoToDisplay: {
          type: Object,
          required: true
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
