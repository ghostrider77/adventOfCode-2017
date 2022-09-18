import math


def calc_manhattan_distance(n):
    k = math.ceil(math.sqrt(n))
    if k % 2 == 1:
        k -= 1

    ring_id = k // 2
    previous_corner = k - 1
    midpoints = [previous_corner ** 2 + ring_id + 2 * k * ring_id for k in range(4)]
    return min(map(lambda x: abs(x - n), midpoints)) + ring_id


def main():
    square = 265149
    result = calc_manhattan_distance(square)
    print(result)


if __name__ == "__main__":
    main()
