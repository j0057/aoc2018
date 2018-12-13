#!/usr/bin/env python3

import sys
import time

from day13 import parse, day13, EX13A, EX13B

def animate(grid, carts, cleanup=0):
    try:
        w = max(int(c.real) for c in grid)
        h = max(int(c.imag) for c in grid)
        sys.stdout.buffer.write(b'\x1b[2J') # clear screen
        sys.stdout.buffer.write(b'\x1b[?25l') # hide cursor
        for grid, carts, crashes in day13(grid, carts, cleanup):
            sys.stdout.buffer.write(b'\x1b[0;0f')
            for y in range(76):
                for ofs in [0, 75]:
                    for x in range(w+1):
                        p = x + y * 1j + ofs * 1j
                        if p in carts:
                            sys.stdout.buffer.write(b'\x1b[1;33m')
                            sys.stdout.buffer.write({+1j:'v', -1j:'^', -1:'<', +1:'>'}[carts[p][0]].encode('ascii'))
                            sys.stdout.buffer.write(b'\x1b[0m')
                        elif p in crashes:
                            sys.stdout.buffer.write(b'\x1b[1;31mX\x1b[0m')
                        else:
                            sys.stdout.buffer.write(grid[p].encode('ascii'))
                    sys.stdout.buffer.write(b'   ')
                sys.stdout.buffer.write(b'\n')
            time.sleep(0.5)
    finally:
        sys.stdout.buffer.write(b'\x1b[?25h') # show cursor

if __name__ == '__main__':
    #animate(*parse(EX13A))
    animate(*parse(EX13B), cleanup=1)

    #with open('input/day13.txt') as f:
    #    animate(*parse(f.read()))
