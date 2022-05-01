<template>
  <q-layout view="hhh lpR fFf">

    <q-header elevated class="bg-primary text-white q-mb-xl">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
          </q-avatar>
          Travel Planner
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

<!--    <q-page-container>-->
<!--      <router-view />-->
<!--    </q-page-container>-->
    <q-page class="flex flex-center">
      <q-card class="col-8 q-mt-xl">
        <q-card-section class="col-12 full-width">
          <h1>Travel Planner</h1>
          <q-form
            action="https://webhook.site/5f87d83b-b7d1-4b35-ab61-5c6c1ade027e"
            method="post"
            @submit.prevent="onSubmit"
          >
            <q-card class="q-pa-lg q-mb-md">
              <p>Overall Safety</p>
              <q-field outlined name="safety">
                <q-slider
                  name="safety"
                  v-model="safety"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Low Prices</p>
              <q-field outlined name="price">
                <q-slider
                  name="price"
                  v-model="price"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Good Weather</p>
              <q-field outlined name="weather">
                <q-slider
                  name="weather"
                  v-model="weather"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Knowledge of English</p>
              <q-field outlined name="english">
                <q-slider
                  name="english"
                  v-model="english"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Walkability</p>
              <q-field outlined name="walkability">
                <q-slider
                  name="walkability"
                  v-model="walkability"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Cleanliness</p>
              <q-field outlined name="cleanliness">
                <q-slider
                  name="cleanliness"
                  v-model="cleanliness"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Religiousness</p>
              <q-field outlined name="religiousness">
                <q-slider
                  name="religiousness"
                  v-model="religiousness"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <p>Alcohol Culture</p>
              <q-field outlined name="alcohol">
                <q-slider
                  name="alcohol"
                  v-model="alcohol"
                  marker-labels
                  :min="0"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-btn label="Submit" type="submit" color="primary"/>


          </q-form>
        </q-card-section>

        <q-card-section class="row justify-center">

        </q-card-section>
      </q-card>
    </q-page>

  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import axios from 'axios'

export default defineComponent({
  name: 'MainLayout',
  setup: () => {

    const safety = ref(5)
    const price = ref(5)
    const weather = ref(5)
    const english = ref(5)
    const walkability = ref(5)
    const cleanliness = ref(5)
    const religiousness = ref(5)
    const alcohol = ref(5)

    const onSubmit = async (evt) => {
      console.log(evt)
      let res = await axios({
        method: 'post',
        url: 'https://randomthing2.free.beeceptor.com',
        headers: {},
        data: {
          safety: safety.value,
          price: price.value,
          weather: weather.value,
          english: english.value,
          walkability: walkability.value,
          cleanliness: cleanliness.value,
          religiousness: religiousness.value,
          alcohol: alcohol.value
        }
      })

      //let data = res.data;
      //console.log(data);
      //evt.target.submit()
    }

    return {
      safety, price, weather, english, walkability, cleanliness, religiousness, alcohol, onSubmit

    };
  },
})
</script>
