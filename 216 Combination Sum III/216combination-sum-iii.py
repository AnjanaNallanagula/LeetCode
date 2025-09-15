class Solution:
    def combinationSum1(self, i, start, k, n, ls1, ls):
        if (n < 0):
            return
        if (i == k and n == 0):
            ls.append(ls1[:])
            return
        if (i == k):
            return
        
        for j in range(start, 10):
            ls1[i] = j
            self.combinationSum1(i + 1, j + 1, k, n - j, ls1, ls)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ls = []
        ls1 = [0 for i in range(k)]

        self.combinationSum1(0, 1, k, n, ls1, ls)

        return ls