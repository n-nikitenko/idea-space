import {OpenAPI, Service,} from "~/api";
import type {PartialOnUndefinedDeep} from "type-fest";

import {useAuthStore} from "~/stores/auth";


export function setAuthToken(token: string | undefined) {
    OpenAPI.TOKEN = token;
}

/**
 * Обертка для вызовов API с обработкой истечения токена
 * @param apiCall Функция, выполняющая API-запрос
 * @returns Результат вызова API
 */
export async function callApi<T>(apiCall: () => Promise<T>): Promise<T> {
    const authStore = useAuthStore();
    const router = useRouter();

    try {
         // Выполняем запрос
        return await apiCall()
    } catch (error: any) {
        if (error.status === 401) {
            try {
                // Пытаемся обновить токен
                await authStore.refreshToken();
                // Повторяем запрос
                return await apiCall();
            } catch (refreshError) {
                console.error("Не удалось обновить токен:", refreshError);
                await router.push({ path: "/login", query: { reason: "Войдите снова." } }); // Перенаправление на логин
                throw refreshError; // Пробрасываем ошибку
            }
        }
        else throw error; // Пробрасываем другие ошибки
    }
}


// noinspection JSUnusedGlobalSymbols
export const API = {
    Service,
    createOrUpdate: async <T, TC extends PartialOnUndefinedDeep<T>, TU extends PartialOnUndefinedDeep<T>>(
        id: number | undefined | null, data: T,
        create: (data: TC) => Promise<T>,
        update: (id: number, data: TU) => Promise<T>
    ) =>await callApi(() => (id) ? update(id, data as any) : create(data as any))
}
