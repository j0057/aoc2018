from collections import Counter
from itertools import groupby
import re

def parse(lines):
    for line in sorted(lines):
        (ts, msg) = re.match(r'\[(.*)\] (.*)', line).groups()
        if msg.startswith('Guard'):
            guard = int(msg.split()[1][1:])
        elif msg == 'falls asleep':
            start = int(ts[-2:])
        elif msg == 'wakes up':
            stop = int(ts[-2:])
            yield (guard, start, stop)

def day04(times):
    return {k: [m for (_, start, stop) in g
                  for m in range(start, stop)]
            for (k, g) in groupby(sorted(times), lambda t: t[0])}

def day04a(times):
    guard, minutes = max(day04(times).items(), key=lambda t: len(t[1]))
    return guard * Counter(minutes).most_common(1)[0][0]

def day04b(times):
    times = {k: Counter(M).most_common(1)[0] for (k, M) in day04(times).items()}
    guard = max(times, key=lambda k: times[k][1])
    return guard * times[guard][0]

EX04 = lambda: ((10,5,25), (10,30,55), (99,40,50), (10,24,29), (99,36,46), (99,45,55))

def test_04_ex1(): assert day04a(EX04()) == 240
def test_04_ex2(): assert day04b(EX04()) == 4455

def test_04a(day04_lines): assert day04a(parse(day04_lines)) == 19025
def test_04b(day04_lines): assert day04b(parse(day04_lines)) == 23776
