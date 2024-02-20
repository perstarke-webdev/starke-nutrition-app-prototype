<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <div class="q-px-lg q-pt-xl q-mb-md">
        <div class="text-h5 text-center">Starke Nutrition Coaching (Prototype)</div>
        <hr>
        <div class="text-h6 text-center">Meal-planning</div>
      </div>
      <q-img
        src="~assets/header.jpg"
        class="header-image absolute-top"/>
    </q-header>


    <q-footer class="footer">
      <div class="flex flex-center column">
        <div class="q-pa-md">
          <div class="q-gutter-x-md">
              <router-link to="/coach">
                  <q-btn class="slight-rounded" rounded color="primary" label="Coach"/>
              </router-link>
              <router-link to="/trainee">
                  <q-btn class="slight-rounded" rounded color="primary" label="Trainee"/>
              </router-link>
            <q-btn class="slight-rounded" rounded color="primary" label="X"/>
            <q-btn class="slight-rounded" rounded color="primary" label="X"/>
            <q-btn class="slight-rounded" rounded color="primary" label="X"/>
          </div>
        </div>
      </div>
    </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MainLayout'
})
</script>

<style lang="scss">

  .header-image {
    height: 100%;
    z-index: -1;
    opacity: 0.2;
  }

  .footer {
    background-color: grey;
  }

  .slight-rounded {
    border-radius: 5px;
  }
</style>
