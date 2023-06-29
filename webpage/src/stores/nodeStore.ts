import { defineStore } from 'pinia';
import { Nodes, Edges, Layouts, Paths } from 'v-network-graph';

export const useDataStore = defineStore({
    id: 'nodes',
    state: () => ({
        nodes: {} as Nodes,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Paths
    }),
    actions: {
        async updateData() {
            // Use a dynamic import expression to import the JSON file
            // const data = await import(`@/data/node_edges.json?${Date.now()}`);
            const response = await fetch('src/data/node_edges.json');
            const data = await response.json();

            // Update the nodes
            const nodes: Nodes = {};
            for (const node of data.nodes) {
                nodes[node.id] = { name: node.name };
            }
            this.nodes = nodes;

            // Update the edges
            const edges: Edges = {};
            for (const edge of data.edges) {
                edges[edge.id] = { source: edge.from, target: edge.to };
            }
            this.edges = edges;

            // Update the layouts
            const layouts: Layouts = { "nodes": {} };
            for (const node of data.nodes) {
                layouts["nodes"][node.id] = { x: node.x, y: node.y };
            }
            this.layouts = layouts;

            // Update the paths
            const paths: Paths = {};
            for (const path of data.paths) {
                paths[path.id] = { edges: path.edges };
            }
            this.paths = paths;
        },
        startPolling() {
            // Define a variable to store the previous data
            let prevData: typeof data | undefined;

            // Define a function to check if the data has changed
            function hasDataChanged(newData: typeof data) {

                // Compare the new data with the previous data
                if (prevData && (JSON.stringify(newData) === JSON.stringify(prevData))) {
                    // The data has not changed
                    return false;
                } else {
                    // The data has changed
                    prevData = newData;
                    return true;
                }
            }

            // Define a function to poll for changes to the JSON file
            const poll = async () => {
                // Use a dynamic import expression to import the JSON file
                const response = await fetch('src/data/node_edges.json');
                const newData = await response.json();

                // Check if the data has changed
                if (hasDataChanged(newData)) {
                    // The data has changed, so call the updateData action
                    this.updateData();
                }
            }

            // Start polling for changes to the JSON file
            setInterval(poll, 500);
        }
    }
});
