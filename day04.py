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
    times = day04(times)
    guard = max(times, key=lambda k: len(times[k]))
    return guard * Counter(times[guard]).most_common(1)[0][0]

def day04b(times):
    times = {k: Counter(M).most_common(1)[0] for (k, M) in day04(times).items()}
    guard = max(times, key=lambda k: times[k][1])
    return guard * times[guard][0]

EX04 = '''
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
'''.strip().split('\n')

def test_04_ex1(): assert day04a(parse(EX04)) == 240
def test_04_ex2(): assert day04b(parse(EX04)) == 4455

def test_04a(day04_lines): assert day04a(parse(day04_lines)) == 19025
def test_04b(day04_lines): assert day04b(parse(day04_lines)) == 23776
