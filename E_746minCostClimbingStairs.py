class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
        # add the final step
        cost.append(0)
        
        # moving from backward, starts at third last pos
        for i in range(len(cost) - 1 - 2, -1, -1):
            # i+1: one step; i+2: two steps
            cost[i] = min(cost[i] + cost[i + 1], cost[i]+cost[i + 2])
            
        # can either start at indices 0 or 1
        return min(cost[0],cost[1])
