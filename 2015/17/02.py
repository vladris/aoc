input = list(map(int, open("input").readlines()))

solutions = []
def mix(containers, vol, used):
    global solutions
    if vol == 0:
        solutions += [len(used)]
        return

    if vol < 0 or not containers:
        return

    mix(containers[1:], vol - containers[0], used + [containers[0]])
    mix(containers[1:], vol, used)

mix(input, 150, [])
print(len(list(filter(lambda x: x == min(solutions), solutions))))