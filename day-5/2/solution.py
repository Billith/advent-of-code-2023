def solve(input: str) -> int:
    parts = [line.strip() for line in input.strip().split('\n\n')]
    seeds_ranges = [int(seed) for seed in parts[0].split(': ')[1].split()]
    it = iter(seeds_ranges)
    maps = parts[1:]
    min_location = None

    for seed, rg in zip(it, it):
        for x in range(rg):
            current_val = seed + x
            # print(f'current_val: {current_val}')

            for i, m in enumerate(maps):
                for line in m.splitlines():
                    if ' map:' in line:
                        continue

                    dest, source, r = [int(n) for n in line.split()]
                    
                    if current_val >= source and current_val < (source + r):
                        current_val = dest + current_val - source
                        break
                
                # print(f'-- finished processing map #{i} --')

            if min_location == None or current_val < min_location:
                min_location = current_val

    return min_location

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
    assert result == 46

# test()
print(solve(open('input.txt').read()))
