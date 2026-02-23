class Solution:
    def combinationSum1(self, i, candidates, target, ls1, s):
        if (target == 0):
            s.add(tuple(ls1))
            return
        if (i == len(candidates) or target < 0):
            return
        
        ls1.append(candidates[i])

        self.combinationSum1(i + 1, candidates, target - candidates[i], ls1, s)

        ls1.pop()
        
        j = i + 1

        while (j < len(candidates) and candidates[j] == candidates[i]):
            j += 1
        
        self.combinationSum1(j, candidates, target, ls1, s)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ls1 = []
        s = set()

        self.combinationSum1(0, candidates, target, ls1, s)

        ls = []

        for i in s:
            ls.append(list(i))
        
        return ls