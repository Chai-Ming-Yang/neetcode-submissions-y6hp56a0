class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for u, v, p in flights:
            adj[u].append((v, p))
        
        mn = [(0, 0, src)]

        while mn:
            p, i, u = heapq.heappop(mn)
            if i > k+1: continue
            if u == dst: return p
            for v, p2 in adj[u]:
                heapq.heappush(mn, (p+p2, i+1, v))
        return -1