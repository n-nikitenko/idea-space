import type {ToastServiceMethods} from "primevue/toastservice";
import type {ToastMessageOptions} from "primevue/toast";

const life = 3000

// noinspection JSUnusedGlobalSymbols
export const toastError = (toast: ToastServiceMethods, message: ToastMessageOptions) => toast.add({
    severity: 'error',
    life,

    ...message
})

// noinspection JSUnusedGlobalSymbols
export const toastSuccess = (toast: ToastServiceMethods, message: ToastMessageOptions) => toast.add({
    severity: 'success',
    life,

    ...message
})

// noinspection JSUnusedGlobalSymbols
export const toastMessage = (toast: ToastServiceMethods, message: ToastMessageOptions) => toast.add({
    severity: 'info',
    life,

    ...message
})

// noinspection JSUnusedGlobalSymbols
export function showErr(toast: ToastServiceMethods, msg: string, title?: string) {
    toastError(toast, {detail: msg, summary: title || 'Ошибка'})
}
