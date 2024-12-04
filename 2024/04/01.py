lines = ["..." + line.strip() + "..." for line in open("input").readlines()]
pad = "." * len(lines[0]) 
lines = [pad] * 3 + lines + [pad] * 3

def scan(i, j):
    return sum([
        lines[i][j-3:j+1] == "SAMX",
        lines[i][j:j+4] == "XMAS",
        lines[i-3][j] + lines[i-2][j] + lines[i-1][j] + lines[i][j] == "SAMX",
        lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j] == "XMAS",
        lines[i-3][j-3] + lines[i-2][j-2] + lines[i-1][j-1] + lines[i][j] == "SAMX",
        lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3] == "XMAS",
        lines[i-3][j+3] + lines[i-2][j+2] + lines[i-1][j+1] + lines[i][j] == "SAMX",
        lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3] == "XMAS"
    ])

print(sum([scan(i, j) for i in range(3, len(lines) - 3) for j in range(3, len(lines[i]) - 3)]))
