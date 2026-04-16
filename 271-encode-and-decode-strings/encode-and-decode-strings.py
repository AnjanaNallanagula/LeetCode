class Codec:
    def encode(self, strs: List[str]) -> str:
        s = ""

        for i in strs:
            d = "{:4}".format(str(len(i)))
            s += (d + i)
        
        return s

    def decode(self, s: str) -> List[str]:
        ls = []
        i = 0
        n = 0

        while (i < len(s)):
            n = int(s[i: i + 4])
            i += 4
            s1 = s[i: i + n]
            ls.append(s1)
            i += n
        
        return ls

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))