def solve(input: str) -> int:
    lines = input.strip().splitlines()
    race_time = int(''.join(lines[0].split(':')[1].split()))
    distance_record = int(''.join(lines[1].split(':')[1].split()))
    wins = 0
    
    for held_time in range(1, race_time):
        distance_traveled = (race_time - held_time) * held_time
        
        if distance_traveled > distance_record:
            wins += 1

    return wins

def test() -> None:
    input = '''
Time:      7  15   30
Distance:  9  40  200
'''
    result = solve(input)
    assert result == 71503, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
