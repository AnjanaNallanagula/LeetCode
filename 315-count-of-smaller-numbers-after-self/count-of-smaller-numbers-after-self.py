class Solution:
    def merge(self, nums, low, mid, high, ls):
        n1 = mid - low + 1
        n2 = high - mid
        left = [nums[low + i] for i in range(n1)]
        right = [nums[mid + 1 + j] for j in range(n2)]
        i = 0
        j = 0
        k = low

        while (i < n1 and j < n2):
            if (left[i][0] <= right[j][0]):
                index = left[i][1]
                ls[index] += j
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while (i < n1):
            index = left[i][1]
            ls[index] += j
            nums[k] = left[i]
            i += 1
            k += 1
        while (j < n2):
            nums[k] = right[j]
            j += 1
            k += 1
        
    def mergeSort(self, nums, low, high, ls):
        if (low < high):
            mid = low + (high - low) // 2

            self.mergeSort(nums, low, mid, ls)
            self.mergeSort(nums, mid + 1, high, ls)
            self.merge(nums, low, mid, high, ls)
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [(nums[i], i) for i in range(n)]
        ls = [0 for i in range(n)]

        self.mergeSort(nums, 0, n - 1, ls)

        return ls