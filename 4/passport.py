#!/usr/bin/env python
"""Passport problems."""

from dataclasses import dataclass
import re
from typing import Optional

import pandas as pd


HEIGHT_PATTERN = re.compile(r"^(\d+)(cm|in)$")
HAIR_PATTERN = re.compile(r"^#[0-9a-f]{6}$")
EYE_PATTERN = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
PID_PATTERN = re.compile(r"^[0-9]{9}")

@dataclass
class Passport:
    """Passport class"""

    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None

    def part_two(self) -> bool:
        """Better validators
        
        Returns:
            bool: False if invalid
        """
        if len(self.byr) == 4:
            new_byr = int(self.byr)
            if new_byr < 1920 or new_byr > 2002:
                return False
        else:
            return False
        if len(self.iyr) == 4:
            new_iyr = int(self.iyr)
            if new_iyr < 2010 or new_iyr > 2020:
                return False
        else:
            return False
        if len(self.eyr) == 4:
            new_eyr = int(self.eyr)
            if new_eyr < 2020 or new_eyr > 2030:
                return False
        else:
            return False
        match_height = re.fullmatch(HEIGHT_PATTERN, self.hgt)
        if match_height:
            if match_height.group(2) == "in":
                height = int(match_height.group(1))
                if height < 59 or height > 76:
                    return False
            elif match_height.group(2) == "cm":
                height = int(match_height.group(1))
                if height < 150 or height > 193:
                    return False
            else:
                return False
        else:
            return False
        if not re.fullmatch(HAIR_PATTERN, self.hcl):
            return False
        if not re.fullmatch(EYE_PATTERN, self.ecl):
            return False
        if not re.fullmatch(PID_PATTERN, self.pid):
            return False
        return True


def read_and_count(filename: str) -> None:
    """Read and count passports.

    Args:
        filename (str): filename to open
    """
    out_l = []
    bad_passports = 0
    good_passports = 0
    good_pt_2 = 0
    with open(filename, "r") as in_f:
        passports_raw = in_f.read()
    for document in passports_raw.split("\n\n"):
        chunks = document.replace("\n", " ").split(" ")
        mapped_passport = dict()
        for chunk in chunks:
            pair = chunk.split(":")
            try:
                mapped_passport[pair[0]] = pair[1]
            except:
                continue
        try:
            passport = Passport(**mapped_passport)
            out_l.append(passport)
            good_passports += 1
        except TypeError:
            bad_passports += 1
    for passport in out_l:
        if passport.part_two():
            good_pt_2 += 1
    print("Good pt 1: ", good_passports)
    print("Good pt 2: ", good_pt_2)



def main() -> None:
    """Validates input.txt"""
    read_and_count("input.txt")



if __name__ == "__main__":
    main()
