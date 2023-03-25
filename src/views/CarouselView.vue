<template>
        <div class="nav-bar">
            <div class="logo-container">
                <img :src="require('@/assets/icons/eyes.png')" class="logo">
                <h1>
                    Melodic Eyes
                </h1>
            </div>
            <button class="learn-button no-cursor" 
                @:click="this.$router.push('about')"
                @:mouseover="this.cursor_color = [255,255,255]"
                @:mouseleave="this.cursor_color = undefined">
                Learn More
            </button>
        </div>
        <hr class="divider">

        <div class="info-text">
            <h2 class="info-text-style">
                Hear what you see, as the colors in the section of the painting you are looking at are transformed into piano chords.
            </h2>
        </div>

        <carousel ref="artCarousel" :itemsToShow="3" :transition="500" :wrapAround="true">
            <slide v-for="(item, index) in art_data" :key="item.file">
              <div class="card-container carousel__item"
                    @:mouseover="viewArtButtonHover = true; artIndex = index; button_hover=true" 
                    @:mouseleave="viewArtButtonHover = false; button_hover=false"
                    @:click="this.$router.push('/art-view/' + this.artIndex)">
                    <h3>{{item.title}}</h3>

                    <img class="car_img" :src="require(`@/assets/${item.file}`)">
                    <div class="card-content">
                        <p>{{item.artist + " - " + item.date}}</p>
                        <button class="view-button no-cursor">
                            <span :id="'art/' + index" :style="{ 'width': slideHoverProgress[index] + 'px' }"></span> <!--Grey button on hover-->
                            <div class="view-art-text"> View Art </div>
                        </button>
                    </div>
              </div>
            </slide>
        
            <template #addons>
              <navigation />
            </template>
          </carousel>

        <div class="alert-container">
            <alert :alert_height="25"> </alert>
        </div>

        <div class="animated-progress left-arrow-progress slide-arrow" 
            @:mouseover="leftArrowHover = true; button_hover = true"                   
            @:mouseleave="leftArrowHover = false; button_hover=false; cursor_color = undefined"
            @:click="leftArrowProgress = 0; slide_left(); ">
            <span :style="{ 'width': leftArrowProgress + 'px' }"></span>
            <button class="lightbox-nav nav-left"></button>
        </div>
        

        <div class="animated-progress right-arrow-progress slide-arrow" 
            @:mouseover="rightArrowHover = true; button_hover = true" 
            @:mouseleave="rightArrowHover = false; button_hover=false; cursor_color = undefined"
            @:click=" rightArrowProgress = 0; slide_right();">
            <span :style="{ 'width': rightArrowProgress + 'px' }"></span>
            <button class="lightbox-nav nav-right"></button>
        </div>
        

        <cursor :hover_on="button_hover" :color="cursor_color"/>
  </template>

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import cursor from '@/components/cursor.vue'
import alert from '@/components/alert.vue'


const ART_DATA = require("@/assets/art_data.json")    


    export default {
        name: 'CarouselView',
        components: {
            Carousel,
            Slide,
            cursor,
            alert,
            Pagination,
            Navigation,
        },
        data() {
            return {
                art_data: ART_DATA,
                viewArtButtonProgress: 0,
                viewArtButtonHover: false,
                artIndex: 0,
                button_hover: false,
                cursor_color: undefined,
                rightArrowProgress: 0,
                rightArrowHover: false,
                leftArrowProgress: 0,
                leftArrowHover: false,
                slideHoverProgress: new Array(ART_DATA.length).fill(0)
            }
        },
        watch: {
            viewArtButtonProgress: {
                handler(value) {
                    this.slideHoverProgress[this.artIndex] = this.viewArtButtonProgress;
                    if(value < 100) {
                        setTimeout(() => {
                        if(value >= 1 && this.viewArtButtonHover)
                            this.viewArtButtonProgress++;
                        }, 35);
                    } else {
                        setTimeout(() => {
                        this.$router.push('/art-view/' + this.artIndex);
                        this.viewArtButtonProgress = 0;
                        }, 100);
                    }
                }
            },

            viewArtButtonHover: {
                handler(value) {
                    this.viewArtButtonProgress = value ? 1 : 0;
            }
            },
            rightArrowProgress: {
                handler(value) {
                    if(value < 70) { // Note: value must be equal to button width
                        setTimeout(() => {
                        if(value >= 1 && this.rightArrowHover)
                            this.rightArrowProgress++;
                        }, 20);
                    } else {
                        setTimeout(() => {
                        this.rightArrowProgress = 1;
                        this.slide_right();
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
                    if(value < 70) {
                        setTimeout(() => {
                        if(value >= 1 && this.leftArrowHover)
                            this.leftArrowProgress++;
                        }, 20);
                    } else {
                        setTimeout(() => {
                        this.leftArrowProgress = 1;
                        this.slide_left();
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
            }
        },
        methods: {
            slide_left() {
                this.$refs.artCarousel.prev();
            },
            slide_right() {
                this.$refs.artCarousel.next();
            },

        }
    } 

</script> 

<style scoped>
    .nav-bar {
        display: flex;  
        align-items: center;
        justify-content: space-between;
    }

    .carousel {
        width: 90%;
        left: 5%;
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
        width: 120px;
        height: var(--dl-size-size-small);
        border-width: 3px;
        border-color: var(--dl-color-gray-500);
        border-radius: var(--dl-radius-radius-radius8);
        box-shadow: 0px 4px 2px 0px #595959;
        position: relative;
    }

    .learn-button:hover {
        background-color: white;
    }

    .info-text {
        margin-bottom: 0px;

        flex: 0 0 auto;
        width: auto;
        display: flex;
        align-items: flex-start;
        flex-direction: column;
    }

    .info-text-style {
        align-self: center;
        text-align: center;
    }

    .alert-container {
        margin-top: 15px;
        margin-bottom: 0px;

        width: auto;
        align-self: center;
        flex: 0 0 auto;
        display: flex;
        align-items: flex-start;
        flex-direction: column;
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

    .slide-arrow {
        position: absolute;
        top: calc(210px) !important;
        
        width: 70px;
    }

    .lightbox-nav {
        width: 50px;
        height: 50px;
    }

    .nav-left {
        left: 10px;
    }

    .nav-right {
        right: 10px;
    }


</style>

<style>
    .carousel__icon {
        display: none !important;
    }
</style>
