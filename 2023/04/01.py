total = 0
for line in open('input').readlines():
    line = line.split(':')[1]
    winning, yours = line.split('|')
    winning, yours = set(winning.strip().split(' ')) - {''}, set(yours.strip().split(' ')) - {''}
    matches = len(winning.intersection(yours))

    if matches > 0:
        total += 2 ** (matches - 1)

print(total)
