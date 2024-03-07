<template>
  <q-page class="text-center">
    <div class="text-h5 q-pt-lg">Target macros</div>
    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>
          <td class="text-center">{{wanted_kcal}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
          <td class="text-center">{{wanted_proteins}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
          <td class="text-center">{{wanted_carbs}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
          <td class="text-center">{{wanted_fats}}</td>
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

    <q-btn
      color="primary"
      class="q-mt-md q-mb-xl"
      label="Recipe details"
      :href="recipe_link"
      target="_blank"
    />
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'TraineeView',

  data() {
    return {
      recipe_id: '0',
      wanted_kcal: '0',
      wanted_proteins: '0',
      wanted_carbs: '0',
      wanted_fats: '0',
      recipeTitle: '',
      recipeKcal: '0',
      recipeProteins: '0g',
      recipeCarbs: '0g',
      recipeFats: '0g',
      recipeImgPath: '',
      recipe_link: '',
    };
  },

  mounted() {
    this.fetchRecipe();
  },

  methods: {
    fetchRecipe() {
      axios.get('https://sna-prototype-backend-v2.vercel.app/latest_recipe')
        .then(response => {
          this.recipe_id = response.data.id;
          this.recipeTitle = response.data.title;
          this.recipeKcal = response.data.calories;
          this.recipeProteins = response.data.protein;
          this.recipeCarbs = response.data.carbs;
          this.recipeFats = response.data.fat;
          this.recipeImgPath = response.data.image;
          this.wanted_kcal = response.data.wanted_kcal;
          this.wanted_proteins = response.data.wanted_proteins;
          this.wanted_carbs = response.data.wanted_carbs;
          this.wanted_fats = response.data.wanted_fats;

          axios.get('https://sna-prototype-backend-v2.vercel.app/get_link', {
            params: {
              recipe_id: this.recipe_id,
            },
          })
          .then((linkResponse) => {
            this.recipe_link = linkResponse.data;
          })
          .catch((linkError) => {
            console.error('Error fetching recipe link:', linkError);
          });
        })
        .catch(error => {
          console.error('Error fetching recipe:', error);
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
