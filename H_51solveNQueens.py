class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
      # loop along row, queens can't fall on the same col and diagonals
      col = set()
      posDiag = set() # r + c
      negDiag = set() # r - c
      
      # initialise the result and n * n board
      result = []
      board = [["."] * n for i in range(n))]
      
      def backtrack(row):
        if r == n:
          # join all the rows before appending to result
          ans = ["".join(row) for row in board]
          result.append(ans)
          return
        
        for c in range(n):
          # base case: will attack each other
          if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
            
          # update set
          col.add(c)
          posDiag.add(r + c)
          negDiag.add(r - c)
          
          # update board
          board[r][c] = "Q"
          
          # move to next row
          backtrack[r + 1)
                    
          # clean up
          col.remove(c)
          posDiag.remove(r + c)
          negDiag.remove(r - c)
          board[r][c] = "."
                    
      backtrack(0)      
