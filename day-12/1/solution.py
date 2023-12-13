from itertools import combinations


def solve(puzzle: str) -> int:
    lines = puzzle.strip().splitlines()
    all_possible_arrangements = 0

    for line in lines:
        data, damaged_groups = line.split()
        damaged_groups = [int(x) for x in damaged_groups.split(',')]
        data = list(data)
        damaged_springs_number = data.count('#')
        missing_damaged_springs_number = sum(damaged_groups) - damaged_springs_number
        unknown_indices = [i for i, c in enumerate(data) if c == '?']
        damaged_springs_combinations = list(combinations(unknown_indices, missing_damaged_springs_number))

        for possible_damaged_springs in damaged_springs_combinations:
            data_copy = [f for f in data]
            
            for i in possible_damaged_springs:
                data_copy[i] = '#'

            for i in range(len(data_copy)):
                if data_copy[i] == '?':
                    data_copy[i] = '.'
            
            data_copy = ''.join(data_copy)
            possible_damaged_springs_groups_lengths = [len(x) for x in data_copy.split('.') if x]

            if len(possible_damaged_springs_groups_lengths) == len(damaged_groups):
                if all([x == y for x, y in zip(possible_damaged_springs_groups_lengths, damaged_groups)]):
                    all_possible_arrangements += 1

    return all_possible_arrangements

def test() -> None:
    input = '''
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
    result = solve(input)
    assert result == 21, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
