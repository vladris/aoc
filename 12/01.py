import re

planets = []
vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in open('input').readlines():
    planets.append([int(i) for i in re.match('<x=(-?\\d+), y=(-?\\d+), z=(-?\\d+)>', line).groups()])

def gravity():
    for i in range(len(planets)):
        for j in range(len(planets)):
            if planets[i] == planets[j]: continue

            for k in range(3):
                if planets[i][k] < planets[j][k]:
                    vel[i][k] += 1
                elif planets[i][k] > planets[j][k]:
                    vel[i][k] -= 1

def velocity():
    for i in range(len(planets)):
        for k in range(3):
            planets[i][k] += vel[i][k]

def energy():
    total = 0
    for i in range(len(planets)):
        total += sum([abs(c) for c in planets[i]]) * sum([abs(v) for v in vel[i]])
    return total

for _ in range(1000):
    gravity()
    velocity()

print(energy())