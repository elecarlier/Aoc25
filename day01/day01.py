
import sys

res1 = 0

def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    # print(data)
    return data

def calc_2(data):
    hits = 0
    pos = 50
    for i in data:
        direction = i[0]
        num = int(i[1:])
        step = +1 if direction == 'R' else -1

        for _ in range(num):
            pos = (pos + step) % 100
            if pos == 0:
                hits += 1
    return hits


def calc(data):
    res = 0
    start = 50
    for i in data:
        direction = i[0]
        num = int(i[1:])
        if direction == 'L':
            start = (start - num) % 100
        else:
            start = (start + num) % 100
        print(start)
        if start == 0:
            res += 1
    return res

def main():
    data = []
    data = parse_input("input.txt")
    print(data)
    res1 = calc(data)
    res2 = calc_2(data)
    print("#1 ->", res1)
    print("#1 ->", res2)


main()