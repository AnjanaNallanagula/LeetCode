class Solution:
    def isValid(self, arr, max1):
        s = "".join(arr)
        h = s[:2]
        m = s[2:]
        
        if (int(s) < 0 or int(s) > max1 or int(h) < 0 or int(h) > 23 or int(m) < 0 or int(m) > 59):
            return False
        return True
    
    def permutations(self, arr, low, high, ls, max1):
        if (low == high):
            if (self.isValid(arr, max1) == True):
                s = "".join(arr)
                t = "".join(ls)
                    
                if (s > t):
                    ls[0] = s
            return
        
        for i in range(low, high + 1):
            arr[low], arr[i] = arr[i], arr[low]
            self.permutations(arr, low + 1, high, ls, max1)
            arr[low], arr[i] = arr[i], arr[low]
        
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ls = [""]
        max1 = 2359
        arr = [str(i) for i in arr]
        
        self.permutations(arr, 0, len(arr) - 1, ls, max1)

        if (ls[0] != ""):
            s = ls[0][:2] + ":" + ls[0][2:]
            return s
        
        return ""