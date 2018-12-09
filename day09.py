import re
from blist import blist

def parse(text):
    return [*map(int, re.findall(r'-?\d+', text))]

def day09(players, marbles):
    S, C = [0]*players, blist([0])
    p, i = 0, 1
    for m in range(1, marbles+1):
        if m % 23 == 0:
            i = (i-7) % len(C)
            S[p] += m + C.pop(i)
        else:
            i = (i+2) % len(C)
            C.insert(i, m)
        p = (p+1) % len(S)
    return max(S)

def day09b(players, marbles):
    return day09(players, marbles*100)

def test_09_ex0(): assert day09(9, 25) == 32
def test_09_ex5(): assert day09(30, 5807) == 37305

def test_09a(day09_text): assert day09(*parse(day09_text)) == 418237
def test_09b(day09_text): assert day09b(*parse(day09_text)) == 3505711612
