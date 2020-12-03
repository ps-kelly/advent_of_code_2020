#!/usr/bin/env python
"""Advent of code day 3 code."""

from dataclasses import dataclass, field, InitVar
from typing import Tuple, Optional

import numpy as np


def parse_row(row: str) -> bool:
    out_r = []
    for c in row:
        if c == "#":
            out_r.append(True)
        elif c == ".":
            out_r.append(False)
    return out_r

@dataclass
class Slope:

    file_name: InitVar[str]
    slope_data: np.array = field(init=False)

    def __post_init__(self, file_name: str) -> None:
        temp_l = []
        with open(file_name, "r") as in_f:
            for row in in_f:
                temp_l.append(parse_row(row))
        self.slope_data = np.array(temp_l)

    def slide(self, right: int, down: int, start_x: int=0, start_y: int=0) -> int:
        """Recursive method for sliding down the slope.

        Args:
            right (int): how many squares right to slide
            down (int): how many square down to slide
            start_coord (Tuple[int, int], optional]: starting coordinates

        Returns:
            int: number of trees hit
        """
        target_right = start_x + right
        target_down = start_y + down
        if target_down >= self.slope_data.shape[0]:
            return 0
        tree_found = self.slope_data[target_down][target_right % self.slope_data.shape[1]]
        print(f"slide called with: right: {right} down: {down}, start_x: {start_x}, start_y: {start_y}, hit {tree_found}")
        return self.slide(right, down, target_right, target_down) + self.slope_data[target_down][target_right % self.slope_data.shape[1]]


def main() -> None:
    """Main function"""
    slope = Slope("input.txt")
    print("Part 1:", slope.slide(3, 1))
    print("Part 2:", slope.slide(1,1) * slope.slide(3,1) * slope.slide(5,1) * slope.slide(7,1) * slope.slide(1,2))

if __name__ == "__main__":
    main()
