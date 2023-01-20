class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        if not height: return 0
        
        # initialise
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        area = 0

        # depends on min height
        # left < right -> move left ptr to increase the height
        while l < r:
            if maxLeft < maxRight:
                l += 1
                # minus elevated section
                area += maxLeft - height[l] if maxLeft - height[l] > 0 else 0
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                # minus elevated section
                area += maxRight - height[r] if maxRight - height[r] > 0 else 0
                maxRight = max(maxRight, height[r])
                
        return area
