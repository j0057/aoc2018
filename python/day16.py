import re

def op_addr(r, a, b, c): r[c] = r[a] + r[b]
def op_mulr(r, a, b, c): r[c] = r[a] * r[b]
def op_banr(r, a, b, c): r[c] = r[a] & r[b]
def op_borr(r, a, b, c): r[c] = r[a] | r[b]
def op_setr(r, a, b, c): r[c] = r[a]

def op_addi(r, a, b, c): r[c] = r[a] + b
def op_muli(r, a, b, c): r[c] = r[a] * b
def op_bani(r, a, b, c): r[c] = r[a] & b
def op_bori(r, a, b, c): r[c] = r[a] | b
def op_seti(r, a, b, c): r[c] =   a

def op_gtir(r, a, b, c): r[c] =   a  > r[b] and 1 or 0
def op_gtri(r, a, b, c): r[c] = r[a] >   b  and 1 or 0
def op_gtrr(r, a, b, c): r[c] = r[a] > r[b] and 1 or 0

def op_eqir(r, a, b, c): r[c] =   a  == r[b] and 1 or 0
def op_eqri(r, a, b, c): r[c] = r[a] ==   b  and 1 or 0
def op_eqrr(r, a, b, c): r[c] = r[a] == r[b] and 1 or 0

OPS = [op_banr, op_muli, op_bori, op_borr, op_addi, op_mulr, op_addr,]

def parse(lines):
    nums = lambda s: [int(x) for x in re.findall(r'-?\d+', s)]
    split = next(i for i in range(len(lines)-2) if lines[i:i+3] == ['', '', ''])+1
    captures = [(nums(lines[i]), nums(lines[i+1]), nums(lines[i+2]))
                for i in range(0, split, 4)]
    program = [nums(lines[i]) for i in range(split+2, len(lines))]
    return (captures, program)

def possible_ops(before, ins, after):
    ops = [fn for (name, fn) in globals().items() if name.startswith('op_')]
    run = lambda op: (lambda before: op(before, *ins[1:]) or before)(before[:])
    return {op.__name__[3:] for op in ops if run(op) == after}

def get_evidence(captures):
    possible = {i: set() for i in range(16)}
    for (before, ins, after) in captures:
        possible[ins[0]] |= possible_ops(before, ins, after)
    return possible

def deduce_opcodes(possible):
    opcodes = {}
    while any(len(c) == 1 for c in possible.values()):
        opcode = min(possible.keys(), key=lambda k: len(possible[k]))
        opname = possible[opcode].pop()
        opcodes[opcode] = opname
        del possible[opcode]
        for c in possible.values():
            if opname in c:
                c ^= {opname}
    return opcodes

def run_program(code, ip, reg, ops):
    while 0 <= ip < len(code):
        ops[code[ip][0]](reg, *code[ip][1:])
        ip += 1 # that's it?
    return reg

def day16a(captures, _):
    return sum(len(possible_ops(before, instr, after)) >= 3
               for (before, instr, after) in captures)

def day16b(captures, code):
    possible = get_evidence(captures)
    opcodes = deduce_opcodes(possible)
    print(opcodes)
    ops = {i: globals()[f"op_{name}"] for (i, name) in opcodes.items()}
    reg = run_program(code, 0, [0]*4, ops)
    return reg[0]

EX16 = 'Before: [3, 2, 1, 1]|9 2 1 2|After: [3, 2, 2, 1]|||'.split('|')

def test_16_ex1(): assert parse(EX16) == ([([3, 2, 1, 1], [9, 2, 1, 2], [3, 2, 2, 1])], [])

def test_16_ex2(): assert day16a(*parse(EX16)) == 1

def test_16a(day16_lines): assert day16a(*parse(day16_lines)) == 493
def test_16b(day16_lines): assert day16b(*parse(day16_lines)) == 445
