import math

lines = open('input').readlines()

moves = lines[0].strip()
nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}

current = [node for node in nodes if node[-1] == 'A']

def find_z(cell, moves):
    i = 0
    while cell[-1] != 'Z':
        cell = nodes[cell][0] if moves[0] == 'L' else nodes[cell][1]
        moves = moves[1:] + moves[0]
        i += 1

    return i


zs = [find_z(node, moves) for node in current]

def lcm(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // math.gcd(lcm, i)

    return lcm

print(lcm(zs))
