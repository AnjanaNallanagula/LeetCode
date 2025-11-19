class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {order[i]: i for i in range(26)}

        for i in range(20):
            prev = -1
            flag = True

            for j in range(len(words)):
                if (i < len(words[j])):
                    curr = d[words[j][i]]
                else:
                    curr = -1

                if (curr < prev):
                    return False
                elif (curr == prev):
                    flag = False
                
                prev = curr
            
            if (flag == True):
                return True
        
        return True