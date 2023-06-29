import { defineStore } from 'pinia';
import { reactive } from "vue";
import { type Node, type Nodes, type Edges, type Layouts, type Paths, defineConfigs } from 'v-network-graph';

interface NodeX extends Node {
    color: string,
    radius: number
}

export const useGraphStore = defineStore({
    id: 'graph',
    state: () => ({
        nodes: {} as Record<string, NodeX>,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Paths,
        configs: defineConfigs<NodeX>({}),
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
            const nodes: Record<string, NodeX> = {};
            for (const node of graph_data.nodes) {
                console.log(node.name, node.color, node.radius);

                if (node.color === undefined) {
                    node.color = "#000000";
                }

                if (node.radius === undefined) {
                    node.radius = 25;
                }

                nodes[node.id] = { name: node.name, color: node.color, radius: node.radius };
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
            // for (const node in this.nodes) {
            //     graph_config.configs["node"]["normal"] = 
            // }
            const default_configs = defineConfigs(graph_config.configs);
            this.configs = reactive(defineConfigs<NodeX>({
                node: {
                    normal: {
                        type: "circle",
                        radius: node => node.radius,
                        color: node => node.color,
                    },
                    hover: {
                        color: "#88bbff"
                    },
                    label: {
                        visible: true,
                        fontSize: 12,
                        directionAutoAdjustment: true
                    }
                }
            }))
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
