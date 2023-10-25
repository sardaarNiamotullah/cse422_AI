src = input('Start Node: ')
des = input('Destination: ')

inputFile = open('Input file.txt', 'r')\

tree = {}
heuristic = {}
anotherTree = {}

for string in inputFile:
    line = string.split(' ')
    arr = []
    diss = {}
    for i in range(len(line)-1, 1, -2):
        arr.append([line[i-1], int(line[i])])
        diss[line[i-1]] = int(line[i])

    tree[line[0]] = arr
    heuristic[line[0]] = int(line[1])
    anotherTree[line[0]] = diss

cost = {src: 0}
def aStarSearch():
    closed = []
    opened = [[src, heuristic[src]]]

    while True:
        fn = [i[1] for i in opened]
        chosen_index = fn.index(min(fn))
        node = opened[chosen_index][0]
        closed.append(opened[chosen_index])
        del opened[chosen_index]
        if closed[-1][0] == des:
            break
        for item in tree[node]:
            if item[0] in [closed_item[0] for closed_item in closed]:
                continue
            cost.update({item[0]: cost[node] + item[1]})
            fn_node = cost[node] + heuristic[item[0]] + item[1]
            temp = [item[0], fn_node]
            opened.append(temp)

    trace_node = des
    sequence = [des]
    for i in range(len(closed)-2, -1, -1):
        check_node = closed[i][0]
        if trace_node in [children[0] for children in tree[check_node]]:
            children_costs = [temp[1] for temp in tree[check_node]]
            children_nodes = [temp[0] for temp in tree[check_node]]

            if cost[check_node] + children_costs[children_nodes.index(trace_node)] == cost[trace_node]:
                sequence.append(check_node)
                trace_node = check_node
    distance = 0

    for i in range(len(sequence)-1):
        froM, tO = sequence[i], sequence[i+1]
        distance += anotherTree[froM][tO]

    sequence.reverse()

    return sequence, distance


try:
    pathToFollow, distance = aStarSearch()
    print(f'Path: ', end='')
    for i in range(len(pathToFollow)-1):
        print(f'{pathToFollow[i]} -> ', end='')
    print(pathToFollow[len(pathToFollow)-1])
    print(f'Total distance: {distance} km')
except:
    print('NO PATH FOUND')