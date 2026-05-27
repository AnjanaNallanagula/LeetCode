class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ls = [0 for i in range(len(cost) + 1)]
        ls[0] = 0
        ls[1] = cost[0]

        for i in range(2, len(cost) + 1):
            ls[i] = cost[i - 1] + min(ls[i - 2], ls[i - 1])

        return min(ls[-1], ls[-2])