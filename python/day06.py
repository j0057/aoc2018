from itertools import takewhile
from functools import reduce
from collections import Counter

def parse(lines):
    points = [tuple(int(i) for i in line.split(', ')) for line in lines]
    L, T = reduce(lambda a, b: map(min, zip(a, b)), points)
    R, B = reduce(lambda a, b: map(max, zip(a, b)), points)
    return (points, L, T, R, B)

def day06a(points, L, T, R, B):
    grid = {}
    for x in range(L, R+1):
        for y in range(T, B+1):
            distances = sorted((abs(px-x) + abs(py-y), n) for (n, (px, py)) in enumerate(points))
            closest = [*takewhile(lambda t: t[0] == distances[0][0], distances)]
            if len(closest) > 1:
                continue
            grid[x, y] = closest[0][1]
    edges = {n for ((x, y), n) in grid.items() if x in {L, R} or y in {T, B}}
    counts = Counter(n for n in grid.values() if n not in edges)
    return counts.most_common(1)[0][1]

def day06b(points, L, T, R, B, s):
    grid = {}
    for x in range(L, R+1):
        for y in range(T, B+1):
            d = sum(abs(px-x) + abs(py-y) for (px, py) in points)
            if d >= s:
                continue
            grid[x, y] = 1
    return sum(grid.values())

EX06 = [(1, 1), (1, 6), (8, 3), (3, 4), (5, 5), (8, 9)]

def test_06_ex1(): assert day06a(EX06, 1, 1, 8, 9)     == 17
def test_06_ex2(): assert day06b(EX06, 1, 1, 8, 9, 32) == 16

def test_06a(day06_lines): assert day06a(*parse(day06_lines))        == 4754
def test_06b(day06_lines): assert day06b(*parse(day06_lines), 10000) == 42344
