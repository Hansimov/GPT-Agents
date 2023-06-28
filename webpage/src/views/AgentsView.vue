<script setup lang="ts">
import { VNetworkGraph } from 'v-network-graph'
import data from '@/agents_data'
</script>

<template>
  <v-network-graph
    class="graph"
    :nodes="data.nodes"
    :edges="data.edges"
    :paths="data.paths"
    :layouts="data.layouts"
    :configs="data.configs"
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
