def load_names(filename):
    names = {}
    with open(filename, "r") as file:
        for line in file:
            for i, name in enumerate(
                sorted(name.strip('"') for name in line.strip("\n").split(","))
            ):
                names[name] = i + 1
    return names


def compute_score(name, position):
    score = sum(ord(char) - ord("A") + 1 for char in name)
    return score * position


if __name__ == "__main__":
    total = 0
    names = load_names("p22/names.txt")
    for name, position in names.items():
        score = compute_score(name, position)
        total += score
        if name == "COLIN":
            print(score)
    print(total)
