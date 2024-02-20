<template>
  <q-page class="text-center">

    <div class="text-h5 q-pt-lg">Target macros</div>

    <div class="q-pa-md">
      <q-markup-table separator="cell">
        <tbody>
        <tr>
          <td class="text-center text-bold">Kcal</td>
          <td class="text-center">{{kcal}}</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Proteins</td>
          <td class="text-center">{{proteins}}g</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Carbs</td>
          <td class="text-center">{{carbs}}g</td>
        </tr>
        <tr>
          <td class="text-center text-bold">Fats</td>
          <td class="text-center">{{fats}}g</td>
        </tr>
        </tbody>
      </q-markup-table>
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

    <q-btn color="primary" class="q-mt-md q-mb-xl" label="Recipe details" />

  </q-page>
</template>




<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TraineeView',
  data() {
    return {
      kcal: '0',
      proteins: '0',
      carbs: '0',
      fats: '0',
    };
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
