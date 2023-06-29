import { defineStore } from 'pinia';
import { type Nodes, type Edges, type Layouts, type Paths, defineConfigs } from 'v-network-graph';

export const useGraphStore = defineStore({
    id: 'graph',
    state: () => ({
        nodes: {} as Nodes,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Paths,
        configs: defineConfigs({}),
        graph_data_json_path: 'src/data/graph.json',
        graph_config_json_path: 'src/data/graph_config.json',
    }),
    actions: {
        async fetchJsonData(json_path: string) {
            const response = await fetch(json_path);
            return await response.json();
        },
        async updateGraphData() {
            const graph_data = await this.fetchJsonData(this.graph_data_json_path)
            // update nodes
            const nodes: Nodes = {};
            for (const node of graph_data.nodes) {
                nodes[node.id] = { name: node.name };
            }
            this.nodes = nodes;

            // update edges
            const edges: Edges = {};
            for (const edge of graph_data.edges) {
                edges[edge.id] = { source: edge.from, target: edge.to };
            }
            this.edges = edges;

            // update layouts
            const layouts: Layouts = { "nodes": {} };
            for (const node of graph_data.nodes) {
                layouts["nodes"][node.id] = { x: node.x, y: node.y };
            }
            this.layouts = layouts;

            // update paths
            const paths: Paths = {};
            for (const path of graph_data.paths) {
                paths[path.id] = { edges: path.edges };
            }
            this.paths = paths;
        },
        async updateGraphConfig() {
            const graph_config = await this.fetchJsonData(this.graph_config_json_path)
            // update configs
            this.configs = defineConfigs(graph_config.configs);
        },
        startPolling() {
            let preGraphData: any;
            let preGraphConfig: any;

            function isValueChanged(newValue: any, valueType: string) {
                let preValue: any;
                if (valueType === 'graph_data') {
                    preValue = preGraphData;
                } else {
                    preValue = preGraphConfig;
                }

                if (preValue && (JSON.stringify(newValue) === JSON.stringify(preValue))) {
                    return false;
                } else {
                    if (valueType === 'graph_data') {
                        preGraphData = newValue;
                    } else {
                        preGraphConfig = newValue;
                    }
                    return true;
                }
            }

            const poll = async () => {
                const new_graph_data = await this.fetchJsonData(this.graph_data_json_path);
                if (isValueChanged(new_graph_data, "graph_data")) {
                    this.updateGraphData();
                }

                const new_graph_config = await this.fetchJsonData(this.graph_config_json_path);
                if (isValueChanged(new_graph_config, "graph_config")) {
                    this.updateGraphConfig();
                }
            }

            setInterval(poll, 500);
        }
    }
});
