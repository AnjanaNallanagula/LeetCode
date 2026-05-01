class Solution:
    def compress(self, chars: List[str]) -> int:
        d = 1
        pos = 0

        for i in range(1, len(chars)):
            if (chars[i] != chars[i - 1]):
                chars[pos] = chars[i - 1]
                pos += 1

                if (d > 1):
                    d = str(d)
                    
                    for j in d:
                        chars[pos] = j
                        pos += 1
                
                d = 1
            else:
                d += 1
        
        chars[pos] = chars[-1]
        pos += 1

        if (d > 1):
           d = str(d)

           for j in d:
            chars[pos] = j
            pos += 1
        
        return pos