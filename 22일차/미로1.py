def bfs(sr, sc, N):
    visited = [[0] * N for _ in range(0, N)]
    q = []
    visited[sr][sc] = 1
    q.append((sr, sc))

    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(0, 4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and maze[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 0

def find_start(N):
    for r in range(0, N):
        for c in range(0, N):
            if maze[r][c] == 2:
                return r, c

T = 10

for i in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(0, N)]
    sr, sc = find_start(N)
    ans = bfs(sr, sc, N)
    print(f"#{tc} {ans}")