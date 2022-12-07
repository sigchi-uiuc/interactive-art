<template>
  <div class="home">
    <Art image='park.jpg'/>
  </div>
</template>

<script>
// @ is an alias to /src
import Art from '@/components/art.vue'

export default {
  name: 'HomeView',
  components: {
    Art
  }
}
</script>
