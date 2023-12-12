from itertools import combinations


def solve(puzzle: str, extrapolation_val: int) -> int:
    image = [list(line) for line in puzzle.strip().splitlines()]
    extrapolated_rows = []
    extrapolated_cols = []

    for i in reversed(range(len(image))):
        if all([c == '.' for c in image[i]]):
            extrapolated_rows.append(i)
    
    for i in reversed(range(len(image[0]))):
        if all([image[j][i] == '.' for j in range(len(image))]):
            extrapolated_cols.append(i)

    galaxies = []

    for i, line in enumerate(image):
        for j, char in enumerate(line):
            if char == '#':
                galaxies.append((i, j))
    
    all_galaxies_pairs = list(combinations(galaxies, 2))
    paths_lengths = []
    # since passing through each extrapolated row and column is now worth 1m field
    # we need to subtract 1 each time, since in the calculation of path length those
    # fields are already counted in the path length as 1
    extrapolation_val -= 1

    for first_galaxy, second_galaxy in all_galaxies_pairs:
        path_length = abs(first_galaxy[0] - second_galaxy[0]) + abs(first_galaxy[1] - second_galaxy[1])

        if first_galaxy[0] > second_galaxy[0]:
            path_length += extrapolation_val * len([r for r in extrapolated_rows if second_galaxy[0] < r < first_galaxy[0]])
        else:
            path_length += extrapolation_val * len([r for r in extrapolated_rows if first_galaxy[0] < r < second_galaxy[0]])

        if first_galaxy[1] > second_galaxy[1]:
            path_length += extrapolation_val * len([c for c in extrapolated_cols if second_galaxy[1] < c < first_galaxy[1]])
        else:
            path_length += extrapolation_val * len([c for c in extrapolated_cols if first_galaxy[1] < c < second_galaxy[1]])

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
    result = solve(input, 100)
    assert result == 8410, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read(), 1000000))
