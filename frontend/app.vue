<template>
  <div>
    <TestButton/>
    <div>Тест</div>
  </div>
</template>
<script setup lang="ts">

import {type User} from "~/api";

const newUser: User = {
  username: 'newuser2',
  password: '@WSX3edc',
  email: 'newuser2@example.com',
};

// Пример вызова API
// onMounted(async () => {
//   try {
//
//     const response = await API.Service.usersCreate(newUser)
//
//     console.log('User created successfully', response)
//   } catch (error) {
//     console.error('Error creating user', error);
//   }
// })
</script>