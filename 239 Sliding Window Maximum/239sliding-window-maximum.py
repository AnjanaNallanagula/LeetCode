from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ls = []

        for i in range(k):
            while (len(q) != 0 and nums[q[-1]] <= nums[i]):
                q.pop()
            
            q.append(i)
        
        for i in range(k, len(nums)):
            ls.append(nums[q[0]])

            while (len(q) != 0 and nums[q[-1]] <= nums[i]):
                q.pop()
            
            while (len(q) != 0 and q[0] < (i - k + 1)):
                q.popleft()
            
            q.append(i)
        
        ls.append(nums[q[0]])

        return ls