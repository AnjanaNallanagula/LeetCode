from collections import deque

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        q = deque([])

        for i in range(k):
            if ((len(q) != 0) and (nums[i] != nums[q[-1]] + 1)):
                q.clear()
            
            q.append(i)
        
        ls = []
        
        for i in range(k, len(nums)):
            if (len(q) == k):
                ls.append(nums[q[-1]])
            else:
                ls.append(-1)
            
            if ((len(q) != 0) and (nums[i] != nums[q[-1]] + 1)):
                q.clear()
            
            while ((len(q) != 0) and (q[0] < (i - k + 1))):
                q.popleft()
            
            q.append(i)
        
        if (len(q) == k):
            ls.append(nums[q[-1]])
        else:
            ls.append(-1)
        
        return ls