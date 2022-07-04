class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        s = set()
        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                bull += 1
                s.add(i)
        if (bull == len(secret)):
            s = str(bull) + "A0B"
            return s
        
        d = {}
        for i in range(len(secret)):
            if (i not in s):
                if (secret[i] in d):
                    d[secret[i]] += 1
                else:
                    d[secret[i]] = 1
        m = {}
        for i in range(len(guess)):
            if (i not in s):
                if (guess[i] in m):
                    m[guess[i]] += 1
                else:
                    m[guess[i]] = 1
        cow = 0
        for i in m:
            if (i in d):
                cow += min(m[i], d[i])
        s = str(bull) + "A" + str(cow) + "B"
        return s