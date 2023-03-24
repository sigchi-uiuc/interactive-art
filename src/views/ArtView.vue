<template>
  <div>
    <div class="vl-parent">
      <loading v-model:active="loading" :is-full-page="true"/>
    </div>

    <div class="image-container">
      <div class="close-button-animated-progress" 
          @:mouseover="closeButtonHover = true; button_hover = true"                              
          @:mouseleave="closeButtonHover = false; button_hover = false"               
          @:click="this.$router.push({name: 'home'})">
        <span :style="{ 'width': closeButtonProgress + 'px', 'height': closeButtonProgress + 'px'}"></span>
      </div>
      <div class="close-button no-cursor"/>

      <div class="animated-progress left-arrow-progress" 
          @:mouseover="leftArrowHover = true; button_hover = true"                   
          @:mouseleave="leftArrowHover = false; button_hover=false; cursor_color = undefined"
          @:click="leftArrowProgress = 0; left_button(); ">
        <span :style="{ 'width': leftArrowProgress + 'px' }"></span>
      </div>
      <button class="lightbox-nav nav-left"></button>

      <img 
        class="image-style"
        :style="[!music_started ? {opacity: 0.6} : {opacity: 1}]"
        ref="art"
        :src="require(`@/assets/${art_data[image_index].file}`)" 
        v-on:mousemove="updateNote"
        @mouseleave="stop_music"
        @mouseover="start_music_loop">

      <div class="animated-progress right-arrow-progress" 
          @:mouseover="rightArrowHover = true; button_hover = true" 
          @:mouseleave="rightArrowHover = false; button_hover=false; cursor_color = undefined"
          @:click=" rightArrowProgress = 0; right_button();">
        <span :style="{ 'width': rightArrowProgress + 'px' }"></span>
      </div>
      <button class="lightbox-nav nav-right"></button>

      <p v-if="!loading" class="caption">{{art_data[image_index].citation}}</p>
      <p v-else class="caption">
        {{ loading_text }}
      </p>
    </div>

    <div v-if="!music_started && !loading" class="start-info">
      <alert text="Hover over the painting to load the music" :transparency="0.95"/>
    </div>
    
    <cursor :color="cursor_color" :hover_on="button_hover"/>
  </div>
</template>

<script>
import Loading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/css/index.css'
import axios from 'axios'
import PianoMp3 from 'tonejs-instrument-piano-mp3'
import cursor from '@/components/cursor.vue'
import alert from '@/components/alert.vue'

const ART_DATA = require("@/assets/art_data.json")
const BASE_URL = process.env.VUE_APP_BASE_URL

