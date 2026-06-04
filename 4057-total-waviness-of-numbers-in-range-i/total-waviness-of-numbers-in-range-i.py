class Solution:
    def waviness(self, n):
        count = 0

        for i in range(1, len(n) - 1):
            if (n[i] < n[i - 1] and n[i] < n[i + 1]):
                count += 1
            if (n[i] > n[i - 1] and n[i] > n[i + 1]):
                count += 1
        
        return count
    
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0

        for i in range(num1, num2 + 1):
            count = self.waviness(str(i))
            total += count
        
        return total