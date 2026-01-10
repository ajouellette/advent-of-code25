import sys
import numpy as np


def parse_input(filename: str) -> list[str]:
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def largest_joltage(bank: list[str], n_digits: int = 2) -> int:
    digits = []
    start_ind = 0
    for i in range(n_digits):
        remaining_digits = n_digits - i - 1
        digit = str(max(map(int, bank[start_ind:len(bank)-remaining_digits])))
        digits.append(digit)
        start_ind = bank.index(digit, start_ind) + 1
    return int(''.join(digits))


def main():
    banks = parse_input(sys.argv[1])

    total = 0
    total_part2 = 0
    for bank in banks:
        total += largest_joltage(bank)
        total_part2 += largest_joltage(bank, n_digits=12)
    print(total)
    print(total_part2)


if __name__ == "__main__":
    main()
