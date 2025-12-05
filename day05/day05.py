
def parse_input(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def format_data(data):
    ranges = []
    ids = []

    parse_range = True
    for i in data:
        # print("i ", i)
        if i == '':
            parse_range = False
            continue
        if parse_range:
            start, end = i.split('-')
            ranges.append((int(start), int(end)))
        else:
            ids.append(int(i))

    return ranges, ids

def part_one(ranges, ids):
    fresh = 0
    for i in range(len(ids)):
        for start, end in ranges:
            if start <= ids[i] <= end:
                fresh += 1
                # print("fresh ", ids[i], "-> in interval", start, end)
                break
    return fresh

# new approach : merging the intervales that overlap
def part_two(ranges):
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return sum(end - start + 1 for start, end in merged)

# This approach was consuming too much CPU and would end up with a sigkill
# def part_two(ranges):
#
#     ids = set()
#     for start, end in ranges:
#         num = start
#         for i in range(start, end + 1):
#             ids.add(i)
#
#     return len(ids)

def main():
    data = []
    data = parse_input("input.txt")
    ranges, ids = format_data(data)
    res1 = part_one(ranges, ids)
    res2 = part_two(ranges)
    print("#1 ->", res1)
    print("#1 ->", res2)


main()