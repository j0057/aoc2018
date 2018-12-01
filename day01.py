from itertools import cycle

def day01a(changes):
    return sum(changes)

def day01b(changes):
    seen, freq = {0}, 0
    for change in cycle(changes):
        freq += change
        if freq in seen:
            return freq
        seen.add(freq)

def test_01a_ex1(): assert day01a([+1, +1, +1]) == 3
def test_01a_ex2(): assert day01a([+1, +1, -2]) == 0
def test_01a_ex3(): assert day01a([-1, -2, -3]) == -6

def test_01b_ex1(): assert day01b([-1, +1]) == 0
def test_01b_ex2(): assert day01b([+3, +3, +4, -2, -4]) == 10
def test_01b_ex3(): assert day01b([-6, +3, +8, +5, -6]) == 5
def test_01b_ex3(): assert day01b([+7, +7, -2, -7, -4]) == 14

def test_01a(day01_numbers): assert day01a(day01_numbers) == 508
def test_01b(day01_numbers): assert day01b(day01_numbers) == 549
