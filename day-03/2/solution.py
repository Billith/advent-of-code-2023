import itertools


def solve(input: str) -> int:
    lines = [line.strip() for line in input.strip().splitlines()]
    gears = {}

    for line_index in range(len(lines)):
        char_index = 0

        while char_index < len(lines[line_index]) - 1:
            if not lines[line_index][char_index].isdigit():
                char_index += 1
                continue

            number = ''
            is_part_number = False
            is_gear_adjacent = False
            adjacent_gears = []

            while lines[line_index][char_index].isdigit():
                # check left side of a number
                if char_index > 0:
                    if not (lines[line_index][char_index - 1].isdigit() or lines[line_index][char_index - 1] == '.'):
                        is_part_number = True

                    if lines[line_index][char_index - 1] == '*':
                        adjacent_gears.append(tuple([line_index, char_index - 1]))
                
                # check right side of a number
                if char_index < len(lines[line_index]) - 1:
                    if not (lines[line_index][char_index + 1].isdigit() or lines[line_index][char_index + 1] == '.'):
                        is_part_number = True

                    if lines[line_index][char_index + 1] == '*':
                        adjacent_gears.append(tuple([line_index, char_index + 1]))

                # check line above number
                if line_index > 0:
                    # check left diagonal
                    if char_index > 0:
                        if not (lines[line_index - 1][char_index - 1].isdigit() or lines[line_index - 1][char_index - 1] == '.'):
                            is_part_number = True

                        if lines[line_index - 1][char_index - 1] == '*':
                            adjacent_gears.append(tuple([line_index - 1, char_index - 1]))
                    
                    # check right diagonal
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index - 1][char_index + 1].isdigit() or lines[line_index - 1][char_index + 1] == '.'):
                            is_part_number = True
                        
                        if lines[line_index - 1][char_index + 1] == '*':
                            adjacent_gears.append(tuple([line_index - 1, char_index + 1]))
                    
                    # check character above
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index - 1][char_index].isdigit() or lines[line_index - 1][char_index] == '.'):
                            is_part_number = True
                        
                        if lines[line_index - 1][char_index] == '*':
                            adjacent_gears.append(tuple([line_index - 1, char_index]))

                # check line below number
                if line_index < len(lines) - 1:
                    # check left diagonal
                    if char_index > 0:
                        if not (lines[line_index + 1][char_index - 1].isdigit() or lines[line_index + 1][char_index - 1] == '.'):
                            is_part_number = True
                        
                        if lines[line_index + 1][char_index - 1] == '*':
                            adjacent_gears.append(tuple([line_index + 1, char_index - 1]))
                    
                    # check right diagonal
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index + 1][char_index + 1].isdigit() or lines[line_index + 1][char_index + 1] == '.'):
                            is_part_number = True

                        if lines[line_index + 1][char_index + 1] == '*':
                            adjacent_gears.append(tuple([line_index + 1, char_index + 1]))
                    
                    # check character below
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index + 1][char_index].isdigit() or lines[line_index + 1][char_index] == '.'):
                            is_part_number = True
                        
                        if lines[line_index + 1][char_index] == '*':
                            adjacent_gears.append(tuple([line_index + 1, char_index]))

                number += lines[line_index][char_index]
                
                if char_index < len(lines[line_index]) - 1:
                    char_index += 1
                else:
                    break
            
            # not required since we are using set below
            # adjacent_gears = list(k for k, _ in itertools.groupby(adjacent_gears))

            for adjacent_gear in adjacent_gears:
                if adjacent_gear in gears.keys():
                    gears[adjacent_gear].add(number)
                else:
                    gears[adjacent_gear] = set([number])

    solution = 0

    for gear in gears:
        if len(gears[gear]) == 2:
            first, second = [int(e) for e in gears[gear]]
            solution += first * second

    return solution

def test():
    input = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''
    result = solve(input)
    print(f'Result: {result}')
    assert result == 467835

# test()
print(solve(open('input.txt').read()))
