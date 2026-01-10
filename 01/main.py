import sys
import numpy as np


def brute_force(start, rots, count_all=True):
    count = 0
    pos = start
    for rot in rots:
        for step in range(1, abs(rot)+1):
            pos = (pos + np.sign(rot)) % 100
            if count_all:
                if pos == 0:
                    count += 1
        if not count_all:
            if pos == 0:
                count += 1
    return count


def main():
    start = 50

    input_file = sys.argv[1]
    with open(input_file) as f:
        rots = f.readlines()

    def parse_rot(s):
        sign = s[0]
        num = int(s[1:])
        if sign == "L":
            return -num
        return num

    rots = np.array([parse_rot(rot) for rot in rots])

    # part one
    # count number of times dial ends at zero
    raw_positions = np.cumsum(np.hstack([[start,], rots]))
    dial_positions = raw_positions % 100
    end_at_zero = dial_positions == 0
    print(np.sum(end_at_zero))
    print(brute_force(start, rots, count_all=False))
    print()

    # part two
    # count number of times dial passes zero
    print(brute_force(start, rots))


if __name__ == "__main__":
    main()
