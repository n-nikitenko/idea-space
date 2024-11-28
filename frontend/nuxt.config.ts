// https://nuxt.com/docs/api/configuration/nuxt-config
import Aura from '@primevue/themes/aura';
export default defineNuxtConfig({
  ssr: false,
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  typescript: {
        strict: true,
        typeCheck: true
  },
  vite: {
        vue: {},
        vueJsx: {},
        build: {cssMinify: false},
        optimizeDeps: {include: ['lodash-es']},
        esbuild: {supported: {'top-level-await': true}},
    },
  css: [
       'normalize.css/normalize.css',

      'primeicons/primeicons.css',
    ],
  modules: ['@primevue/nuxt-module', '@vueuse/nuxt', 'nuxt-lodash', '@pinia/nuxt'],
  primevue: {
      options: {
          theme: {
              preset: Aura
          }
      }
  }

})
