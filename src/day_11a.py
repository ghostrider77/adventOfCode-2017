
class Direction:
    def __init__(self, direction):
        self.dq, self.dr, self.ds = self._get_direction_coordinates(direction)

    @staticmethod
    def _get_direction_coordinates(direction):
        if direction == "se":
            return 1, 0, -1

        if direction == "ne":
            return 1, -1, 0

        if direction == "n":
            return 0, -1, 1

        if direction == "nw":
            return -1, 0, 1

        if direction == "sw":
            return -1, 1, 0

        if direction == "s":
            return 0, 1, -1

        raise ValueError(f"Unknown direction string {direction}.")


class Hexagon:
    def __init__(self, q, r, s):
        self._q = q
        self._r = r
        self._s = s

    def __repr__(self):
        return f"Hexagon({self._q}, {self._r}, {self._s})"

    def __add__(self, direction):
        return Hexagon(self._q + direction.dq, self._r + direction.dr, self._s + direction.ds)

    def distance_from_origin(self):
        return (abs(self._q) + abs(self._r) + abs(self._s)) // 2


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def calc_hexagonal_distance(directions):
    hexagon = Hexagon(0, 0, 0)
    for direction in map(Direction, directions):
        hexagon = hexagon + direction

    return hexagon.distance_from_origin()


def main():
    data = read_input_data("../resources/input_11.txt")
    directions = data[0].split(",")
    result = calc_hexagonal_distance(directions)
    print(result)


if __name__ == "__main__":
    main()
