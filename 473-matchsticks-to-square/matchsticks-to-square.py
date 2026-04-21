class Solution:
    def makesquare1(self, i, matchsticks, ls, d):
        if (i == len(matchsticks) and len(set(ls)) == 1 and ls[0] == d):
            return True
        if (i == len(matchsticks)):
            return False
        
        for j in range(4):
            if (ls[j] + matchsticks[i] <= d):
                ls[j] += matchsticks[i]

                if (self.makesquare1(i + 1, matchsticks, ls, d)):
                    return True
                
                ls[j] -= matchsticks[i]

        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        sum1 = sum(matchsticks)

        if (sum1 % 4 != 0):
            return False
        
        matchsticks.sort(reverse = True)
        ls = [0, 0, 0, 0]
        d = sum1 // 4

        return self.makesquare1(0, matchsticks, ls, d)