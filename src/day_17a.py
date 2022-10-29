
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def get_spinlock_value(step_size, nr_rounds):
    buffer = [0]
    position = 0
    for n in range(1, nr_rounds+1):
        position = (position + step_size) % n + 1
        buffer.insert(position, n)

    position = (position + 1) % n
    return buffer[position]


def main():
    step_size = 328
    nr_rounds = 2017
    result = get_spinlock_value(step_size, nr_rounds)
    print(result)


if __name__ == "__main__":
    main()
