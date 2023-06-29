import { Nodes, Edges, Layouts, Paths, defineConfigs, type Path } from 'v-network-graph'
import 'v-network-graph/lib/style.css'
import data from '@/data/graph.json';

const nodes: Nodes = {};
const edges: Edges = {};
const layouts: Layouts = { "nodes": {} };
const paths: Paths = {};


for (const node of data.nodes) {
    nodes[node.id] = { name: node.name };
    layouts["nodes"][node.id] = { x: node.x, y: node.y };
}

for (const edge of data.edges) {
    edges[edge.id] = { source: edge.from, target: edge.to };
}

for (const path of data.paths) {
    paths[path.id] = { edges: path.edges };
}

const configs = defineConfigs(
    data.configs
)

export default {
    nodes,
    edges,
    paths,
    layouts,
    configs,
}