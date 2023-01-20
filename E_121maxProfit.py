class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      # initialise
      # left ptr at 0, pointing to lower price
      l = 0
      maxProfit = 0
      
      # move right ptr to check the changes
      for r in range(1, len(prices)):
          # update left ptr, if lower price found
          if prices[r] < prices[l]:
              l = r
          # update the maxProfit if new max, otherwise keep the old
          maxProfit = max(maxProfit, prices[r]-prices[l])
      return maxProfit
