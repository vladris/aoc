robots = [line.strip().split(" ") for line in open("input").readlines()]
robots = [((int(r[0][2:].split(",")[0]), int(r[0].split(",")[1])), 
          (int(r[1][2:].split(",")[0]), int(r[1].split(",")[1]))) for r in robots]

max_x, max_y = 101, 103

def render():
    for i in range(max_y):
        for j in range(max_x):
            if (j, i) in [robot[0] for robot in robots]:
                print("#", end="")
            else:
                print(" ", end="")
        print()
    print()


counter = 0
while True:
    robots = [((((r[0][0] + r[1][0]) % max_x), ((r[0][1] + r[1][1]) % max_y)), r[1]) for r in robots]
    counter += 1
    if (counter - 33) % 103 == 0:
        render()
        print(counter)
        input()
