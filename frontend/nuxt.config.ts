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
            hmr: {
                overlay: true, // Показывает ошибки HMR в браузере
                timeout: 60000,
            },
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

    app: {
        head: {
            title: 'Idea Space',
        }
    },

    compatibilityDate: '2024-11-01',
})