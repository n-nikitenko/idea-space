<script setup lang="ts">
import {toastError} from "~/utils/toast";

const authStore = useAuthStore()
const {isLoggedIn} = storeToRefs(authStore)
const router = useRouter()
const toast = useToast()

const goToLogin = () => router.push('/login')
const onLogout = async () => {
  try {
    await authStore.logout()
    toastSuccess(toast, {summary: "Вы успешно вышли из системы"})
  } catch (e: any) {
    toastError(toast, {detail: e.body.detail, summary: "Ошибка"})
  }
}
</script>

<template>
  <Card>
    <template #title><h1>Добро пожаловать в IdeaSpace</h1></template>
    <template #content>

      <Button v-if="!isLoggedIn" label="Войти" @click="goToLogin"/>
      <Button v-else label="Выйти" @click="onLogout"/>
    </template>
  </Card>

</template>

<style scoped>

</style>