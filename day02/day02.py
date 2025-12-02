

def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            s = line.strip()

    data.append(s.split(","))
    return data[0]



def calc_valid(ids):
    sum = 0
    min = ids[0]
    max = ids[1]

    diff = int(max) - int(min)
    len_min = len(min)
    len_max = len(max)

    for i in range(diff + 1):
        len_cur = len(min)
        if len_cur % 2 != 0:
            # nombre impair → impossible, on skip
            min = str(int(min) + 1)
            continue
        half = len_cur // 2
        x = int(min[:half])
        y = int(min[half:])
        if x == y:
            # print("INVALID :", min)
            sum += int(min)
        min = str(int(min) + 1)

    return sum


def calc_valid2(ids):
    sum = 0
    min = ids[0]
    max = ids[1]

    diff = int(max) - int(min)
    for j in range(diff + 1):
        len_s = len(min)
        k = 1
        for i in range(len_s // 2):
            if len_s % k == 0:
                motif = min[:k]
                rep = motif * (len_s // k)
                if rep == min:
                    # print("INVALID :", min)
                    sum += int(min)
                    break
            k+=1
        min = str(int(min) + 1)
    return sum

def main():
    res1 = 0
    res2 = 0
    data = []
    ids = []
    data = parse_input("input.txt")
    # print(data)
    for i, range in enumerate(data):
        ids.append(range.split("-"))
        res1  += calc_valid(ids[i])
        res2 += calc_valid2(ids[i])

    print("#1 ->", res1)
    print("#1 ->", res2)


main()