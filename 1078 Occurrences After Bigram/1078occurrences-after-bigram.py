class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        ls = []
        
        for i in range(len(text) - 2):
            if (text[i] == first and text[i + 1] == second):
                ls.append(text[i + 2])
        
        return ls