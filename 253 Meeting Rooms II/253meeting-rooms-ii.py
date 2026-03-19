class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        i = 1
        j = 0
        n = 1
        result = 1

        while (i < len(intervals) and j < len(intervals)):
            if (start[i] < end[j]):
                n += 1
                i += 1
            else:
                n -= 1
                j += 1
            
            result = max(result, n)
        
        return result