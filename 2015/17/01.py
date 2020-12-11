input = list(map(int, open("input").readlines()))

found = 0
def mix(containers, vol):
    global found
    if vol == 0:
        found += 1
        return

    if vol < 0 or not containers:
        return

    mix(containers[1:], vol - containers[0])
    mix(containers[1:], vol)

mix(input, 150)
print(found)