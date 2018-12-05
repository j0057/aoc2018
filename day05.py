from functools import reduce

def day05(polymer):
    return reduce(lambda a, b: a[1:] if a and a[0] != b and a[0].upper() == b[0].upper() else b+a, reversed(polymer))

def day05a(polymer):
    return len(day05(polymer))

def day05b(polymer):
    return min((len(day05(polymer.replace(r, '').replace(r.lower(), ''))) for r in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

def test_05_ex0(): assert day05('dabAcCaCBAcCcaDA') == 'dabCBAcaDA'
def test_05_ex1(): assert day05a('dabAcCaCBAcCcaDA') == 10
def test_05_ex2(): assert day05b('dabAcCaCBAcCcaDA') == 4

def test_05a(day05_text): assert day05a(day05_text) == 9808
def test_05b(day05_text): assert day05b(day05_text) == 6484
