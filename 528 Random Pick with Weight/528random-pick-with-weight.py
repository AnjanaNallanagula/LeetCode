import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.ls = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        index = random.choices(self.ls, weights = self.w, k = 1)[0]

        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()