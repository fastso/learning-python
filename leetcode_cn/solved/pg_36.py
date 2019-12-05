from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = [set() for i in range(9)]
        row_set = [set() for i in range(9)]
        box_set = [set() for i in range(9)]

        for y in range(9):
            for x in range(9):
                if board[y][x] == '.':
                    continue
                box_index = (y // 3) * 3 + x // 3
                if board[y][x] in col_set[y]:
                    return False
                if board[y][x] in row_set[x]:
                    return False
                if board[y][x] in box_set[box_index]:
                    return False
                col_set[y].add(board[y][x])
                row_set[x].add(board[y][x])
                box_set[box_index].add(board[y][x])
        return True
