#/usr/bin/env python
"""Halting problem"""
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional

class Operator(Enum):
    NOP = auto()
    ACC = auto()
    JMP = auto()

OP_MAP = {
        "nop": Operator.NOP,
        "acc": Operator.ACC,
        "jmp": Operator.JMP,
        }

@dataclass
class Instruction:

    opc: Operator
    arg: int

    @staticmethod
    def from_string(text: str) -> 'Instruction':
        """Parse an instruction from text"""
        pieces = text.split(" ")
        return Instruction(OP_MAP[pieces[0]], int(pieces[1]))

@dataclass
class Processor:

    code: List[Instruction]
    accumulator: int = 0
    pointer: int = 0
    past_instructions: List[Optional[int]] = field(default_factory=list)

    def execute_instructions(self) -> None:
        """Execute instructions as long as it hasn't been executed before"""
        while True:
            if self.pointer not in self.past_instructions:
                instruction = self.code[self.pointer]
                self.past_instructions.append(self.pointer)
                if instruction.opc == Operator.NOP:
                    self.pointer += 1
                if instruction.opc == Operator.ACC:
                    self.pointer += 1
                    self.accumulator += instruction.arg
                if instruction.opc == Operator.JMP:
                    self.pointer += instruction.arg
            else:
                return self.accumulator


def main() -> None:
    """Runs this"""
    instructions = list()
    with open("input.txt", "r") as in_f:
        for row in in_f:
            instructions.append(Instruction.from_string(row))
    proc = Processor(instructions)
    print(proc.execute_instructions())

if __name__ == "__main__":
    main()
