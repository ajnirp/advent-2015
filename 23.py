inp = '''jio a, +19
inc a
tpl a
inc a
tpl a
inc a
tpl a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +23
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7'''

prog = inp.split('\n')

a, b, idx = 0, 0, 0

seen = set()

def run_vm(a, b, idx):
    while 0 <= idx < len(prog):
        inst = prog[idx]
        if inst.startswith('inc'):
            var = inst[-1]
            if var == 'a':
                a += 1
            elif var == 'b':
                b += 1
            idx += 1
        elif inst.startswith('tpl'):
            var = inst[-1]
            if var == 'a':
                a *= 3
            elif var == 'b':
                b *= 3
            idx += 1
        elif inst.startswith('hlf'):
            var = inst[-1]
            if var == 'a':
                a >>= 1
            elif var == 'b':
                b >>= 1
            idx += 1
        elif inst.startswith('jmp'):
            idx += int(inst.split()[1])
        elif inst.startswith('jie'):
            var = inst[4]
            offset = int(inst.split(',')[1][1:])
            if var == 'a':
                if a % 2 == 0:
                    idx += offset
                else:
                    idx += 1
            elif var == 'b':
                if b % 2 == 0:
                    idx += offset
                else:
                    idx += 1
        elif inst.startswith('jio'):
            var = inst[4]
            offset = int(inst.split(',')[1][1:])
            if var == 'a':
                if a == 1:
                    idx += offset
                else:
                    idx += 1
            elif var == 'b':
                if b == 1:
                    idx += offset
                else:
                    idx += 1
    return a, b, idx

print run_vm(0, 0, 0)[1], run_vm(1, 0, 0)[1] # 184 231