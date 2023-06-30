import { defineStore } from 'pinia';
import { reactive } from "vue";
import { type Node, type Edge, type Path, type Nodes, type Edges, type Layouts, type Paths, defineConfigs } from 'v-network-graph';

interface NodeX extends Node {
    color: string,
    radius: number
}

interface EdgeX extends Edge {

}

interface PathX extends Path {

}

export const useGraphStore = defineStore({
    id: 'graph',
    state: () => ({
        nodes: {} as Record<string, NodeX>,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Paths,
        configs: defineConfigs<NodeX, EdgeX, PathX>({}),
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
        updateNestedDict(target: any, source: any) {
            for (const key of Object.keys(source)) {
                // console.log(key, source[key]);
                if (typeof source[key] === 'object' && source[key].constructor === Object && key in target) {
                    target[key] = this.updateNestedDict(target[key], source[key]);
                    console.log("Dict - ", key, ':', target[key], source[key])
                } else {
                    target[key] = source[key];
                    console.log("Config - ", key, ':', target[key], source[key])
                }
            }
            // console.log("target:", target);
            return target;
        },
        async updateGraphConfig() {
            const graph_config = await this.fetchJsonData(this.graph_config_json_path)
            // update configs
            const default_configs = graph_config.configs;
            this.configs = defineConfigs<NodeX>(
                this.updateNestedDict(
                    default_configs,
                    reactive({
                        node: {
                            normal: {
                                radius: (node: NodeX) => node.radius || default_configs.node.normal.radius,
                                color: (node: NodeX) => node.color || default_configs.node.normal.color
                            },
                            label: {
                                fontSize: (node: NodeX) => node.radius || default_configs.node.label.fontSize
                            }
                        }
                    }
                    )
                )
            )
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
                const new_graph_config = await this.fetchJsonData(this.graph_config_json_path);

                if (isValueChanged(new_graph_config, "graph_data") || isValueChanged(new_graph_data, "graph_config")) {
                    this.updateGraphData();
                    this.updateGraphConfig();
                }
            }

            setInterval(poll, 500);
        }
    }
});
