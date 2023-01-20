class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set()
        direction = {
            "N": (0,1),
            "E": (1,0),
            "S": (0,-1),
            "W": (-1,0)
        }

        x, y = 0, 0
        visit.add((x,y))
        for p in path:
            dirX, dirY = direction.get(p)
            x, y = x + dirX, y + dirY
            if (x,y) in visit:
                return True
            else:
                visit.add((x,y))
        return False
