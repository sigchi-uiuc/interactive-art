<template>
    <div v-if="initial_mouse_move"
      class="cursor-circle"
      :style="[hover_on ? { left: x + 'px', top: y + 'px', 'background-color': 'rgba(' + hover_color.toString() + ',' + transparency + ')'} :
                          { left: x + 'px', top: y + 'px', 'background-color': 'rgba(' + color.toString() + ',' + transparency + ')'}]"
    ></div>
  </template>
  
  <script>
  export default {
    props: {
        color: {
            type: Array,
            default: [0,0,0]
        },
        hover_on: {
          type: Boolean,
          default: false
        }
    },
    data() {
      return {
        x: 0,
        y: 0,
        transparency: '0.6',
        initial_mouse_move: false,
        hover_color: [50, 168, 80]
      };
    },
    mounted() {
      document.addEventListener("mousemove", this.updatePosition);
    },
    beforeDestroy() {
      document.removeEventListener("mousemove", this.updatePosition);
    },
    methods: {
      updatePosition(event) {
        this.initial_mouse_move = true
        this.x = event.clientX - 30;
        this.y = event.clientY - 30;
      }
    }
  };
  </script>
  
  <style>
  .cursor-circle {
    position: fixed;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    transition: all 0.2s ease-out;
    outline-color: black;
    outline-width: 10px;
    outline: solid;
    pointer-events: none;
  }
  </style>
  