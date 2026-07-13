EMPTY = "."

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for line, values in enumerate(board, start=1):
            for col, value in enumerate(values, start=1):
                if value == EMPTY:
                    continue

                if value in row:
                    return False
                row.add(value)

                if value in cols[col]:
                    return False
                cols[col].add(value)

                box = math.ceil(col / 3)
                if value in boxes[box]:
                    return False
                boxes[box].add(value)

            row = set()
            boxes.clear() if line % 3 == 0 else None

        return True


def display(board: List[List[str]]) -> None:
    for line in board:
        print(line)
