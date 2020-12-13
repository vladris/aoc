with open("input") as f:
    start = int(f.readline())
    buses = list(map(int, filter(lambda b: b != "x", f.readline().split(","))))

wait = 0
while True:
    for bus in buses:
        if (start + wait) % bus == 0:
            print(wait * bus)
            exit()
    wait += 1
