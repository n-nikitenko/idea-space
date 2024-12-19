<script setup lang="ts">
import {toastError} from "~/utils/toast";

const login = ref('')
const password = ref('')
const authStore = useAuthStore()
const router = useRouter()
const toast = useToast()

const handleLogin = async () => {
  try {
    await authStore.login(login.value, password.value);
    await router.push('/');
  } catch (error: any) {
    toastError(toast, {detail: error.body.detail, summary: "Ошибка"})
  }
}
</script>

<template>
  <div class="login-container">

    <Card>
      <template #title>Вход</template>
      <template #content>
        <form @submit.prevent="handleLogin" class="flex flex-col gap-10">
          <div class="p-field">
            <FloatLabel variant="in">
              <label for="login">Логин</label>
              <InputText id="login" v-model="login" required/>
            </FloatLabel>
          </div>

          <FloatLabel variant="in">
            <Password :feedback="false" inputId="password" v-model="password" toggleMask required/>
            <label for="password">Пароль</label>
          </FloatLabel>

          <Button label="Войти" type="submit" class="p-button-primary"/>
        </form>
      </template>
    </Card>

  </div>
</template>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}
</style>