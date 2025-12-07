from collections import defaultdict

lines = open("input").readlines()
beams = {lines[0].index("S"): 1}

for line in lines: 
    new_beams = defaultdict(int)
    for beam in beams:
        if line[beam] == "^":
            new_beams[beam - 1] += beams[beam]
            new_beams[beam + 1] += beams[beam]
        else:
            new_beams[beam] += beams[beam]
    beams = new_beams

print(sum(beams.values()))