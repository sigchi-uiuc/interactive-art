<template>
    <div class="alert-container">
      <div class="alert-container1" :style="{height: alert_height + 'px'}">
        <svg viewBox="0 0 1024 1024" class="alert-icon">
          <path
            d="M470 384v-86h84v86h-84zM512 854q140 0 241-101t101-241-101-241-241-101-241 101-101 241 101 241 241 101zM512 86q176 0 301 125t125 301-125 301-301 125-301-125-125-301 125-301 301-125zM470 726v-256h84v256h-84z"
          ></path>
        </svg>
        <span class="alert-text">{{ text }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Alert',
    props: {
      text: {
        type: String,
        default: 'Make sure your browser autoplay is on!',
      }, 
      alert_height: {
        type: Number,
        default: 50
      }
    },
  }
  </script>
  
  <style scoped>
  .alert-container {
    width: auto;
    height: auto;
    display: flex;
    position: relative;
    align-items: flex-start;
    border-radius: var(--dl-radius-radius-radius8);
    flex-direction: column;
  }
  .alert-container1 {
    flex: 0 0 auto;
    width: 100%;
    display: flex;
    align-items: flex-start;
    border-radius: var(--dl-radius-radius-radius8);
    background-color: rgba(7, 19, 24, 0.888);
  }
  .alert-icon {
    fill: #25A6E0;
    width: 20px;
    height: 20px;
    margin: var(--dl-space-space-halfunit);
    align-self: center;
  }
  .alert-text {
    color: #B8E7FB;
    align-self: center;
    margin-right: var(--dl-space-space-unit);
  }
  </style>
  