time, dist = [line.strip().split(':')[1].split(' ') 
              for line in open('input').readlines()]

time = list(map(int, filter(lambda x: x != '', time)))
dist = list(map(int, filter(lambda x: x != '', dist)))

def acc(t, d):
    return sum([i * (t - i) > d for i in range(t)])
        
total = 1
for t, d in zip(time, dist):
    total *= acc(t, d)

print(total)
