from typing import List


def predict_value(history: List[int]) -> int:
    sequences = [history]

    while any([val != 0 for val in sequences[-1]]):
        new_sequence = []

        for i, val in enumerate(sequences[-1][:-1]):
            new_sequence.append(sequences[-1][i + 1] - val)
        
        sequences.append(new_sequence)

    predicted_val = 0

    for sequence in sequences[::-1]:
        predicted_val = sequence[0] - predicted_val

    return predicted_val

def solve(input: str) -> int:
    histories = [[int (val) for val in line.split()] for line in input.strip().splitlines()]
    return sum([predict_value(history) for history in histories])

def test() -> None:
    input = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
'''
    result = solve(input)
    assert result == 2, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
