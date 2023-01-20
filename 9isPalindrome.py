class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        div = 1
        while x >= 10 * div:
            div *= 10
            
        # x > 0
        while x: 
            r = x % 10
            l = x // div
            
            if l != r: return False
            
            # chop off both left and right digit
            x = (x % div) // 10
            div  = div / 100

        return True
