class Solution:
    def generateParenthesis1(self, i, open1, close, n, ls1, ls):
        if (close == n):
            s = "".join(ls1)
            ls.append(s)
            return
        
        if (open1 < n):
            ls1[i] = "("

            self.generateParenthesis1(i + 1, open1 + 1, close, n, ls1, ls)
        if (close < open1):
            ls1[i] = ")"

            self.generateParenthesis1(i + 1, open1, close + 1, n, ls1, ls)
    
    def generateParenthesis(self, n: int) -> List[str]:
        ls1 = ["" for i in range(2 * n)]
        ls = []

        self.generateParenthesis1(0, 0, 0, n, ls1, ls)

        return ls