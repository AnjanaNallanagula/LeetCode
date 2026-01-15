class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n1 = len(a)
        n2 = len(b)

        if (n1 > n2):
            d = n1 - n2
            b = "0" * d + b
        else:
            d = n2 - n1
            a = "0" * d + a
        
        s = ""
        carry = "0"

        for i in range(len(a) - 1, -1, -1):
            sum1 = ""
            count0 = 0
            count1 = 0

            count0 = (count0 + 1) if (a[i] == "0") else count0
            count1 = (count1 + 1) if (a[i] == "1") else count1
            count0 = (count0 + 1) if (b[i] == "0") else count0
            count1 = (count1 + 1) if (b[i] == "1") else count1
            count0 = (count0 + 1) if (carry == "0") else count0
            count1 = (count1 + 1) if (carry == "1") else count1

            if (count0 == 3):
                sum1 = "0"
            elif (count1 == 3):
                sum1 = "1"
                carry = "1"
            elif (count0 == 2):
                sum1 = "1"
                carry = "0"
            else:
                sum1 = "0"
                carry = "1"
            
            s = sum1 + s
        
        if (carry == "1"):
            s = carry + s
        
        return s