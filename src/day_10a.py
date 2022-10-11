def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def convert_to_intlist(line):
    return list(map(int, line.split(",")))


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
    for length in lengths:
        if length <= size:
            numbers = partial_reverse(numbers, length, position, size)
            position = (position + length + skip_size) % size
            skip_size += 1

    return numbers[0] * numbers[1]


def main():
    data = read_input_data("../resources/input_10.txt")
    lengths = convert_to_intlist(data[0])
    result = calc_knot_hash(lengths)
    print(result)


if __name__ == "__main__":
    main()
