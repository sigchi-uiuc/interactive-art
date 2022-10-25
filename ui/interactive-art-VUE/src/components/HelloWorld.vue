<template>
  <div class="hello" >
    <div style="position: relative">
      <img src="@/assets/test-art.jpg" @mousedown="handleClick" @mouseup="handleRelease"/>
    </div>
  </div>
</template>

<script>
import * as Tone from 'tone'
import json from '@/assets/sample.json'

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0, coords: json
    }
  },

  created() {
    console.log("here")
    this.coords = Object.values(this.coords)
    this.synth =  new Tone.Synth().toDestination()
  },

  methods: {
    handleClick(event) {
      var x = event.offsetX
      var y = event.offsetY
      console.log(`x: ${x}, y: ${y}`)
      console.log(`image ${this.coords[x][y]}`)
      var note = "C4"
      if (x<=700) {
        note = "F4"
      }
      this.synth.triggerAttack(note, Tone.now())
    },
    handleRelease() {
      console.log("click up")
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
