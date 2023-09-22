'''
1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''

from heapq import heappop, heappush

INF = 10000000  


# s : 시작 정점
def dijkstra(s):
    q = []
    heappush(q, (0, s))  
    D[s] = 0 

    while q:
        
        w, v = heappop(q)
         # (가중치, 정점번호)

        
        if D[v] < w:
            continue

       
        for u, uw in adjl[v]:
            cost = D[v] + uw  
            if cost < D[u]:  
                D[u] = cost 
                heappush(q, (cost, u)) 


T = int(input())

for tc in range(1, T + 1):
    N, M, X = map(int, input().split()) # N : 집의 개수 M : 간선의 개수 X : 안수파티집
    adjl = [[] for _ in range(0, N+1)]
    INF = 100000000

    for i in range(0, M):
        s, e, w = map(int, input().split())  # s : 시작 정점  # e : 도착 정점  w : 가중치
        adjl[s].append((e, w))
    
    D = [INF] * (N+1)
    lst = []
    
    dijkstra(X)
    lst = D
    lst[0] = 0
    for i in range(1, N+1):
        D = [INF] * (N+1)
        dijkstra(i)
        lst[i] = lst[i] + D[X]

        
    print(f"#{tc} {max(lst)}")

    