"""
1
3 5
2 3 1 8 9 
7 6 2 2 6 
5 7 3 8 7 
"""

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(0, N)]
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]
    ans = 0
    print(arr)
    for r in range(0, N):
        for c in range(0, M):
            counts = 0
            for d in range(0, 8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[r][c] > arr[nr][nc]:
                        counts = counts + 1
                    if counts == 4:
                        ans = ans + 1
                        break
    print(f"#{tc} {ans}")