
def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    print(data)
    return data

def part_two(bank):
    remove = len(bank) - 12
    stack = []
    for digit in bank:
        while remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            remove -= 1
        stack.append(digit)

    return "".join(stack[:12])

def part_one(bank):
    digits = list(bank)
    best = 0

    for i in range(len(digits) - 1):
        first = int(digits[i])
        rest = digits[i+1:]
        second = max(int(d) for d in rest)
        pair = first * 10 + second
        if pair > best:
            best = pair

    return best


def main():
    res1 = 0
    res2 = 0
    data = []
    data = parse_input("input.txt")
    for i in data:
        res1 += part_one(i)
        res2 += int(part_two(i))
    print("#1 ->", res1)
    print("#1 ->", res2)


main()