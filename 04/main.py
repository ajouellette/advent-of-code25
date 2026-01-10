import sys
import numpy as np


def parse_input(filename: str) -> list[list[int]]:
    rows = []
    with open(filename) as f:
        for line in f.readlines():
            rows.append(list(map(lambda x: 1 if x == '@' else 0, line.strip())))
    return rows


def get_accessible_inds(rows):
    # assumes input is zero padded
    # so that we don't need to care about boundary conditions
    mask = np.zeros(rows.shape, dtype=bool)
    for row_i, row in enumerate(rows):
        if row_i == 0 or row_i == len(rows)-1:
            continue
        for col_i, x in enumerate(row):
            if not x:
                continue
            if col_i == 0 or col_i == len(row)-1:
                continue
            total_adjacent = rows[row_i-1,col_i-1] + rows[row_i,col_i-1] + rows[row_i+1,col_i-1] + \
                             rows[row_i-1,col_i] + rows[row_i+1,col_i] + \
                             rows[row_i-1,col_i+1] + rows[row_i,col_i+1] + rows[row_i+1,col_i+1]
            if total_adjacent < 4:
                mask[row_i,col_i] = True
    return mask



def main():
    rows = parse_input(sys.argv[1])

    # zero-pad input
    rows = np.pad(rows, 1, mode="constant", constant_values=0)

    accessible = get_accessible_inds(rows)
    print(np.sum(accessible))

    # part 2
    total_removed = 0
    while True:
        accessible = get_accessible_inds(rows)
        total = np.sum(accessible)
        if total == 0:
            break
        total_removed += total
        rows[accessible] = 0
    print(total_removed)


if __name__ == "__main__":
    main()
