class Solution:
    def change1(self, n, amount, coins, mat):
        if (amount == 0):
            return 1
        if (n == 0):
            return 0
        
        if (mat[n][amount] != -1):
            return mat[n][amount]
        if (coins[n - 1] <= amount):
            mat[n][amount] = self.change1(n, amount - coins[n - 1], coins, mat) + self.change1(n - 1, amount, coins, mat)
        else:
            mat[n][amount] = self.change1(n - 1, amount, coins, mat)
        
        return mat[n][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        mat = [[-1 for j in range(amount + 1)] for i in range(n + 1)]

        return self.change1(n, amount, coins, mat)