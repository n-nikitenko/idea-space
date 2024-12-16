// https://nuxt.com/docs/api/configuration/nuxt-config
import Aura from '@primevue/themes/aura';

export default defineNuxtConfig({
    ssr: false,
    devtools: {enabled: false},
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
        server: {
            proxy: {'/api': 'http://backend:8000'},
        }
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
    },
    runtimeConfig: {
        public: {
            VERSION: '1.1.1'
        }
    },
app: {
        head: {
            title: 'Контроль конфигураций',
        }
    },

})
