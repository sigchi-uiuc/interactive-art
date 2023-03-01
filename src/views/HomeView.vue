<template>
  <div class="home">
    <router-link :to="{ name: 'CarouselView'}">
      <div class="view-button no-cursor" @:mouseover="cursor_color = hover_cursor_color" @:mouseleave="cursor_color = reg_cursor_color">
        View Art
      </div>     
    </router-link>

    <cursor v-if="cursor_on" :color="cursor_color"/>
  </div>
</template>

<script>
// @ is an alias to /src
import cursor from '@/components/cursor.vue'

export default {
  name: 'HomeView',
  components: {
    cursor
  },
  data () {
    return {
      cursor_on: true,
      hovered: false,
      hover_cursor_color: [0, 200, 200],
      reg_cursor_color: [0, 0, 0],
      cursor_color: [0, 0, 0]
    }
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
