<script setup lang="ts">
import { VNetworkGraph } from 'v-network-graph'
import { onMounted } from 'vue'
import { useDataStore } from '@/stores/nodeStore'

const dataStore = useDataStore()

onMounted(() => {
  dataStore.startPolling()
})
</script>

<template>
  <v-network-graph
    class="graph"
    :nodes="dataStore.$state.nodes"
    :edges="dataStore.$state.edges"
    :paths="dataStore.$state.paths"
    :layouts="dataStore.$state.layouts"
    :configs="dataStore.$state.configs"
  />
</template>

<style>
@media (min-width: 1024px) {
  .graph {
    width: 800px;
    height: 600px;
    border: 1px solid gray;
  }
}
</style>
