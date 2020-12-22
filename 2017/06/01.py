banks = list(map(int, open("input").read().split("\t")))

known = set()

steps = 0
while True:
    steps += 1 
    i = banks.index(max(banks))
    v = banks[i]
    banks[i] = 0
    while v:
        i = (i + 1) % len(banks)
        banks[i] += 1
        v -= 1

    state = ",".join(map(str, banks))
    if state in known:
        break
    known.add(state)
    
print(steps)
