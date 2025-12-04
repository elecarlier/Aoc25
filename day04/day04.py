def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    # print(data)
    return data

def part_one(data):
    directions = [(-1, -1), (-1, 0), (-1, +1),(0, -1), (0, +1),(+1, -1), (+1, 0), (+1, +1)]

    accessible_rolls = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '@':
                count = 0
                for di in range(len(directions)):
                        posy = i + directions[di][0]
                        posx = j + directions[di][1]
                        if 0 <= posx < len(data[i]) and 0 <= posy < len(data):
                            if data[posy][posx] == '@':
                                count += 1
                if count < 4:
                    accessible_rolls += 1


    print(accessible_rolls)
    return accessible_rolls


def part_two(data):
    directions = [(-1, -1), (-1, 0), (-1, +1),(0, -1), (0, +1),(+1, -1), (+1, 0), (+1, +1)]
    accessible_rolls = 1
    sum = 0
    while accessible_rolls != 0:
        state = []
        accessible_rolls = 0
        for i in range(len(data)):
            new_line = []
            for j in range(len(data[i])):
                if data[i][j] == '@':
                    count = 0
                    for di in range(len(directions)):
                            posy = i + directions[di][0]
                            posx = j + directions[di][1]
                            if 0 <= posx < len(data[i]) and 0 <= posy < len(data):
                                if data[posy][posx] == '@':
                                    count += 1
                    if count < 4:
                        accessible_rolls += 1
                        new_line.append('.')
                    else:
                        new_line.append('@')
                else:
                    new_line.append('.')
            state.append(new_line)
        sum += accessible_rolls
        data = state

    print(sum)
    return sum

def main():
    data = []
    data = parse_input("input.txt")
    # print(data)
    res1 = part_one(data)
    res2 = part_two(data)
    # print("#1 ->", res1)
    # print("#1 ->", res2)

main()