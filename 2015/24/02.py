import sys

input = list(map(int, open("input").readlines()))

target, count, qe = sum(input) // 4, sys.maxsize, sys.maxsize

def group(items, total, prod, rest):
    global target, count, qe

    if total > target or len(items) > count:
        return

    if total == target:
        if len(items) < count:
            count, qe = len(items), prod
        else:
            qe = min(qe, prod)
        return

    if not rest:
        return

    group(items + [rest[0]], total + rest[0], prod * rest[0], rest[1:])
    group(items, total, prod, rest[1:])

group([], 0, 1, input)
print(qe)
