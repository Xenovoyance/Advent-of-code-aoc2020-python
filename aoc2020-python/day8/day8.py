input = 'aoc2020-python/day8/input.txt'
input_list = []
pointer = 0
ran_operations = []
bool_toggle = True
accumulator = 0

with open(input) as blockstream:
    for stream in blockstream: input_list.append(stream.strip())

while bool_toggle:
    op_parts = input_list[pointer].rstrip().split()

    if op_parts[0] == "nop":
        if ran_operations.count(pointer) == 0:
            ran_operations.append(pointer)
            pointer += 1
        else: bool_toggle = False
    elif op_parts[0] == "acc":
        if ran_operations.count(pointer) == 0:
            ran_operations.append(pointer)
            pointer += 1
            accumulator += int(op_parts[1])
        else: bool_toggle = False
    elif op_parts[0] == "jmp":
        if ran_operations.count(pointer) == 0:
            ran_operations.append(pointer)
            pointer += int(op_parts[1])
        else: bool_toggle = False
    else: bool_toggle = False

print("P1 Accumulator: " + str(accumulator)) #1654