orbits = [line.strip().split(')') for line in open('input')]

tree = { orbit[1]: orbit[0] for orbit in orbits }

def count_orbits(obj):
    return 1 + count_orbits(tree[obj]) if obj != 'COM' else 0

count = 0
for obj in tree:
    count += count_orbits(obj)

print(count)