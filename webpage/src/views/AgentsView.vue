<script setup lang="ts">
import { VNetworkGraph } from 'v-network-graph'
import { onMounted } from 'vue'
import { useGraphStore } from '@/stores/graphStore'

const graphStore = useGraphStore()

onMounted(() => {
  graphStore.startPolling()
})
</script>

<template>
  <v-network-graph
    class="graph"
    :nodes="graphStore.$state.nodes"
    :edges="graphStore.$state.edges"
    :paths="graphStore.$state.paths"
    :layouts="graphStore.$state.layouts"
    :configs="graphStore.$state.configs"
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
