from itertools import combinations


def solve(puzzle: str) -> int:
    image = [list(line) for line in puzzle.strip().splitlines()]

    for i in reversed(range(len(image))):
        if all([c == '.' for c in image[i]]):
            image.insert(i + 1, list('.' * len(image[i])))
    
    for i in reversed(range(len(image[0]))):
        if all([image[j][i] == '.' for j in range(len(image))]):
            for line in image:
                line.insert(i + 1, '.')

    galaxies = []

    for i, line in enumerate(image):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i, j))
    
    all_galaxies_pairs = list(combinations(galaxies, 2))
    paths_lengths = []

    for first_galaxy, second_galaxy in all_galaxies_pairs:
        path_length = abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1])
        # print(f'{first_galaxy} -> {second_galaxy} = {path_length}')
        paths_lengths.append(path_length)

    return sum(paths_lengths)

def test() -> None:
    input = '''
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
    result = solve(input)
    assert result == 374, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
