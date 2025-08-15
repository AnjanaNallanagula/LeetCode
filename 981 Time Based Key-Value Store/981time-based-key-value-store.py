from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.d):
            return ""

        index = -1
        low = 0
        high = len(self.d[key]) - 1

        while (low <= high):
            mid = low + (high - low) // 2

            if (self.d[key][mid][0] <= timestamp):
                index = mid
                low = mid + 1
            else:
                high = mid - 1

        if (index == -1):
            return ""
        return self.d[key][index][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)