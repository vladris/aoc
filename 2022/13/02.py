import functools


def patch_types(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left, right

    if isinstance(left, int):
        return patch_types([left], right)

    if isinstance(right, int):
        return patch_types(left, [right])

    for i in range(min(len(left), len(right))):
        left[i], right[i] = patch_types(left[i], right[i])
    return left, right


def compare(i, j):
    i, j = patch_types(i, j)
    if i > j:
        return 1
    elif i < j:
        return -1
    else:
        return 0


lines = [eval(line) for line in open('input').readlines()
         if line != '\n'] + [[2], [6]]

lines = sorted(lines, key=functools.cmp_to_key(compare))
for i, line in enumerate(lines):
    if compare(line, 2) == 0:
        d1 = i + 1
    if compare(line, 6) == 0:
        d2 = i + 1

print(d1 * d2)
