disk = [(i // 2 if i % 2 == 0 else None, int(c)) for i, c in enumerate(open("input").read().strip())]

end = len(disk) - 1
while end > 0:
    if disk[end][0] is None:
        end -= 1
        continue

    for start in range(end):
        if disk[start][0] != None:
            continue

        if disk[start][1] > disk[end][1]:
            disk = disk[:start] + [disk[end]] + [(None, disk[start][1] - disk[end][1])] + disk[start + 1:end] + [(None, disk[end][1])] + disk[end + 1:]
            end -= 1
            break;
        elif disk[start][1] == disk[end][1]:
            disk = disk[:start] + [disk[end]] + disk[start + 1:end] + [disk[start]] + disk[end + 1:]
            end -= 1
            break
    else:
        end -= 1


i, total = 0, 0
for segment in disk:
    total += sum([(segment[0] if segment[0] else 0) * (i + j) for j in range(segment[1])])
    i += segment[1]

print(total)
