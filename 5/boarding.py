"""Day 5 things"""

from dataclasses import dataclass, field
import math
import operator

@dataclass
class BoardingPass:
    """Boarding pass"""

    col: int
    row: int

    @staticmethod
    def from_string(text: str) -> 'BoardingPass':
        """Alternate constructor from text.

        Args:
            text (str): text of the pass

        Returns:
            BoardingPass: a new BoardingPass
        """
        min_row = 0
        max_row = 127
        min_col = 0
        max_col = 7
        for i, c in enumerate(text):
            if i < 7:
                if c == "F":
                    max_row = math.floor((max_row - min_row) / 2) + min_row
                if c == "B":
                    min_row = math.ceil((max_row - min_row) / 2) + min_row
            else:
                if c == "R":
                    min_col = math.ceil((max_col - min_col) / 2) + min_col
                if c == "L":
                    max_col = math.floor((max_col - min_col) / 2) + min_col
        if min_row == max_row and min_col == max_col:
            return BoardingPass(col=min_col, row=min_row)

    def get_id(self) -> int:
        """Get the id of this"""
        return self.row * 8 + self.col

    def __lt__(self, other: "BoardingPass") -> bool:
        """LT dunder """
        return self.get_id() < other.get_id()


def main() -> None:
    """Runs this"""
    out_l = []
    max_id = 0
    with open("input.txt", "r") as in_f:
        for row in in_f:
            boarding_pass = BoardingPass.from_string(row)
            new_id = boarding_pass.get_id()
            if new_id > max_id:
                max_id = new_id 
            out_l.append(boarding_pass)
    print(max_id)
    sorted_seats = sorted(out_l)
    prev_id = -1
    min_row = sorted_seats[0].row
    max_row = sorted_seats[-1].row
    for seat in sorted_seats:
        print(seat)
        if seat.row > min_row and seat.get_id() - prev_id > 1:
            print(seat, seat.get_id() - 1)
            break
        prev_id = seat.get_id()



def test_passes():
    """test passes"""
    b = BoardingPass.from_string("FBBFBBBRLR")
    BoardingPass.from_string("BFFFBBFRRR")
    BoardingPass.from_string("FFFBBBFRRR")

if __name__ == "__main__":
    main()

