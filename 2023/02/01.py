limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def valid_game(game):
    for colors in game.strip('\n').split(';'):
        for color in colors.split(','):
            count, color = color.strip(' ').split(' ')
            
            if int(count) > limits[color]:
                return False
    return True

total = 0

for i, line in enumerate(open('input').readlines()):
    if valid_game(line.split(':')[1]):
        total += i + 1

print(total)
