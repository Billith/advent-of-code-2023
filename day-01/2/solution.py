digits_words = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def solve(input: str) -> list[int]:
    solution = []

    for line in input.splitlines():
        line_digits = []
        index = 0

        while index < len(line):
            if line[index].isdigit():
                line_digits.append(line[index])
                index += 1
                continue

            for digit_word in digits_words.keys():
                if line[index:].startswith(digit_word):
                    line_digits.append(digits_words[digit_word])
                    index += 1
                    break
            else:
                index += 1

        assert len(line_digits) > 0
        solution.append(int(f'{line_digits[0]}{line_digits[-1]}'))

    return solution

def test():
    input = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen'''
    solution = solve(input)
    assert sum(solution) == 281

# test()
with open('input.txt') as input:
    print(sum(solve(input.read())))
