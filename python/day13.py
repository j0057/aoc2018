from collections import defaultdict

def parse(text):
    grid = {x+y*1j: '|' if char in '|^v' else '-' if char in '-<>' else char
            for (y, line) in enumerate(text.split('\n'))
            for (x, char) in enumerate(line)
            if char != ' '}

    cart = {x+y*1j: ({'v': +1j, '^': -1j, '<': -1, '>': +1}[char], -1j)
            for (y, line) in enumerate(text.split('\n'))
            for (x, char) in enumerate(line)
            if char in 'v^<>'}

    return (defaultdict(lambda: ' ', grid), cart)

def day13(grid, carts, cleanup=0):
    crashes = set()
    yield (grid, carts.copy(), crashes.copy())
    while carts:
        if cleanup:
            crashes.clear()
        for (pos, (vec, turn)) in sorted(carts.items(), key=lambda c: (c[0].imag, c[0].real)):
            if not carts.pop(pos, None):
                continue
            pos += vec
            if pos in carts or pos in crashes:
                carts.pop(pos, None)
                crashes.add(pos)
                continue
            elif grid[pos] == '/':  carts[pos] = (vec * (-1j if vec.real else +1j), turn)
            elif grid[pos] == '\\': carts[pos] = (vec * (-1j if vec.imag else +1j), turn)
            elif grid[pos] == '+':  carts[pos] = (vec * turn, {-1j: 1, 1: +1j, +1j: -1j}[turn])
            else:                   carts[pos] = (vec, turn)
        yield (grid, carts.copy(), crashes.copy())

def day13a(grid, carts):
    return next(crashes for (grid, carts, crashes) in day13(grid, carts) if crashes)

def day13b(grid, carts):
    return next(carts for (grid, carts, crashes) in day13(grid, carts, cleanup=1) if len(carts) == 1)

EX13A = r'''
/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   '''[1:]

EX13B = r'''
/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/'''[1:]

def test_13_ex1(): assert day13a(*parse(EX13A)) == {7+3j}
def test_13_ex2(): assert day13b(*parse(EX13B)) == {6+4j: (-1j, -1j)}

def test_13a(day13_raw): assert day13a(*parse(day13_raw)) == {91+69j}
def test_13b(day13_raw): assert day13b(*parse(day13_raw)) == {44+87j: (1+0j, -1j)}
