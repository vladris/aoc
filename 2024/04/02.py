lines = ["." + line.strip() + "." for line in open("input").readlines()]
pad = "." * len(lines[0]) 
lines = [pad] + lines + [pad]

def scan(i, j):
    return (lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] in ["MAS", "SAM"]) and \
        (lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1] in ["MAS", "SAM"])

print(sum([scan(i, j) for i in range(1, len(lines) - 1) for j in range(1, len(lines[i]) - 1)]))
