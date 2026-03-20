class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max1 = 0
        
        for i in range(len(accounts)):
            sum1 = 0
            
            for j in range(len(accounts[0])):
                sum1 += accounts[i][j]
            
            max1 = max(max1, sum1)
        
        return max1