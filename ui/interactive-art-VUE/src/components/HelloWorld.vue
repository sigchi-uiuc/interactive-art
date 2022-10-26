<template>
  <div class="hello" >
    <div style="position: relative">
      <img src="@/assets/test-art.jpg" @mousedown.once="start" @mousedown="stop" v-on:mousemove="updateNote">
    </div>
  </div>
</template>

<script>
import * as Tone from 'tone'
import json from '@/assets/test-art.json'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },

  data() {
    return {
      count: 0, coords: json, x: 0, y: 0, started: false
    }
  },

  created() {
    console.log("loaded page")
    this.coords = Object.values(this.coords)
  },

  methods: {
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
