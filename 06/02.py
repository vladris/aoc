orbits = [line.strip().split(')') for line in open('input')]

tree = { orbit[1]: orbit[0] for orbit in orbits }

def count_orbits(obj):
    return 1 + count_orbits(tree[obj]) if obj != 'COM' else 0

def step(obj, count):
    for _ in range(count):
        obj = tree[obj]
    return obj

you, san = 'YOU', 'SAN'
delta_you, delta_san = count_orbits('YOU'), count_orbits('SAN')

if delta_san > delta_you:
    san = step(san, delta_san - delta_you)
elif delta_you > delta_san:
    you = step(you, delta_you - delta_san)

count = abs(delta_san - delta_you)

while san != you:
    san, you = step(san, 1), step(you, 1)
    count += 2

print(count - 2)