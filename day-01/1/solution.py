def solve(input: str) -> list[int]:
    solution = []

    for line in input.splitlines():
        line_digits = [char for char in line if char.isdigit()]
        solution.append(int(f'{line_digits[0]}{line_digits[-1]}'))

    return solution

def test():
    input = '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet'''
    solution = solve(input)
    calibration_values = [12, 38, 15, 77]
    assert solution == calibration_values

with open('input.txt') as input:
    print(sum(solve(input.read())))
