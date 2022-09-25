import functools as ft

from collections import Counter


class Graph:
    def __init__(self, adjacency_list, node_weights):
        self._adjacency_list = adjacency_list
        self._node_weights = node_weights

    @ft.cached_property
    def leaves(self):
        leaves = []
        for children in self._adjacency_list.values():
            for child in children:
                if child not in self._adjacency_list:
                    leaves.append(child)
        return tuple(leaves)

    def _get_ripe_nodes(self, total_weights):
        ripe_nodes = []
        for node, children in self._adjacency_list.items():
            if node not in total_weights and all(child in total_weights for child in children):
                ripe_nodes.append(node)
        return ripe_nodes

    def get_correct_weight(self):
        total_weights = {leaf: self._node_weights[leaf] for leaf in self.leaves}
        while (ripe_nodes := self._get_ripe_nodes(total_weights)):
            for node in ripe_nodes:
                children = self._adjacency_list[node]
                children_total_weights = {child: total_weights[child] for child in children}
                (most_common, _), = Counter(children_total_weights.values()).most_common(n=1)
                for child, total_weight in children_total_weights.items():
                    if total_weight != most_common:
                        return self._node_weights[child] + (most_common - total_weight)

                total_weights[node] = self._node_weights[node] + sum(children_total_weights.values())


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def read_edges(lines):
    adjacency_list = {}
    node_weights = {}
    for line in lines:
        node_info, *rest = line.split(" -> ")
        name, weight = node_info.split(" ")
        node_weights[name] = int(weight[1:-1])
        if rest:
            neighbours = rest[0].split(", ")
            adjacency_list[name] = tuple(neighbours)

    return Graph(adjacency_list, node_weights)


def main():
    data = read_input_data("../resources/input_07.txt")
    graph = read_edges(data)
    result = graph.get_correct_weight()
    print(result)


if __name__ == "__main__":
    main()
