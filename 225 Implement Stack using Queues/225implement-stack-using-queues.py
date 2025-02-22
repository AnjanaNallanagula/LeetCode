class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
    
    def push(self, x: int) -> None:
        if (len(self.q1) == 0):
            self.q1.append(x)
        else:
            self.q2.append(x)
            while (len(self.q1) != 0):
                d = self.q1.pop(0)
                self.q2.append(d)
            self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        if (len(self.q1) == 0):
            return -1
        d = self.q1.pop(0)
        return d

    def top(self) -> int:
        if (len(self.q1) == 0):
            return -1
        return self.q1[0]

    def empty(self) -> bool:
        if (len(self.q1) == 0):
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()