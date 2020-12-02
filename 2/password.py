#!/usr/bin/env python

import re
from dataclasses import dataclass


@dataclass
class PasswordValidator:

    min_count: int
    max_count: int
    target_char: str
    password: str

    @staticmethod
    def from_string(text: str) -> "PasswordValidator":
        """Generate this from a string
        
        Args:
            text (str): text to parse

        Returns:
            PasswordValidator: a password validator
        """
        first_split = text.split(" ")
        ranges = first_split[0].split("-")
        return PasswordValidator(
            min_count=int(ranges[0]),
            max_count=int(ranges[1]),
            target_char=first_split[1][0],  # always 1 char
            password=first_split[2],
        )

    def validate_part_one(self) -> bool:
        """Validate a password.

        Returns:
            bool: True for valid, False for invalid
        """
        count = 0
        for c in self.password:
            if c == self.target_char:
                count += 1
        if count >= self.min_count and count <= self.max_count:
            return True
        return False

    def validate_part_two(self) -> bool:
        """Validate a password, part two style.

        Returns:
            bool: True for valid, False for invalid
        """
        if self.password[self.min_count - 1] == self.target_char:
            if self.password[self.max_count - 1] != self.target_char:
                return True
            return False
        if self.password[self.max_count - 1] == self.target_char:
            return True
        return False


def main() -> None:
    count_one = 0
    count_two = 0
    with open("input.txt", "r") as in_f:
        for row in in_f:
            validator = PasswordValidator.from_string(row)
            if validator.validate_part_one():
                count_one += 1
            if validator.validate_part_two():
                count_two += 1
    print("Part One Valid: ", count_one)
    print("Part Two Valid: ", count_two)


if __name__ == "__main__":
    main()
