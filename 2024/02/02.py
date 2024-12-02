lines = [line.split() for line in open("input").readlines()]
lines = [list(map(int, l)) for l in lines]

def safe(line):
    direction = 1 if line[0] > line[1] else -1
    return all([1 <= (x - y) * direction <= 3 for x, y in zip(line, line[1:])])
        
def safe_line(line):
    if safe(line):
        return True

    for i in range(len(line)):
        l = line[:i] + line[i + 1:]
        if safe(l):
            return True

    return False

total = [safe_line(line) for line in lines].count(True)

print(total)
