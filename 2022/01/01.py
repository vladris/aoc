print(max([sum(map(int, elf.split('\n')))
    for elf in open('input').read().split('\n\n')]))
