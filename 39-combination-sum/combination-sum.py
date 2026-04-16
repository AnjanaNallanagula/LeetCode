class Solution:
    def combinationSum1(self, i, candidates, target, ls, ls1):
        if (target == 0):
            ls.append(ls1[:])
            return
        if (i == len(candidates) or target < 0):
            return
        
        ls1.append(candidates[i])
        self.combinationSum1(i, candidates, target - candidates[i], ls, ls1)
        ls1.pop()
        self.combinationSum1(i + 1, candidates, target, ls, ls1)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ls = []
        ls1 = []

        self.combinationSum1(0, candidates, target, ls, ls1)

        return ls