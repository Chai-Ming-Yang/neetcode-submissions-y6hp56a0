class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        vis = [float('inf') for _ in range(n)]
        vis[src] = 0

        for _ in range(k + 1):
            tmp = vis.copy()
            for u, v, p in flights:
                if vis[u] != float('inf') and vis[u] + p < tmp[v]:
                    tmp[v] = vis[u] + p
            vis = tmp
        return -1 if vis[dst] == float('inf') else vis[dst]