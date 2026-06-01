class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        min_cost = 0
        i = len(cost) - 1

        while (i >= 0):
            min_cost += cost[i]

            if (i - 1 >= 0):
                min_cost += cost[i - 1]
            
            i -= 3
        
        return min_cost