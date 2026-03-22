class Codec:
    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            d = len(i)
            s += (str(d) + "#" + i)
        
        return s

    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        n = 0

        while (i < len(s)):
            while (i < len(s) and s[i] != "#"):
                n = n * 10 + int(s[i])
                i += 1
            
            i += 1
            s1 = ""
            j = 0

            while (i < len(s) and j < n):
                s1 += s[i]
                i += 1
                j += 1
            
            ls.append(s1)
            n = 0
        
        return ls

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))