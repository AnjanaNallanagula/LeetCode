class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        flag = True

        while (i < len(bits)):
            if (bits[i] == 1):
                i += 2
                flag = False
            else:
                i += 1
                flag = True
        
        if (flag == True):
            return True
        return False