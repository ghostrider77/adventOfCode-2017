def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def leave_maze(instructions):
    nr_instructions = len(instructions)
    position = 0
    nr_steps = 0
    while 0 <= position < nr_instructions:
        offset = instructions[position]
        next_position = position + offset
        nr_steps += 1
        instructions[position] += (-1 if offset >= 3 else 1)
        position = next_position

    return nr_steps


def main():
    data = read_input_data("../resources/input_05.txt")
    instructions = list(map(int, data))
    result = leave_maze(instructions)
    print(result)


if __name__ == "__main__":
    main()
