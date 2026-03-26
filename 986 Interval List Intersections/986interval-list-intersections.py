class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ls = []
        i = 0
        j = 0

        while (i < len(firstList) and j < len(secondList)):
            if (firstList[i][0] > secondList[j][1]):
                j += 1
            elif (secondList[j][0] > firstList[i][1]):
                i += 1
            else:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                ls.append([start, end])

                if (firstList[i][1] <= secondList[j][1]):
                    i += 1
                else:
                    j += 1
        
        return ls