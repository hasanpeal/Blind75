from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
        seen = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr != ".":
                    row = f"{curr} in row {i}"
                    col = f"{curr} in col {j}"
                    box = f"{curr} in box {(i//3 * 3) + j//3}"
                    print(box)
                    if row in seen or col in seen or box in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
        return True

board = [["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

isValidSudoku(board)