from functools import reduce

input = open("input").read().strip()

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

print(hash)
