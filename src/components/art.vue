<template>
  <div class="container">
    <div class="vl-parent">
      <loading v-model:active="loading"
              :is-full-page="true"/>
    </div>
    <img 
      class="image-container"
      :style="[!music_started ? {opacity: 0.6} : {opacity: 1}]"
      ref="art"
      :src="require(`@/assets/${image}`)" 
      v-on:mousemove="updateNote">
    <button v-if="!music_started" class="btn" @click="start">
      Start
    </button>
  </div>
  
</template>

<script>
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'
import axios from 'axios'
import PianoMp3 from 'tonejs-instrument-piano-mp3'
const BASE_URL = process.env.VUE_APP_BASE_URL

export default {
  name: 'Art',
  components: {
    Loading
  },
  props: {
    image: String
  },

  data() {
    return {
      image_info: undefined,
      loading: false,
      music_started: false,
      time_delay: 800,
      base_url: ""
    }
  },

  created() {
      window.addEventListener('load', () => {
        this.image_height = this.$refs.art.clientHeight
        this.image_width = this.$refs.art.clientWidth
      })

      if (!location.toString().includes("localhost")) {
        this.base_url = BASE_URL
      }
  },

  methods: {
    load_notes_audio() {
      var request_url = `${this.base_url}/coords/${this.image}/${this.image_width}/${this.image_height}`
      console.log(`getting notes from backend at ${request_url}`)

      axios.get(request_url)
      .then(response => {
        this.image_info = response.data
        console.log("notes loaded from backend")
      })
      .catch(error => {
        console.log(`failed getting notes from backend: ${error}`)
      })
      .finally(() => {
       console.log(`number of sections: ${this.image_info.length}`)
       this.synth = new PianoMp3({
              minify: true,
              onload: () => {
                console.log("audio samples loaded")
                this.loading = false
                this.music_started = true
              }
          }).toDestination()
      })
    },

    updateNote(event) {
      if (!this.music_started || this.loading) {
        return 
      }

      if ((!this.start_time) || (new Date() - this.start_time > this.time_delay)) {
        var x = event.offsetX
        var y = event.offsetY 
        var note = this.get_note(x, y)

        this.synth.triggerAttack(note)
        console.log(`note playing: ${note} for x: ${x}, y: ${y}`)
        this.start_time = new Date()
      }
    },

    start() {      
      this.loading = true
      this.load_notes_audio()
    },

    get_note(x, y) {
      var get_section = function(section) {
        var start_x = section.area[0]
        var start_y = section.area[1]
        var end_x = section.area[2]
        var end_y = section.area[3]
  
        return x >= start_x && y >= start_y && x <= end_x && y <= end_y
      }
      var section = this.image_info.filter(get_section)
      // console.log(`image section: ${[...section[0].area]}`)
      return section[0].note
    }
  }
}
</script>

<style scoped>

.image-container {
  height: 100%;
  max-width: 100%;
  max-height: 100%;
  bottom: 0;
  left: 0;
  margin: auto;
  overflow: auto;
  position: fixed;
  right: 0;
  top: 0;
  -o-object-fit: contain;
  object-fit: contain;
}

.container {
  position: relative;
}

.btn {
  
  background-color: #555;
  color: white;
  font-size: 16px;
  padding: 12px 24px;
  border: none;
  cursor: pointer;
  border-radius: 5px;

  bottom: 0;
  left: 0;
  margin: auto;
  overflow: auto;
  position: fixed;
  right: 0;
  top: 0;

  height: 40px;
}

</style>
