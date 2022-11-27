<template>
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
import json from '@/assets/test-art.json'
import axios from 'axios'

export default {
  name: 'Art',
  props: {
    image: String
  },

  data() {
    return {
      coords: json, 
      x: 0, 
      y: 0, 
      started: false,
      width: 0,
      height: 0
    }
  },

  created() {
    this.coords = Object.values(this.coords)
      window.addEventListener('load', () => {
        this.height = this.$refs.art.clientHeight
        this.width = this.$refs.art.clientWidth
        this.get_pixel_coords()
      })
  },

  methods: {
    async get_pixel_coords() {
      axios.get(`api/coords/${this.image}/${this.width}/${this.height}`)
      .then(response => (console.log(response)))
    },
    updateNote(event) {
      if (!this.started) {
        return
      }

      this.x = event.offsetX
      this.y = event.offsetY 
      var note = this.coords[this.x][this.y]
     
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
      this.synth.triggerRelease(Tone.now())
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.image-container {
  height: 100%
}
</style>
