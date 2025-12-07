lines = open("input").readlines()
beams = set([lines[0].index("S")])

hits = 0
for line in lines: 
    new_beams = set()
    for beam in beams:
        if line[beam] == "^":
            hits += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        else:
            new_beams.add(beam)
    beams = new_beams

print(hits)