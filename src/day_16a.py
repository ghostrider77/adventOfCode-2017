import string

ALPHABET = string.ascii_lowercase


def read_input_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def lets_dance(programs, moves):
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

    return "".join(programs)


def main():
    data = read_input_data("../resources/input_16.txt")
    moves = data[0].split(",")
    programs = list(ALPHABET[:16])
    result = lets_dance(programs, moves)
    print(result)


if __name__ == "__main__":
    main()
