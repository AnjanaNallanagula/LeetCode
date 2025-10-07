class Solution:
    def rowAndMaximumOnes1(self, ls):
        ls.sort()
        low = 0
        high = len(ls) - 1
        index = -1

        while (low <= high):
            mid = low + (high - low) // 2

            if (ls[mid] == 1):
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if (index == -1):
            return 0
        return (len(ls) - index)
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ls = [float("inf"), 0]

        for i in range(len(mat)):
            count = self.rowAndMaximumOnes1(mat[i])

            if (count > ls[1]):
                ls[0] = i
                ls[1] = count
            elif (count == ls[1]):
                ls[0] = min(ls[0], i)
        
        if (ls[0] != float("inf")):
            return ls
        return [0, 0]