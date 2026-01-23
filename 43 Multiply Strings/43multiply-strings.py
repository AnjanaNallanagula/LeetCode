class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if (len(num2) < len(num1)):
            num1, num2 = num2, num1
        
        result = 0
        n = len(num1)
        m = len(num2)
        level = 0

        for i in range(n - 1, -1, -1):
            d1 = int(num1[i])
            sum1 = ""
            carry = 0

            for j in range(m - 1, -1, -1):
                d2 = int(num2[j])
                p = d1 * d2 + carry
                sum1 = str(p % 10) + sum1
                carry = p // 10

            if (carry > 0):
                sum1 = str(carry) + sum1
            
            result += int(sum1 + "0" * level)
            level += 1
        
        return str(result)