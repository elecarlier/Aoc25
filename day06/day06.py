def parse_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def format_data(data):
    split_lines = [line.split() for line in data]

    problems = list(zip(*split_lines))
    print(problems)
    return problems
    operations = data[-1].split()
    problems = []
    # print("OPERATIONS:", operations)
    for i in range(len(data) - 1):
        new_line = data[i].split(' ')
        new_line.append(operations[i])
        problems.append(new_line)
    print("problems", problems)
    return problems

def part_one(data):
    sum = 0

    for i in range(len(data)):
        res = 0
        if data[i][-1] == '*':
            for j in range(len(data[i]) - 1):
                if data[i][j] == '':
                    continue
                if j != 0:
                    res *= int(data[i][j])
                else:
                    res = int(data[i][j])
        else:
            for j in range(len(data[i]) - 1):
                if data[i][j] == '':
                    continue
                res += int(data[i][j])
        print("Res =", res)
        sum += res
    return sum


def main():
    data = []
    data = parse_input("input.txt")
    print(data)
    pb = format_data(data)

    res1 = part_one(pb)
    # res2 = part_two(ranges)
    print("#1 ->", res1)
    # print("#1 ->", res2)


main()