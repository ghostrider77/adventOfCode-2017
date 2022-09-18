from collections import namedtuple

Cell = namedtuple("Cell", ["x", "y"])


def calc_neighbour_sum(grid, cell):
    s = 0
    for ix in range(-1, 2):
        for jy in range(-1, 2):
            if (neighbour := Cell(cell.x + ix, cell.y + jy)) != cell:
                s += grid.get(neighbour, 0)
    return s


def get_next_direction(direction):
    if direction == (1, 0):
        return (0, 1)

    if direction == (0, 1):
        return (-1, 0)

    if direction == (-1, 0):
        return (0, -1)

    return (1, 0)


def get_first_element_in_spiral_path_exceeding_limit(limit):
    grid = {Cell(0, 0): 1}

    direction = (1, 0)
    cell = Cell(1, 0)
    step_in_one_direction = 1
    k = 0

    while (s := calc_neighbour_sum(grid, cell)) <= limit:
        grid[cell] = s
        k += 1
        if k >= step_in_one_direction:
            k = 0
            direction = get_next_direction(direction)
            if direction == (1, 0) or direction == (-1, 0):
                step_in_one_direction += 1

        delta_x, delta_y = direction
        cell = Cell(cell.x + delta_x, cell.y + delta_y)

    return s


def main():
    limit = 265149
    result = get_first_element_in_spiral_path_exceeding_limit(limit)
    print(result)


if __name__ == "__main__":
    main()
