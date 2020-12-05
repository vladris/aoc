passports = open("input").readlines()

def toid(s):
    return int(s
        .replace("B", "1")
        .replace("R", "1")
        .replace("F", "0")
        .replace("L", "0"), 2)

ids = set(map(toid, passports))
seat = min(ids)
while seat in ids:
    seat += 1
print(seat)
