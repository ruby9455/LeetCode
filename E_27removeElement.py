class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count no. of target value in the list
        count = nums.count(val)
        # remove it for (count) times
        for i in range(count):
            nums.remove(val)
