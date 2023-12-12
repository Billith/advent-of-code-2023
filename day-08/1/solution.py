from itertools import cycle

def solve(input: str) -> int:
    lines = input.strip().splitlines()
    instructions = lines[0]
    nodes = {}

    for line in lines[2:]:
        name, choices = line.split(' = ')
        nodes[name] = tuple(choices[1:-1].split(', '))

    steps = 0
    current_node = 'AAA'

    for instruction in cycle(instructions):
        if current_node == 'ZZZ':
            break

        current_node = nodes[current_node][0] if instruction == 'L' else nodes[current_node][1]
        steps += 1

    return steps

def test() -> None:
    input = '''
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
'''
    result = solve(input)
    assert result == 6, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
