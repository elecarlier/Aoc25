from collections import defaultdict

def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    # print(data)
    return data


def part_two(data):
    hauteur = len(data)
    largeur = len(data[0])

    start_x = None
    for x in range(largeur):
        if data[0][x] == 'S':
            start_x = x
            break

    beams = {start_x: 1}

    for y in range(hauteur - 1):
        next_beams = defaultdict(int)
        for x, count in beams.items():
            cell = data[y + 1][x]
            if cell == '.':
                next_beams[x] += count
            elif cell == '^':

                if x - 1 >= 0:
                    next_beams[x - 1] += count
                if x + 1 < largeur:
                    next_beams[x + 1] += count

        beams = next_beams

    total_timelines = sum(beams.values())
    return total_timelines

def part_one(data):
    hauteur = len(data)
    largeur = len(data[0])

    for x in range(largeur):
        if data[0][x] == 'S':
            start_x = x
            break

    split_count = 0
    beams = {start_x: 1}

    for y in range(hauteur - 1):
        next_beams = {}
        splitters_touches_ligne = set()

        for x, count in beams.items():
            cell = data[y + 1][x]
            if cell == '.':
                if x in next_beams:
                    next_beams[x] += count
                else:
                    next_beams[x] = count
            elif cell == '^':
                splitters_touches_ligne.add(x)
                if x - 1 >= 0:
                    next_beams[x - 1] = next_beams.get(x - 1, 0) + count
                if x + 1 < largeur:
                    next_beams[x + 1] = next_beams.get(x + 1, 0) + count

        split_count += len(splitters_touches_ligne)
        beams = next_beams
        return split_count

def main():
    data = []
    # data = parse_input("input_test.txt")
    data = parse_input("input.txt")
    # print(data)
    res1 = part_one(data)
    res2 = part_two(data)
    print("#1 ->", res1)
    print("#1 ->", res2)


main()