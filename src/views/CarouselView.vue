<template>
        <carousel :itemsToShow="3">
            <slide v-for="(item, index) in art_data" :key="item.file">
              <div>
                  <h2>{{item.title}}</h2>
                  <img class="car_img" :src="require(`@/assets/${item.file}`)">
                  <p>{{item.artist}}</p>
                  <p>{{item.date}}</p>
                      <button class="view-button" @:mouseover="viewArtButtonHover = true; artIndex = index; button_hover=true" 
                                                  @:mouseleave="viewArtButtonHover = false; button_hover=false"
                                                  @:click="this.$router.push('/art-view/' + this.artIndex)">
                          <span :id="'art/' + index"></span>
                          <div class="view-art-text"> View Art </div>
                      </button>
              </div>
            </slide>
        
            <template #addons>
              <navigation />
              <pagination />
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
    .car_img {
        height: 300px;
        object-fit: contain;
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

