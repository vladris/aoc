lines = [line.strip().split(' ') for line in open('input').readlines()]
lines = [(line[0], list(map(int, line[1].split(',')))) for line in lines]
lines = [('?'.join([line[0]] * 5), line[1] * 5) for line in lines]

def arrangements(tail, broken):
    if not broken:
        return 1 if all([c in '?.' for c in tail]) else 0

    while tail and tail[0] == '.':
        tail = tail[1:]

    if not tail:
        return 0

    if len(tail) < sum(broken) + len(broken) - 1:
        return 0

    if (tail[1:], len(broken)) not in cache:
        cache[(tail[1:], len(broken))] = arrangements(tail[1:], broken) if tail[0] == '?' else 0

    total = cache[(tail[1:], len(broken))]

    if any([c not in '?#' for c in tail[:broken[0]]]):
        return total
        
    if len(broken) == 1 and len(tail) == broken[0]:
        return total + 1
        
    if tail[broken[0]] not in '?.':
        return total
        
    return total + arrangements(tail[broken[0] + 1:], broken[1:])


total = 0
for line in lines:
    cache = {}
    total += arrangements(line[0], line[1])

print(total)
