<template>
  <Button @click="onClick">Press</Button>
  <NuxtPage class="flex-1"
  />
  <Toast position="bottom-right"/>
</template>
<script setup lang="ts">

import {type User} from "~/api";
import {callApi} from "~/utils/API"

const newUser: User = {
  username: 'newuser123',
  password: '@WSX3edc',
  email: 'newuser2@example.com',
};

// Пример вызова API
const onClick = async () => {
  const response = await callApi(() => API.Service.usersList())
  try {
    console.log("hello")



    console.log('Users list getted', response)
  } catch (error) {
    console.error('Error get userList', error);
  }
}
</script>