
import sys

res1 = 0

def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip())
    # print(data)
    return data


def calc(data):

    res = 0
    start = 50
    num = 0
    for i in data:
        if len(i) == 2:
            num = i[1]
        else:
            num = i[1] + i[2]
        if i[0] == 'L':
            start -= int(num)
            if start < 0:
                start = 100 + start
        else:
            start += int(num)
            if start >= 100:
                start = start - 100
        print(start)
        if start == 0:
            res += 1
    return res

def main():
    data = []
    data = parse_input("input.txt")
    print(data)
    res1 = calc(data)
    print("#1 ->", res1)


main()