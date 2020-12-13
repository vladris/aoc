from math import gcd

with open("input") as f:
    f.readline()
    buses = [(i, int(b)) for i, b in enumerate(f.readline().split(",")) if b != "x"]

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

time, step, i = 0, 1, 0
while i < len(buses):
    while (time + buses[i][0]) % buses[i][1] != 0:
        time += step
    step = lcm(step, buses[i][1])
    i += 1

print(time)
