<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <div class="q-px-lg q-pt-xl q-mb-md">
        <div class="text-h5 text-center">Starke Nutrition Coaching</div>
        <hr>
        <div class="text-h6 text-center">Meal-planning</div>
      </div>
      <q-img
        src="~assets/header.jpg"
        class="header-image absolute-top"/>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'


export default defineComponent({
  name: 'MainLayout',

  setup () {
  }

})
</script>

<style lang="scss">
  .header-image {
    height: 100%;
    z-index: -1;
    opacity: 0.2;
  }
</style>
