inp = open('input').read()

maps = inp.split('\n\n')

values = [int(seed) for seed in maps[0][7:].split(' ')]

for mapping in maps[1:]:
    data = mapping.split('\n')
    new_values = values[:]
    for rng in [[int(n) for n in rng.split(' ')] for rng in data[1:]]:
        for i in range(len(values)):
            if rng[1] <= values[i] < rng[1] + rng[2]:
                new_values[i] = rng[0] + (values[i] - rng[1])
    values = new_values

print(min(values))
