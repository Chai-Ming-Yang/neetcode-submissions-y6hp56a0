class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for u, v, p in flights:
            adj[u].append((v, p))
        
        mn = [(0, 0, src)]
        res = float('inf')
        while mn:
            p, i, u = heapq.heappop(mn)
            if i > k+1: continue
            if p > res: continue
            if u == dst: res = p; continue
            for v, p2 in adj[u]:
                if p+p2 > res: continue
                heapq.heappush(mn, (p+p2, i+1, v))
        return -1 if res == float('inf') else res