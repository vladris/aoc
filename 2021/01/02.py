depths = map(int, open("input").readlines())

depths = map(sum, zip(depths, depths[1:], depths[2:]))

print(len(filter(
    lambda d: d > 0, 
    (map(
        lambda d: d[0] - d[1], 
        zip(depths, [depths[0]] + depths))))))

