class Solution:
    def maximumSwap(self, num: int) -> int:
        ls = [i for i in str(num)]
        max_index = -1
        max1 = "0"
        left = -1
        right = -1

        for i in range(len(ls) - 1, -1, -1):
            if (ls[i] > max1):
                max1 = ls[i]
                max_index = i
            elif (ls[i] < max1):
                left = i
                right = max_index
        
        if (left != -1):
            ls[left], ls[right] = ls[right], ls[left]

        n = int("".join(ls))

        return n