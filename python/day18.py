#!/usr/bin/env python3.7

from collections import defaultdict
import sys
import time

from day10 import iterate
from day12 import nth

def parse(lines):
    return {x + y * 1j: char
            for y, line in enumerate(lines)
            for x, char in enumerate(line)}

def score(state):
    return sum(v=='|' for v in state.values()) * sum(v=='#' for v in state.values())

def day18(state):
    surrounding = [-1-1j, -1j, +1-1j, -1, +1, -1+1j, +1j, +1+1j]
    return iterate(state, lambda state: {p: {'.': '|' if sum(state.get(p+c, None)=='|' for c in surrounding) >= 3 else '.',
                                             '|': '#' if sum(state.get(p+c, None)=='#' for c in surrounding) >= 3 else '|',
                                             '#': '#' if any(state.get(p+c, None)=='#' for c in surrounding)
                                                     and any(state.get(p+c, None)=='|' for c in surrounding) else '.'}[cell]
                                         for (p, cell) in state.items()})

def day18a(state, N):
    state = nth(day18(state), N)
    return score(state)

def day18b(state, N):
    w, h = max(int(c.real) for c in state), max(int(c.imag) for c in state)
    counts = defaultdict(int)
    hashed = lambda state: hash(''.join(state[x+y*1j] for y in range(h+1) for x in range(w+1)))
    I = iter(enumerate((hashed(s), s) for s in day18(state)))
    for (p, (H, _)) in I: # after this loop, p is the first state to occur a 2nd time
        counts[H] += 1
        if counts[H] == 2:
            break
    for (q, (H, _)) in I: # after this loop, q is the first state to occur a 3rd time
        counts[H] += 1
        if counts[H] == 3:
            break
    print(p, q)
    x = (N - p) % (q - p) # x is how many iterations into the repetition we'll be at iteration N (BUG: N should be sufficiently big)
    for (_, (_, S)) in I: # iterate x times into the repeated pattern
        x -= 1
        if x == 0:
            return score(S)

def show(state):
    w, h = max(int(c.real) for c in state), max(int(c.imag) for c in state)
    counts = defaultdict(int)
    for y in range(h+1):
        print(''.join(state[x+y*1j] for x in range(w+1)))
    print(f"|: {sum(v=='|' for v in state.values())}")
    print(f"#: {sum(v=='#' for v in state.values())}")

def animate(state):
    try:
        w, h = max(int(c.real) for c in state), max(int(c.imag) for c in state)
        N = 0
        sys.stdout.buffer.write(b'\x1b[2J') # clear screen
        sys.stdout.buffer.write(b'\x1b[?25l') # hide cursor
        for state in day18(state):
            sys.stdout.buffer.write(b'\x1b[0;0f')
            for y in range(h+1):
                sys.stdout.buffer.write(b''.join(state[x+y*1j].encode('ascii') for x in range(w+1))+b'\n')
            sys.stdout.buffer.write(f"\n{N}\n".encode('ascii'))
            sys.stdout.buffer.write(f"|: {sum(v=='|' for v in state.values())}\n".encode('ascii'))
            sys.stdout.buffer.write(f"#: {sum(v=='#' for v in state.values())}\n".encode('ascii'))
            N += 1
            #time.sleep(0.1)
    finally:
        sys.stdout.buffer.write(b'\x1b[?25h') # show cursor

EX18 = '.#.#...|#.\n.....#|##|\n.|..|...#.\n..|#.....#\n#.#|||#|#|\n...#.||...\n.|....|...\n||...#|.#|\n|.||||..|.\n...#.|..|.'.split('\n')

def test_18_ex0(): assert day18a(parse(EX18),  0) == 27 * 17
def test_18_ex1(): assert day18a(parse(EX18),  1) == 40 * 12
def test_18_ex2(): assert day18a(parse(EX18), 10) == 37 * 31

def test_18a(day18_lines): assert day18a(parse(day18_lines),            10) == 1118 * 523 == 584714
def test_18b(day18_lines): assert day18b(parse(day18_lines), 1_000_000_000) == 161160

if __name__ == '__main__':
    with open('input/day18.txt', 'r') as f:
        animate(parse([line.strip() for line in f]))
