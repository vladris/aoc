lines = [line.split(":") for line in open("input").readlines()]
lines = [(int(line[0]), list(map(int, line[1].strip().split()))) for line in lines]

def find(target, current, tail):
    if current == target and tail == []:
        return True

    if current > target or tail == []:
        return False
    
    return find(target, current + tail[0], tail[1:]) or find(target, current * tail[0], tail[1:])

print(sum([line[0] for line in lines if find(line[0], 0, line[1])]))
