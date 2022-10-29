import string

ALPHABET = string.ascii_lowercase


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def lets_dance(programs, moves, nr_rounds):
    first_program = "".join(programs)
    configurations = [first_program]
    for _ in range(nr_rounds):
        for move in moves:
            if move.startswith("s"):
                k = int(move[1:])
                programs = programs[-k:] + programs[:-k]
            elif move.startswith("x"):
                ix, jy = map(int, move[1:].split("/"))
                programs[ix], programs[jy] = programs[jy], programs[ix]
            elif move.startswith("p"):
                p, q = move[1:].split("/")
                ix = programs.index(p)
                jy = programs.index(q)
                programs[ix], programs[jy] = programs[jy], programs[ix]
            else:
                raise ValueError(f"Unknown move {move} encountered.")

        if (result := "".join(programs)) == first_program:
            return configurations[nr_rounds % len(configurations)]

        configurations.append(result)

    return result


def main():
    data = read_input_data("../resources/input_16.txt")
    moves = data[0].split(",")
    programs = list(ALPHABET[:16])
    nr_rounds = 1_000_000_000
    result = lets_dance(programs, moves, nr_rounds)
    print(result)


if __name__ == "__main__":
    main()
