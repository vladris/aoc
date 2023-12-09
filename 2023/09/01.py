seqs = [list(map(int, line.strip().split(' '))) for
        line in open('input').readlines()]

def next_value(seq):
    deltas = []
    while any([val != 0 for val in seq]):
        deltas.append(seq)
        seq = [v[1] - v[0] for v in zip(seq, seq[1:])]

    return sum([seq[-1] for seq in deltas])


print(sum([next_value(seq) for seq in seqs]))
