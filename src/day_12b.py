import functools as ft
import itertools as it

from collections import defaultdict


class Graph:
    def __init__(self, adjacency_list):
        self._adjacency_list = adjacency_list
        self._nodes = self._collect_all_nodes()

        self._previsit_numbers = {}
        self._postvisit_numbers = {}
        self._previsit_id = it.count(1)
        self._postvisit_id = it.count(1)

    @ft.cached_property
    def nr_connected_components(self):
        components = self._get_connected_components()
        return len(components)

    def _collect_all_nodes(self):
        nodes = set()
        for node, neighbours in self._adjacency_list.items():
            nodes.add(node)
            nodes.update(neighbours)
        return frozenset(nodes)

    def _get_connected_components(self):
        components = []
        for starting_node in self._nodes:
            if not self._is_visited_in_dfs(starting_node):
                current_component = self._explore(starting_node)
                components.append(frozenset(current_component))
        return tuple(components)

    def _is_visited_in_dfs(self, node):
        return node in self._previsit_numbers

    def _explore(self, starting_node):
        self._previsit_numbers[starting_node] = next(self._previsit_id)
        previsit_stack = [starting_node]
        current_component = {starting_node}
        while previsit_stack:
            last_node = previsit_stack.pop(-1)
            if (unvisited_neighbour := self._find_unvisited_neighbour_of_a_node(last_node)) is None:
                self._postvisit_numbers[last_node] = next(self._postvisit_id)
            else:
                self._previsit_numbers[unvisited_neighbour] = next(self._previsit_id)
                previsit_stack.append(last_node)
                previsit_stack.append(unvisited_neighbour)
                current_component.add(unvisited_neighbour)
        return current_component

    def _find_unvisited_neighbour_of_a_node(self, node):
        neighbours = self._adjacency_list.get(node, set())
        for neighbour in neighbours:
            if not self._is_visited_in_dfs(neighbour):
                return neighbour

        return None


def convert_to_intlist(line):
    return tuple(int(item) for item in line.split(", "))


def create_adjacency_list(lines):
    adjacency_list = defaultdict(set)
    for node_id, neighbours_string in map(lambda x: x.split(" <-> "), lines):
        neighbours = convert_to_intlist(neighbours_string)
        node = int(node_id)
        for neighbour in neighbours:
            adjacency_list[node].add(neighbour)
            adjacency_list[neighbour].add(node)
    return dict(adjacency_list)


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def main():
    data = read_input_data("../resources/input_12.txt")
    adjacency_list = create_adjacency_list(data)
    graph = Graph(adjacency_list)
    result = graph.nr_connected_components
    print(result)


if __name__ == "__main__":
    main()
