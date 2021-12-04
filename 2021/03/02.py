lines = open("input").readlines()

bits = [map(int, list(line.strip())) for line in lines]

def search(bits, cond):
    i = 0
    while len(bits) > 1:
        n = int(sum([b[i] for b in bits])) 
        c = int(cond(n, len(bits) - n))
        bits = filter(lambda b: b[i] == c, bits)
        i += 1
    return int("".join(map(str, bits[0])), 2)

o2 = search(bits[:], lambda x, y: x >= y)
co2 = search(bits[:], lambda x, y: x < y)

print(o2 * co2)