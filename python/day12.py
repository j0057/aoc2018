#!/usr/bin/env python3

from collections import defaultdict
from itertools import islice

from day10 import iterate

nth = lambda g, i: next(islice(g, i, i+1))

def parse(lines):
    state = defaultdict(int, {i: 1 for (i, ch) in enumerate(lines[0][15:]) if ch == '#'})
    rules = {tuple(1 if ch == '#' else 0 for ch in line[0:5]) for line in lines[2:-1] if line[-1] == '#'}
    return (state, rules)

def day12(state, rules):
    return iterate(state, lambda s: defaultdict(int,
        {i: 1 for i in range(min(s)-2, max(s)+3) if (s[i-2], s[i-1], s[i], s[i+1], s[i+2]) in rules}))

def day12a(state, rules):
    return sum(nth(day12(state, rules), 20))

def day12b(state, rules):
    return sum(k+50000000000-1000 for k in nth(day12(state, rules), 1000))

EX12 = 'initial state: #..#.#..##......###...###\n\n...## => #\n..... => .\n..#.. => #\n.#... => #\n.#.#. => #\n.#.## => #\n.##.. => #\n.#### => #\n#.#.# => #\n#.### => #\n##.#. => #\n##.## => #\n###.. => #\n###.# => #\n####. => #\n'.split('\n')

def test_12_ex0(): assert parse(EX12)[0][0] == 1

def test_12_ex1(): assert ((0, 0, 0, 1, 1) in parse(EX12)[1]) == True
def test_12_ex2(): assert ((0, 0, 0, 0, 0) in parse(EX12)[1]) == False

def test_12_ex3(): assert day12a(*parse(EX12)) == 325

def test_12a(day12_lines): assert day12a(*parse(day12_lines)) == 3258
def test_12b(day12_lines): assert day12b(*parse(day12_lines)) == 3600000002022

if __name__ == '__main__':
    with open('input/day12.txt', 'r') as f:
        for i, state in enumerate(day12(*parse([line.strip() for line in f]))):
            print(i, sum(state), min(state), '.'*(20+min(state))+''.join('#' if state[i] else '.' for i in range(min(state)-2, max(state)+3)))
