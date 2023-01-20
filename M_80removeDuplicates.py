class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dict for num counts
        numDict = {}
        # nums to be deleted
        deletes = []

        for num in nums:
            # appear > 1
            if num in numDict:
                # more than twice
                if numDict[num] >= 2:
                    deletes.append(num)
                # less than twice
                else:
                    numDict[num] += 1
            # new
            else:
                numDict[num] = 1
        
        # delete the nums
        for delete in deletes:
            nums.remove(delete)
        
        return len(nums)
