from heapq import heappop, heappush

INF = 100000000

def dijkstra(s):
    q = []
    heappush(q, (0, s))
    D[s] = 0


    while q:
        w, v = heappop(q)

        if D[v] < w:
            continue

        for u, uw in adjl[v]:
            cost = D[v] + uw
            if cost < D[u]:
                D[u] = cost
                heappush(q, (cost, u))


T = int(input())

for tc in range(1, T + 1):
    N, E = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(0, E)]
    adjl = [[] for _ in range(N+1)]
    for i in road:
        s, e, w = i[0], i[1], i[2]
        # print("#", s, e, w)
        adjl[s].append((e, w))

    D = [INF] * (N+1)

    dijkstra(0)
    
    print(f"#{tc} {D[N]}")