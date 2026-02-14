class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = ((nums[i] << 10) | (nums[i + n]))
        
        j = 2 * n - 1

        for i in range(n - 1, -1, -1):
            y_i = (nums[i] & (2 ** 10 - 1))
            x_i = (nums[i] >> 10)

            nums[j] = y_i
            nums[j - 1] = x_i
            j -= 2
        
        return nums