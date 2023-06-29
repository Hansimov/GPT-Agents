<template>
  <v-network-graph
    class="graph"
    :nodes="dataStore.$state.nodes"
    :edges="dataStore.$state.edges"
    :paths="dataStore.$state.paths"
    :layouts="dataStore.$state.layouts"
    :configs="configs"
  />
</template>

<script setup lang="ts">
import { VNetworkGraph } from 'v-network-graph'
import { defineComponent, computed, onMounted } from 'vue'
import { useDataStore } from '@/stores/nodeStore'
import data from '@/agents_data'

const dataStore = useDataStore()

const configs = computed(() => data.configs)

// Call the updateData action when the component is mounted
onMounted(() => {
  dataStore.startPolling()
})
</script>

<style>
@media (min-width: 1024px) {
  .graph {
    width: 800px;
    height: 600px;
    border: 1px solid gray;
  }
}
</style>
