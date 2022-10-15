
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def parse_firewall_layers(lines):
    return {int(depth): int(area_range) for depth, area_range in map(lambda x: x.split(": "), lines)}


def is_caught(layers, delay):
    for depth, scanning_area_range in layers.items():
        period = 2 * (scanning_area_range - 1)
        if (depth + delay) % period == 0:
            return True

    return False


def calc_smallest_delay(firewall_layers):
    delay = 0
    while is_caught(firewall_layers, delay):
        delay += 1
    return delay


def main():
    data = read_input_data("../resources/input_13.txt")
    firewall_layers = parse_firewall_layers(data)
    result = calc_smallest_delay(firewall_layers)
    print(result)


if __name__ == "__main__":
    main()
