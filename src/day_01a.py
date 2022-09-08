
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def calc_sum_of_matching_digits(circular_number):
    s = 0
    for a, b in zip(circular_number, circular_number[1:]):
        if a == b:
            s += int(a)

    if circular_number and circular_number[-1] == circular_number[0]:
        s += int(circular_number[0])

    return s


def main():
    data = read_input_data("../resources/input_01.txt")
    circular_number = data[0]
    result = calc_sum_of_matching_digits(circular_number)
    print(result)


if __name__ == "__main__":
    main()
