from graphviz import Digraph


def render(graph):
    """
    graph = {
        "nodes":[{
            "id": "1",
            "label": "node1",
            "color": "black",
        }]
        "edges":[{
            "source": node1["id"],
            "target": node2["id"],
            "color": "black"
        }]
    }
    """
    nodes = graph["nodes"]
    edges = graph["edges"]
    # 实例化一个Digraph对象(有向图)，name:生成的图片的图片名，format:生成的图片格式
    dot = Digraph(name="graph", comment="graph", format="png")
    dot.graph_attr["rankdir"] = "LR"

    for node in nodes:
        dot.node(name=str(node["id"]),
                 label=node["label"],
                 color=node.get("color", "black"))
    for edge in edges:
        dot.edge(str(edge["source"]),
                 str(edge["target"]),
                 label=edge["label"],
                 color=edge.get("color", "black"))

    # 打印生成的源代码
    print(dot.source)
    dot.render(filename='MyPicture', view=True)


if __name__ == "__main__":
    graph = {
        "nodes": [{
            "id": 0,
            "label": "q0",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 1,
            "label": "q1",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 2,
            "label": "q2",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 3,
            "label": "q3",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 4,
            "label": "q4",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 5,
            "label": "q5",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 6,
            "label": "q6",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 7,
            "label": "q7",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 8,
            "label": "q8",
            "style": "fill:#ffffff00;stroke:#000;"
        }, {
            "id": 9,
            "label": "q9",
            "style": "fill:#ffffff00;stroke:red;",
            "color": "red",
        }],
        "edges": [{
            "source": 2,
            "target": 3,
            "label": "b"
        }, {
            "source": 0,
            "target": 1,
            "label": "a"
        }, {
            "source": 4,
            "target": 5,
            "label": "c"
        }, {
            "source": 7,
            "target": 6,
            "label": "\u03b5"
        }, {
            "source": 1,
            "target": 8,
            "label": "\u03b5"
        }, {
            "source": 8,
            "target": 9,
            "label": "\u03b5"
        }, {
            "source": 6,
            "target": 2,
            "label": "\u03b5"
        }, {
            "source": 5,
            "target": 7,
            "label": "\u03b5"
        }, {
            "source": 8,
            "target": 6,
            "label": "\u03b5"
        }, {
            "source": 6,
            "target": 4,
            "label": "\u03b5"
        }, {
            "source": 3,
            "target": 7,
            "label": "\u03b5"
        }, {
            "source": 7,
            "target": 9,
            "label": "\u03b5"
        }]
    }
    render(graph)