from typing import Tuple
from functools import cache


# part 2 taken from 0xdf, I couldn't figure it out
# https://gitlab.com/0xdf/aoc2023/-/blob/main/day12/day12.py?ref_type=heads

@cache
def get_combinations(data: str, damaged_groups_lengths: Tuple[int]) -> int:
    possible_arrangements = 0

    if len(data) == 0:
        if len(damaged_groups_lengths) == 0:
            return 1
        return 0

    if len(damaged_groups_lengths) == 0:
        if '#' in data:
            return 0
        return 1
    
    if len(data) < sum(damaged_groups_lengths) + len(damaged_groups_lengths) - 1:
        return 0

    if data[0] in '.?':
        possible_arrangements += get_combinations(data[1:], damaged_groups_lengths)

    n = damaged_groups_lengths[0]

    if (
        data[0] in '#?'
        and '.' not in data[:n]
        and (len(data) == n or data[n] in '.?')
    ):
        possible_arrangements += get_combinations(data[n+1:], damaged_groups_lengths[1:])

    return possible_arrangements

def solve(puzzle: str) -> int:
    lines = puzzle.strip().splitlines()
    all_possible_arrangements = 0

    for line in lines:
        data, damaged_groups_lengths = line.split()
        data = '?'.join([data] * 5)
        damaged_groups_lengths = tuple(int(x) for x in damaged_groups_lengths.split(',')) * 5
        all_possible_arrangements += get_combinations(data, damaged_groups_lengths)

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
    assert result == 525152, f'[!] test failed, unexpected result -> {result}'
    print(f'[+] test passed, result -> {result}')

test()
print(solve(open('input.txt').read()))
