class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(3):
            flag = False

            for j in range(len(triplets)):
                if (triplets[j][i] == target[i]):
                    flag = True
                    break
            
            if (flag == False):
                return False
        
        return True