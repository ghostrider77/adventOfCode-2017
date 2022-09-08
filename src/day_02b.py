
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def convert_to_intlist(line):
    return [int(item) for item in line.split()]


def read_spreadsheet(lines):
    return [convert_to_intlist(line) for line in lines]


def calc_division_result(numbers):
    sorted_numbers = sorted(numbers)
    for ix, a in enumerate(sorted_numbers):
        for b in sorted_numbers[ix+1:]:
            k, r = divmod(b, a)
            if r == 0:
                return k
    return 0


def calc_checksum(spreadsheet):
    checksum = 0
    for line in spreadsheet:
        checksum += calc_division_result(line)
    return checksum


def main():
    data = read_input_data("../resources/input_02.txt")
    spreadsheet = read_spreadsheet(data)
    result = calc_checksum(spreadsheet)
    print(result)


if __name__ == "__main__":
    main()
