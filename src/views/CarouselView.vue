<template>
        <div class="nav-bar">
            <div class="logo-container">
                <img :src="require('@/assets/icons/eyes.png')" class="logo">
                <h1>
                    Melodic Eyes
                </h1>
            </div>
            <button class="learn-button" @:click="this.$router.push('about')">
                Learn More
            </button>
        </div>
        <hr class="divider">

        <div class="info-text">
            <h2 class="info-text-style">
                This is how you use Melodic Eyes, I would give you better instructions, but I can't think of how to phrase it.
            </h2>
        </div>

        <carousel :itemsToShow="3">
            <slide v-for="(item, index) in art_data" :key="item.file">
              <div class="card-container">
                    <h3>{{item.title}}</h3>

                    <img class="car_img" :src="require(`@/assets/${item.file}`)">
                    <div class="card-content">
                        <p>{{item.artist + " - " + item.date}}</p>
                        <button class="view-button" @:mouseover="viewArtButtonHover = true; artIndex = index; button_hover=true" 
                                                    @:mouseleave="viewArtButtonHover = false; button_hover=false"
                                                    @:click="this.$router.push('/art-view/' + this.artIndex)">
                            <span :id="'art/' + index"></span>
                            <div class="view-art-text"> View Art </div>
                        </button>
                    </div>
              </div>
            </slide>
        
            <template #addons>
              <navigation />
            </template>
          </carousel>
        <cursor :hover_on="button_hover"/>
  </template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import cursor from '@/components/cursor.vue'

const ART_DATA = require("@/assets/art_data.json")    

    export default {
        name: 'CarouselView',
        components: {
            Carousel,
            Slide,
            cursor,
            Pagination,
            Navigation,
        },
        data() {
            return {
                art_data: ART_DATA,
                viewArtButtonProgress: 0,
                viewArtButtonHover: false,
                artIndex: 0,
                button_hover: false
            }
        },
        watch: {
            viewArtButtonProgress: {
                handler(value) {
                    if(value < 100) {
                        setTimeout(() => {
                        if(value >= 1 && this.viewArtButtonHover)
                            this.viewArtButtonProgress++;
                            let greyButton = document.getElementById('art/' + this.artIndex);
                            greyButton.style.width = this.viewArtButtonProgress + 'px';
                        }, 20);
                    } else {
                        setTimeout(() => {
                        this.$router.push('/art-view/' + this.artIndex);
                        this.viewArtButtonProgress = 0;
                        let greyButton = document.getElementById('art/' + this.artIndex);
                        greyButton.style.width = this.viewArtButtonProgress + 'px';

                        }, 100);
                    }
                }
            },

            viewArtButtonHover: {
                handler(value) {
                if(value == true) {
                    this.viewArtButtonProgress = 1;
                    let greyButton = document.getElementById('art/' + this.artIndex);
                    greyButton.style.width = this.viewArtButtonProgress + 'px';
                } else {
                    this.viewArtButtonProgress = 0;
                    let greyButton = document.getElementById('art/' + this.artIndex);
                    greyButton.style.width = this.viewArtButtonProgress + 'px';
                }
            }
            }
        }
    } 

</script> 

<style scoped>
    .nav-bar {
        display: flex;  
        align-items: center;
        justify-content: space-between;
    }

    .logo-container {
        display: flex;
        align-items: center;
        margin-left: var(--dl-space-space-unit);
        order: 1;
    }

    .logo {
        width: 100px;
        height: 100px;
    }

    .learn-button {
        order: 2;
        margin-right: var(--dl-space-space-unit);

        background-color: rgba(50, 168, 80, 0.6);
        font-size: 16px;
        width: 100px;
        height: var(--dl-size-size-small);
        border-width: 3px;
        border-color: var(--dl-color-gray-500);
        border-radius: var(--dl-radius-radius-radius8);
        box-shadow: 0px 4px 2px 0px #595959;
        position: relative;
    }

    .info-text {
        margin-bottom: 35px;
    }

    .divider {
        margin-left: var(--dl-space-space-unit);
        margin-right: var(--dl-space-space-unit);
    }

    .card-container {
        border-radius: 4px;
        background-color: #fff;
        box-shadow: 0 3px 1px -2px rgba(0,0,0,.2), 0 2px 2px 0 rgba(0,0,0,.14), 0 1px 5px 0 rgba(0,0,0,.12);
        color: rgba(0,0,0,.87);

        overflow: hidden;
        position: relative;
        width: 410px;
        height: 450px;
        margin-bottom: var(--dl-space-space-unit);
        margin-top: var(--dl-space-space-unit);
    }
    .car_img {
        object-fit: cover;
        height: 70%;
        width: 100%;
    }

    .card-content {
        overflow: hidden;
        position: absolute; /* Position the text relative to the card container */
        bottom: 0;
        left: 0;
        width: 100%;
        height: 30%; /* Set the height of the text container */
        background-color: #fff; /* Set the background color of the text container */
      }
    
    .view-button {
        margin: var(--dl-space-space-halfunit);
        align-items: center;
        justify-content: center;

        background-color: white;
        font-size: 16px;
        width: 100px;
        height: var(--dl-size-size-small);
        border-width: 3px;
        border-color: var(--dl-color-gray-500);
        border-radius: var(--dl-radius-radius-radius8);
        box-shadow: 0px 4px 2px 0px #595959;
        position: relative;
    }

    .view-art-text {
    position: relative;
    z-index: 10;
  }

    .view-button span {
        top: 0;
        left: 0;
        height: 100%;
        max-width: 100%;
        border-width: 3px;
        border-radius: var(--dl-radius-radius-radius6);
        display: block;
        background: rgb(193, 193, 193);;
        position: absolute;
        z-index: 0 !important; 
    }

</style>

