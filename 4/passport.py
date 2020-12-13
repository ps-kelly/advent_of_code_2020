#!/usr/bin/env python
"""Passport problems."""

from dataclasses import dataclass
from typing import Optional

import pandas as pd

@dataclass
class Passport:
    """Passport class"""

    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None

def read_and_count(filename: str) -> None:
    """Read and count passports.

    Args:
        filename (str): filename to open
    """
    out_l = []
    df_l = []
    bad_passports = 0
    good_passports = 0
    with open(filename, "r") as in_f:
        passports_raw = in_f.read()
    for document in passports_raw.split("\n\n"):
        chunks = document.replace("\n", " ").split(" ")
        mapped_passport = dict()
        for chunk in chunks:
            pair = chunk.split(":")
            try:
                mapped_passport[pair[0]] = pair[1]
            except IndexError:
                pass
        try:
            out_l.append(Passport(**mapped_passport))
            good_passports += 1
            print(mapped_passport, " good passport, number ", good_passports, " keys: ", mapped_passport.keys())
        except TypeError:
            bad_passports += 1
            print(mapped_passport, ", bad passport, number ", bad_passports, " keys: ", mapped_passport.keys())
    print(len(out_l))
    print(good_passports)


def main() -> None:
    """Validates input.txt"""
    read_and_count("input.txt")
    read_and_count("input_test.txt")



if __name__ == "__main__":
    main()
