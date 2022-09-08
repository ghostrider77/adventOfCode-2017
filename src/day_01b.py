
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def calc_sum_of_matching_digits(circular_number):
    n = len(circular_number)
    k = n // 2
    s = 0
    for ix, elem in enumerate(circular_number):
        jy = (ix + k) % n
        if elem == circular_number[jy]:
            s += int(elem)
    return s


def main():
    data = read_input_data("../resources/input_01.txt")
    circular_number = data[0]
    result = calc_sum_of_matching_digits(circular_number)
    print(result)


if __name__ == "__main__":
    main()
