from itertools import islice

class Tree:
    def __init__(self, g):
        #from pudb import set_trace ; set_trace()
        nch, ndt = islice(g, 2)
        self.ch = [Tree(g) for _ in range(nch)]
        self.dt = [*islice(g, ndt)]

    def __repr__(self):
        return f"({' '.join(repr(c) for c in self.ch)}{' ' if self.ch else ''}{' '.join(repr(d) for d in self.dt)})"

    def total(self):
        return sum(self.dt) + sum(ch.total() for ch in self.ch)

    def value(self):
        if not self.ch:
            return sum(self.dt)
        else:
            return sum(self.ch[i-1].value() if 0 < i <= len(self.ch) else 0 for i in self.dt)

def parse(text):
    return [int(x) for x in text.split()]

EX08 = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

def test_08_ex1(): assert repr(Tree(iter(EX08))) == '((10 11 12) ((99) 2) 1 1 2)'
def test_08_ex2(): assert Tree(iter(EX08)).total() == 138
def test_08_ex3(): assert Tree(iter(EX08)).value() == 66

def test_08a(day08_text): assert Tree(iter(parse(day08_text))).total() == 40848
def test_08b(day08_text): assert Tree(iter(parse(day08_text))).value() == 34466
