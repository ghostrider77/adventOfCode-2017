import functools as ft
import itertools as it


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


def calc_nr_used_cells(key_string):
    cells = create_grid_cells(key_string)
    nr_used_cells = 0
    for row in cells:
        binary = it.chain.from_iterable([bin(int(h, base=16))[2:].zfill(4) for h in row])
        for bit in binary:
            if bit == "1":
                nr_used_cells += 1

    return nr_used_cells


def main():
    key_string = "oundnydw"
    result = calc_nr_used_cells(key_string)
    print(result)


if __name__ == "__main__":
    main()
