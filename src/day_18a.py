from collections import defaultdict


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def get_value(registers, y):
    try:
        value = int(y)
    except ValueError:
        value = registers[y]

    return value


def recover_frequency(instructions):
    registers = defaultdict(int)
    n = len(instructions)
    last_sound_played = None

    ix = 0
    while 0 <= ix < n:
        instruction = instructions[ix]
        if instruction.startswith("snd"):
            last_sound_played = get_value(registers, instruction.removeprefix("snd "))
            ix += 1
        elif instruction.startswith("set"):
            x, y = instruction.removeprefix("set ").split(" ")
            registers[x] = get_value(registers, y)
            ix += 1
        elif instruction.startswith("add"):
            x, y = instruction.removeprefix("add ").split(" ")
            registers[x] += get_value(registers, y)
            ix += 1
        elif instruction.startswith("mul"):
            x, y = instruction.removeprefix("mul ").split(" ")
            registers[x] *= get_value(registers, y)
            ix += 1
        elif instruction.startswith("mod"):
            x, y = instruction.removeprefix("mod ").split(" ")
            registers[x] %= get_value(registers, y)
            ix += 1
        elif instruction.startswith("rcv"):
            x = instruction.removeprefix("rcv ")
            if registers[x] != 0:
                return last_sound_played
            ix += 1
        elif instruction.startswith("jgz"):
            x, y = instruction.removeprefix("jgz ").split(" ")
            offset = get_value(registers, y)
            ix = ix + offset if registers[x] != 0 else ix + 1


def main():
    data = read_input_data("../resources/input_18.txt")
    result = recover_frequency(data)
    print(result)


if __name__ == "__main__":
    main()
