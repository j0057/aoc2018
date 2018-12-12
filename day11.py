def power_level(n, x, y):
    return ((x+10)*y + n) * (x+10) // 100 % 10 - 5

def square_power(n, x, y, sz):
    return sum(power_level(n, x+dx, y+dy)
               for dx in range(sz)
               for dy in range(sz))

def summed_area(n, sz):
    S = [[power_level(n, x, y) for x in range(sz)] for y in range(sz)]
    for y in range(0, sz):
        for x in range(0, sz):
            S[y][x] += S[y-1][x] if y else 0
            S[y][x] += S[y][x-1] if x else 0
            S[y][x] -= S[y-1][x-1] if x and y else 0
    def get(x, y, n):
        return S[y+n-1][x+n-1] \
             - (S[y-1][x+n-1] if y else 0) \
             - (S[y+n-1][x-1] if x else 0) \
             + (S[y-1][x-1] if x and y else 0)
    return get

def day11a(n):
    sums = summed_area(n, 300)
    return max(((x, y) for x in range(0, 300-3)
                       for y in range(0, 300-3)),
               key=lambda c: sums(*c, 3))

def day11b(n):
    sums = summed_area(n, 300)
    return max(((x, y, sz) for sz in range(1, 300)
                           for y in range(0, 300-sz)
                           for x in range(0, 300-sz)),
               key=lambda c: sums(*c))

def test_11_ex0(): assert power_level(8, 3, 5) == 4
def test_11_ex1(): assert power_level(57, 122, 79) == -5
def test_11_ex2(): assert power_level(39, 217, 196) == 0
def test_11_ex3(): assert power_level(71, 101, 153) == 4

def test_11_ex4(): assert day11a(18) == (33, 45)
def test_11_ex5(): assert day11a(42) == (21, 61)

def test_11_ex6(): assert day11b(18) == (90, 269, 16)
def test_11_ex7(): assert day11b(42) == (232, 251, 12)

def test_11a(day11_number): assert day11a(day11_number) == (34, 72)
def test_11b(day11_number): assert day11b(day11_number) == (233, 187, 13)
