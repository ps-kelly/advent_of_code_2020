#!/usr/bin/env python
from typing import List

def part_one(data: List[int]) -> int:
    """Find product of two numbers in the list that equal 2020

    Args:
        data (List[int]): list of integers to search

    Returns:
        int: product of the two numbers
    """
    for d1 in data:
        for d2 in data:
            if d1 != d2 and d1 + d2 == 2020:
                return d1 * d2
    raise ValueError("Apparently a bad list")

def part_two(data: List[int]) -> int:
    """Find product of three numbers in the list that equal 2020

    Args:
        data (List[int]): list of integers to search

    Returns:
        int: product of the three numbers
    """
    for d1 in data:
        for d2 in data:
            for d3 in data:
                if d1 != d2 and d2 != d3 and d1 + d2 + d3 == 2020:
                    return d1 * d2 * d3
    raise ValueError("Apparently unsolvable with this list")



def read_data(file_name: str) -> List[int]:
    """Read an input file that has ints in each row.

    Args:
        file_name (str): file name or path to read

    Returns:
        List[int]: list of integers read from file
    """
    data = []
    with open(file_name, "r") as in_f:
        for row in in_f:
            data.append(int(row))
    return data

def main() -> None:
    data = read_data("input.txt")
    print("Part 1:", part_one(data))
    print("Part 2:", part_two(data))

if __name__ == "__main__":
    main()
