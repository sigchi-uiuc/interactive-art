<template>
  <div>
    <div class="vl-parent">
      <loading v-model:active="loading" :is-full-page="true"/>
    </div>
    
    <div class="image-container">
      <router-link :to="{ name: 'home'}" class="close-button"></router-link> 

      <button class="lightbox-nav nav-left" @click="left_button"></button>
      <img 
        class="image-style"
        :style="[!music_started ? {opacity: 0.6} : {opacity: 1}]"
        ref="art"
        :src="require(`@/assets/${art_data[image_index].file}`)" 
        v-on:mousemove="updateNote">

      <button class="lightbox-nav nav-right" @click="right_button"></button>

      <p class="caption">{{art_data[image_index].citation}}</p>
    </div>

    <button v-if="!music_started" class="start-button" @click="start">
      Start
    </button>
    
    <cursor :color="cursor_color"/>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'
import axios from 'axios'
import PianoMp3 from 'tonejs-instrument-piano-mp3'
const ART_DATA = require("@/assets/art_data.json")
const BASE_URL = process.env.VUE_APP_BASE_URL

import cursor from '@/components/cursor.vue'


export default {
  name: 'ArtView',
  components: {
    Loading,
    cursor
  },
  data () {
    return {
      image_info: undefined,
      loading: false,
      music_started: false,
      time_delay: 800,
      resize_delay: 500,
      timeoutId: 0,
      base_url: "",
      art_data: ART_DATA,
      image_index: 0,
      cursor_color: [0,0,0]
    }
  },

  mounted() {
    window.addEventListener("resize", () => {
      this.image_height = this.$refs.art.clientHeight
      this.image_width = this.$refs.art.clientWidth
      
      if (this.music_started) {
        this.loading = true
        clearTimeout(this.timeoutId)
        this.timeoutId = setTimeout(this.note_resize, this.resize_delay)
      }
    })

    if (!location.toString().includes("localhost")) {
      this.base_url = BASE_URL
    }

  },

  destroyed() {
    window.removeEventListener("resize", this.myEventHandler);
  },


  methods: {
    async note_resize() {
        await this.load_notes()
        this.loading = false
    },

    async load_notes() {
      this.image_height = this.$refs.art.clientHeight
      this.image_width = this.$refs.art.clientWidth

      var image_file = this.art_data[this.image_index].file
      
      var request_url = `${this.base_url}/coords/${image_file}/${this.image_width}/${this.image_height}`
      console.log(`getting notes from backend at ${request_url}`)

      const response = await axios.get(request_url)
      this.image_info = response.data

      console.log("notes loaded from backend")
      return 
    },

    updateNote(event) {
      if (!this.music_started || this.loading) {
        return 
      }

      if ((!this.start_time) || (new Date() - this.start_time > this.time_delay)) {
        var x = event.offsetX
        var y = event.offsetY 
        var section = this.get_note(x, y)

        // update cursor color
        this.cursor_color = section.color

        this.synth.triggerAttack(section.note)
        console.log(`note playing: ${section.note} for x: ${x}, y: ${y}`)
        this.start_time = new Date()
      }
    },

    async start() {      
      this.loading = true

      await this.load_notes()
      
      this.synth = await new PianoMp3({
              minify: true,
              onload: () => {
                console.log("audio samples loaded") 
                this.loading = false
                this.music_started = true
              }
          }).toDestination() 
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
      return section[0]
    },

    calc_index(n, m) {
      return ((n % m) + m) % m
    },

    left_button() {
      var new_index = this.calc_index(this.image_index - 1, this.art_data.length)
      this.image_index = new_index
      this.music_started = false
    },

    right_button() {
      var new_index = this.calc_index(this.image_index + 1, this.art_data.length)
      this.image_index = new_index
      this.music_started = false
    }
  },


}
</script>

 <style scoped>

  .close-button {
    position: absolute;
    top: 0;
    right: 0;
    cursor: pointer;
    z-index: 1;

    width: var(--dl-size-size-medium);
    height: var(--dl-size-size-medium);
    background-color: transparent;
    border-width: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    align-items: center;
    justify-content: center;
    display: flex;
    margin: var(--dl-space-space-unit);
    background-image: url('@/assets/icons/exit.svg');
  }

  .image-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .image-style {
    height: 100%;
    /*max-height: 70%;*/
    max-width: 100%;
    max-width: calc(100% - 200px);
    object-fit: contain;
    margin-bottom: var(--dl-space-space-unit);
    margin-top: var(--dl-space-space-unit)
  }

  .caption {
    width: 100%;
    text-align: center;
    margin-bottom: var(--dl-space-space-twounits)
  }
  
  .start-button {
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

  .lightbox-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
    z-index: 1;
    width: var(--dl-size-size-small);
    height: var(--dl-size-size-small);
    background-color: transparent;
    border-width: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    align-items: center;
    justify-content: center;
    display: flex;
  }

  .nav-left {
    left: 20px;
    background-image: url('@/assets/icons/left.svg');  
  }

  .nav-right {
    right: 20px;
    background-image: url('@/assets/icons/right.svg'); 
  }

</style>