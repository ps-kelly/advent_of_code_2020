#!/usr/bin/env python
"""Day 7"""

from dataclasses import dataclass
import json
import re
from typing import Mapping, Optional

BAG_PATTERN = re.compile(r"^([\w\s]+)(?=\sbags contain)(\sbags\scontain\s)(.+)(?=\.)")
BAG_COUNT = re.compile(r"^(\d+)\s([\w\s]+)")
Bags = Mapping[str, Optional[Mapping[str, int]]]

def parse_bags(text: str) -> Bags:
    """Parse bag descriptions
    
    Args:
        text (str): text to parse

    Returns:
        dict: dictionary of bags, and their child bags and counts of children
    """
    bags = dict()
    for row in text.split("\n"):
        match = re.match(BAG_PATTERN, row)
        if match:
            child_bags: Optional[Mapping[str, int]] = dict()
            for bag in match[3].split(", "):
                parsed_bag = re.fullmatch(BAG_COUNT, bag)
                if parsed_bag and child_bags is not None:
                    child_bags[parsed_bag[2].split("bag")[0][:-1]] = int(parsed_bag[1])
                else:
                    child_bags = None
            bags[match[1]] = child_bags
    return bags


def bag_walker_one(data: dict, start_key: str) -> int:
    count = 0
    if data[start_key] is not None:
        for v in data[start_key]:
            if v == "shiny gold":
                count += 1
            elif v is not None:
                count += bag_walker_one(data, v)
    return count

def part_two(data: dict, key: str) -> int:
    print(key)
    count = 1
    if data[key] is not None:
        for k, v in data[key].items():
            count += v * part_two(data, k)
    return count


def part_one(bags: Bags) -> int:
    count = 0
    for k in bags:
        count += 1 if bag_walker_one(bags, k) > 0 else 0
    return count


def main() -> None:
    """Runs this"""
    text = str()
    with open("input.txt", "r") as in_f:
        text = in_f.read()[:-1]
    bags = parse_bags(text)
    print(part_one(bags))
    print(part_two(bags, "shiny gold") -1)



if __name__ == "__main__":
    main()

