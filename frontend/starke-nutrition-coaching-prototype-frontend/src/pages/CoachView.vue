<template>
  <q-page class="text-center">

    <div class="text-h5 q-pt-lg">Nutritional requirements</div>

    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>

            <q-input input-class="text-center"
                     data-test="input"
                     outlined
                     :select-on-focus="true"
                     v-model="kcal_wanted"
                     type="number" />

        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
            <q-input input-class="text-center" data-test="input" outlined v-model="proteins_wanted" type="number" />
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
            <q-input input-class="text-center" data-test="input" outlined v-model="carbs_wanted" type="number" />
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
            <q-input input-class="text-center" data-test="input" outlined v-model="fats_wanted" type="number" />
        </tr>
        </tbody>
      </q-markup-table>


      <q-btn data-test="submit-btn" color="primary" class="q-mt-md" label="Submit" @click="submitForm" />


    </div>

      <div class="text-h5 q-mb-md">Suggested recipe</div>

      <div class="image-container">
        <q-img data-test="recipe-img" :src="recipe_img_path" class="recipe-img" />
        <div class="image-overlay"></div>
        <div class="text-h5 text-bold recipe-title">{{recipe_title}}</div>
      </div>

      <div class="q-pt-sm">
      <q-text data-test="received-nutrients">
        {{recipe_kcal}} kcal,
        {{recipe_proteins}} proteins,
        {{recipe_carbs}} carbs,
        {{recipe_fats}} fat
      </q-text>
      </div>

    <q-btn color="primary" class="q-mt-md" label="Recipe details"/>
    <br>

    <div class="q-gutter-x-md q-mb-xl">
      <q-btn color="primary" class="q-mt-md" label="Generate new" @click="submitForm"/>
      <q-btn color="primary" class="q-mt-md" label="Send to trainee" @click="sendToTrainee" />
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
      kcal_wanted: '0',
      proteins_wanted: '0',
      carbs_wanted: '0',
      fats_wanted: '0',
      recipe_id: '0',
      recipe_title: null,
      recipe_calories: '0',
      recipe_proteins: '0g',
      recipe_carbs: '0g',
      recipe_fats: '0g',
      recipe_img_path: null,
    };
  },

  methods: {

    submitForm() {
      axios.get('http://127.0.0.1:8000/get_recipe', {
        params: {
          kcal: this.kcal_wanted,
          proteins: this.proteins_wanted,
          carbs: this.carbs_wanted,
          fats: this.fats_wanted,
        }
      })
      .then(response => {
        this.recipe_id = response.data.id;
        this.recipe_title = response.data.title;
        this.recipe_kcal = response.data.calories;
        this.recipe_proteins = response.data.protein;
        this.recipe_carbs = response.data.carbs;
        this.recipe_fats = response.data.fat;
        this.recipe_img_path = response.data.image;
      })
      .catch(error => {
        console.error('Error:', error);
      });
    },


    sendToTrainee() {

      axios.get('http://127.0.0.1:8000/write_recipe', {
          params: {
            id: this.recipe_id,
            title: this.recipe_title,
            calories: this.recipe_kcal,
            protein: this.recipe_proteins,
            carbs: this.recipe_carbs,
            fat: this.recipe_fats,
            image: this.recipe_img_path,
          }
        })
        .then(response => {
          console.log('Response:', response);
        })
        .catch(error => {
          console.error('Error:', error);
        });

  }

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
