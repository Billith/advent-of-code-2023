from functools import reduce


def solve(input: str) -> int:
    lines = input.strip().splitlines()
    races = zip([int(n) for n in lines[0].split(':')[1].split()], [int(n) for n in lines[1].split(':')[1].split()])
    race_wins = []

    for race_time, distance_record in races:
        print(f'race: {race_time, distance_record}')
        wins = 0

        for held_time in range(1, race_time):
            distance_traveled = (race_time - held_time) * held_time
            print(f'held: {held_time}, traveled: {distance_traveled}')
            
            if distance_traveled > distance_record:
                wins += 1

        race_wins.append(wins)
    
    return reduce(lambda x, y: x*y, race_wins)

def test() -> None:
    input = '''
Time:      7  15   30
Distance:  9  40  200
'''
    result = solve(input)
    assert result == 288, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
