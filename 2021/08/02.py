from itertools import permutations

lines = open("input").readlines()

display = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

def convert(c, digit):
    d = ""
    for wire in digit:
        d += c[wire]
    return "".join(sorted(d))

def solve(digits, output):
    letters = "abcdefg"

    options = permutations(letters)
    for opt in options:
        c = {letters[i]: opt[i] for i in range(len(letters))}
        if all(convert(c, digit) in display for digit in digits):
            result = 0
            for d in output:
                result = result * 10 + display.index(convert(c, d))
            return result

total = 0
for line in lines:
    digits, output = line.split("|")
    digits, output = digits.strip().split(" "), output.strip().split(" ")
    total += solve(digits, output)

print(total)
