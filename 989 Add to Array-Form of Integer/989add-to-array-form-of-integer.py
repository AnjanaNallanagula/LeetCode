class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = [int(i) for i in str(k)]
        
        def addZeros(ls, d):
            while (d > 0):
                ls.insert(0, 0)
                d -= 1
        
        if (len(num) >= len(num1)):
            d = len(num) - len(num1)
            addZeros(num1, d)
        else:
            d = len(num1) - len(num)
            addZeros(num, d)
        
        carry = 0
        
        for i in range(len(num) - 1, -1, -1):
            sum1 = num[i] + num1[i] + carry
            num[i] = sum1 % 10
            carry = sum1 // 10
 
        if (carry > 0):
            num.insert(0, carry)
        
        return num