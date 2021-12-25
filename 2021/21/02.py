with open("input") as f:
    p1 = int(f.readline()[28:])
    p2 = int(f.readline()[28:])

combs = {}
for d1 in range(1, 4):
    for d2 in range(1, 4):
        for d3 in range(1, 4):
            total = d1 + d2 + d3
            if total not in combs:
                combs[total] = 0
            combs[total] += 1

def play(pos, rest, moves, fact, wins, plays):
    if rest <= 0:
        if moves not in wins:
            wins[moves] = 0
        wins[moves] += fact
        return
    else:
        if moves not in plays:
            plays[moves] = 0
        plays[moves] += fact

    for d in range(3, 10):
        p = pos + d
        while p > 10:
            p -= 10
        play(p, rest - p, moves + 1, fact * combs[d], wins, plays)

wins1, plays1, wins2, plays2 = {}, {}, {}, {}
play(p1, 21, 0, 1, wins1, plays1)
play(p2, 21, 0, 1, wins2, plays2)

total1 = sum([wins1[w] * plays2[w - 1] for w in wins1])
total2 = sum([wins2[w] * (plays1[w] if w in plays1 else 0) for w in wins2])

print(max(total1, total2))
