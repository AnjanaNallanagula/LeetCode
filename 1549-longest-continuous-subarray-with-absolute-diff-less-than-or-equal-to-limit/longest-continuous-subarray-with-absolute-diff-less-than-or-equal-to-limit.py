from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_que = deque([])
        min_que = deque([])
        n = len(nums)
        j = 0
        result = -1

        for i in range(n):
            while (max_que and max_que[-1] < nums[i]):
                max_que.pop()
            while (min_que and min_que[-1] > nums[i]):
                min_que.pop()
            
            max_que.append(nums[i])
            min_que.append(nums[i])

            if (max_que[0] - min_que[0] <= limit):
                result = max(result, (i - j + 1))
            else:
                if (max_que[0] == nums[j]):
                    max_que.popleft()
                if (min_que[0] == nums[j]):
                    min_que.popleft()
                j += 1
        
        return result