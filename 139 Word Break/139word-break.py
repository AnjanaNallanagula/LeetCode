class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ls = [False for i in range(len(s) + 1)]
        ls[0] = True
        wordDict = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                s1 = s[j:i]

                if ((s1 in wordDict) and (ls[j] == True)):
                    ls[i] = True
                    break
        
        return ls[-1]