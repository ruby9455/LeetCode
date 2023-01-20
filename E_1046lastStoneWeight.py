class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
      # minHeap
      stones = [-s for s in stones]
      heapq.heapify(stones)
      
      while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(sotnes)
        # x != y, update the weight, then add back 
        if second > first:
          heapq.heappust(stones, first-second)
          
      if stones:
        return abs(stones[0])
      return 0
