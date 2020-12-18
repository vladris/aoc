input = open("input").readlines()

def id(line):
    name, check = line.split("[")
    elems = name.split("-")
    name, id, cnt = "".join(elems[:-1]), int(elems[-1]), {}

    for c in name:
        if c not in cnt:
            cnt[c] = 0
        cnt[c] += 1

    return id if "".join(sorted(cnt.keys(), key=lambda x: (-cnt[x], x)))[:5] == check[:-2] else 0

print(sum([id(line) for line in input]))
