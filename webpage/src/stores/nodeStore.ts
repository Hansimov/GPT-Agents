import { defineStore } from 'pinia';
import { Nodes, Edges, Layouts, Paths, defineConfigs } from 'v-network-graph';

export const useDataStore = defineStore({
    id: 'nodes',
    state: () => ({
        nodes: {} as Nodes,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Paths,
        configs: defineConfigs({}),
    }),
    actions: {
        async updateData() {
            const response = await fetch('src/data/node_edges.json');
            const data = await response.json();

            // update nodes
            const nodes: Nodes = {};
            for (const node of data.nodes) {
                nodes[node.id] = { name: node.name };
            }
            this.nodes = nodes;

            // update edges
            const edges: Edges = {};
            for (const edge of data.edges) {
                edges[edge.id] = { source: edge.from, target: edge.to };
            }
            this.edges = edges;

            // update layouts
            const layouts: Layouts = { "nodes": {} };
            for (const node of data.nodes) {
                layouts["nodes"][node.id] = { x: node.x, y: node.y };
            }
            this.layouts = layouts;

            // update paths
            const paths: Paths = {};
            for (const path of data.paths) {
                paths[path.id] = { edges: path.edges };
            }
            this.paths = paths;

            // update configs
            this.configs = defineConfigs(data.configs);
        },
        startPolling() {
            let prevData: typeof data | undefined;

            function isDataChanged(newData: typeof data) {
                if (prevData && (JSON.stringify(newData) === JSON.stringify(prevData))) {
                    return false;
                } else {
                    prevData = newData;
                    return true;
                }
            }

            const poll = async () => {
                const response = await fetch('src/data/node_edges.json');
                const newData = await response.json();
                if (isDataChanged(newData)) {
                    this.updateData();
                }
            }

            setInterval(poll, 500);

        }
    }
});
