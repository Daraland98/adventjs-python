'''The elf programmers are creating a small magical assembler to control the machines in Santa Claus's workshop.

To assist them, we will implement a simple interpreter that supports the following magical instructions:

· MOV x y: Copies the value x (which can be a number or the content of a register) into register y
· INC x: Increments the content of register x by 1
· DEC x: Decrements the content of register x by 1
· JMP x y: If the value in register x is 0, then jumps to the instruction at index y and continues executing the program from there.

Expected behavior:

· If an attempt is made to access, increment, or decrement a register that has not been initialized, the default value 0 will be used.
· The jump with JMP is absolute and goes to the exact index indicated by y.
· Upon completion, the program should return the content of register A. If A did not have a defined value, it returns undefined.'''

def compile(instructions):
    registers = {}
    def get_value(x):
        return int(x) if x.lstrip('-').isdigit() else registers.get(x, 0)
    idx = 0
    while idx < len(instructions):
        parts = instructions[idx].split()
        cmd = parts[0]
        if cmd == "MOV":
            x, y = parts[1], parts[2]
            registers[y] = get_value(x) 
        elif cmd == "INC":
            x = parts[1]
            registers[x] = get_value(x) + 1  
        elif cmd == "DEC":
            x = parts[1]
            registers[x] = get_value(x) - 1  
        elif cmd == "JMP":
            x, y = parts[1], int(parts[2])
            if get_value(x) == 0:  # Si el registro x es 0, salta al índice indicado
                idx = y
                continue 
        idx += 1
    return registers.get("A", "undefined")

instructions = [
  'MOV -1 C',  ## copies -1 to register 'C',
  'INC C', ##  increments the value of register 'C'
  'JMP C 1', ##  jumps to the instruction at index 1 if 'C' is 0
  'MOV C A', ##  copies register 'C' to register 'A',
  'INC A' ##  increments the value of register 'A'
]

print(compile(instructions))