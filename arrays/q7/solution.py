from collections import defaultdict

class Solution:

    def scan_board(self, board: List[List[str]]) -> bool:
        row_counts = [set() for _ in board]
        col_counts = [set() for _ in board]
        square_counts = [[set(), set(), set()] for _ in range(3)]
        index_mapping = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                if num == ".":
                    continue
                if num in row_counts[row_index]:
                    return False
                elif num in col_counts[col_index]:
                    return False

                square_col = index_mapping[col_index]
                square_row = index_mapping[row_index]

                if num in square_counts[square_col][square_row]:
                    return False
                
                row_counts[row_index].add(num)
                col_counts[col_index].add(num)
                square_counts[square_col][square_row].add(num)

        print(row_counts)
        print(col_counts)
        return True


    def is_row_valid(self, row: List[str]) -> bool:
        visited = set()
        for num in row:
            if num == ".":
                continue
            if num in visited:
                return False
            else:
                visited.add(num)
        return True

    def not_working(self, board: List[List[str]]) -> bool:
        for row in board:
            result = self.is_row_valid(row)
            if not result:
                return result
        
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.scan_board(board)

        