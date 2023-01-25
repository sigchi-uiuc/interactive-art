<template>
  <div class="home">
    <router-link :to="{ name: 'ArtView'}">
      <div class="view-button">
        View Art
      </div>     
    </router-link>
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

<style scoped>
  .view-button {
    position: relative;
    left: calc(50% - 100px);
    top: calc(50% - 25px);
    width: 200px;
    height: 50px;
    border-radius: 15px;
    color: white;
    background: black;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .home {
    height: 100vh !important;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
