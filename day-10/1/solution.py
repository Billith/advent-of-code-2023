from enum import Enum
from math import ceil
from typing import Tuple


class SquareType(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

def make_move(position: Tuple[int], move: chr, came_from: SquareType) -> Tuple[Tuple[int], SquareType]:
    match move:
        case "|":
            if came_from == SquareType.BOTTOM:
                return (position[0]-1, position[1]), SquareType.BOTTOM
            else:
                return (position[0]+1, position[1]), SquareType.TOP
        case "-":
            if came_from == SquareType.LEFT:
                return (position[0], position[1]+1), SquareType.LEFT
            else:
                return (position[0], position[1]-1), SquareType.RIGHT
        case "L":
            if came_from == SquareType.TOP:
                return (position[0], position[1]+1), SquareType.LEFT
            else:
                return (position[0]-1, position[1]), SquareType.BOTTOM
        case "J":
            if came_from == SquareType.TOP:
                return (position[0], position[1]-1), SquareType.RIGHT
            else:
                return (position[0]-1, position[1]), SquareType.BOTTOM
        case "7":
            if came_from == SquareType.BOTTOM:
                return (position[0], position[1]-1), SquareType.RIGHT
            else:
                return (position[0]+1, position[1]), SquareType.TOP
        case "F":
            if came_from == SquareType.BOTTOM:
                return (position[0], position[1]+1), SquareType.LEFT
            else:
                return (position[0]+1, position[1]), SquareType.TOP
        case _:
            assert False, f"something went wrong while making the move"

def solve(puzzle: str) -> int:
    diagram = [[*line] for line in puzzle.strip().splitlines()]
    
    for i, line in enumerate(diagram):
        if 'S' in line:
            current_position = (i, line.index('S'))
    
    steps = 0
    # print(f'S -> {current_position}')
    # print(f'first move from {current_position} -> {diagram[current_position[0]][current_position[1]]}', end='')

    if current_position[0] > 0 and diagram[current_position[0] - 1][current_position[1]] in ['|', '7', 'F']:
        current_position = (current_position[0] - 1, current_position[1])
        came_from = SquareType.BOTTOM
    elif current_position[0] < (len(diagram) - 1) and diagram[current_position[0] + 1][current_position[1]] in ['|', 'L', 'J']:
        current_position = (current_position[0] + 1, current_position[1])
        came_from = SquareType.TOP
    elif current_position[0] > 0 and diagram[current_position[0]][current_position[1] - 1] in ['-', 'L', 'F']:
        current_position = (current_position[0], current_position[1] - 1)
        came_from = SquareType.RIGHT
    elif current_position[0] < (len(diagram[current_position[0]]) - 1) and diagram[current_position[0]][current_position[1] + 1] in ['-', 'J', '7']:
        current_position = (current_position[0], current_position[1] + 1)
        came_from = SquareType.LEFT
    else:
        assert False, f'something went wrong, no move to make from {current_position} -> {diagram[current_position[0]][current_position[1]]}'
    
    steps += 1
    # print(f' to {current_position} -> {diagram[current_position[0]][current_position[1]]}')
    
    while diagram[current_position[0]][current_position[1]] != 'S':
        # print(f'moved from {current_position} -> {diagram[current_position[0]][current_position[1]]}', end='')
        # current_position, came_from = make_move(current_position, diagram[current_position[0]][current_position[1]], came_from)
        current_position, came_from = make_move(current_position, diagram[current_position[0]][current_position[1]], came_from)
        steps += 1
        # print(f' to {current_position} -> {diagram[current_position[0]][current_position[1]]}')
        # input()

    return ceil(steps / 2)

def test() -> None:
    input = '''
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
'''
    result = solve(input)
    assert result == 8, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
