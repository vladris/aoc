disk = [(i // 2 if i % 2 == 0 else None, int(c)) for i, c in enumerate(open("input").read().strip())]

start, end = 1, len(disk) - 1
while start <= end:
    if disk[start][1] > disk[end][1]:
        disk = disk[:start] + [disk[end]] + [(None, disk[start][1] - disk[end][1])] + disk[start + 1:end] + disk[end + 1:]
        start += 1
        end -= 1
    elif disk[start][1] < disk[end][1]:
        disk = disk[:start] + [(disk[end][0], disk[start][1])] + disk[start + 1:end] + [(disk[end][0], disk[end][1] - disk[start][1])] + disk[end + 1:]
        start += 2
    else:
        disk = disk[:start] + [disk[end]] + disk[start + 1:end] + [disk[start]] + disk[end + 1:]
        start += 2
        end -= 2

    
i, total = 0, 0
for segment in disk:
    total += sum([(segment[0] if segment[0] else 0) * (i + j) for j in range(segment[1])])
    i += segment[1]

print(total)
