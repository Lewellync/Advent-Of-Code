import os, sys
import re

circuits = {}

def answer_one(input):
    for line in re.split(r'\n', input):
        instruction, wire = line.split(' -> ')
        circuits[wire] = instruction       
    return solve('a')
    
def solve(value) -> int:
    if value.isdigit():
        return int(value)
    if re.match(r'^\d+$', str(circuits[value])):
        return int(circuits[value])
    inputs = circuits[value].split()
    if len(inputs) == 3:
        lhs, op, rhs = inputs
        match op:
            case 'AND':
                circuits[value] = solve(lhs) & solve(rhs)
            case 'OR':
                circuits[value] = solve(lhs) | solve(rhs)
            case 'RSHIFT':
                circuits[value] = solve(lhs) >> solve(rhs)
            case 'LSHIFT':
                circuits[value] = solve(lhs) << solve(rhs)
    if len(inputs) == 2:
        op, lhs = inputs
        circuits[value] = ~solve(lhs)
    if len(inputs) == 1:
        lhs = inputs[0]
        circuits[value] = solve(lhs)
    return int(circuits[value])
    
        
def answer_two(input):
    p1 = answer_one(input)
    for line in re.split(r'\n', input):
        instruction, wire = line.split(' -> ')
        circuits[wire] = instruction
    circuits['b'] = p1
    return solve('a')
    
if __name__ == "__main__":
    input_path = os.path.join(sys.argv[0].removesuffix("answer.py"), "input.txt")
    with open(input_path, 'r') as file:
        input = file.read()
        print(answer_one(input))
        print(answer_two(input))