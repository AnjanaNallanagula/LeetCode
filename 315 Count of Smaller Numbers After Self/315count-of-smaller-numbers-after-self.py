class Solution:
    def merge(self, low, mid, high, nums, ls):
        n1 = mid - low + 1
        n2 = high - mid
        left = [nums[low + i] for i in range(n1)]
        right = [nums[mid + 1 + j] for j in range(n2)]
        i = 0
        j = 0
        k = low

        while (i < n1 and j < n2):
            if (left[i][0] <= right[j][0]):
                ls[left[i][1]] += j
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while (i < n1):
            ls[left[i][1]] += j
            nums[k] = left[i]
            i += 1
            k += 1
        
        while (j < n2):
            nums[k] = right[j]
            j += 1
            k += 1
    
    def mergeSort(self, low, high, nums, ls):
        if (low < high):
            mid = low + (high - low) // 2

            self.mergeSort(low, mid, nums, ls)
            self.mergeSort(mid + 1, high, nums, ls)
            self.merge(low, mid, high, nums, ls)
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums))]
        ls = [0 for i in range(len(nums))]

        self.mergeSort(0, len(nums) - 1, nums, ls)

        return ls