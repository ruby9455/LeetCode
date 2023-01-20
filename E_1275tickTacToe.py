class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        aMoves = []
        bMoves = []
        wins = [ # horizontal
                [[0,0],[1,0],[2,0]],
                [[0,1],[1,1],[2,1]],
                [[0,2],[1,2],[2,2]],
                # vertical
                [[0,0],[0,1],[0,2]],
                [[1,0],[1,1],[1,2]],
                [[2,0],[2,1],[2,2]],
                # diagnoal
                [[0,0],[1,1],[2,2]],
                [[0,2],[1,1],[2,0]]
               ]
        
        count = 1
        for move in moves:
            if count % 2 == 1:
                aMoves.append(move)
            else:
                bMoves.append(move)
            count += 1

        for win in wins:
            aCount = bCount = 0
            for move in win:
                if move in aMoves:
                    aCount += 1
                elif move in bMoves:
                    bCount += 1
                if aCount == 3:
                    return "A"
                if bCount == 3:
                    return "B"
        if len(aMoves) + len(bMoves) == 9:
            return "Draw"
        else:
            return "Pending"
