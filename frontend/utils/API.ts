import {
    Service,
} from "~/api";
import type {PartialOnUndefinedDeep} from "type-fest";

// noinspection JSUnusedGlobalSymbols
export const API = {
    Service,
    createOrUpdate: async <T, TC extends PartialOnUndefinedDeep<T>, TU extends PartialOnUndefinedDeep<T>>(
        id: number | undefined | null, data: T,
        create: (data: TC) => Promise<T>,
        update: (id: number, data: TU) => Promise<T>
    ) => (id) ? await update(id, data as any) : await create(data as any)
}
