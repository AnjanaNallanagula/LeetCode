class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if ((i.isdigit() == True) or (i[0] == "-" and len(i) > 1)):
                if (i[0] == "-"):
                    d = -1 * int(i[1:])
                else:
                    d = int(i)
                stack.append(d)
            else:
                a = stack.pop()
                b = stack.pop()

                if (i == "+"):
                    stack.append(a + b)
                elif (i == "-"):
                    stack.append(b - a)
                elif (i == "*"):
                    stack.append(a * b)
                else:
                    stack.append(int(b / a))
        
        return stack[0]