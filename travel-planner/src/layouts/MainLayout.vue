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

    <q-dialog v-model="alert">
      <div class="q-pa-md full-width">
        <q-carousel
          arrows
          animated
          v-model="slide"
          height="400px"
        >
          <q-carousel-slide v-for="(country,index) in countryLoc" :name="index" :img-src="country.media" :key="index">
            <div class="absolute-bottom custom-caption">
              <div class="text-h2">{{country.name}}</div>
<!--              <div class="text-subtitle1">Mountains</div>-->
            </div>
          </q-carousel-slide>
<!--          <q-carousel-slide :name="1" img-src="https://cdn.quasar.dev/img/mountains.jpg">-->
<!--            <div class="absolute-bottom custom-caption">-->
<!--              <div class="text-h2">First stop</div>-->
<!--              <div class="text-subtitle1">Mountains</div>-->
<!--            </div>-->
<!--          </q-carousel-slide>-->
        </q-carousel>
      </div>
    </q-dialog>

    <!--    <q-dialog v-model="alert">-->
<!--      <q-card class="my-card">-->
<!--        <q-img-->
<!--          :src="img_link"-->
<!--        />-->

<!--        <q-card-section>-->
<!--          <q-btn-->
<!--            fab-->
<!--            color="primary"-->
<!--            icon="place"-->
<!--            class="absolute"-->
<!--            style="top: 0; right: 12px; transform: translateY(-50%);"-->
<!--          />-->

<!--          <div class="row no-wrap items-center">-->
<!--            <div class="col text-h6 ellipsis">-->
<!--              {{ countryLoc }}-->
<!--            </div>-->
<!--            <div class="col-auto text-grey text-caption q-pt-md row no-wrap items-center">-->
<!--            </div>-->
<!--          </div>-->

<!--          <q-rating readonly v-model="stars" :max="5" size="32px" />-->
<!--        </q-card-section>-->

<!--        <q-card-section class="q-pt-none">-->
<!--          <div class="text-subtitle1">-->
<!--            Suggested Holiday Location-->
<!--          </div>-->
<!--          <div class="text-caption text-grey">-->
<!--            Your ideal holiday destination was discovered using our custom algorithm and datasets.-->
<!--          </div>-->
<!--        </q-card-section>-->

<!--        <q-separator />-->

<!--        <q-card-actions align="right">-->
<!--          <q-btn v-close-popup flat color="primary" label="More info" @click="redir" />-->
<!--&lt;!&ndash;          <q-btn v-close-popup flat color="primary" round icon="event" />&ndash;&gt;-->
<!--        </q-card-actions>-->
<!--      </q-card>-->
<!--    </q-dialog>-->

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
                <p class="q-pb-md">Temperature Selector</p>
                <q-select v-model="selectModel" :options="selectOptions" label="Select" />
              </q-card>

              <q-card class="q-pa-lg q-mb-md">
                <div class="row justify-between">
                  <p class="q-pb-md">Temperature not important</p>
                  <p class="q-pb-md">Temperature important</p>
                </div>
<!--                <p class="q-pb-md">Temperature not important -&#45;&#45; Temperature important</p>-->
                <q-field outlined name="temp_imp">
                  <q-slider
                    name="temp_imp"
                    v-model="temperature"
                    snap
                    label
                    label-always
                    markers
                    :min="-10"
                    :max="10"
                  />
                </q-field>
              </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Low Safety</p>
                  <p class="q-pb-md">High Safety</p>
                </div>
              <q-field outlined name="safety">
                <q-slider
                  name="safety"
                  v-model="safety"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Expensive</p>
                  <p class="q-pb-md">Cheap</p>
              </div>
              <q-field outlined name="price">
                <q-slider
                  name="price"
                  v-model="price"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Bad Weather</p>
                  <p class="q-pb-md">Good Weather</p>
                </div>
              <q-field outlined name="weather">
                <q-slider
                  name="weather"
                  v-model="weather"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Low Knowledge of English</p>
                  <p class="q-pb-md">High Knowledge of English</p>
                </div>
              <q-field outlined name="english">
                <q-slider
                  name="english"
                  v-model="english"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Low Walkability</p>
                  <p class="q-pb-md">High Walkability</p>
                </div>
              <q-field outlined name="walkability">
                <q-slider
                  name="walkability"
                  v-model="walkability"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Dirty</p>
                  <p class="q-pb-md">Clean</p>
                </div>
              <q-field outlined name="cleanliness">
                <q-slider
                  name="cleanliness"
                  v-model="cleanliness"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Not Religious</p>
                  <p class="q-pb-md">Very Religious</p>
                </div>
              <q-field outlined name="religiousness">
                <q-slider
                  name="religiousness"
                  v-model="religiousness"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                  <p class="q-pb-md">Low Alcohol Consumption</p>
                  <p class="q-pb-md">High Alcohol Consumption</p>
                </div>
              <q-field outlined name="alcohol">
                <q-slider
                  name="alcohol"
                  v-model="alcohol"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
                  :max="10"
                />
              </q-field>
            </q-card>

            <q-card class="q-pa-lg q-mb-md">
              <div class="row justify-between">
                <p class="q-pb-md">Not Touristic</p>
                <p class="q-pb-md">Touristic</p>
              </div>
              <q-field outlined name="tourist">
                <q-slider
                  name="tourist"
                  v-model="tourist"
                  snap
                  label
                  label-always
                  markers
                  :min="-10"
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
import {useQuasar} from "quasar";
import {useRouter} from "vue-router";

const $q = useQuasar()

export default defineComponent({
  name: 'MainLayout',
  setup: () => {

    const safety = ref(0)
    const price = ref(0)
    const weather = ref(0)
    const english = ref(0)
    const walkability = ref(0)
    const cleanliness = ref(0)
    const religiousness = ref(0)
    const alcohol = ref(0)
    const temperature = ref(0)
    const tourist = ref(0)
    let countryLoc = ref('')
    let stars = ref(5)
    let alert = ref(false)
    let slide = ref(0)
    let selectModel = ref('Warm')
    let selectOptions = ["Very Hot", "Hot", "Warm", "Chilly", "Cold", "Very Cold"]

    const redir = (evt) => {
      window.open(`https://www.google.com/search?q=${countryLoc.value}`, '_blank')
      // this.$router.push(`https://www.google.com/search?q=${countryLoc.value}`)
      //redirect(`https://www.google.com/search?q=${countryLoc.value}`)
    }

    const onSubmit = async (evt) => {
      // console.log(evt)
      let res = await axios({
        method: 'post',
        url: 'http://localhost:7777/submit',
        headers: {},
        data: {
          safety: safety.value,
          price: price.value,
          weather: weather.value,
          english: english.value,
          walkability: walkability.value,
          cleanliness: cleanliness.value,
          religiousness: religiousness.value,
          alcohol: alcohol.value,
          temperature: temperature.value,
          selectModel: selectModel.value,
          tourist: tourist.value
        }
      })
      let data = res.data;
      console.log(data);
      countryLoc.value = data
      alert.value = true
      slide.value = 0
      //evt.target.submit()
    }

    return {
      safety, price, weather, english, walkability, cleanliness, religiousness, alcohol, onSubmit, alert, countryLoc, stars, redir, slide, selectModel, selectOptions, temperature, tourist

    };
  },
})
</script>

<style lang="sass" scoped>
.custom-caption
  text-align: center
  padding: 12px
  color: white
  background-color: rgba(0, 0, 0, .3)
</style>
