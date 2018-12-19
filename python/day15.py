from itertools import count
from dataclasses import dataclass
from math import inf as INF
from queue import Queue
import sys

import pytest

@dataclass
class Player:
    team: int
    health: int

def parse(lines):
    G = {x+y*1j: char if char in '#.' else '.'
         for (y, line) in enumerate(lines)
         for (x, char) in enumerate(line)}
    T = {x+y*1j: Player('EG'.index(char), 200)
         for (y, line) in enumerate(lines)
         for (x, char) in enumerate(line) if char in 'EG'}
    return (G, T)

def dijkstra(src, dst, grid, teams):
    #from pudb import set_trace; set_trace()
    open_set = {v for v in grid if grid[v] == '.'} ^ {*teams} | {src}
    distance = {v: INF for v in open_set}
    previous = {v: [] for v in open_set}
    distance[src] = 0
    while open_set:
        cur = min(open_set, key=lambda v: distance[v])
        open_set.remove(cur)
        for nxt in [cur+ofs for ofs in [-1j, -1, +1, +1j] if grid[cur+ofs] == '.' and (cur+ofs) not in teams]:
            if nxt not in open_set:
                continue
            if distance[cur]+1 < distance[nxt]:
                distance[nxt] = distance[cur]+1
                previous[nxt] = [cur]
            elif distance[cur]+1 == distance[nxt]:
                previous[nxt] += [cur]
    def reconstruct_path(previous, dst):
        result = [dst]
        while previous[dst]:
            dst = min(previous[dst], key=lambda c: (c.imag, c.real))
            result.insert(0, dst)
        return result
    return reconstruct_path(previous, dst)

def day15(grid, teams):
    w, h = max(int(c.real) for c in grid), max(int(c.imag) for c in grid)
    for rnd in count(0):
        yield rnd, grid, teams
        for (pos, player) in sorted(teams.items(), key=lambda t: (t[0].imag, t[0].real)):
            if player.health <= 0:
                print(f"{pos} {player} is already dead")
            adj = [pos+ofs for ofs in [-1j, -1, +1, +1j] if pos+ofs in teams and teams[pos+ofs].team == 1-player.team]
            if not adj:
                routes = [dijkstra(pos, dst, grid, teams)
                          for (pos2, player2) in teams.items() if player2.team == 1-player.team
                          for dst in [pos2-1j, pos2-1, pos2+1, pos2+1j]
                          if grid[dst] == '.' and dst not in teams]
                shortest = min((r for r in routes if r), default=None, key=len)
                if not shortest:
                    print(f"{pos} {player} waiting...")
                    continue
                step = shortest[1]
                print(f"{pos} {player} move from {pos} to {step}")
                grid[pos], grid[step] = grid[step], grid[pos]
                teams[step] = teams.pop(pos)
                pos = step
            adj = [pos+ofs for ofs in [-1j, -1, +1, +1j] if pos+ofs in teams and teams[pos+ofs].team == 1-player.team]
            if adj:
                atk = min(adj, default=None, key=lambda c: teams[c].health)
                print(f"{pos} {player} attacks {teams[atk]}")
                teams[atk].health -= 3
                if teams[atk].health <= 0:
                    print(f"{teams[atk]} has died!")
                    del teams[atk]
            if len({p.team for p in teams.values()}) != 2:
                print(f"only one team left, bailing out!! {teams}")
                return

def day15a(grid, teams):
    for rnd, grid, teams in day15(grid, teams):
        print(f"\nround {rnd}: {teams}")
        draw(grid, teams)
        print()
    h = sum(p.health for p in teams.values())
    return (rnd, h, rnd * h)

def draw(G, T):
    P = lambda s: sys.stdout.buffer.write(s.encode('ascii'))
    w, h = max(int(c.real) for c in G), max(int(c.imag) for c in G)
    for y in range(h+1):
        for x in range(w+1):
            if x+y*1j in T:
                P('EG'[T[x+y*1j].team])
            else:
                P(G[x+y*1j])
        P('  ')
        P(', '.join(f"{'EG'[T[c].team]}({T[c].health})" for c in sorted((c for c in T if c.imag == y), key=lambda c: c.real)))
        P('\n')

ex15a     = pytest.fixture(lambda: parse('#######|#E..G.#|#...#.#|#.G.#G#|#######'.split('|')))
ex15b     = pytest.fixture(lambda: parse('#######|#.G...#|#...EG#|#.#.#G#|#..G#E#|#.....#|#######'.split('|')))
ex15b_r24 = pytest.fixture(lambda: parse('#######|#..G..#|#...#.#|#.#####|#...#E#|#.....#|#######'.split('|')))
ex15c     = pytest.fixture(lambda: parse('#######|#G..#E#|#E#E.E#|#G.##.#|#...#E#|#...E.#|#######'.split('|')))
ex15d     = pytest.fixture(lambda: parse('#######|#E..EG#|#.#G.E#|#E.##E#|#G..#.#|#..E#.#|#######'.split('|')))
ex15e     = pytest.fixture(lambda: parse('#######|#E.G#.#|#.#G..#|#G.#.G#|#G..#.#|#...E.#|#######'.split('|')))
ex15f     = pytest.fixture(lambda: parse('#######|#.E...#|#.#..G#|#.###.#|#E#G#G#|#...#G#|#######'.split('|')))
ex15g     = pytest.fixture(lambda: parse('#########|#G......#|#.E.#...#|#..##..G#|#...##..#|#...#...#|#.G...G.#|#.....G.#|#########'.split('|')))


def test_15_ex_a1(ex15a): assert ex15a[1][2+3j].team == 1
def test_15_ex_a2(ex15a): assert dijkstra(1+1j, 3+1j, *ex15a) == [1+1j, 2+1j, 3+1j]

def test_15_ex_b(ex15b): assert day15a(*ex15b) == (47, 590, 27730)
#ef test_15_ex_c(ex15c): assert day15a(*ex15c) == (37, 982, 36334)
#ef test_15_ex_d(ex15d): assert day15a(*ex15d) == (46, 859, 39514)
#ef test_15_ex_e(ex15e): assert day15a(*ex15e) == (35, 793, 27755)
#ef test_15_ex_e(ex15f): assert day15a(*ex15f) == (54, 536, 28944)
#ef test_15_ex_e(ex15g): assert day15a(*ex15g) == (20, 937, 18740)

def test_15_ex_b_r24(ex15b_r24):
    # round 24: top G should move left not down ("the unit chooses the step which is first in reading order")
    draw(*ex15b_r24)
    assert dijkstra(3+1j, 5+5j, *ex15b_r24) == [3+1j, 2+1j, 1+1j, 1+2j, 1+3j, 1+4j, 2+4j, 3+4j, 3+5j, 4+5j, 5+5j]

#ef test_15a(day15_lines): assert day15a(*parse(day15_lines)) == -1
