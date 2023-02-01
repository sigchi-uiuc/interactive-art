<template>
  <div class="art-container">
    <Art image='park.jpg'/>
    <router-link :to="{ name: 'home'}" id="exit-icon">
      <svg viewBox="0 0 256 256" >
        <path d="M202.82861,197.17188a3.99991,3.99991,0,1,1-5.65722,5.65624L128,133.65723,58.82861,202.82812a3.99991,3.99991,0,0,1-5.65722-5.65624L122.343,128,53.17139,58.82812a3.99991,3.99991,0,0,1,5.65722-5.65624L128,122.34277l69.17139-69.17089a3.99991,3.99991,0,0,1,5.65722,5.65624L133.657,128Z"></path>
      </svg>
    </router-link>
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

 <style scoped>

  #exit-icon {
    width: var(--dl-size-size-medium);
    height: var(--dl-size-size-medium);
    margin: var(--dl-space-space-unit);
    align-self: flex-end;
  }

  .art-container {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
    position: fixed;
    justify-content: center;
  }


</style>
  