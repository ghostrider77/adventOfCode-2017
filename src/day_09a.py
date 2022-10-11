def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def process_stream(stream):
    score = 0
    depth = 0
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

        elif char == "<":
            garbage = True

        elif char == "{":
            depth += 1

        elif char == "}":
            score += depth
            depth -= 1

    return score


def main():
    data = read_input_data("../resources/input_09.txt")
    result = process_stream(data[0])
    print(result)


if __name__ == "__main__":
    main()
