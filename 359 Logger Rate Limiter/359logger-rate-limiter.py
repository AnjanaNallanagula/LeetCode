from collections import deque

class Logger:

    def __init__(self):
        self.q = deque()
        self.s = set()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while (len(self.q) != 0 and self.q[0][0] <= timestamp):
            t, d = self.q.popleft()
            self.s.remove(d)
        
        if (message not in self.s):
            self.q.append((timestamp + 10, message))
            self.s.add(message)
            
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)