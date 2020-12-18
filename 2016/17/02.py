from hashlib import md5

def hash(path):
    passcode = "pvhmgsws"

    return tuple([d in "bcdef" for d in md5((passcode + path).encode("utf-8")).hexdigest()[:4]])

queue = [("", 0, 0)]
longest = ""

while queue:
    path, x, y = queue.pop(0)
    if x == y == 3:
        longest = path
        continue

    u, d, l, r = hash(path)
    if u and y != 0:
        queue.append((path + "U", x, y - 1))
    if d and y != 3:
        queue.append((path + "D", x, y + 1))
    if l and x != 0:
        queue.append((path + "L", x - 1, y)) 
    if r and x != 3:
        queue.append((path + "R", x + 1, y))

print(len(longest))
