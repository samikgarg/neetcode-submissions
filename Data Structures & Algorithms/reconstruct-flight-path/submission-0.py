class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for ticket in tickets:
            if ticket[0] not in adj:
                adj[ticket[0]] = []
            if ticket[1] not in adj:
                adj[ticket[1]] = []
            adj[ticket[0]].append(ticket[1])
        
        for arr in adj.values():
            arr.sort(reverse=True)
        
        stack = ["JFK"]
        res = []
        while stack:
            if not adj[stack[-1]]:
                res.append(stack.pop())
                continue
            stack.append(adj[stack[-1]].pop())
        
        res.reverse()
        return res
        