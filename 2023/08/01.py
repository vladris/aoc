lines = open('input').readlines()

moves = lines[0].strip()
nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}

node, i = 'AAA', 0
while node != 'ZZZ':
    node = nodes[node][0] if moves[0] == 'L' else nodes[node][1]
    i += 1
    moves = moves[1:] + moves[0]

print(i)
