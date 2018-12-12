from collections import defaultdict, deque
import re

def parse(text):
    return [*map(int, re.findall(r'-?\d+', text))]

def day09a(players, marbles):
    S = defaultdict(int)
    C = deque([0])
    for m in range(1, marbles+1):
        if m % 23 == 0:
            C.rotate(7)
            S[m % players] += m + C.pop()
            C.rotate(-1)
        else:
            C.rotate(-1)
            C.append(m)
    return max(S.values(), default=0)

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
