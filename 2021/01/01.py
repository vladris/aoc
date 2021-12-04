depths = map(int, open("input").readlines())

print(len(filter(
    lambda d: d > 0, 
    (map(
        lambda d: d[0] - d[1], 
        zip(depths, [depths[0]] + depths))))))
