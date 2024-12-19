/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { TokenObtainPair } from '../models/TokenObtainPair';
import type { TokenRefresh } from '../models/TokenRefresh';
import type { User } from '../models/User';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class Service {
    /**
     * Получение списка пользователей
     * @returns User
     * @throws ApiError
     */
    public static usersList(): CancelablePromise<Array<User>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/users/',
        });
    }
    /**
     * Регистрация пользователя
     * @param data
     * @returns User
     * @throws ApiError
     */
    public static usersCreate(
        data: User,
    ): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/',
            body: data,
        });
    }
    /**
     * Получение токена. Этот эндпоинт позволяет получить JWT токен на основе учетных данных пользователя.
     * @param data
     * @returns TokenRefresh Успех
     * @throws ApiError
     */
    public static usersLoginCreate(
        data: TokenObtainPair,
    ): CancelablePromise<TokenRefresh> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/login/',
            body: data,
            errors: {
                401: `Неверные учетные данные`,
            },
        });
    }
    /**
     * Выход из системы
     *
     * @param data
     * @returns any Успех
     * @throws ApiError
     */
    public static usersLogout(
        data: TokenRefresh,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/logout/',
            body: data,
            errors: {
                400: `Неверные данные`,
                401: `Пользователь не авторизован`,
            },
        });
    }
    /**
     * Обновление токена. Этот эндпоинт позволяет обновить JWT токен, предоставленный ранее.
     * @param data
     * @returns TokenRefresh Успех
     * @throws ApiError
     */
    public static usersTokenRefreshCreate(
        data: TokenRefresh,
    ): CancelablePromise<TokenRefresh> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/users/token/refresh/',
            body: data,
            errors: {
                401: `Токен недействителен`,
            },
        });
    }
    /**
     * Получение данных пользователя по id
     * @param id A unique integer value identifying this Пользователь.
     * @returns User
     * @throws ApiError
     */
    public static usersRead(
        id: number,
    ): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/users/{id}/',
            path: {
                'id': id,
            },
        });
    }
    /**
     * Обновление данных пользователя по id
     * @param id A unique integer value identifying this Пользователь.
     * @param data
     * @returns User
     * @throws ApiError
     */
    public static usersUpdate(
        id: number,
        data: User,
    ): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/users/{id}/',
            path: {
                'id': id,
            },
            body: data,
        });
    }
    /**
     * Частичное обновление данных пользователя по id
     * @param id A unique integer value identifying this Пользователь.
     * @param data
     * @returns User
     * @throws ApiError
     */
    public static usersPartialUpdate(
        id: number,
        data: User,
    ): CancelablePromise<User> {
        return __request(OpenAPI, {
            method: 'PATCH',
            url: '/users/{id}/',
            path: {
                'id': id,
            },
            body: data,
        });
    }
    /**
     * Удаление данных пользователя по id
     * @param id A unique integer value identifying this Пользователь.
     * @returns void
     * @throws ApiError
     */
    public static usersDelete(
        id: number,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/users/{id}/',
            path: {
                'id': id,
            },
        });
    }
}
