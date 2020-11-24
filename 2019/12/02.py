import re
import math

planets = []
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in open('input').readlines():
    planets.append([int(i) for i in re.match('<x=(-?\\d+), y=(-?\\d+), z=(-?\\d+)>', line).groups()])

def gravity(dim):
    for i in range(len(planets)):
        for j in range(len(planets)):
            if planets[i] == planets[j]: continue

            if planets[i][dim] < planets[j][dim]:
                vel[i][dim] += 1
            elif planets[i][dim] > planets[j][dim]:
                vel[i][dim] -= 1

def velocity(dim):
    for i in range(len(planets)):
        planets[i][dim] += vel[i][dim]
        
origin = planets[:]

def at_origin(dim):
    for i in range(len(planets)):
        if planets[i][dim] != origin[i][dim]:
            return False

    for velocity in vel:
        if velocity != [0, 0, 0]:
            return False

    return True

def period(dim):
    i = 1
    while True:
        gravity(dim)
        velocity(dim)
        if at_origin(dim):
            return i
        i += 1

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

p1, p2, p3 = period(0), period(1), period(2)
print(lcm(lcm(p1, p2), p3) * 2)