import re

sensors = []

for line in open('input').readlines():
    m = re.match('Sensor at x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)$', line)
    sx, sy, bx, by = map(int, m.groups())
    radius = abs(sx - bx) + abs(sy - by)
    sensors.append((sx, sy, radius))


def in_range(x, y):
    for sensor in sensors:
        if abs(sensor[0] - x) + abs(sensor[1] - y) <= sensor[2]:
            return True, sensor

    return False, None


x, y = 0, 0
while True:
    found, sensor = in_range(x, y)
    if not found:
        break

    x = sensor[0] + sensor[2] - abs(sensor[1] - y) + 1
    if x > 4_000_000:
        x = 0
        y += 1


print(x * 4_000_000 + y)
