def bfs(sti, stj, N):
    # visited 생성
    visited = [[0] * N for  _ in range(0, N)]
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sti, stj))
    # 시작점 인큐 표시
    visited[sti][stj] = 1
    # 큐가 비워질 때 까지
    while q:
        # 디큐
        i, j = q.pop(0)
        # 처리
        if maze[i][j] == 3:
            # 지나온 칸수 리턴
            return visited[i][j] - 2
        # 인접하고 인큐된 적이 없음ㄴ
        # 인큐, 인큐표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    # 3인칸에 도달할 수 없는경우
    return 0
def find_start(N):
    for i in range(0, N):
        for j in range(0, N):
            if maze[i][j] == 2:
                return i, j


T = int(input())

for tc in range(1 , T + 1):
    for tc in range(1, T + 1):
        N = int(input())
        maze = [list(map(int, input())) for _ in range(0, N)]
        sti, stj = find_start(N)
        ans = bfs(sti, stj, N)
        print(f"#{tc} {ans}")