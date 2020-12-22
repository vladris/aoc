step = 344

buffer = [0]
pos = 0

for i in range(1, 2018):
    pos = (pos + step) % len(buffer)
    buffer.insert(pos + 1, i)
    pos += 1

print(buffer[buffer.index(2017) + 1])