export default {
  name: 'ArtView',
  components: {
    Loading,
    cursor,
    alert
  },
  props: ['id'],
  data () {
    return {
      music_data: undefined,
      loading: false,
      music_started: false,
      painting_hover: false,
      bpm: 60,
      current_note: undefined,
      music_interval: undefined,
      resize_delay: 500,
      timeoutId: 0,
      base_url: "",
      art_data: ART_DATA,
      image_index: 0,
      cursor_color: undefined,
      button_hover: false,
      rightArrowProgress: 0,
      rightArrowHover: false,
      leftArrowProgress: 0,
      leftArrowHover: false,
      closeButtonProgress: 0,
      closeButtonHover: false,
      startButtonProgress: 0,
      startButtonHover: false,
      loading_text: ""
    }
  },
  created() {
    if(this.id != null)
      this.image_index = this.id
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

  watch: {
    rightArrowProgress: {
      handler(value) {
          if(value < 125) { // Note: value must be equal to button width
            setTimeout(() => {
              if(value >= 1 && this.rightArrowHover)
                this.rightArrowProgress++;
            }, 20);
          } else {
            setTimeout(() => {
              this.rightArrowProgress = 1;
              this.right_button();
            }, 100);
          }
      }
    },
    rightArrowHover: {
      handler(value) {
        if(value == true) {
          this.rightArrowProgress = 1;
        } else {
          this.rightArrowProgress = 0;
        }
      }
    },
    leftArrowProgress: {
      handler(value) {
          if(value < 125) {
            setTimeout(() => {
              if(value >= 1 && this.leftArrowHover)
                this.leftArrowProgress++;
            }, 20);
          } else {
            setTimeout(() => {
              this.leftArrowProgress = 1;
              this.left_button();
            }, 100);
          }
      }
    },
    leftArrowHover: {
      handler(value) {
        if(value == true) {
          this.leftArrowProgress = 1;
        } else {
          this.leftArrowProgress = 0;
        }
      }
    },
    closeButtonProgress: {
      handler(value) {
          if(value < 125) {
            setTimeout(() => {
              if(value >= 1 && this.closeButtonHover)
                this.closeButtonProgress++;
            }, 20);
          } else {
            setTimeout(() => {
              this.$router.push({name: 'home'});
              this.closeButtonProgress = 0;
            }, 100);
          }
      }
    },
    closeButtonHover: {
      handler(value) {
        if(value == true) {
          this.closeButtonProgress = 1;
        } else {
          this.closeButtonProgress = 0;
        }
      }
    },
    startButtonProgress: {
      handler(value) {
          if(value < 100) {
            setTimeout(() => {
              if(value >= 1 && this.startButtonHover)
                this.startButtonProgress++;
            }, 20);
          } else {
            setTimeout(() => {
              this.start_viewing();
            }, 100);
          }
      }
    },
    startButtonHover: {
      handler(value) {
        if(value == true) {
          this.startButtonProgress = 1;
        } else {
          this.startButtonProgress = 0;
        }
      }
    }
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
      this.loading_text = "analyzing image..."

      const response = await axios.get(request_url)
      this.music_data = response.data
      console.log(`number of sections: ${this.music_data.sections.length}`)

      // initialize current note and color
      var first_section = this.music_data.sections[0]
      this.current_note = first_section.note
      this.cursor_color = first_section.color
      // initialize bpm 
      this.bpm = this.music_data.bpm
      
      console.log(`bpm set to: ${this.bpm}`)
      console.log("notes loaded from backend")
      return 
    },

    updateNote(event) {
      if (!this.music_started || this.loading) {
        return 
      }
      var x = event.offsetX
      var y = event.offsetY 
      var section = this.get_note(x, y)
      // update note
      this.current_note = section.note
      // update cursor color
      this.cursor_color = section.color
    },

    play_current_note() {
      let note = this.current_note
      this.synth.triggerAttack(note)
      console.log(`note playing: ${note}`)
    },

    start_music_loop() {
      if (this.music_started && !this.loading && !this.painting_hover) {
        this.play_current_note()
        this.music_interval = setInterval(this.play_current_note, this.bpm_to_ms(this.bpm)) 
        this.painting_hover = true
      } else if (!this.music_started) {
        // for the user to start the music for the first hover
        this.button_hover = true;
        this.start_viewing()
      }
    }, 

    stop_music() {
      if (this.music_started) {
        clearInterval(this.music_interval)
        this.painting_hover = false
      } else {
        // for the user to start the music for the first hover 
        this.button_hover=false; this.cursor_color = undefined;
      }
    },

    async start_viewing() { 
      this.startButtonProgress = 0;     
      this.loading = true

      await this.load_notes()
      
      this.loading_text = "loading piano..."
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
      var section = this.music_data.sections.filter(get_section)
      return section[0]
    },

    bpm_to_ms(bpm) {
      return Math.round((60 / bpm) * 1000)
    },

    calc_index(n, m) {
      return ((n % m) + m) % m
    },

    left_button() {
      var new_index = this.calc_index(this.image_index - 1, this.art_data.length)
      this.image_index = new_index
      this.$router.push('/art-view/' + this.image_index);
      this.music_started = false
    },

    right_button() {
      var new_index = this.calc_index(this.image_index + 1, this.art_data.length)
      this.image_index = new_index
      this.$router.push('/art-view/' + this.image_index);
      this.music_started = false
    }
  }


}
</script>

 <style>
  .close-button {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 1;

    width: 125px;
    height: 125px;
    background-color: transparent;
    border-width: 0;
    background-size: contain;
    background-position: center;
    align-items: center;
    justify-content: center;
    display: flex;
    margin: var(--dl-space-space-unit);
    background-image: url('@/assets/icons/exit.svg');
    pointer-events: none;
  }

  .close-button-animated-progress {
    position: absolute;
    top: 0;
    right: 0;
    width: 125px;
    height: 125px;
    border-radius: 50%;
    border-width: 5px;
    outline-color: lightgrey;
    outline-width: 1px;
    margin: var(--dl-space-space-unit);
    outline-style: solid;
  }

  .close-button-animated-progress span {
    position: relative;
    margin: 50%;
    display: block;
    background: rgb(117, 117, 117);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    position: absolute;
  }

  .toggle-button {
    position: absolute;
    top: 0;
    left: 0;
    margin: var(--dl-space-space-twounits);
    display: flex;
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
    width: auto;
    max-width: calc(100% - 200px);
    max-height: calc(100% - 50px);
    object-fit: contain;
    margin-top: var(--dl-space-space-halfunit);
    margin-bottom: var(--dl-space-space-unit);
  }

  .caption {
    width: 100%;
    text-align: center;
    margin-bottom: var(--dl-space-space-twounits)
  }

  .start-info {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .arrow-box-right {
    width: 100px;
    height: 500px;
    background-color: transparent;

    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
    z-index: 1;
    border-width: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    align-items: center;
    justify-content: center;
    display: flex;
    border-radius: 20px;
  }

  .arrow-box-left {
    width: 100px;
    height: 500px;
    background-color: transparent;

    position: absolute;
    top: 50%;
    left: 20px;
    transform: translateY(-50%);
    z-index: 1;
    border-width: 0;
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    align-items: center;
    justify-content: center;
    display: flex;
    border-radius: 20px;
  }

  .arrow-box-right:hover {
    background-color: rgb(185, 185, 185);
  }

  .arrow-box-left:hover {
    background-color: rgb(185, 185, 185);
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
    left: 37px;
    background-image: url('@/assets/icons/left.svg');  
    pointer-events: none;
  }
  .nav-right {
    right: 37px;
    background-image: url('@/assets/icons/right.svg'); 
    pointer-events: none;

  }

  .animated-progress {
    position: absolute;
    width: 125px;
    max-width: 10%;
    height: 500px;
    max-height: 50%;
    border-radius: 5px;
    border-width: 5px;
    outline-color: lightgrey;
    outline-width: 1px;
    outline-style: solid;
  }

  .right-arrow-progress {
    right: -1px;
    
  }

  .left-arrow-progress {
    left: -1px;
    
  }

  .animated-progress span {
    height: 100%;
    display: block;
    color: purple;
    background: rgb(117, 117, 117);
    border-radius: 5px;
    position: absolute;
    top: 0;
  }

  .left-arrow-progress span {
    right: 0;
  }

  .right-arrow-progress span {
    left: 0;
  }

</style>