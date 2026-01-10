import sys


def is_invalid_id1(num: int) -> bool:
    s = str(num)
    if len(s) % 2 != 0:
        return False
    return s[:len(s)//2] == s[len(s)//2:]


def is_invalid_id2(num: int) -> bool:
    s = str(num)
    for sub_len in range(1, len(s)//2+1):
        if len(s) % sub_len == 0:
            sub_strs = [s[i:i+sub_len] for i in range(0, len(s), sub_len)]
            if len(set(sub_strs)) == 1:
                return True
    return False


def main():
    input_file = sys.argv[1]
    ranges = []
    with open(input_file) as f:
        for line in f.readlines():
            for x in line.split(','):
                ranges.append(list(map(int, x.split('-'))))

    invalid_ids1 = []
    invalid_ids2 = []
    for id_range in ranges:
        for num in range(id_range[0], id_range[1]+1):
            if is_invalid_id1(num):
                invalid_ids1.append(num)
            if is_invalid_id2(num):
                invalid_ids2.append(num)

    print(invalid_ids1)
    print(sum(invalid_ids1))

    print(invalid_ids2)
    print(sum(invalid_ids2))


if __name__ == "__main__":
    main()
