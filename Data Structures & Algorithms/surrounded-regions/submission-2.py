class Solution:
    def solve(self, board: List[List[str]]) -> None:
        display(board)

        min_i, max_i = 0, len(board) - 1
        min_j, max_j = 0, len(board[0]) - 1

        saved = set()

        for i, line in enumerate(board):
            for j, _ in enumerate(line):

                # print(i, j, not (i in (min_i, max_i) or j in (min_j, max_j)), board[i][j] == "X")

                if (
                    not (i in (min_i, max_i) or j in (min_j, max_j))
                    or board[i][j] == "X"
                    or (i, j) in saved
                ):
                    continue

                neighbours = deque([(i, j)])

                print(i, j)
                turns = 0

                while neighbours:
                    turns += 1

                    neighbour = neighbours.pop()
                    saved.add(neighbour)

                    print(neighbours)
                    print(neighbour)

                    for offset_i in (-1, 0, 1):
                        for offset_j in (-1, 0, 1):
                            if abs(offset_i) == abs(offset_j):
                                continue

                            new_i = neighbour[0] + offset_i
                            new_j = neighbour[1] + offset_j
    
                            print(new_i, new_j)

                            if (
                                not self.aligned_i(board, new_i)
                                or not self.aligned_j(board, new_j)
                                or board[new_i][new_j] == "X"
                                or (new_i, new_j) in saved
                                or (new_i, new_j) in neighbours
                            ):
                                continue

                            print(new_i, new_j, (new_i, new_j) in saved)

                            neighbours.append((new_i, new_j))

        print(saved)

        for i, line in enumerate(board):
            for j, _ in enumerate(line):
                if (
                    board[i][j] == "X"
                    or (i, j) in saved
                ):
                    continue
                
                print(i, j)

                board[i][j] = "X"

        return None

    @staticmethod
    def aligned_i(board: List[List[str]], i: int) -> bool:
        min_i, max_i = 0, len(board) - 1
        return i >= min_i and i <= max_i

    @staticmethod
    def aligned_j(board: List[List[str]], j: int) -> bool:
        min_j, max_j = 0, len(board[0]) - 1
        return j >= min_j and j <= max_j


def display(board: List[List[str]]) -> None:
    for line in board:
        print(line)
