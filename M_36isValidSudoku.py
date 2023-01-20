class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # existing numbers 
        cols = defaultdict(set)
        rows = defaultdict(set)
        subgrids = defaultdict(set)
        
        # scan the board by row and col
        for x in range(9):
            for y in range(9):
                # empty cell
                if board[x][y] == ".":
                    continue
                # duplicate num
                if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in subgrids[(x/3),(y/3)]:
                    return False
                # new num
                cols[y].add(board[x][y])
                rows[x].add(board[x][y])
                subgrids[(x/3),(y/3)].add(board[x][y])
        return True
