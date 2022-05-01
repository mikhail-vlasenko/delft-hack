<template>
  <q-page>
    <div class="row">
      <div class="justify-center full-height full-width text-center">
        <divzzz class="q-pa-md row items-start q-gutter-md">
          <q-card class="my-card">
            <q-card-section>
              <q-slider
                v-model="model"
                marker-labels
                :min="0"
                :max="6"
              />
            </q-card-section>
          </q-card>
        </divzzz>
      </div>
    </div>

  </q-page>
</template>

<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      slider: ref(50),
      range: ref({
        min: 10,
        max: 30
      }),

      knob: ref(50),

      time: ref(''),
      date: ref('')
    }
  }
}
</script>
