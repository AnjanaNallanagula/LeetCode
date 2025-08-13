class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        s = []
        ls = [-1 for i in range(len(prices))]

        for i in range(len(prices)):
            curr = prices[i]

            while (len(s) != 0 and curr <= prices[s[-1]]):
                ls[s[-1]] = curr
                s.pop()
            
            s.append(i)
        
        ls1 =  []

        for i in range(len(prices)):
            if (ls[i] != -1):
                ls1.append(prices[i] - ls[i])
            else:
                ls1.append(prices[i])
        
        return ls1