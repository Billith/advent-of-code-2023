def solve(input: str) -> int:
    parts = [line.strip() for line in input.strip().split('\n\n')]
    seed_ranges = [int(seed) for seed in parts[0].split(': ')[1].split()]
    it = iter(seed_ranges)
    seed_ranges = [[seed, seed_range] for seed, seed_range in zip(it, it)]
    maps = [m.splitlines()[1:] for m in parts[1:]]

    for m in maps:
        srs = [r for r in seed_ranges]
        mapped_seed_ranges = []

        while srs:
            seed_range_start, seed_length = srs.pop()
            seed_range_end = seed_range_start + seed_length
            # print(f'seed {seed_range_start}, {seed_length}')

            for line in m:
                dest, range_start, range_length = [int(n) for n in line.split()]
                range_end = range_start + range_length
                
                if range_start <= seed_range_start < range_end:
                    if seed_range_end <= range_end:
                        mapped_seed_ranges.append([dest + (seed_range_start - range_start), seed_length])
                        # print(f'#1 append {[dest + (seed_range_start - range_start), seed_length]}')
                    else:
                        mapped_seed_ranges.append([dest + (seed_range_start - range_start), range_end - seed_range_start])
                        # print(f'#2 append {[dest + (seed_range_start - range_start), range_end - seed_range_start]}')
                        srs.append([seed_range_start + (range_end - seed_range_start), seed_range_end - range_end])
                    break
                elif range_start < seed_range_end <= range_end:
                    mapped_seed_ranges.append([dest, seed_range_end - range_start])
                    # print(f'#3 append {[dest + (range_start - seed_range_start), seed_range_end - range_start]}')
                    srs.append([seed_range_start, range_start - seed_range_start])
                    break
            else:
                mapped_seed_ranges.append([seed_range_start, seed_length])
                # print(f'#4 append {[seed_range_start, seed_length]}')

        seed_ranges = mapped_seed_ranges

    print()
    return min([s for s, _ in seed_ranges])

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
    assert result == 46, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
