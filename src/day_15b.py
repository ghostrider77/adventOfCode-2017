import itertools as it

MODULUS = 2147483647


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def extract_starting_value(line):
    parts = line.split()
    return int(parts[-1])


def create_generator(starting_value, factor, m):
    value = starting_value
    while True:
        value = value * factor % MODULUS
        if value % m == 0:
            yield value


def run_judge(starting_value_a, starting_value_b, nr_rounds):
    generator_a = create_generator(starting_value_a, factor=16807, m=4)
    generator_b = create_generator(starting_value_b, factor=48271, m=8)

    nr_matches = 0
    for a, b in it.islice(zip(generator_a, generator_b), nr_rounds):
        if a & 0xffff == b & 0xffff:
            nr_matches += 1

    return nr_matches


def main():
    data = read_input_data("../resources/input_15.txt")
    starting_value_a = extract_starting_value(data[0])
    starting_value_b = extract_starting_value(data[1])
    nr_rounds = 5_000_000
    result = run_judge(starting_value_a, starting_value_b, nr_rounds)
    print(result)


if __name__ == "__main__":
    main()
