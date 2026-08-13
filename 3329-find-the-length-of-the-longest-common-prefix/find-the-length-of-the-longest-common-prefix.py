class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for i in arr1:
            s = str(i)

            for j in range(1, len(s) + 1):
                prefixes.add(s[:j])
        
        max1 = 0

        for i in arr2:
            s = str(i)

            for j in range(len(s) + 1, 0, -1):
                if (s[:j] in prefixes):
                    max1 = max(max1, len(s[:j]))
                    break
        
        return max1