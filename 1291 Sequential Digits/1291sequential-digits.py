class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ls = []

        for i in range(1, 10):
            n = i
            for j in range(i + 1, 10):
                n = n * 10 + j
                if (low <= n <= high):
                    ls.append(n)

        ls.sort()

        return ls