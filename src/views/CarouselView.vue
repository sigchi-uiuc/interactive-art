
<!-- <template>
    <Carousel>
        <div v-for="item in art_data" :key="item.file">
            <slide>
                <h2>{{item.title}}</h2>
                link: 'assets\' + {{item.file}}
                <img :src=link>
                <p>{{item.artist}}</p>
                <p>{{item.date}}</p>
                @slideclick="handleSlideClick"> 
            </slide>
        </div>
    </Carousel>
</template> -->
<template>
    <carousel :itemsToShow="3">
      <slide v-for="item in art_data" :key="item.file">
        <div>
            <h2>{{item.title}}</h2>
            <img class="car_img" :src="require(`@/assets/${item.file}`)">
            <p>{{item.artist}}</p>
            <p>{{item.date}}</p>
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
//import { Carousel, Slide } from 'vue-carousel';
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
        width: 50%;
        height: 50%;
    }
</style>

