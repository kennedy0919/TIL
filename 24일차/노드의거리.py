# G : 그래프 정보(인접 행렬, 인접리스트)
# v : 시작 정점 번호
# N : 정점의 개수
# E : 도착 정점 번호
def bfs(G, v, N, E):
    visited = [0] * (N + 1)
    q = []
    q.append(v)

    while q:
        t = q.pop(0)
        
        for i in G[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
                if i == E:
                    q = []
                    break
    if visited[E] == 0:
        return 0
        
    return visited[i]

T = int(input())

for tc in range(1, T + 1):
    # V : 정점의 개수
    # E : 간선의 개수
    # S : 출발 노드
    # G : 도착노드
    V, E = map(int, input().split())
    list1 = [[] for _ in range(V + 1)]
    for _ in range(0, E):
        start, to = map(int, input().split())
        list1[start].append(to)
        list1[to].append(start)
    S, G = map(int, input().split())

    print(f"#{tc} {bfs(list1, S, V, G)}")

    

