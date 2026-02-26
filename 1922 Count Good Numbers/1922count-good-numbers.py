class Solution:
    def power(self, n, x):
        if (x == 0 or n == 1):
            return 1
        if (x == 1):
            return n
        
        p = self.power(n, x // 2)

        if (x % 2 == 0):
            return ((p ** 2) % (10 ** 9 + 7))
        return ((p * p * n) % (10 ** 9 + 7))
        
    def countGoodNumbers(self, n: int) -> int:
        if (n % 2 == 0):
            even = n // 2
            odd = n // 2
        else:
            even = (n // 2) + 1
            odd = n // 2
        
        even_power = self.power(5, even)
        odd_power = self.power(4, odd)
        count = even_power * odd_power
        count %= (10 ** 9 + 7)

        return count