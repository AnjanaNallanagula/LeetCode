class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ls1 = version1.split(".")
        ls2 = version2.split(".")
        i = 0
        j = 0

        while (i < len(ls1) and j < len(ls2)):
            n1 = int(ls1[i])
            n2 = int(ls2[i])

            if (n1 > n2):
                return 1
            elif (n1 < n2):
                return -1
            i += 1
            j += 1
        
        while (i < len(ls1)):
            if (int(ls1[i]) > 0):
                return 1
            i += 1
        
        while (j < len(ls2)):
            if (int(ls2[j]) > 0):
                return -1
            j += 1
        
        return 0