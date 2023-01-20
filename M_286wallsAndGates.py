class Solution:
  def wallsAndGates(self, rooms: List[List[int]]):
    rows, cols = len(rooms), len(rooms[0])
    visit = set() # record the grid that been visited
    q = collections.deque()
    distance = 0
    
    def addRoom(r, c):
      # base case: out of bound, been visited or obstacles
      if r < 0 or r == rows or c < 0 or c < cols or (r, c) in visit or rooms[r][c] == -1:
        return
      # mark as visited and add to q
      visit.add((r, c))
      q.append([r, c])
      
      # scan the whole map for gates
      for r in range(rows):
        for c in range(cols):
          if rooms[r][c] == 0:
            q.append([r,c])
            visit.append([r,c])
            
      # bfs: starts from the gates
      while q:
        for i in range(len(q)):
          r,c = q.popleft()
          rooms[r][c] == distance
          
          # add neighbour to the queue
          addRoom(r + 1, c)
          addRoom(r - 1, c)
          addRoom(r, c + 1)
          addRoom(r, c - 1)
        # update distance
        distance += 1
                             
