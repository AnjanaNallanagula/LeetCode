class Solution:
    def combinationSum1(self, i, candidates, target, ls, ls1):
        if (target == 0):
            ls.append(tuple(ls1))
            return
        if (i == len(candidates) or target < 0):
            return
        
        ls1.append(candidates[i])

        self.combinationSum1(i + 1, candidates, target - candidates[i], ls, ls1)

        ls1.pop()
        
        j = i + 1

        while (j < len(candidates) and candidates[j] == candidates[i]):
            j += 1
        
        self.combinationSum1(j, candidates, target, ls, ls1)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ls = []
        ls1 = []

        self.combinationSum1(0, candidates, target, ls, ls1)
        
        return ls