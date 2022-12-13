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


lines = open('input').readlines()
i, total = 0, 0
while i < len(lines):
    left, right = eval(lines[i]), eval(lines[i + 1])
    left, right = patch_types(left, right)
    if left <= right:
        total += i // 3 + 1
    i += 3

print(total)
