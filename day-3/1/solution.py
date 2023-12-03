def solve(input: str) -> int:
    lines = [line.strip() for line in input.strip().splitlines()]
    solution = 0

    for line_index in range(len(lines)):
        char_index = 0

        while char_index < len(lines[line_index]) - 1:
            if not lines[line_index][char_index].isdigit():
                char_index += 1
                continue

            number = ''
            is_part_number = False

            while lines[line_index][char_index].isdigit():
                # check left side of a number
                if char_index > 0:
                    if not (lines[line_index][char_index - 1].isdigit() or lines[line_index][char_index - 1] == '.'):
                        is_part_number = True
                
                # check right side of a number
                if char_index < len(lines[line_index]) - 1:
                    if not (lines[line_index][char_index + 1].isdigit() or lines[line_index][char_index + 1] == '.'):
                        is_part_number = True

                # check line above number
                if line_index > 0:
                    # check left diagonal
                    if char_index > 0:
                        if not (lines[line_index - 1][char_index - 1].isdigit() or lines[line_index - 1][char_index - 1] == '.'):
                            is_part_number = True
                    
                    # check right diagonal
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index - 1][char_index + 1].isdigit() or lines[line_index - 1][char_index + 1] == '.'):
                            is_part_number = True
                    
                    # check character above
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index - 1][char_index].isdigit() or lines[line_index - 1][char_index] == '.'):
                            is_part_number = True

                # check line below number
                if line_index < len(lines) - 1:
                    # check left diagonal
                    if char_index > 0:
                        if not (lines[line_index + 1][char_index - 1].isdigit() or lines[line_index + 1][char_index - 1] == '.'):
                            is_part_number = True
                    
                    # check right diagonal
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index + 1][char_index + 1].isdigit() or lines[line_index + 1][char_index + 1] == '.'):
                            is_part_number = True
                    
                    # check character below
                    if char_index < len(lines[line_index]) - 1:
                        if not (lines[line_index + 1][char_index].isdigit() or lines[line_index + 1][char_index] == '.'):
                            is_part_number = True

                number += lines[line_index][char_index]
                
                if char_index < len(lines[line_index]) - 1:
                    char_index += 1
                else:
                    break

            if number and is_part_number:
                solution += int(number)

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
    assert result == 4361

# test()
print(solve(open('input.txt').read()))
