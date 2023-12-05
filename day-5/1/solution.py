def solve(input: str) -> int:
    parts = [line.strip() for line in input.strip().split('\n\n')]
    seeds = [[int(seed)] for seed in parts[0].split(': ')[1].split()]
    maps = parts[1:]

    for i, m in enumerate(maps):
        for line in m.splitlines():
            if ' map:' in line:
                continue

            dest, source, r = [int(n) for n in line.split()]
            
            for x, seed in enumerate(seeds):
                print(f'checking seed "{seed[-1]}" for line "{line}" - seeds {seeds}')

                if len(seed) >= i+2:
                    continue

                if seed[-1] >= source and seed[-1] < (source + r):
                    seed.append(dest + seed[-1] - source)
                    print(f'append #1 ({x}) seed {seed}: {dest + seed[-1] - source}')
        
        for seed in seeds:
            if len(seed) < i+2:
                seed.append(seed[-1])
                print(f'append #2 seed {seed}: {seed[-1]}')

        print(seeds)
        print(f'-- finished processing map #{i} --')

    return min([s[-1] for s in seeds])

def test():
    input = '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''
    result = solve(input)
    print(result)
    assert result == 35

# test()
print(solve(open('input.txt').read()))
