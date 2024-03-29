<template>
  <q-page class="text-center">
    <div class="text-h5 q-pt-lg">Nutritional requirements</div>

    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>
          <q-input
            input-class="text-center"
            data-test="input"
            outlined
            :select-on-focus="true"
            v-model="kcal_wanted"
            type="number"
          />
        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
          <q-input
            input-class="text-center"
            data-test="input"
            outlined
            v-model="proteins_wanted"
            type="number"
          />
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
          <q-input
            input-class="text-center"
            data-test="input"
            outlined
            v-model="carbs_wanted"
            type="number"
          />
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
          <q-input
            input-class="text-center"
            data-test="input"
            outlined
            v-model="fats_wanted"
            type="number"
          />
        </tr>
        </tbody>
      </q-markup-table>
      <q-btn
        data-test="submit-btn"
        color="primary"
        class="q-mt-md"
        label="Submit"
        @click="submitForm"
      />
    </div>

    <div class="text-h5 q-mb-md">Suggested recipe</div>

    <div class="image-container">
      <q-img data-test="recipe-img" :src="recipe_img_path" class="recipe-img" />
      <div class="image-overlay"></div>
      <div class="text-h5 text-bold recipe-title">{{recipe_title}}</div>
    </div>

    <div class="q-pt-sm">
      <q-text data-test="received-nutrients">
        {{recipe_kcal}} kcal, {{recipe_proteins}} proteins, {{recipe_carbs}} carbs, {{recipe_fats}} fat
      </q-text>
    </div>

    <q-btn
      color="primary"
      class="q-mt-md"
      label="Recipe details"
      :href="recipe_link"
      target="_blank"
    />
    <br />

    <div class="q-gutter-x-md q-mb-xl">
      <q-btn
        color="primary"
        class="q-mt-md"
        label="Generate new"
        @click="submitForm"
      />
      <q-btn
        v-if="!sendToTraineeSuccess"
        :color="sendToTraineeSuccess ? 'secondary' : 'primary'"
        :class="{ 'q-opacity-half': sendToTraineeSuccess }"
        class="q-mt-md"
        label="Send to trainee"
        @click="handleSendToTrainee"
      />
      <q-btn
        v-if="sendToTraineeSuccess"
        :color="sendToTraineeSuccess ? 'secondary' : 'primary'"
        class="q-mt-md"
        label="Successfully sent to trainee"
      />
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
      recipe_link: null,
      recipe_title: null,
      recipe_calories: '0',
      recipe_proteins: '0g',
      recipe_carbs: '0g',
      recipe_fats: '0g',
      recipe_img_path: null,
      sendToTraineeSuccess: false,
    };
  },

  computed: {
    sendToTraineeButtonLabel() {
      return this.sendToTraineeSuccess ? 'Successfully sent to trainee' : 'Send to trainee';
    },
    sendToTraineeButtonColor() {
      return this.sendToTraineeSuccess ? 'secondary' : 'primary';
    },
  },

  methods: {
    submitForm() {
      axios
        .get('https://sna-prototype-backend-v2.vercel.app/get_recipe', {
          params: {
            kcal: this.kcal_wanted,
            proteins: this.proteins_wanted,
            carbs: this.carbs_wanted,
            fats: this.fats_wanted,
          },
        })
        .then((response) => {
          this.recipe_id = response.data.id;
          this.recipe_title = response.data.title;
          this.recipe_kcal = response.data.calories;
          this.recipe_proteins = response.data.protein;
          this.recipe_carbs = response.data.carbs;
          this.recipe_fats = response.data.fat;
          this.recipe_img_path = response.data.image;

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
        .catch((error) => {
          console.error('Error:', error);
        });
    },

    deleteAllRecipes() {
      axios
        .get('https://sna-prototype-backend-v2.vercel.app/delete_all_recipes')
        .then((response) => {
          console.log('All recipes deleted successfully:', response);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },

    sendToTrainee() {
  this.deleteAllRecipes();

  axios
    .post('https://sna-prototype-backend-v2.vercel.app/write_recipe', {
      id: this.recipe_id,
      title: this.recipe_title,
      kcal: this.recipe_kcal,
      proteins: this.recipe_proteins,
      carbs: this.recipe_carbs,
      fats: this.recipe_fats,
      image_path: this.recipe_img_path,
      wanted_kcal: this.kcal_wanted,
      wanted_proteins: this.proteins_wanted,
      wanted_carbs: this.carbs_wanted,
      wanted_fats: this.fats_wanted,
    })
    .then((response) => {
      console.log('Response:', response.data);
      this.sendToTraineeSuccess = true;
    })
    .catch((error) => {
      console.error('Error:', error);
    })
},


    handleSendToTrainee() {
      this.sendToTrainee();
      setTimeout(() => {
        this.sendToTraineeSuccess = false;
      }, 3000);
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
