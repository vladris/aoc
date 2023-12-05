inp = open('input').read()

maps = inp.split('\n\n')

data = [int(seed) for seed in maps[0][7:].split(' ')]
values = list(zip(data[::2], data[1::2]))
values = [(v[0], v[0] + v[1] - 1) for v in values]

for mapping in maps[1:]:
    data = mapping.split('\n')
    ranges = [[int(n) for n in rng.split(' ')] for rng in data[1:]]
    ranges = [(r[1], r[1] + r[2] - 1, r[0] - r[1]) for r in ranges]

    new_values = []
    for rng in ranges:
        for v in values[:]:
            # ( ) [ ]
            if v[1] < rng[0]:
                continue

            # [ ] ( )
            if v[0] > rng[1]:
                continue

            values.remove(v)

            # ( [ ) ]
            if v[0] < rng[0] and v[1] <= rng[1]:
                values.append((v[0], rng[0] - 1))
                new_values.append((rng[0] + rng[2], v[1] + rng[2]))
                continue

            # ( [ ] )
            if v[0] < rng[0] and v[1] > rng[1]:
                values.append((v[0], rng[0] - 1))
                values.append((rng[1] + 1, v[1]))
                new_values.append((rng[0] + rng[2], rng[1] + rng[2]))
                continue

            # [ ( ) ]
            if v[0] >= rng[0] and v[1] <= rng[1]:
                new_values.append((v[0] + rng[2], v[1] + rng[2]))
                continue

            # [ ( ] ) 
            values.append((rng[1] + 1, v[1]))
            new_values.append((v[0] + rng[2], rng[1] + rng[2]))

    values += new_values

print(min(values)[0])
