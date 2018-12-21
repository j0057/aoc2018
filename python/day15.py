from itertools import count
from dataclasses import dataclass
from math import inf as INF
import sys

import pytest

@dataclass
class Player:
    health: int = 200
    attack: int = 3

class Elf(Player):
    disp: str = 'E'

class Goblin(Player):
    disp: str = 'G'

def parse(lines, elf_attack=3):
    return {x+y*1j: {'E': lambda s: Elf(attack=elf_attack),
                     'G': lambda s: Goblin()}.get(char, str)(char)
            for (y, line) in enumerate(lines)
            for (x, char) in enumerate(line)}

def distances(src, open_set):
    distance = {src: 0}
    while open_set:
        cur = min(open_set, key=lambda v: distance.get(v, INF))
        open_set.remove(cur)
        if cur not in distance:
            continue
        for nxt in [cur+ofs for ofs in [-1j, -1, +1, +1j] if (cur+ofs) in open_set]:
            if distance[cur]+1 < distance.get(nxt, INF):
                distance[nxt] = distance[cur]+1
    return distance

def day15(grid):
    for rnd in count(0):
        yield rnd, grid
        for (pos, player) in sorted((t for t in grid.items() if isinstance(t[1], Player)),
                                    key=lambda t: (t[0].imag, t[0].real)):
            Enemy = {Elf: Goblin, Goblin: Elf}[type(player)]
            if player.health <= 0:
                print(f"{pos} {player} is already dead")
                continue
            if {type(p) for p in grid.values()} != {Elf, Goblin, str}:
                print(f"only one team left, bailing out!!")
                return
            adj = [pos+o for o in [-1j, -1, +1, +1j] if isinstance(grid[pos+o], Enemy)]
            if not adj:
                dist = distances(pos, {c for c in grid if grid[c] == '.'} | {pos})
                target = min((c+o for c in grid if isinstance(grid[c], Enemy)
                                  for o in [-1j, -1, +1, +1j] if grid[c+o] == '.'),
                                  key=lambda c: (dist.get(c, INF), c.imag, c.real),
                                  default=None)
                if dist.get(target, INF) == INF:
                    print(f"{pos} {player} waiting...")
                    continue
                dist = distances(target, {c for c in grid if grid[c] == '.'} | {target})
                step = min((pos+o for o in [-1j, -1, 1, 1j] if grid[pos+o] == '.'),
                           key=lambda c: dist.get(c, INF))
                print(f"{pos} {player} move from {pos} to {step}")
                grid[pos], grid[step] = grid[step], grid[pos]
                pos = step
            adj = [pos+o for o in [-1j, -1, +1, +1j] if isinstance(grid[pos+o], Enemy)]
            if adj:
                atk = min(adj, default=None, key=lambda c: grid[c].health)
                print(f"{pos} {player} attacks {grid[atk]}")
                grid[atk].health -= player.attack
                if grid[atk].health <= 0:
                    print(f"{grid[atk]} has died!")
                    grid[atk] = '.'

def day15a(grid):
    for rnd, grid in day15(grid):
        print(f"\nAfter {rnd} round{'s' if rnd != 1 else ''}:")
        draw(grid)
        print()
    h = sum(v.health for v in grid.values() if isinstance(v, Player))
    return (rnd, h, rnd * h)

def day15b(lines):
    for elf_attack in count(4):
        grid = parse(lines, elf_attack)
        elfs = [v for v in grid.values() if isinstance(v, Elf)]
        for rnd, grid in day15(grid):
            if any(e.health <= 0 for e in elfs):
                break
        else:
            if any(e.health <= 0 for e in elfs):
                continue
            health = sum(v.health for v in grid.values() if isinstance(v, Player))
            return (elf_attack, rnd, health, rnd * health)

def draw(G):
    P = lambda s: sys.stdout.write(s)
    w, h = max(int(c.real) for c in G), max(int(c.imag) for c in G)
    for y in range(h+1):
        for x in range(w+1):
            P(G[x+y*1j].disp if isinstance(G[x+y*1j], Player) else G[x+y*1j])
        P('  ')
        P(', '.join(f"{G[c].disp}({G[c].health})" for c in sorted(
            (c for c in G if isinstance(G[c], Player) and c.imag == y),
            key=lambda c: c.real)))
        P('\n')

EX15A = '#######|#E..G.#|#...#.#|#.G.#G#|#######'.split('|')
EX15B = '#######|#.G...#|#...EG#|#.#.#G#|#..G#E#|#.....#|#######'.split('|')
EX15C = '#######|#G..#E#|#E#E.E#|#G.##.#|#...#E#|#...E.#|#######'.split('|')
EX15D = '#######|#E..EG#|#.#G.E#|#E.##E#|#G..#.#|#..E#.#|#######'.split('|')
EX15E = '#######|#E.G#.#|#.#G..#|#G.#.G#|#G..#.#|#...E.#|#######'.split('|')
EX15F = '#######|#.E...#|#.#..G#|#.###.#|#E#G#G#|#...#G#|#######'.split('|')
EX15G = '#########|#G......#|#.E.#...#|#..##..G#|#...##..#|#...#...#|#.G...G.#|#.....G.#|#########'.split('|')

def test_15a_ex0(): assert isinstance(parse(EX15A)[2+3j], Goblin)

def test_15a_ex1(): assert day15a(parse(EX15B)) == (47, 590, 27730)
def test_15a_ex2(): assert day15a(parse(EX15C)) == (37, 982, 36334)
def test_15a_ex3(): assert day15a(parse(EX15D)) == (46, 859, 39514)
def test_15a_ex4(): assert day15a(parse(EX15E)) == (35, 793, 27755)
def test_15a_ex5(): assert day15a(parse(EX15F)) == (54, 536, 28944)
def test_15a_ex6(): assert day15a(parse(EX15G)) == (20, 937, 18740)

def test_15b_ex1(): assert day15b(EX15B) == (15, 29, 172, 4988)
def test_15b_ex2(): assert day15b(EX15D) == (4, 33, 948, 31284)
def test_15b_ex3(): assert day15b(EX15E) == (15, 37, 94, 3478)
def test_15b_ex5(): assert day15b(EX15F) == (12, 39, 166, 6474)
def test_15b_ex6(): assert day15b(EX15G) == (34, 30, 38, 1140)

def test_15a(day15_lines): assert day15a(parse(day15_lines)) == (82, 2624, 215168)

def test_15a(day15_lines): assert day15b(day15_lines) == (16, 42, 1247, 52374)
