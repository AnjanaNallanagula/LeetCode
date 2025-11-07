class NumArray:

    def __init__(self, nums: List[int]):
        self.ls = [0 for i in range(len(nums))]
        self.ls[0] = nums[0]

        for i in range(1, len(nums)):
            self.ls[i] = self.ls[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0):
            return self.ls[right]
        return (self.ls[right] - self.ls[left - 1])
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)