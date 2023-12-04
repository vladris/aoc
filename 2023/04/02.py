lines = [[1, line] for line in open('input').readlines()]
for i, line in enumerate(lines):
    ln = line[1].split(':')[1]
    winning, yours = ln.split('|')
    winning, yours = set(winning.strip().split(' ')) - {''}, set(yours.strip().split(' ')) - {''}
    matches = len(winning.intersection(yours))
    for j in range(1, matches + 1):
        if i + j == len(lines):
            break

        lines[i + j][0] += line[0]

print(sum([line[0] for line in lines]))
