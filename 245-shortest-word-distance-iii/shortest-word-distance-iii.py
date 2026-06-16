class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        distance = float("inf")

        if (word1 != word2):
            i = float("-inf")
            j = float("-inf")

            for k in range(len(wordsDict)):
                if (wordsDict[k] == word1):
                    i = max(i, k)
                elif (wordsDict[k] == word2):
                    j = k

                if (i != float("-inf") and j != float("-inf")):
                    distance = min(distance, abs(j - i))
        else:
            j = -1

            for i in range(len(wordsDict)):
                if (wordsDict[i] == word1):
                    if (j != -1):
                        distance = min(distance, i - j)
                    j = i
        
        return distance