class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if (len(sentence1) != len(sentence2)):
            return False
        
        parent = {}
        
        def find(u):
            if (u not in parent):
                parent[u] = u
            if (parent[u] != u):
                parent[u] = find(parent[u])
            
            return parent[u]
            
        def union(u, v):
            u_rep = find(u)
            v_rep = find(v)
            
            if (u_rep != v_rep):
                parent[v_rep] = u_rep
        
        for u, v in similarPairs:
            union(u, v)
        
        for i in range(len(sentence1)):
            if (sentence1[i] == sentence2[i]):
                continue
            if ((sentence1[i] not in parent) or (sentence2[i] not in parent)):
                return False
            if (find(sentence1[i]) != find(sentence2[i])):
                return False
        
        return True