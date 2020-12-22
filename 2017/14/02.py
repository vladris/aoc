from functools import reduce

input = "amgozmfv"

def knot(input):
    input = [ord(c) for c in input] + [17, 31, 73, 47, 23]

    nums = list(range(256))

    def reverse(f, t):
        while f != t:
            nums[f], nums[t] = nums[t], nums[f]
            f = (f + 1) % len(nums)
            if f == t:
                return
            t = (t - 1) % len(nums)

    pos, skip = 0, 0
    for _ in range(64):
        for l in input:
            if l != 0:
                reverse(pos, (pos + l - 1) % len(nums))
            pos = (pos + l + skip) % len(nums)
            skip += 1

    hash = ""
    for i in range(16):
        hash += "{:02x}".format(reduce(lambda a, b: a ^ b, nums[i * 16:(i + 1) * 16]))

    return(hash)

grid = []
for row in range(128):
    k = knot(f"{input}-{row}")
    line = ""
    for c in k:
        line += "{:04b}".format(int(c, 16))
    grid.append([c for c in line])

def fill(i, j):
    if i == -1 or i == 128:
        return
    if j == -1 or j == 128:
        return
    if grid[i][j] == "0":
        return

    grid[i][j] = "0"
    fill(i - 1, j)
    fill(i + 1, j)
    fill(i, j - 1)
    fill(i, j + 1)

total = 0
for i in range(128):
    for j in range(128):
        if grid[i][j] == "1":
            total += 1
            fill(i, j)

print(total)
