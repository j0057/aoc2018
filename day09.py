import re
from functools import reduce

def parse(text):
    return [*map(int, re.findall(r'-?\d+', text))]

def day09a(players, marbles):
    S = [0]*players
    P, N = [0], [0]
    p, i = 0, 0
    for m in range(1, marbles+1):
        if m % 23 == 0:
            i = reduce(lambda a, _: P[a], range(6), i)
            N.append(-1)
            P.append(-1)
            S[p] += m + i
            N[P[i]], P[N[i]] = N[i], P[i]
        else:
            i = reduce(lambda a, _: N[a], range(2), i)
            N.append(N[i])
            P.append(i)
            N[P[m]], P[N[m]] = m, m
        p = (p+1) % len(S)
    return max(S)

def day09b(players, marbles):
    return day09a(players, marbles*100)

def test_09_ex0(): assert day09a(9, 25) == 32
def test_09_ex1(): assert day09a(10, 1618) == 8317
def test_09_ex2(): assert day09a(13, 7999) == 146373
def test_09_ex3(): assert day09a(17, 1104) == 2764
def test_09_ex4(): assert day09a(21, 6111) == 54718
def test_09_ex5(): assert day09a(30, 5807) == 37305

def test_09a(day09_text): assert day09a(*parse(day09_text)) == 418237
def test_09b(day09_text): assert day09b(*parse(day09_text)) == 3505711612
