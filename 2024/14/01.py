robots = [line.strip().split(" ") for line in open("input").readlines()]
robots = [((int(r[0][2:].split(",")[0]), int(r[0].split(",")[1])), 
          (int(r[1][2:].split(",")[0]), int(r[1].split(",")[1]))) for r in robots]

max_x, max_y = 101, 103

def move(robot):
    x, y = robot[0]
    dx, dy = robot[1]

    for i in range(100):
        x = (x + dx) % max_x
        y = (y + dy) % max_y

    return x, y


q1, q2, q3, q4 = 0, 0, 0, 0
for robot in robots:
    x, y = move(robot)
    if x < max_x // 2 and y < max_y // 2:
        q1 += 1
    elif x > max_x // 2 and y < max_y // 2:
        q2 += 1
    elif x < max_x // 2 and y > max_y // 2:
        q3 += 1
    elif x > max_x // 2 and y > max_y // 2:
        q4 += 1

print(q1 * q2 * q3 * q4)
