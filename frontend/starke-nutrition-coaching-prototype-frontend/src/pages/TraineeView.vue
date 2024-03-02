<template>
  <q-page class="text-center">
    <div class="text-h5 q-pt-lg">Target macros</div>
    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>
          <td class="text-center">{{recipeKcal}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
          <td class="text-center">{{recipeProteins}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
          <td class="text-center">{{recipeCarbs}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
          <td class="text-center">{{recipeFats}}</td>
        </tr>
        </tbody>
      </q-markup-table>
    </div>

    <div class="text-h5 q-mb-md">Suggested recipe</div>

    <div class="image-container">
      <q-img :src="recipeImgPath" class="recipe-img" />
      <div class="image-overlay"></div>
      <div class="text-h5 text-bold recipe-title">{{recipeTitle}}</div>
    </div>

    <div class="q-pt-sm">
      <q-text>
        {{recipeKcal}} kcal,
        {{recipeProteins}} proteins,
        {{recipeCarbs}} carbs,
        {{recipeFats}} fat
      </q-text>
    </div>

    <q-btn color="primary" class="q-mt-md q-mb-xl" label="Recipe details" />
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'TraineeView',

  data() {
    return {
      recipeTitle: '',
      recipeKcal: '0',
      recipeProteins: '0g',
      recipeCarbs: '0g',
      recipeFats: '0g',
      recipeImgPath: '',
    };
  },

  mounted() {
    this.fetchRecipe();
  },

  methods: {
    fetchRecipe() {
      axios.get('http://127.0.0.1:8000/latest_recipe')
        .then(response => {
          this.recipeTitle = response.data.title;
          this.recipeKcal = response.data.calories;
          this.recipeProteins = response.data.protein;
          this.recipeCarbs = response.data.carbs;
          this.recipeFats = response.data.fat;
          this.recipeImgPath = response.data.image;
        })
        .catch(error => {
          console.error('Error:', error);
        });
    },
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
