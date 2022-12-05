lines = open('input').readlines()

stacks = [[] for _ in range(10)]

for n, line in enumerate(lines[:8]):
    for i in range(9):
        if (c := line[i * 4 + 1]) != ' ':
            stacks[i].insert(0, line[i * 4 + 1])

for line in lines[10:]:
    [_, count, _, src, _, dst] = line.strip().split(' ')
    count, src, dst = int(count), int(src) - 1, int(dst) - 1
    stacks[dst] += stacks[src][-count:]
    stacks[src] = stacks[src][:-count]

print(''.join([stack[-1] if stack else '' for stack in stacks]))
