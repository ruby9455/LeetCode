class Solution:
    def maxArea(self, height: List[int]) -> int:
      # initialise
      maxArea = 0
      maxHeight = max(height)
      l, r = 0, len(height) - 1
      
      # moving l, r ptr inward
      while l < r:
        area = (r - l) * min(height[l], height[r])
        maxArea = max(maxArea, area)
        # if no more possible update on maxArea
        if maxArea/maxHeight > r - l:
          break
        # area depends on minHeight
        if height[l] < height[r]:
          l += 1
        else:
          r -= 1
      return maxArea
    
