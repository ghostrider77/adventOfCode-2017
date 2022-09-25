import functools as ft
import itertools as it


class RootNotFoundException(Exception):
    pass


class Graph:
    def __init__(self, adjacency_list):
        self._adjacency_list = adjacency_list

    @ft.cached_property
    def root(self):
        return self._find_root_node()

    def _find_root_node(self):
        children = set(it.chain.from_iterable(self._adjacency_list.values()))
        for node in self._adjacency_list:
            if node not in children:
                return node

        raise RootNotFoundException("No root has been found in directed tree.")


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def read_edges(lines):
    adjacency_list = {}
    for line in lines:
        node_info, *rest = line.split(" -> ")
        name, _ = node_info.split(" ")
        if rest:
            neighbours = rest[0].split(", ")
            adjacency_list[name] = tuple(neighbours)

    return Graph(adjacency_list)


def main():
    data = read_input_data("../resources/input_07.txt")
    graph = read_edges(data)
    print(graph.root)


if __name__ == "__main__":
    main()
