def solve(input: str) -> int:
    result = 0

    for line in input.splitlines():
        game_id, result_sets = line.split(':')
        if not contains_impossible_results(result_sets):
            result += int(game_id[5:])

    return result

def contains_impossible_results(result_sets: str) -> bool:
    for result_set in result_sets.split(';'):
        for r in result_set.split(','):
            number, color = r.strip().split(' ')
            
            if ((color == 'red' and int(number) > 12) or (color == 'green' and int(number) > 13) or (color == 'blue' and int(number) > 14)):
                return True
    
    return False

def test():
    input = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    assert solve(input) == 8

# test()
print(solve(open('input.txt').read()))
