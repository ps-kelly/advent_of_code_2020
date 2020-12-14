#!/usr/bin/env python
"""Day 3 code"""


def part_one(group_text: str) -> int:
    """Count of unique yeses
    
    Args:
        group_text (str): groups text data

    Returns:
        int: count of unique yeses
    """
    out_l = []
    for c in group_text.replace("\n", ""):
        out_l.append(ord(c))
    return len(set(out_l))


def part_two(total_text: str) -> int:
    """Count of "all" yeses

    Args:
        group_text (str): group text data

    Returns:
        int: count of total yeses
    """
    out_l = []
    for group_text in total_text.split("\n\n"):
        set_list = []
        for row in group_text.split("\n"):
            if row == "":
                continue
            set_list.append(set(row))
        print(group_text, set_list)
        out_l.append(len(set.intersection(*set_list)))
    return sum(out_l)


def main() -> None:
    """Run this"""
    count_pt_1 = 0
    with open("input.txt", "r") as in_f:
        total_text = in_f.read()
    print(sum([part_one(group_text) for group_text in total_text.split("\n\n")]))
    print(part_two(total_text))


if __name__ == "__main__":
    main()
