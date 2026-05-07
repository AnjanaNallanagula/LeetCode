class Solution:
    def minimumChairs(self, s: str) -> int:
        max1 = 0
        count = 0

        for i in s:
            if (i == "E"):
                count += 1
            else:
                count -= 1

            max1 = max(max1, count)
        
        return max1