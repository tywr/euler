import networkx as nx



def load_pyramid_as_graph():
    graph = nx.DiGraph()
    with open("p18/pyramid.txt", "r") as file:
        pyramid = [list(map(int, line.split())) for line in file]
        for i, (base_layer, next_layer) in enumerate(zip(pyramid, pyramid[1:])):
            for j, value in enumerate(base_layer):
                base_node = f"{i}_{j}"
                node_1 = f"{i + 1}_{j}"
                node_2 = f"{i + 1}_{j + 1}"
                graph.add_node(node_1)
                graph.add_edge(base_node, node_1, weight=next_layer[j])
                graph.add_node(node_2)
                graph.add_edge(base_node, node_2, weight=next_layer[j + 1])
    return graph, pyramid[0][0]


def finx_max_path_sum(pyramid): ...


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    graph, base_value = load_pyramid_as_graph()
    longest_path = nx.dag_longest_path_length(graph, weight="weight")
    print(nx.dag_longest_path(graph, weight="weight"))
    print(longest_path + base_value)

