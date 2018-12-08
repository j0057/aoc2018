from collections import defaultdict
from itertools import chain, groupby
import re

def parse(lines):
    return [re.findall(r'[Ss]tep ([A-Z])', line) for line in lines]

def day07a(steps):
    G = {k: [v for (_, v) in g] for (k, g) in groupby(sorted(steps), lambda t: t[0])}
    L, S = [], {v for  v in G.keys() if v not in chain(*G.values())}
    while S:
        n = min(S)
        S.remove(n)
        L.append(n)
        S.update({m for m in G.pop(n, []) if m not in chain(*G.values())})
    return ''.join(L)

def day07b(steps, workers, time):
    G = {k: [v for (_, v) in g] for (k, g) in groupby(sorted(steps), lambda t: t[0])}
    L, S = [], {v for  v in G.keys() if v not in chain(*G.values())}
    t, W, U = 0, [0]*workers, defaultdict(list)
    while S or U:
        t, W = t+1, [max(0, w-1) for w in W]
        for u in U[t]:
            u()
        del U[t]
        while S and 0 in W:
            n = min(S)
            S.remove(n)
            L.append(n)
            U[t+ord(n)-time].append((lambda n: lambda: S.update({m for m in G.pop(n, []) if m not in chain(*G.values())}))(n))
            W[W.index(0)] = ord(n)-time
    return t-1

EX07 = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]

def test_07_ex1(): assert day07a(EX07) == 'CABDFE'
def test_07_ex2(): assert day07b(EX07, 2, 64) == 15

def test_07a(day07_lines): assert day07a(parse(day07_lines)) == 'BFLNGIRUSJXEHKQPVTYOCZDWMA'
def test_07b(day07_lines): assert day07b(parse(day07_lines), 5, 4) == 880
