<script setup lang="ts">
import {useTestStore} from "~/stores/test";

const store = useTestStore()
const array = [1, 2, 3];
const doubled = useMap(array, (n) => n * 2);
console.log(doubled);
</script>

<template>
  <Button label="Success" severity="success" rounded icon="pi pi-users"
          @click="store.increment()"
  />
</template>

<style scoped>

</style>