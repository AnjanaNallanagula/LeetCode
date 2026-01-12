class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = []
        ls.append([1])
        
        for i in range(2, numRows + 1):
            prev = [0] + ls[-1] + [0]
            curr = []

            for j in range(1, len(prev)):
                curr.append(prev[j - 1] + prev[j])
            
            ls.append(curr)
        
        return ls