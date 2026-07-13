class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        display(board)

        seen_row = set()
        seen_col = defaultdict(set)
        seen_box = defaultdict(set)

        for y, row in enumerate(board, 1):
            for x, val in enumerate(row, 1):
                # print(seen_row)
                # print(seen_col)
                print(seen_box)

                if val == '.':
                    continue

                if val in seen_row:
                    return False
                seen_row.add(val)

                if val in seen_col[x]:
                    return False
                seen_col[x].add(val)

                if val in seen_box[math.ceil(x / 3)]:
                    return False
                seen_box[math.ceil(x / 3)].add(val)

            seen_row = set()
            seen_box = defaultdict(set) if y % 3 == 0 else seen_box

        return True


def display(board: List[List[str]]) -> None:
    for row in board:
        print(row)
