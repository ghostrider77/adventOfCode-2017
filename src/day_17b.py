from collections import deque


def get_spinlock_value(step_size, nr_rounds):
    buffer = deque([0])
    for n in range(1, nr_rounds+1):
        buffer.rotate(-step_size)
        buffer.append(n)

    position = (buffer.index(0) + 1) % n
    return buffer[position]


def main():
    step_size = 328
    nr_rounds = 50_000_000
    result = get_spinlock_value(step_size, nr_rounds)
    print(result)


if __name__ == "__main__":
    main()
