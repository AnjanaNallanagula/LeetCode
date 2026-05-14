class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ls = [pref[0]]

        for i in range(1, len(pref)):
            ls.append(pref[i - 1] ^ pref[i])
        
        return ls