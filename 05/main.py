import sys


def parse_input(filename):
    ranges = []
    ids = []
    with open(filename) as f:
        for line in f.readlines():
            if '-' in line:
                ranges.append(list(map(int, line.strip().split('-'))))
            elif len(line.strip()) > 0:
                ids.append(int(line))
    return ranges, ids


def in_range(x, a, b):
    return x >= a and x <= b


def check_id(id, ranges):
    for id_range in ranges:
        if in_range(id, *id_range):
            return True
    return False


def get_nonoverlapping_ranges(ranges):
    # sort by first element of range
    ranges = sorted(ranges, key=lambda x: x[0])
    unique_ranges = [ranges.pop(0),]
    while len(ranges) > 0:
        test_range = ranges.pop(0)
        if test_range[0] <= unique_ranges[-1][1]:
            unique_ranges[-1] = [unique_ranges[-1][0], max(unique_ranges[-1][1], test_range[1])]
        else:
            unique_ranges.append(test_range)
    return unique_ranges


def main():
    ranges, ids = parse_input(sys.argv[1])
    unique_ranges = get_nonoverlapping_ranges(ranges)

    total = 0
    for id_ in ids:
        if check_id(id_, unique_ranges):
            total += 1
    print(total)

    # part 2
    total = 0
    for a, b in unique_ranges:
        total += b - a + 1
    #print(ranges)
    #print(unique_ranges)
    print(total)


if __name__ == "__main__":
    main()
