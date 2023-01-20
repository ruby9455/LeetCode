class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 2:
            if i != len(bits) - 2:
                if bits[i] == 1:
                    i += 2
                else:
                    i += 1
        if bits[i] == 1:
            return False
        return True
