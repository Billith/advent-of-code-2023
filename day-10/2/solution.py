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
    loop = [current_position]

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
    loop.append(current_position)

    while diagram[current_position[0]][current_position[1]] != 'S':
        current_position, came_from = make_move(current_position, diagram[current_position[0]][current_position[1]], came_from)
        loop.append(current_position)
        steps += 1

    cleaned_diagram = []

    for i, line in enumerate(diagram):
        new_line = []
        for j, char in enumerate(line):
            if (i, j) in loop:
                new_line.append(char)
            else:
                new_line.append('.')
        cleaned_diagram.append(new_line)

    # shamelessly taken from 0xdf (https://gitlab.com/0xdf/aoc2023/-/blob/main/day10/day10.py?ref_type=heads)
    # no idea how does this work
    # https://en.wikipedia.org/wiki/Point_in_polygon

    part2 = 0
    for line in cleaned_diagram:
        outside = True
        startF = None
        for ch in line:
            match ch:
                case ".":
                    if not outside:
                        part2 += 1
                case "|":
                    outside = not outside
                case "F":
                    startF = True
                case "L":
                    startF = False
                case "-":
                    assert not startF is None
                case "7":
                    assert not startF is None
                    if not startF:
                        outside = not outside
                    startF = None
                case "J":
                    assert not startF is None
                    if startF:
                        outside = not outside
                    startF = None

    return part2

def test() -> None:
    input = '''
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''
    result = solve(input)
    assert result == 10, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
