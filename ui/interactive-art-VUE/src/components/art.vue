<template>
  <div class="vl-parent">
    <loading v-model:active="loading"
             :is-full-page="true"/>
  </div>
  <img 
    ref="art"
    class="image-container"
    :src="require(`@/assets/${image}`)" 
    @mousedown.once="start" 
    @mouseleave="stop" 
    v-on:mousemove="updateNote">
</template>

<script>
import * as Tone from 'tone'
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
import axios from 'axios'

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
      loading: true,
      started: false,
      image_width: 0,
      image_height: 0
    }
  },

  created() {
      window.addEventListener('load', () => {
        this.image_height = this.$refs.art.clientHeight
        this.image_width = this.$refs.art.clientWidth
        this.get_pixel_coords()
      })
  },

  methods: {
    async get_pixel_coords() {
      console.log("getting notes from backend")
      axios.get(`api/coords/${this.image}/${this.image_width}/${this.image_height}`)
      .then(response => (this.notes = response.data.notes))
      .finally(() => {
       console.log("notes loaded from backend")
       console.log(`note array num rows: ${this.notes.length}, cols: ${this.notes[0].length}`)
       this.loading = false;
      });
    },

    updateNote(event) {
      if (!this.started) {
        return
      }

      var x = event.offsetX
      var y = event.offsetY 
      var note = this.notes[x][y]
     
      if ((this.note) && (note != this.note)) {
        this.synth.triggerRelease(Tone.now())
      }

      this.note = note
      this.synth.triggerAttack(this.note, Tone.now())
      console.log(`note playing: ${this.note}`)
    },

    start() {
      Tone.start()
      this.synth =  new Tone.DuoSynth().toDestination()
      this.started = true
      console.log('audio is ready')
    },

    stop() {
      if (!this.started) {
        return
      }
      this.synth.triggerRelease(Tone.now())
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.image-container {
  height: 100%;
}
</style>
