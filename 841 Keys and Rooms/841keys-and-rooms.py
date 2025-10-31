class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        s = set()

        def dfs(i):
            s.add(i)

            for j in rooms[i]:
                if (j not in s):
                    dfs(j)
                    
        dfs(0)

        if (len(s) == len(rooms)):
            return True
        return False