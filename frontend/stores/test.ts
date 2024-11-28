export const useTestStore = defineStore(useUniqueId(), () => {
    const counter = ref(0)
    const increment = () => {
        counter.value += 1
        console.log("counter=", counter.value)
    }
    return {
        increment
    }
});