time, dist = [line.strip().split(':')[1].split(' ') 
              for line in open('input').readlines()]

time = int(''.join(time))
dist = int(''.join(dist))

print(sum([i * (time - i) > dist for i in range(time)]))
