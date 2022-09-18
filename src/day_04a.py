def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def is_valid_passphrase(passphrase):
    s = set()
    for word in passphrase:
        if word in s:
            return False

        s.add(word)

    return True


def calc_nr_valid_passphrases(lines):
    n = 0
    for line in lines:
        passphrase = line.split()
        if is_valid_passphrase(passphrase):
            n += 1
    return n


def main():
    data = read_input_data("../resources/input_04.txt")
    result = calc_nr_valid_passphrases(data)
    print(result)


if __name__ == "__main__":
    main()
