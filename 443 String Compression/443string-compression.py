class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        j = 0
        char = chars[0]

        for i in range(1, len(chars)):
            if (chars[i] == chars[i - 1]):
                count += 1
            else:
                chars[j] = char
                j += 1
                s = str(count)
                k = 0

                if (s != "1"):
                    while (k < len(s)):
                        chars[j] = s[k]
                        k += 1
                        j += 1
                
                count = 1
                char = chars[i]
        
        chars[j] = char
        j += 1
        s = str(count)
        k = 0

        if (s != "1"):
            while (k < len(s)):
                chars[j] = s[k]
                k += 1
                j += 1

        return j