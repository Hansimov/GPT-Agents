<template>
  <div>
    <v-network-graph :nodes="nodes" :edges="edges" :layouts="layouts" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import { Nodes, Edges, Layouts } from 'v-network-graph'
import data from './data'

export default defineComponent({
  name: 'MyComponent',
  data() {
    return {
      nodes: data.nodes as Nodes,
      edges: data.edges as Edges,
      layouts: data.layouts as Layouts
    }
  }
})
</script>
