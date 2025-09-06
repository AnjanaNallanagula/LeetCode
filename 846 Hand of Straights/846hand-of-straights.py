class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize != 0):
            return False
        
        hand.sort()
        d = {}
        count = 0

        for i in hand:
            if (i in d):
                d[i] += 1
            else:
                d[i] = 1
        
        for i in range(len(hand)):
            if (d[hand[i]] > 0):
                count = 0
                curr = hand[i]
                flag = False

                while (curr in d and d[curr] > 0):
                    count += 1
                    d[curr] -= 1
                    curr += 1

                    if (count == groupSize):
                        flag = True
                        break
                
                if (flag == False):
                    return False
        
        return True