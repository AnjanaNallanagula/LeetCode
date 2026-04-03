class Solution:
    def coinChange1(self, n, amount, coins, mat):
        if (amount == 0):
            return 0
        if (n == 0):
            return float("inf")
        
        if (mat[n][amount] != False):
            return mat[n][amount]
        
        if (coins[n - 1] <= amount):
            mat[n][amount] = min(1 + self.coinChange1(n, amount - coins[n - 1], coins, mat), self.coinChange1(n - 1, amount, coins, mat))
        else:
            mat[n][amount] = self.coinChange1(n - 1, amount, coins, mat)
        
        return mat[n][amount]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        mat = [[False for j in range(amount + 1)] for i in range(n + 1)]

        result = self.coinChange1(n, amount, coins, mat)

        if (result != float("inf")):
            return result
        return -1