graph = [line.strip().split(" ") for line in open("input").readlines()]
graph = {line[0][:-1]: line[1:] for line in graph}

total = 0

def traverse(node):
    global total

    if node == "out":
        total += 1
        return

    for n in graph[node]:
        traverse(n)

traverse("you")
print(total)
