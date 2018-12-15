def day14(cont):
    L, a, b, v = [3, 7], 0, 1, 10
    while cont(L, v):
        v = L[a] + L[b]
        L += [v] if v < 10 else [1, v % 10]
        a = (a + 1 + L[a]) % len(L)
        b = (b + 1 + L[b]) % len(L)
    return L

def day14a(n, c=10):
    L = day14(lambda L, _: len(L) < n+c)
    return ''.join(str(x) for x in L[n:n+c])

def day14b(n):
    D = [int(x) for x in str(n)]
    L = day14(lambda L, v: L[-len(D):] != D and L[-len(D)-1:-1] != D)
    return len(L)-len(D)

def test_14_ex1(): assert day14a(9) == '5158916779'
def test_14_ex2(): assert day14a(5) == '0124515891'
def test_14_ex3(): assert day14a(18) == '9251071085'
def test_14_ex4(): assert day14a(2018) == '5941429882'

def test_14_ex5(): assert day14b('51589') == 9
def test_14_ex6(): assert day14b('01245') == 5
def test_14_ex7(): assert day14b('92510') == 18
def test_14_ex8(): assert day14b('59414') == 2018

def test_14a(day14_number): assert day14a(day14_number) == '1150511382'
def test_14b(day14_number): assert day14b(day14_number) == 20173656+1
