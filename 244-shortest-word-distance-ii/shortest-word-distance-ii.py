from collections import defaultdict
import bisect

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d = defaultdict(list)

        for i in range(len(wordsDict)):
            self.d[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        min1 = float("inf")
        ls = self.d[word2]

        for i in self.d[word1]:
            j = bisect.bisect_left(ls, i)

            if (j < len(ls)):
                min1 = min(min1, ls[j] - i)
            if (j > 0):
                min1 = min(min1, i - ls[j - 1])
        
        return min1

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)