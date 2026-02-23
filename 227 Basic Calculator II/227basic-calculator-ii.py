class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        op = "+"
        n = 0

        for i in range(len(s)):
            if (s[i].isdigit() == True):
                n = n * 10 + int(s[i])
            if (s[i] in "+-*/" or i == len(s) - 1):
                if (op == "+"):
                    stack.append(n)
                elif (op == "-"):
                    stack.append(-1 * n)
                elif (op == "*"):
                    d = stack.pop()
                    stack.append(n * d)
                else:
                    d = stack.pop()
                    stack.append(int(d / n))
                
                op = s[i]
                n = 0
        
        sum1 = sum(stack)

        return sum1