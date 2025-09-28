class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        ls = []
        ls1 = []

        for i in range(len(s)):
            if (s[i] == "|"):
                ls.append(i)
        
        for i in queries:
            target_left = i[0]
            left_index = -1
            low = 0
            high = len(ls) - 1

            while (low <= high):
                mid = low + (high - low) // 2
                if (ls[mid] >= target_left):
                    left_index = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            target_right = i[1]
            right_index = -1
            low = 0
            high = len(ls) - 1

            while (low <= high):
                mid = low + (high - low) // 2
                if (ls[mid] <= target_right):
                    right_index = mid
                    low = mid + 1
                else:
                    high = mid - 1

            if ((left_index != -1) and (right_index != -1) and (right_index > left_index)):
                d = (ls[right_index] - ls[left_index]) - (right_index - left_index)
                ls1.append(d)
            else:
                ls1.append(0)
        
        return ls1