class Solution:
    def gray_code(self, n):
        if (n == 1):
            return ['0', '1']
        prev = self.gray_code(n - 1)
        ls = []
        for i in prev:
            s = "0" + str(i)
            ls.append(s)
        for i in prev[::-1]:
            s = "1" + str(i)
            ls.append(s)
        return ls
    
    def grayCode(self, n: int) -> List[int]:
        ls = self.gray_code(n)
        ls1 = []
        for i in ls:
            d = int(i, 2)
            ls1.append(d)
        return ls1
        