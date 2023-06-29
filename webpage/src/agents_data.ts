import { Nodes, Edges, Layouts, Paths, defineConfigs, type Path } from 'v-network-graph'
import 'v-network-graph/lib/style.css'
import data from '@/data/node_edges.json';

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

const configs = defineConfigs({
    node: {
        normal: { type: 'circle', radius: 20, color: '#99ccff' },
        hover: { color: '#88bbff' },
        label: { visible: false, fontSize: 8 }
    },
    edge: {
        gap: 12,
        normal: { color: '#6699cc' }
    },
    path: {
        visible: true,
        normal: {
            width: 10,
            dasharray: '40 16',
            animate: true,
            animationSpeed: 20
        }
    }
})

export default {
    nodes,
    edges,
    paths,
    layouts,
    configs,
}