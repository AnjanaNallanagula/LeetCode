from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0):
            return False
        
        d = defaultdict(lambda: 0)

        for i in hand:
            d[i] += 1
        
        hand.sort()

        for i in hand:
            if (d[i] > 0):
                count = 0
                curr = i
                flag = False

                while (curr in d):
                    count += 1
                    d[curr] -= 1

                    if (d[curr] == 0):
                        del d[curr]
                    
                    curr += 1

                    if (count == groupSize):
                        flag = True
                        break
                
                if (flag == False):
                    return False
        
        return True