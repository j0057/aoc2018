import re
from collections import defaultdict

def parse(claims):
    return [tuple(int(n) for n in re.findall(r'\d+', claim)) for claim in claims]

def day03(claims):
    claimed = defaultdict(list)
    for (nr, left, top, width, height) in claims:
        for x in range(left, left + width):
            for y in range(top, top + height):
                claimed[(x, y)] += [nr]
    return claimed

def day03a(claims):
    return sum(len(v) > 1 for v in day03(claims).values())

def day03b(claims):
    all_claims = {*range(1, claims[-1][0]+1)}
    for claim in day03(claims).values():
        if len(claim) > 1:
            all_claims -= {*claim}
    return all_claims

def test_03_parse(): assert parse(['#123 @ 3,2: 5x4']) == [(123, 3, 2, 5, 4)]

def test_03_ex1(): assert day03a(parse(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])) == 4
def test_03_ex2(): assert day03b(parse(['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2'])) == {3}

def test_03a(day03_lines): assert day03a(parse(day03_lines)) == 118840
def test_03b(day03_lines): assert day03b(parse(day03_lines)) == {919}
