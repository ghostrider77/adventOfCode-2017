
def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def parse_firewall_layers(lines):
    return {int(depth): int(area_range) for depth, area_range in map(lambda x: x.split(": "), lines)}


def calc_severity(firewall_layers):
    severity = 0
    for depth, scanning_area_range in firewall_layers.items():
        period = 2 * (scanning_area_range - 1)
        if depth % period == 0:
            severity += depth * scanning_area_range
    return severity


def main():
    data = read_input_data("../resources/input_13.txt")
    firewall_layers = parse_firewall_layers(data)
    result = calc_severity(firewall_layers)
    print(result)


if __name__ == "__main__":
    main()
