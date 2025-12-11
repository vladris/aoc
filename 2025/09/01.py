points = [line.strip().split(",") for line in open("input").readlines()]
points = [(int(x), int(y)) for x, y in points]

area = 0
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        area = max(area,
                    (1 + abs(points[i][0] - points[j][0])) * 
                    (1 + abs(points[i][1] - points[j][1])))
print(area)
