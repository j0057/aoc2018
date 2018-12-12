from collections import Counter

def day02a(ids):
    counts = [Counter(id) for id in ids]
    return sum(2 in c.values() for c in counts) * sum(3 in c.values() for c in counts)

def day02b(ids):
    return max((''.join(a for a,b in zip(id_a, id_b) if a==b)
               for id_a in ids
               for id_b in ids
               if id_a != id_b), key=len)

def test_02_ex1(): assert day02a('abcdef bababc abbcde abcccd aabcdd abcdee ababab'.split()) == 12
def test_02_ex2(): assert day02b('abcde fghij klmno pqrst fguij axcye wvxyz'.split()) == 'fgij'

def test_02a(day02_lines): assert day02a(day02_lines) == 8892
def test_02b(day02_lines): assert day02b(day02_lines) == 'zihwtxagifpbsnwleydukjmqv'
