head, tail = (0, 0), (0, 0)

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
        head = moves[d](*head)

        if abs(tail[0] - head[0]) <= 1 and abs(tail[1] - head[1]) <= 1:
            continue

        dx, dy = delta(head[0], tail[0]), delta(head[1], tail[1])
        tail = (tail[0] + dx, tail[1] + dy)
        
        visited.add(tail)
        

print(len(visited))
