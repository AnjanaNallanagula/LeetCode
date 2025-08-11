class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        left = [0 for i in range(len(security))]
        right = [0 for j in range(len(security))]

        for i in range(1, len(left)):
            if (security[i] <= security[i - 1]):
                left[i] = left[i - 1] + 1
        
        for j in range(len(security) - 2, -1, -1):
            if (security[j] <= security[j + 1]):
                right[j] = right[j + 1] + 1

        ls = []

        for i in range(len(security)):
            if (min(left[i], right[i]) >= time):
                ls.append(i)
        
        return ls