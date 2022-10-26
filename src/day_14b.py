import functools as ft
import itertools as it


class Graph:
    def __init__(self, grid_state):
        self._grid_state = grid_state
        self._grid_size = len(grid_state)

        self._previsit_numbers = {}
        self._postvisit_numbers = {}
        self._previsit_id = it.count(1)
        self._postvisit_id = it.count(1)

    @ft.cached_property
    def connected_components(self):
        return self._get_connected_components()

    def _is_cell_used(self, coordinate):
        ix, jy = coordinate
        return self._grid_state[ix][jy] == "1"

    def _get_connected_components(self):
        components = []
        for ix in range(self._grid_size):
            for jy in range(self._grid_size):
                starting_cell = (ix, jy)
                if self._is_cell_used(starting_cell) and not self._is_visited_in_dfs(starting_cell):
                    current_component = self._explore(starting_cell)
                    components.append(frozenset(current_component))

        return tuple(components)

    def _is_visited_in_dfs(self, coord):
        return coord in self._previsit_numbers

    def _get_neighbours(self, coord):
        ix, jy = coord
        neighbours = []
        for a, b in [(ix + 1, jy), (ix - 1, jy), (ix, jy - 1), (ix, jy + 1)]:
            if 0 <= a < self._grid_size and 0 <= b < self._grid_size and self._grid_state[a][b] == "1":
                neighbours.append((a, b))

        return neighbours

    def _find_unvisited_neighbour_of_a_node(self, node):
        neighbours = self._get_neighbours(node)
        for neighbour in neighbours:
            if not self._is_visited_in_dfs(neighbour):
                return neighbour

        return None

    def _explore(self, starting_cell):
        self._previsit_numbers[starting_cell] = next(self._previsit_id)
        previsit_stack = [starting_cell]
        current_component = {starting_cell}
        while previsit_stack:
            last_node = previsit_stack.pop(-1)
            unvisited_neighbour = self._find_unvisited_neighbour_of_a_node(last_node)
            if unvisited_neighbour is None:
                self._postvisit_numbers[last_node] = next(self._postvisit_id)
            else:
                self._previsit_numbers[unvisited_neighbour] = next(self._previsit_id)
                previsit_stack.append(last_node)
                previsit_stack.append(unvisited_neighbour)
                current_component.add(unvisited_neighbour)

        return current_component


def convert_to_numbers(line):
    return list(map(ord, line))


def partial_reverse(numbers, length, position, size):
    reversed_list = numbers[:]
    for k in range(length):
        ix = (k + position) % size
        jy = (position + length - k - 1) % size
        reversed_list[ix] = numbers[jy]
    return reversed_list


def calc_knot_hash(lengths):
    size = 256
    position = 0
    skip_size = 0
    numbers = list(range(size))
    for _ in range(64):
        for length in lengths:
            numbers = partial_reverse(numbers, length, position, size)
            position = (position + length + skip_size) % size
            skip_size += 1

    dense_hash = [ft.reduce(lambda x, y: x ^ y, numbers[k*16:(k+1)*16]) for k in range(16)]
    return "".join(map(lambda k: f"{k:02x}", dense_hash))


def create_grid_cells(key_string):
    grid_cells = []
    for k in range(128):
        lengths = convert_to_numbers(f"{key_string}-{k}")
        lengths.extend([17, 31, 73, 47, 23])
        grid_cells.append(calc_knot_hash(lengths))
    return grid_cells


def calc_nr_regions(key_string):
    grid = create_grid_cells(key_string)
    state = [list(it.chain.from_iterable([bin(int(h, base=16))[2:].zfill(4) for h in row])) for row in grid]
    graph = Graph(state)
    return len(graph.connected_components)


def main():
    key_string = "oundnydw"
    result = calc_nr_regions(key_string)
    print(result)


if __name__ == "__main__":
    main()
