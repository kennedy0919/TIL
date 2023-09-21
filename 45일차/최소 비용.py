"""
1
3
0 2 1
0 1 1
1 1 1
"""


from heapq import heappop, heappush

# 다익스트라

INF = 1000000 # 무한대 초기화용

# s : 시작 정점

def dijkstra(s):
    q = []
    heappush(q, (0, s))  # (가중치, 정점)
    D[s] = 0   # 시작 정점 비용은 0        

    while q:
         print(D)
         w, v = heappop(q)
         print(w, v)
         if D[v] < w:
              continue
         
         for u, uw in adjl[v]:
            cost = D[v] + uw
            if cost < D[u]:
                 D[u] = cost
                 heappush(q, (cost, u))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(0, N)]
    adjl = [[] for _ in range(N * N)]
    for r in range(0, N):
        for c in range(0, N):
            # if r != 0 and c != 0:
                s, e, w = r, c, cost[r][c]
                adjl[s].append((e, w))
    D = [INF] * (N * N)

    dijkstra(0)
    print(D)

    
