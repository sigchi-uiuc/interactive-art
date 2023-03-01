<template>
    <carousel :itemsToShow="3">
      <slide v-for="(item, index) in art_data" :key="item.file">
        <div>
            <h2>{{item.title}}</h2>
            <img class="car_img" :src="require(`@/assets/${item.file}`)">
            <p>{{item.artist}}</p>
            <p>{{item.date}}</p>
            <router-link :to="'/art-view/' + index">
                <button class="view-button">
                    View Art
                </button>
            </router-link>
        </div>
      </slide>
  
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </template>
<!-- ask how to format things around -->

<script>
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
    const ART_DATA = require("@/assets/art_data.json")    
    export default {
        name: 'CarouselView',
        components: {
            Carousel,
            Slide,
            Pagination,
            Navigation,
        },
        data() {
            return {
                art_data: ART_DATA
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
    }

</style>

