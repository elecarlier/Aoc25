def parse_input(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            node, neighbors = line.split(':')
            neighbors_list = neighbors.split()
            graph[node] = neighbors_list
    # print(data)
    return graph

def part_one(data):
    start = 'you'
    end = 'out'
    stack = [[start]]
    paths = []

    while stack:
        path = stack.pop()
        node = path[-1]
        if node == end:
            paths.append(path)
        else:
            for neighbor in data.get(node, []):
                stack.append(path + [neighbor])


    print(len(paths))  # 5 pour ton exemple
    print(paths)       # pour voir tous les chemins
    return(len(paths))

def main():
    data = []
    # data = parse_input("input_test.txt")
    data = parse_input("input.txt")
    print(data)
    res1 = part_one(data)
    # res2 = part_two(data)
    # print("#1 ->", res1)
    # print("#1 ->", res2)


main()