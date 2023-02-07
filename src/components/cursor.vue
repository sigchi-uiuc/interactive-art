<template>
    <div
      class="cursor-circle"
      :style="{ left: x + 'px', top: y + 'px', 'background-color': 'rgba(' + color.toString() + ',' + transparency + ')'}"
    ></div>
  </template>
  
  <script>
  export default {
    props: {
        color: {
            type: Array,
            default: [0,0,0]
        }
    },
    data() {
      return {
        x: 0,
        y: 0,
        transparency: '0.6'
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
        this.x = event.clientX;
        this.y = event.clientY;
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
    outline: solid
  }
  </style>
  