from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        q1 = deque()
        q2 = deque()
        max1 = 0
        j = 0
        
        for i in range(len(nums)):
            while (len(q1) != 0 and q1[-1] < nums[i]):
                q1.pop()
            while (len(q2) != 0 and q2[-1] > nums[i]):
                q2.pop()
            
            q1.append(nums[i])
            q2.append(nums[i])
            
            if (q1[0] - q2[0] <= limit):
                max1 = max(max1, (i - j + 1))
            else:
                if (q1[0] == nums[j]):
                    q1.popleft()
                if (q2[0] == nums[j]):
                    q2.popleft()
                
                j += 1
        
        return max1