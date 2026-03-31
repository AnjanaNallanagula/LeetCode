class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        count = 0
        
        for t in words:
            if (set(s) != set(t)):
                continue
            
            i = 0
            j = 0
            flag = False
            
            while (i < len(s) and j < len(t)):
                if (s[i] == t[j]):
                    count1 = 0
                    char = s[i]
                    
                    while (i < len(s) and s[i] == char):
                        i += 1
                        count1 += 1
                    
                    count2 = 0
                    
                    while (j < len(t) and t[j] == char):
                        j += 1
                        count2 += 1
                    
                    if (count1 != count2):
                        if (count1 < count2):
                            flag = True
                            break
                        if (count2 == 1):
                            count2 += 2
                        else:
                            count2 = count1
                        if (count1 < count2):
                            flag = True
                            break
            
            if (flag == False and i == len(s) and j == len(t)):
                count += 1
        
        return count