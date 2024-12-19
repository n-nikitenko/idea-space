import type {TokenRefresh} from "~/api";
import {type RemovableRef, StorageSerializers, useStorage, type UseStorageOptions} from '@vueuse/core'

export const useAuthStore = defineStore('auth', () => {
    const sOptions: UseStorageOptions<TokenRefresh> = {serializer: StorageSerializers.object}
    const token: RemovableRef<TokenRefresh | null> = useStorage('token', null, undefined, sOptions)
    const isLoggedIn = computed(() => token.value != null)

    async function login(login: string, password: string) {
        token.value = await API.Service.usersLoginCreate({username: login, password})
    }

    watch(token, (v) => {
        setAuthToken(v ? v.access : "") // Устанавливаем токен при изменении
    })

    async function logout() {
        if (!isNil(token.value)) {
            try {
                await callApi(() => API.Service.usersLogout({refresh: token.value!.refresh}))
            } finally {
                token.value = null
            }
        }
    }

    async function refreshToken() {
        if (!token.value) {
            throw new Error("Нет токена для обновления.")
        }
        try {
            token.value = await API.Service.usersTokenRefreshCreate({refresh: token.value.refresh})
        } catch (error) {
            token.value = null // Удаляем токен при ошибке
            throw error // Пробрасываем ошибку, чтобы обработать её на уровне вызова
        }
    }


    return {
        isLoggedIn, login, logout, refreshToken
    }
})