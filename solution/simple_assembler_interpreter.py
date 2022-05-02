"""
Simple assembler interpreter
https://www.codewars.com/kata/58e24788e24ddee28e000053
"""
"""
This is the first part of this kata series. Second part is here. https://www.codewars.com/kata/assembler-interpreter-part-ii/

We want to create a simple interpreter of assembler which will support the following instructions:

    mov x y - copies y (either a constant value or the content of a register) into register x
    inc x - increases the content of the register x by one
    dec x - decreases the content of the register x by one
    jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero

Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary (a table in COBOL) with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.
Example

simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])

''' visualized:
mov a 5
inc a
dec a
dec a
jnz a -1
inc a
''''

The above code will:

    set register a to 5,
    increase its value by 1,
    decrease its value by 2,
    then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
    and then increase its value by 1, leaving register a at 1

So, the function should return

{'a': 1}

This kata is based on the Advent of Code 2016 - day 12 https://adventofcode.com/2016/day/12
"""


def simple_assembler(commands):

    commands = [  # pre-parse program code
        [el if el.isalpha() else int(el) for el in cmd.split()]  # split each command to operation and arguments. if element contains no letters - convert to int
        for cmd in commands]  # iterate commands

    regs = {}  # dictionary to store registers
    ptr = 0

    def eval_operand(op):  # if it's int - return it. otherwise, return value of a corresponding register
        return op if isinstance(op, int) else regs[op]

    while ptr < len(commands):  # main loop
        cmd = commands[ptr][0]  # first element is command to execute
        args = commands[ptr][1:]  # all the rest are arguments

        if cmd == 'mov':  # mov x y - copies y (either a constant value or the content of a register) into register x
            regs[args[0]] = eval_operand(args[1])

        elif cmd == 'inc':  # increases the content of the register x by one
            regs[args[0]] += 1

        elif cmd == 'dec':  # dec x - decreases the content of the register x by one
            regs[args[0]] -= 1

        elif cmd == 'jnz':  # jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
            if eval_operand(args[0]):  # if x is not 0
                ptr += eval_operand(args[1]) - 1  # then jump y commands away (-1 to compensate increment of pointer at each step)

        ptr += 1  # proceed to the next command
    return regs