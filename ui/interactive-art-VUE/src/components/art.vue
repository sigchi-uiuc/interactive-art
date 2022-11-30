<template>
  <div class="container">
    <div class="vl-parent">
      <loading v-model:active="loading"
              :is-full-page="true"/>
    </div>
    <img 
      :style="[!music_started ? {opacity: 0.6} : {opacity: 1}]"
      ref="art"
      class="image-container"
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
      notes: undefined,
      loading: false,
      music_started: false,
      time_delay: 800
    }
  },

  created() {
      window.addEventListener('load', () => {
        this.image_height = this.$refs.art.clientHeight
        this.image_width = this.$refs.art.clientWidth
      })
  },

  methods: {
    load_notes_audio() {
      console.log("getting notes from backend")
      axios.get(`api/coords/${this.image}/${this.image_width}/${this.image_height}`)
      .then(response => (this.notes = response.data.notes))
      .finally(() => {
       console.log("notes loaded from backend")
       console.log(`note array num rows: ${this.notes.length}, cols: ${this.notes[0].length}`)
       this.synth = new PianoMp3({
              onload: () => {
                console.log("audio samples loaded")
                this.loading = false
                this.music_started = true
              }
          }).toDestination()
      });
    },

    updateNote(event) {
      if (!this.music_started || this.loading) {
        return 
      }

      if ((!this.start_time) || (new Date() - this.start_time > this.time_delay)) {
        var x = event.offsetX
        var y = event.offsetY 
        var note = this.notes[x][y]

        this.synth.triggerAttack(note)
        console.log(`note playing: ${note}`)
        this.start_time = new Date()
      }
    },

    start() {      
      this.loading = true
      this.load_notes_audio()
    }
  }
}
</script>

<style scoped>
.image-container {
  height: 100%;
}

.container {
  position: relative;
}

.btn {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  background-color: #555;
  color: white;
  font-size: 16px;
  padding: 12px 24px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

</style>
