class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {}
        for c in words[0]:
            adjacency[c] = []
        
        prev = words[0]
        for i in range(1, len(words)):
            for c in words[i]:
                if c not in adjacency:
                    adjacency[c] = []
            for j, c in enumerate(prev):
                if j >= len(words[i]):
                    return ""
                if words[i][j] != prev[j]:
                    adjacency[prev[j]].append(words[i][j])
                    break
            prev = words[i]
        
        res = []
        possible = [True]
        currSeen = set()
        notAdded = set(adjacency.keys())
        def dfs(node):
            if not possible[0]:
                return
            if node in currSeen:
                possible[0] = False
                return
            currSeen.add(node)
            for nei in adjacency[node]:
                if nei in notAdded:
                    dfs(nei)
            res.append(node)
            notAdded.remove(node)
            currSeen.remove(node)
        
        while notAdded:
            dfs(next(iter(notAdded)))
            if not possible[0]:
                return ""
        
        res.reverse()
        return "".join(res)
                
            
        
        
        