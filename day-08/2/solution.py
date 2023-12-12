from itertools import cycle
from math import lcm

def solve(input: str) -> int:
    lines = input.strip().splitlines()
    instructions = lines[0]
    nodes = {}
    current_nodes = []

    for line in lines[2:]:
        name, choices = line.split(' = ')
        nodes[name] = tuple(choices[1:-1].split(', '))
        
        if name.endswith('A'):
            current_nodes.append(name)

    all_steps = []

    for node in current_nodes:
        current_node = node
        steps = 0

        for instruction in cycle(instructions):
            if current_node.endswith('Z'):
                break

            current_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]
            steps += 1
        
        all_steps.append(steps)
    
    return lcm(*all_steps)

def test() -> None:
    input = '''
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
    result = solve(input)
    assert result == 6, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
