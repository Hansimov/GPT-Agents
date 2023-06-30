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
    animate: Boolean,
    animationSpeed: number
}

export const useGraphStore = defineStore({
    id: 'graph',
    state: () => ({
        nodes: {} as Record<string, NodeX>,
        edges: {} as Edges,
        layouts: { "nodes": {} } as Layouts,
        paths: {} as Record<string, PathX>,
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
            const paths: Record<string, PathX> = {};
            for (const path of graph_data.paths) {
                paths[path.id] = { edges: path.edges, animate: path.animate, animationSpeed: path.animationSpeed };
            }
            this.paths = paths;
        },
        updateNestedDict(target: any, source: any) {
            for (const key of Object.keys(source)) {
                if (typeof source[key] === 'object' && source[key].constructor === Object && key in target) {
                    target[key] = this.updateNestedDict(target[key], source[key]);
                } else {
                    target[key] = source[key];
                }
            }
            return target;
        },
        async updateGraphConfig() {
            // Configurations | v-network-graph
            // * https://dash14.github.io/v-network-graph/reference/configurations.html
            const graph_configs = (await this.fetchJsonData(this.graph_config_json_path)).configs;
            const default_configs = (await this.fetchJsonData(this.graph_config_json_path)).configs;
            // update configs
            this.configs = defineConfigs<NodeX, EdgeX, PathX>(
                this.updateNestedDict(
                    graph_configs,
                    reactive({
                        node: {
                            normal: {
                                radius: (node: NodeX) => node.radius || default_configs.node.normal.radius,
                                color: (node: NodeX) => node.color || default_configs.node.normal.color,
                            },
                            label: {
                                fontSize: (node: NodeX) => node.labelFontSize || default_configs.node.label.fontSize,
                            }
                        },
                        edge: {
                        },
                        path: {
                            normal: {
                                animationSpeed: (path: PathX) => path.animationSpeed + 0.001 || default_configs.path.normal.animationSpeed,
                            }
                        }
                    })
                ));
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
