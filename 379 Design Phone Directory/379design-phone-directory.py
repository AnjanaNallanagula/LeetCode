class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.s = set([i for i in range(maxNumbers)])
    
    def get(self) -> int:
        if (len(self.s) == 0):
            return -1
        
        d = self.s.pop()
        
        return d

    def check(self, number: int) -> bool:
        if (number in self.s):
            return True
        return False

    def release(self, number: int) -> None:
        self.s.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)