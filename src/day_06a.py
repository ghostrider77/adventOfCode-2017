def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def convert_to_intlist(line):
    return [int(item) for item in line.split()]


def perform_redistribution(memory_banks, length):
    ix, nr_blocks = max(enumerate(memory_banks), key=lambda x: x[1])
    memory_banks[ix] = 0
    for k in range(1, nr_blocks+1):
        jy = (ix + k) % length
        memory_banks[jy] += 1


def calc_nr_redistributions(memory_banks):
    length = len(memory_banks)
    configurations = set()
    while (configuration := tuple(memory_banks)) not in configurations:
        configurations.add(configuration)
        perform_redistribution(memory_banks, length)

    return len(configurations)


def main():
    data = read_input_data("../resources/input_06.txt")
    memory_banks = convert_to_intlist(data[0])
    result = calc_nr_redistributions(memory_banks)
    print(result)


if __name__ == "__main__":
    main()
