<script setup lang="ts">
import { VNetworkGraph } from 'v-network-graph'
import 'v-network-graph/lib/style.css'
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
.graph {
  width: 800px;
  height: 900px;
  border: 1px solid gray;
}
</style>
