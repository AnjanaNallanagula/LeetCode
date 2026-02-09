class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        curr_num = 0
        sign = 1

        while (i < len(s)):
            if (s[i].isdigit() == True):
                n = 0
                j = i

                while (j < len(s) and s[j].isdigit() == True):
                    n = n * 10 + int(s[j])
                    j += 1
                
                curr_num += sign * n
                i = j - 1
            elif (s[i] == "+"):
                sign = 1
            elif (s[i] == "-"):
                sign = -1
            elif (s[i] == "("):
                stack.append(curr_num)
                stack.append(sign)

                curr_num = 0
                sign = 1
            elif (s[i] == ")"):
                prev_sign = stack.pop()
                prev_num = stack.pop()

                curr_num = prev_sign * curr_num + prev_num
            
            i += 1
        
        return curr_num