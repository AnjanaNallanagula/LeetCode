class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        for i in range(len(list1)):
            if (list1[i] not in d):
                d[list1[i]] = i
        d1 = {}
        for i in range(len(list2)):
            if (list2[i] in d):
                d1[list2[i]] = d[list2[i]] + i
        min1 = 999999
        for i in d1:
            if (d1[i] < min1):
                min1 = d1[i]
        ls = []
        for i in d1:
            if (d1[i] == min1):
                ls.append(i)
        return ls