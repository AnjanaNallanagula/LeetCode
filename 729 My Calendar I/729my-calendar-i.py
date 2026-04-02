class MyCalendar:

    def __init__(self):
        self.ls = []

    def book(self, startTime: int, endTime: int) -> bool:
        if (self.ls == []):
            self.ls.append([startTime, endTime])
            return True
        
        prev = []
        newInterval = [startTime, endTime]

        for i in range(len(self.ls)):
            if (newInterval[1] <= self.ls[i][0]):
                prev.append(newInterval)
                prev.extend(self.ls[i:])
                self.ls = prev
                return True
            elif (self.ls[i][1] <= newInterval[0]):
                prev.append(self.ls[i])
            else:
                return False
        
        prev.append(newInterval)
        self.ls = prev
        
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)