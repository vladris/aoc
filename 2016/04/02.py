input = open("input").readlines()

for line in input:
    name, check = line.split("[")
    elems = name.split("-")
    id = int(elems[-1])

    name = " ".join(["".join([chr((ord(c) - ord("a") + id) % 26 + ord("a")) for c in elem]) for elem in elems[:-1]])
    if "north" in name:
        print(id)
