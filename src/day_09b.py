def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def count_garbage(stream):
    count = 0
    garbage = False
    skip_next_char = False
    for char in stream:
        if garbage:
            if skip_next_char:
                skip_next_char = False

            elif char == "!":
                skip_next_char = True

            elif char == ">":
                garbage = False

            else:
                count += 1

        elif char == "<":
            garbage = True

    return count


def main():
    data = read_input_data("../resources/input_09.txt")
    result = count_garbage(data[0])
    print(result)


if __name__ == "__main__":
    main()
