import json
import networkx as nx
from pathlib import Path
from math import cos, sin, pi

# class NodeManager:
#     def __init__(self):
#         pass


class Node:
    def __init__(self):
        pass


def create_nodes_from_agents():
    agents = [
        {"name": "Center", "role": "center", "color": "cyan"},
        {"name": "Planet1", "role": "planet"},
        {"name": "Planet2", "role": "planet"},
        {"name": "Planet3", "role": "planet"},
        {"name": "Planet4", "role": "planet"},
        {"name": "Planet5", "role": "planet"},
    ]
    nodes = []
    for agent in agents:
        node = Node()
        node.name = agent["name"]
        node.role = agent["role"]
        if "color" in agent.keys():
            node.color = agent["color"]
        else:
            node.color = None
        nodes.append(node)
    return nodes


def create_graph_from_nodes(nodes):
    G = nx.Graph()

    for node in nodes:
        G.add_node(node.name)

    for i in range(len(nodes) - 1):
        planet_name = f"Planet{i+1}"
        G.add_edge("Center", planet_name)

    print(G)
    print(G.edges)
    # print(list(G.adj["Center"]))

    return G


def dump_graph_to_vng_json(G):
    data = {}
    data["nodes"] = [
        {
            "id": "Center",
            "name": "Center",
            "x": 0,
            "y": 0,
            "color": "red",
            "radius": 50,
        },
    ]
    for i in range(len(G.nodes) - 1):
        planet_name = f"Planet{i+1}"
        r = 150
        planet_x = round(r * cos(2 * pi * i / (len(G.nodes) - 1)), 1)
        planet_y = round(r * sin(2 * pi * i / (len(G.nodes) - 1)), 1)
        data["nodes"].append(
            {
                "id": planet_name,
                "name": planet_name,
                "x": planet_x,
                "y": planet_y,
            }
        )

    data["edges"] = []
    for edge in G.edges:
        data["edges"].extend(
            [
                {
                    "id": f"edge-{edge[0]}-{edge[1]}",
                    "name": f"edge-{edge[0]}-{edge[1]}",
                    "from": edge[0],
                    "to": edge[1],
                },
                {
                    "id": f"edge-{edge[1]}-{edge[0]}",
                    "name": f"edge-{edge[1]}-{edge[0]}",
                    "from": edge[1],
                    "to": edge[0],
                },
            ]
        )

    data["paths"] = []
    for edge in G.edges:
        data["paths"].extend(
            [
                {
                    "id": f"path-{edge[0]}-{edge[1]}",
                    "name": f"path-{edge[0]}-{edge[1]}",
                    "edges": [f"edge-{edge[0]}-{edge[1]}"],
                }
            ]
        )

    graph_json_path = Path("./webpage/src/data/graph.json")
    with open(graph_json_path, "w") as wf:
        json.dump(data, wf, indent=4)
    # print(data)


def main():
    nodes = create_nodes_from_agents()
    G = create_graph_from_nodes(nodes)
    dump_graph_to_vng_json(G)


if __name__ == "__main__":
    main()
