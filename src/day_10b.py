import functools as ft


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


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


def main():
    data = read_input_data("../resources/input_10.txt")
    lengths = convert_to_numbers(data[0])
    lengths.extend([17, 31, 73, 47, 23])
    result = calc_knot_hash(lengths)
    print(result)


if __name__ == "__main__":
    main()
