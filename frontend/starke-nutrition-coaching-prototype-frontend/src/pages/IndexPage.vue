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
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
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
