<template>
  <q-page class="text-center">

    <div class="text-h5 q-pt-lg">Nutritional requirements</div>

    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>
            <q-input input-class="text-center" outlined v-model="kcal" type="number" />
        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
            <q-input input-class="text-center" outlined v-model="proteins" type="number" />
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
            <q-input input-class="text-center" outlined v-model="carbs" type="number" />
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
            <q-input input-class="text-center" outlined v-model="fats" type="number" />
        </tr>
        </tbody>
      </q-markup-table>


      <q-btn color="primary" class="q-mt-md" label="Submit" />

    </div>

      <div class="text-h5 q-mb-md">Suggested recipe</div>

      <div class="image-container">
        <q-img src="~assets/oatbar.webp" class="recipe-img" />
        <div class="image-overlay"></div>
        <div class="text-h5 text-bold recipe-title">Oat-Nut-Bar</div>
      </div>

      <div class="q-pt-sm">
      <q-text>
        {{kcal}} kcal,
        {{proteins}}g proteins,
        {{carbs}}g carbs,
        {{fats}}g fat
      </q-text>
      </div>

    <q-btn color="primary" class="q-mt-md" label="Recipe details" />
    <br>

    <div class="q-gutter-x-md q-mb-xl">
      <q-btn color="primary" class="q-mt-md" label="Generate new" />
      <q-btn color="primary" class="q-mt-md" label="Send to trainee" />
    </div>

    <div>
      <div class="text-h5 q-mb-xl">Title: {{title}}</div>
    </div>

  </q-page>
</template>




<script>
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'CoachView',

  data() {
    return {
      kcal: '0',
      proteins: '0',
      carbs: '0',
      fats: '0',
      title: null,
    };
  },

    mounted() {
    // Make an HTTP request after the component is mounted
    axios.get('http://127.0.0.1:8000/get_recipe?kcal=600&proteins=50&carbs=70&fats=10')
      .then(response => {
        // If the request is successful, save the title from the JSON response in the title data property
        this.title = response.data.title;
      })
      .catch(error => {
        // Handle errors
        console.error('Error:', error);
      });
  },

});
</script>




<style lang="scss">

.image-container {
  position: relative;
}

.image-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  max-width: 600px;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1;
}

.recipe-img {
  width: 80%;
  max-width: 600px;
}

.recipe-title {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  z-index: 2;
}

</style>
