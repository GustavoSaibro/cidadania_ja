<template>
  <router-link
    :to="to"
    class="link"
    :class="{ active:isActive }"
  ></router-link>

</template>

<script>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { collapsed } from './state'

export default {
  props: {
    to: { type: String, required: true },
    icon: { type: String, required: true }
  },
  setup (props) {
    const route = useRoute()
    const isActive = computed(() => route.path === props.to)
    return isActive
  }
}


</script>

<style>
</style>