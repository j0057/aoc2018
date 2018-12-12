#!/usr/bin/env python3

import re
import sys
from functools import reduce

def iterate(state, new):
    while 1:
        yield state
        state = new(state)

def parse(lines):
    return [tuple(map(int, re.findall(r'-?\d+', line))) for line in lines]

def move(points):
    return iterate(points, lambda points: [(px+vx, py+vy, vx, vy) for (px, py, vx, vy) in points])

def bbox(points):
    l, t = reduce(lambda a, b: map(min, zip(a, b)), [(x, y) for (x, y, _, _) in points])
    r, b = reduce(lambda a, b: map(max, zip(a, b)), [(x, y) for (x, y, _, _) in points])
    return (l, t, r, b)

def surface(points):
    l, t, r, b = bbox(points)
    return r-l * b-t

def display(points, L, T, R, B):
    on = {(x, y) for (x, y, _, _) in points}
    for y in range(T, B+1):
        for x in range(L, R+1):
            sys.stdout.buffer.write(b'X' if (x, y) in on else b' ')
        sys.stdout.buffer.write(b'\n')

def main():
    with open('input/day10.txt') as f:
        p1, s1, i = None, 2**64, 0
        for p2 in move(parse(f)):
            i += 1
            s2 = surface(p2)
            if s2 > s1:
                display(p1, *bbox(p1))
                print(f"found after {i} iterations")
                break
            p1, s1 = p2, s2

if __name__ == '__main__':
    main()
