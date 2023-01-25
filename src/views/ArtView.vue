<template>
  <div class="home">
    <Art image='park.jpg'/>
    <div id="home-button" v-on:mouseover="homeMouseOver" v-on:mouseleave="homeMouseLeave">
      Return Home
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Art from '@/components/art.vue'

export default {
  name: 'ArtView',
  components: {
    Art
  },
  data () {
    return {
      timeoutId: null
    }
  },

  /*created() {
    window.addEventListener(marker, 'mouseover', function () {
      timeoutId = window.setTimeout(function(){
        alert("I did it!")
      }, 2000)
    })

    window.addEventListener(marker, 'mouseout', function () {
      window.clearTimeout(this.timeoutId)
    })
  },*/

  methods: {
    homeMouseOver() {
      this.timeoutId = window.setTimeout(function(){
        // TODO: Return home
        console.log("Return home")
      }, 2000)
    },

    homeMouseLeave() {
      window.clearTimeout(this.timeoutId)
    }

  },

  /*watch: {
    timeoutId: function (val) {
      console.log("here")
    }
  }*/

}
</script>

 <style>
  #home-button {
    width: 200px;
    height: 50px;
    border-radius: 15px;
    background: orange;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
  }


</style>
  