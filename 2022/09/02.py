nodes = [(0, 0)] * 10

moves = {
    'U': lambda x, y: (x, y + 1),
    'R': lambda x, y: (x + 1, y),
    'D': lambda x, y: (x, y - 1),
    'L': lambda x, y: (x - 1, y),
}

visited = set({(0, 0)})


def delta(h, t):
    return 0 if h == t else (-1 if h < t else 1)


for line in open('input').readlines():
    [d, c] = line.strip().split(' ')

    for _ in range(int(c)):
        nodes[0] = moves[d](*nodes[0])

        for i in range(len(nodes) - 1):
            [head, tail] = nodes[i:i+2]

            if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
                break

            dx, dy = delta(head[0], tail[0]), delta(head[1], tail[1])
            nodes[i+1] = (tail[0] + dx, tail[1] + dy)

            if i == 8:
                visited.add(nodes[i+1])
        
print(len(visited))
