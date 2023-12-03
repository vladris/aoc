def power(game):
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for colors in game.strip('\n').split(';'):
        for color in colors.split(','):
            count, color = color.strip(' ').split(' ')
            
            if int(count) > mins[color]:
                mins[color] = int(count)
    return mins['red'] * mins['green'] * mins['blue']

print(sum([power(line.split(':')[1]) for line in open('input').readlines()]))
