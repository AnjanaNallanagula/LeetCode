from collections import defaultdict

class Solution:
    def binary_search_lower_bound(self, ls, target):
        index = -1
        low = 0
        high = len(ls) - 1

        while (low <= high):
            mid = low + (high - low) // 2

            if (ls[mid] < target):
                index = mid
                low = mid + 1
            else:
                high = mid - 1
        
        if (index != -1):
            return ls[index]
        return ls[-1]
    
    def binary_search_upper_bound(self, ls, target):
        index = -1
        low = 0
        high = len(ls) - 1

        while (low <= high):
            mid = low + (high - low) // 2

            if (ls[mid] > target):
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        
        if (index != -1):
            return ls[index]
        return ls[0]
    
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        d = defaultdict(list)
        n = len(nums)

        for i in range(n):
            d[nums[i]].append(i)
        
        ls = []

        for i in queries:
            target = nums[i]

            if (len(d[target]) == 1):
                ls.append(-1)
            else:
                l = self.binary_search_lower_bound(d[target], i)
                r = self.binary_search_upper_bound(d[target], i)

                min1 = float("inf")

                if (l != -1):
                    min1 = min(min1, (i - l) % n)
                if (r != -1):
                    min1 = min(min1, (r - i) % n)
                
                ls.append(min1)
        
        return ls